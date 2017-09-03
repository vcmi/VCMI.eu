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

Project now have modern static website using HUGO as generator. Everybody is welcome to contribute [on GitHub](https://github.com/vcmi/VCMI.eu). There also links to all of our social networks so check them and follow if you want to be notified once next stable version is released.

Thanks to DigitalOcean for providing us with servers our forums has moved from phpBB2 to Discourse. It's modern forum software that provide many useful features and looks much better on mobile devices. Once you registered on forum you can login on Wiki and Bug tracker with single click.

## macOS support is restored

After several years we started shipping working builds for Mac again. All you need to do is download DMG and copy original game data to specified directory. Click on the download icon for download links and instructions.

## Newer Android builds are available

While Android support is not yet fully integrated into our continuous integration newer APK for VCMI are available for download. Builds still lagging behind latest version, but they in much better shape compared to older 0.97 version.

## Development on Windows become much easier

If you ever had problems with building VCMI on Windows now it's a good time to give it a try. Wiki now has [instruction](https://wiki.vcmi.eu/How_to_build_VCMI_(Windows/Vcpkg)) on setting build environment on Windows and there is dependency package tested by continuous integration. Everything working out of the box and can be setup in minutes. We using Microsoft's Vcpkg to build dependencies and our CMake configuration is updated to generate nice-looking projects for Visual Studio.

## There are Linux and macOS improvements too

Now VCMI will always run properly from build output directory and development version won't be affected by another version of VCMI installed system wide.
