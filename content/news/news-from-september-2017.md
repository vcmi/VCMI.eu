+++
categories = ["News", "Infrastructure"]
date = "2017-09-03"
description = ""
featured = "vcmionmac.jpg"
featuredalt = ""
featuredpath = "date"
linktitle = ""
title = "News from September 2017"
type = "post"
forumurl = "https://forum.vcmi.eu/t/news-from-september-2017/4292"

+++
## New website, forum and more

The VCMI project now has a modern, static website
using [Hugo](https://gohugo.io) as generator. Everybody is welcome to
contribute [on GitHub](https://github.com/vcmi/VCMI.eu). Links are
provided for all of our social networks, so check them out and follow
if you want to be notified when the next stable version is released.

Many thanks to DigitalOcean for providing us with servers for the new
Discourse forum that replaces phpBB2. Discourse is a modern forum
software that provides many useful features and looks much better on
mobile devices. We’ve also implemented single-sign-on; once you’ve
registered on Discourse, you can login on
the [wiki](https://wiki.vcmi.eu/)
and [bug tracker](https://bugs.vcmi.eu/) with single click.

## macOS support is restored

After several years, we’ve started shipping working builds for Mac
again. All you need to do is download the latest DMG and copy your
original game data to the specified directory. See
the
[macOS installation page](https://wiki.vcmi.eu/Installation_on_macOS)
download links and full instructions.

## Newer Android builds are available

While Android support is not yet fully integrated into our continuous
integration newer, APKs for VCMI are available for download. The
builds are still lagging behind latest version, but they’re in much
better shape compared to the older 0.97 version.

## Development on Windows become much easier

If you ever had problems with building VCMI on Windows now it's a good
time to give it a try. Our wiki now
has
[instructions](https://wiki.vcmi.eu/How_to_build_VCMI_(Windows/Vcpkg))
on setting up the build environment on Windows, and there is a archive
with all required libraries, tested by continuous integration.
Everything is working out of the box and can be set up in minutes.
We’ve switched to Microsoft's Vcpkg to build dependencies and our
CMake configuration is updated to generate nice-looking projects for
Visual Studio.

## There are Linux and macOS improvements too

Now VCMI will always run properly from build output directory and
the development version won't be affected by another version of VCMI
installed system-wide.
