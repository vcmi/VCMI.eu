import collections.abc
import io
import os
import json5
import tempfile
import zipfile
import urllib.request
from PIL import Image
import base64
from io import BytesIO
import numpy as np

from defextract import extract_def

def nested_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = nested_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

class ModParser:
    __url = None
    __tempdirname = None

    def __init__(self, url):
        self.__url = url
        self.__extract_mod(self.__url)

    def __del__(self):
        self.__tempdirname.cleanup()
        
    def __extract_mod(self, url):
        mod_data = urllib.request.urlopen(url).read()
        self.__tempdirname = tempfile.TemporaryDirectory()
        with zipfile.ZipFile(io.BytesIO(mod_data), "r") as z:
            z.extractall(self.__tempdirname.name)

    def __parse_subconfig(self, data, dir):
        tmp = {}
        for key, value in data.items():
            if key.lower() in ["artifacts", "factions", "creatures", "heroClasses", "heroes", "spells", "objects", "terrains", "roads", "rivers", "battlefields", "obstacles", "templates"]:
                tmp2 = dict()
                for item in value:
                    tmp_item = item.strip("/")
                    tmp_item = item if item.lower().endswith(".json") else item + ".json"
                    fullpath = os.path.join(dir, "content", tmp_item)
                    for subdir, dirs, files in os.walk(dir):
                        for file in files:
                            if fullpath.lower() == os.path.join(subdir, file).lower():
                                tmp2 = nested_update(tmp2, json5.load(open(os.path.join(subdir, file))))
                if len(tmp2) > 0:
                    tmp[key.lower()] = tmp2
        return tmp

    def get_mods(self):
        mods = []
        for subdir, dirs, files in os.walk(self.__tempdirname.name):
            for file in files:
                if file.lower() == "mod.json":
                    data = json5.load(open(os.path.join(subdir, file)))
                    mods.append(
                        {
                            "pyhsicaldir": subdir,
                            "moddir": os.path.relpath(subdir, os.path.join(self.__tempdirname.name, os.listdir(self.__tempdirname.name)[0])),
                            "data": data,
                            "name": data["name"],
                            "config": self.__parse_subconfig(data, subdir)
                        }
                    )
        return mods
    
    def __get_transparent_image(self, img):
        orig_color = (0, 255, 255, 255)
        replacement_color = (0, 0, 0, 0)
        data = np.array(img.convert('RGBA'))
        data[(data == orig_color).all(axis = -1)] = replacement_color
        return Image.fromarray(data, mode='RGBA')

    def get_image(self, mod, path):
        fullpaths = [os.path.join(mod["pyhsicaldir"], "content/sprites", path), os.path.join(mod["pyhsicaldir"], "content/data", path)]
        fullpaths = [x.rstrip("/") for x in fullpaths]
        fullpaths = [x.rsplit('.', 1)[0] if "." in x.split("/")[-1] else x for x in fullpaths]
        for fullpath in fullpaths:
            for subdir, dirs, files in os.walk(mod["pyhsicaldir"]):
                for file in files:
                    if os.path.join(subdir, file).lower().startswith(fullpath.lower()) and os.path.isfile(os.path.join(subdir, file)):
                        try:
                            return self.__get_transparent_image(Image.open(os.path.join(subdir, file)))
                        except:
                            pass
        
    def image_convert_to_base64_html(self, img, format="PNG"):
        buffered = BytesIO()
        img.save(buffered, format=format)
        img_str = "data:image/" + format.lower() + ";base64," + base64.b64encode(buffered.getvalue()).decode()
        return img_str
                
    def get_image_base64(self, mod, path, format="PNG"):
        img = self.get_image(mod, path)
        if img == None:
            return ""
        return self.image_convert_to_base64_html(img, format)

    def get_animations(self, mod, path):
        fullpaths = [os.path.join(mod["pyhsicaldir"], "content/sprites", path), os.path.join(mod["pyhsicaldir"], "content/data", path)]
        fullpaths = [x.rstrip("/") for x in fullpaths]
        fullpaths = [x.rsplit('.', 1)[0] if "." in x.split("/")[-1] else x for x in fullpaths]
        for fullpath in fullpaths:
            for subdir, dirs, files in os.walk(mod["pyhsicaldir"]):
                for file in files:
                    if os.path.join(subdir, file).lower().startswith(fullpath.lower()):
                        if file.lower().endswith(".json") or file.lower().endswith(".def"):
                            if file.lower().endswith(".json"):
                                tmp = json5.load(open(os.path.join(subdir, file)))
                                for i, sequence in enumerate(tmp["sequences"]):
                                    for j, frame in enumerate(sequence["frames"]):
                                        path_img = tmp["basepath"] + frame
                                        tmp["sequences"][i]["frames"][j] = self.get_image(mod, path_img)
                                return tmp
                            else:
                                return extract_def(os.path.join(subdir, file))