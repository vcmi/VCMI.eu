+++
categories = ["Releases", "Stable"]
date = "2022-09-11"
description = ""
featured = "vcminewterrain.jpg"
featuredalt = ""
featuredpath = "date"
linktitle = ""
title = "VCMI 1.0.0 released"
type = "post"
forumurl = "https://forum.vcmi.eu/"

+++

## We're happy to announce a new release!
 
Several years have passed since VCMI 0.99 and it's about time for a new release.
Tons of changes, improvements, and fixes have been introduced during that time, so it's hard to recall all of them.
However, we'd like to highlight several major changes.
 
## Game engine
Lodestar grail finally can reveal all the map!
We were working hard to track down and fix crashes that severely affected VCMI gameplay. Now they are rare beasts but if you manage to find one do not hesitate to [report it](https://github.com/vcmi/vcmi/issues)!
 
## Adventure map
Hero exchange window has got a few additional buttons and keyboard shortcuts to ease army and artefact exchange. If you do not see them after installing the release make sure you have the latest [VCMI extras mod](https://github.com/vcmi-mods/vcmi-extras) installed.
 
## Artificial intelligence
You are welcome to try an alternative AI algorithm called Nullkiller which shows itself well on small and medium sized maps. For larger maps you should better go with classic VCAI computer player which was also significantly improved. From the launcher settings you can always choose the AI you like and enjoy the most.
 
## Modding and new terrains
VCMI was built for modding, but with this release we significantly enhanced the mod system.
Among various gameplay tools we introduced support for adding new terrains. It is a natural evolution of new town support as they need to have unique terrains, battlefields, mines and map objects. This feature required deep refactoring of the game engine so unfortunately saves you made before release 1.00 will not be compatible. It's a good reason to make new ones!
 
## Random Maps Generator
RMG also has undergone huge changes. First of all, normal and island water options are supported now.
Secondly, as mods can introduce new terrains and objects, RMG has got powerful algorithms to generate new terrain patches and to place new objects provided by mods. And finally, we improved the generator in terms of aesthetics, obstacles placement and stability as well.
 
## Launcher
Good news! We reconsidered our release policy to make releases more frequently and introduced an update notification system into launcher in order to make everybody aware about new features and fixes. In addition to that, launcher works now with our new [mod repository on GitHub](https://github.com/vcmi-mods) that will be used to follow for updates in your favorite mods too!

## Join us!
The project is now actively maintained once again. There are several active contributors working on new amazing features. Not everything made it into this release so stay tuned for next announcements!
 
On top of a shorter release cycle we also want to announce that we slowly started using GitHub built-in tools for bug tracking and project management. Now development activities and release milestones will be more transparent. As always we are open to all contributors who wish to help us move VCMI forward. You can help with both programming or contributing new mods to the repository. Let's make VCMI better together!
