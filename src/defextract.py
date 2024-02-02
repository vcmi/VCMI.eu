#!/usr/bin/env python3
#
# Copyright (C) 2014  Johannes Schauer <j.schauer@email.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


# http://aethra-cronicles-remake.googlecode.com/svn-history/r4/trunk/export/sergroj/RSDef.pas
# vcmi/client/CAnimation.cpp

import struct
from PIL import Image, ImageDraw
from collections import defaultdict
import os
import json
import numpy as np

def extract_def(infile):
    f = open(infile, 'rb')
    bn = os.path.basename(infile)
    bn = os.path.splitext(bn)[0].lower()

    # t - type
    # blocks - # of blocks
    # the second and third entry are width and height which are not used
    t,_,_,blocks = struct.unpack("<IIII", f.read(16))

    palette = []
    for i in range(256):
        r,g,b = struct.unpack("<BBB", f.read(3))
        palette.extend((r,g,b))

    offsets = defaultdict(list)
    for i in range(blocks):
        # bid - block id
        # entries - number of images in this block
        # the third and fourth entry have unknown meaning
        bid,entries,_,_ = struct.unpack("<IIII", f.read(16))
        names=[]
        # a list of 13 character long filenames
        for j in range(entries):
            name, = struct.unpack("13s", f.read(13))
        # a list of offsets
        for j in range(entries):
            offs, = struct.unpack("<I", f.read(4))
            offsets[bid].append(offs)

    out_json = {"sequences":[],"type":t,"format":-1}

    firstfw,firstfh = -1,-1
    for bid,l in list(offsets.items()):
        frames=[]
        for j,offs in enumerate(l):
            f.seek(offs)
            pixeldata = b""
            # first entry is the size which is unused
            # fmt - encoding format of image data
            # fw,fh - full width and height
            # w,h - width and height, w must be a multiple of 16
            # lm,tm - left and top margin
            _,fmt,fw,fh,w,h,lm,tm = struct.unpack("<IIIIIIii", f.read(32))

            # SGTWMTA.def and SGTWMTB.def fail here
            # they have inconsistent left and top margins
            # they seem to be unused
            if lm > fw or tm > fh:
                print("margins (%dx%d) are higher than dimensions (%dx%d)"%(lm,tm,fw,fh))
                return False

            if firstfw==-1 and firstfh == -1:
                firstfw = fw
                firstfh = fh
            else:
                if firstfw > fw:
                    print("must enlarge width")
                    fw = firstfw
                if firstfw < fw:
                    print("first with smaller than latter one")
                    return False
                if firstfh > fh:
                    print("must enlarge height")
                    fh = firstfh
                if firstfh < fh:
                    print("first height smaller than latter one")
                    return False

            if out_json["format"] == -1:
                out_json["format"] = fmt
            elif out_json["format"] != fmt:
                print("format %d of this frame does not match of last frame"%(fmt))
                return False

            if w != 0 and h != 0:
                if fmt == 0:
                    pixeldata = f.read(w*h)
                elif fmt == 1:
                    lineoffs = struct.unpack("<"+"I"*h, f.read(4*h))
                    for lineoff in lineoffs:
                        f.seek(offs+32+lineoff)
                        totalrowlength=0
                        while totalrowlength<w:
                            code,length = struct.unpack("<BB", f.read(2))
                            length+=1
                            if code == 0xff: #raw data
                                pixeldata += f.read(length)
                            else: # rle
                                pixeldata += str.encode(length*chr(code))
                            totalrowlength+=length
                elif fmt == 2:
                    lineoffs = struct.unpack("<%dH"%h, f.read(2*h))
                    _,_ = struct.unpack("<BB", f.read(2)) # unknown
                    for lineoff in lineoffs:
                        if f.tell() != offs+32+lineoff:
                            print("unexpected offset: %d, expected %d"%(f.tell(),offs+32+lineoff))
                            f.seek(offs+32+lineoff)
                        totalrowlength=0
                        while totalrowlength<w:
                            segment, = struct.unpack("<B", f.read(1))
                            code = segment>>5
                            length = (segment&0x1f)+1
                            if code == 7: # raw data
                                pixeldata += f.read(length)
                            else: # rle
                                pixeldata += str.encode(length*chr(code))
                            totalrowlength+=length
                elif fmt == 3:
                    # each row is split into 32 byte long blocks which are individually encoded
                    # two bytes store the offset for each block per line 
                    lineoffs = [struct.unpack("<"+"H"*int(w/32), f.read(int(w/16))) for i in range(h)]

                    for lineoff in lineoffs:
                        for i in lineoff:
                            if f.tell() != offs+32+i:
                                print("unexpected offset: %d, expected %d"%(f.tell(),offs+32+i))
                                f.seek(offs+32+i)
                            totalblocklength=0
                            while totalblocklength<32:
                                segment, = struct.unpack("<B", f.read(1))
                                code = segment>>5
                                length = (segment&0x1f)+1
                                if code == 7: # raw data
                                    pixeldata += f.read(length)
                                else: # rle
                                    pixeldata += str.encode(length*chr(code))
                                totalblocklength+=length
                else:
                    print("unknown format: %d"%fmt)
                    return False
                imp = Image.frombytes('P', (w,h),pixeldata)
                imp.putpalette(palette)
                # convert to RGBA
                imrgb = imp.convert("RGBA")
                # replace special colors
                # 0 -> (0,0,0,0)    = full transparency
                # 1 -> (0,0,0,0x40) = shadow border
                # 2 -> ???
                # 3 -> ???
                # 4 -> (0,0,0,0x80) = shadow body
                # 5 -> (0,0,0,0)    = selection highlight, treat as full transparency
                # 6 -> (0,0,0,0x80) = shadow body below selection, treat as shadow body
                # 7 -> (0,0,0,0x40) = shadow border below selection, treat as shadow border
                pixrgb = np.array(imrgb)
                pixp = np.array(imp)
                pixrgb[pixp == 0] = (0,0,0,0)
                pixrgb[pixp == 1] = (0,0,0,0x40)
                pixrgb[pixp == 4] = (0,0,0,0x80)
                pixrgb[pixp == 5] = (0,0,0,0)
                pixrgb[pixp == 6] = (0,0,0,0x80)
                pixrgb[pixp == 7] = (0,0,0,0x40)
                imrgb = Image.fromarray(pixrgb)
                im = Image.new('RGBA', (fw,fh), (0,0,0,0))
                im.paste(imrgb,(lm,tm))
            else: # either width or height is zero
                im = Image.new('RGBA', (fw,fh), (0,0,0,0))
            frames.append(im)
        out_json["sequences"].append({"group":bid,"frames":frames})
    return out_json