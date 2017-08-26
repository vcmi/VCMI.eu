+++
categories = ["Releases", "Stable"]
date = "2015-04-01"
description = ""
featured = "placeholder.jpg"
featuredalt = ""
featuredpath = "date"
linktitle = ""
title = "VCMI 0.98 released"
type = "post"

+++


## We're happy to give you new version VCMI 0.98.

Previous release 0.97 was not very satisfactory, it has a number of issues with AI as well as crashbugs. Luckily now all these problems are solved and you can play new VCMI 0.98 with no problems.

Finally all the spells in game are supported. New additions include missing adventure spells and Earthquake.
An important new feature is World View option. You will also notice nice fading effect on picked treasures and adventure map transitions.
Pathfinder and AI are allowed to use Monoliths to teleport between different parts of map. This should substantailly improve your game experience.

RMG got significant improvements to balance and look. Most prominent feature is presence of rock tunnels in the underground level.

Savegame format has changed since 0.97, but you still will be able to load games from 0.97c.

## Changelog:
```
0.97 -> 0.98
GENERAL:
* Pathfinder can now find way using Monoliths and Whirlpools (only used if hero has protection)

ADVENTURE AI:
* AI will try to use Monolith entrances for exploration
* AI will now always revisit each exit of two way monolith if exit no longer visible
* AI will eagerly pick guarded and blocked treasures

ADVENTURE MAP:
* Implemented world view
* Added graphical fading effects

SPELLS:
* New spells handled:
- Earthquake
- View Air
- View Earth
- Visions
- Disguise
* Implemented CURE spell negative dispell effect
* Added LOCATION target for spells castable on any hex with new target modifiers

BATTLES:
* Implemented OH3 stack split / upgrade formulas according to AlexSpl

RANDOM MAP GENERATOR:
* Underground tunnels are working now
* Implemented "junction" zone type
* Improved zone placing algorithm
* More balanced distribution of treasure piles
* More obstacles within zones
```

Many thanks to all developers who contributed to this build, especially new joiner ArseniyShestakov aka. SXX.
