+++
categories = ["Releases", "Stable"]
date = "2016-11-01"
description = ""
featured = "placeholder.jpg"
featuredalt = ""
featuredpath = "date"
linktitle = ""
title = "VCMI 0.99 released"
type = "post"

+++


## We're back with new major release!

A lot of work has been done to ensure game stability. A number of "impossible" crash bugs were tracked down and fixed. This opens up chance for better multiplayer support in the future.
RMG has undergone huge improvement, it is now not only closely resembling OH3, but also works much faster. Bonus is about 150 random map templates ported from original game and fan favourites.
Pretty much every aspect has been improved. Pay close attention to spells and cheat codes. Flying spells and artifacts have been restored as well as ability icons in Creature Window. Over 1400 commits were done since previous release 0.98, which means something.

Since 0.98f [over 100 bugs](http://bugs.vcmi.eu/changelog_page.php?version_id=87) have been fixed. Since 0.98 it's difficult to count. For the first time in history more bugs are being fixed than reported ;)

## Changelog:
```
GENERAL:
* New Bonus NO_TERRAIN_PENALTY
* Nomads will remove Sand movement penalty from army
* Flying and water walking is now supported in pathfinder
* New artifacts supported
- Angel Wings
- Boots of Levitation
* Implemented rumors in tavern window
* New cheat codes:
- vcmiglaurung - gives 5000 crystal dragons into each slot
- vcmiungoliant - conceal fog of war for current player
* New console commands:
- gosolo - AI take control over human players and vice versa
- controlai - give control of one or all AIs to player
- set hideSystemMessages on/off - supress server messages in chat

BATTLES:
* Drawbridge mechanics implemented (animation still missing)
* Merging of town and visiting hero armies on siege implemented
* Hero info tooltip for skills and mana implemented

ADVETURE AI:
* Fixed AI trying to go through underground rock
* Fixed several cases causing AI wandering aimlessly
* AI can again pick best artifacts and exchange artifacts between heroes
* AI heroes with patrol enabled won't leave patrol area anymore

RANDOM MAP GENERATOR:
* Changed fractalization algorithm so it can create cycles
* Zones will not have straight paths anymore, they are totally random
* Generated zones will have different size depending on template setting
* Added Thieves Guild random object (1 per zone)
* Added Seer Huts with quests that match OH3
* RMG will guarantee at least 100 pairs of Monoliths are available even if there are not enough different defs
```

Also welcome our latest contributors Dydzio and Chocimier.
