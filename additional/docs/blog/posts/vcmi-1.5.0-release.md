---
categories:
  - Releases
  - Stable
date: 2024-05-10
---

# VCMI 1.5.0 released

A new major release has been published. VCMI 1.5.0 sees the light of day. The main focus this time was on the online lobby. But also many other features were integrated and many bugs were fixed.

<!-- more -->

## Online multiplayer support
VCMI now has an online lobby that can be used to set up multiplayer sessions. But you can also interact with other players. The lobby works on all platforms and regardless of firewall restrictions. It can be opened at any time on desktop systems with `CTRL + Tab` and on mobile platforms with a three-finger touch.

## Better random maps
A new biome system for random maps has been integrated. This makes created maps look much more natural.

Also there are many different optimizations like properly random-looking zone edges, treasure/obstacle density tweaks and underground generation content tweaks leading to better zones.

## AI optimizations
Nullkiller AI got notable speedup improvements, better handling of heroes with "patrol" set in map editor and some other AI bug fixes.

## Most remaining campaign issues fixed
Many different problems and bugs related to campaigns have been fixed.

## Basic game controllers support added
It is now possible to play VCMI with a game controller. Both on PC-based platforms and on mobile platforms.

## Easier installation of game files from gog.com
We have now integrated [innoextract](https://github.com/dscharrer/innoextract) into the launcher. This makes it very easy to extract the offline installer from gog.com (*.exe and *.bin file) for vcmi.

This function is currently available on all platforms except android. With the integration of the launcher in the next few weeks, the function will also be available there.

## Artifact improvements
It is now possible to group several artifacts into sets. This feature is based on the costumes of the HD mod. With `CTRL + [1]...[9]` an artifact set can be saved, which can then be called with `[1]...[9]`.

There are now also new shortcuts. `ALT + click` on artifact slot moves artifact from/to backpack. `CTRL + click` on artifact slot moves artifact to 2nd hero we are trading with.

## Configurable keyboard shortcuts
Keyboard shourtcuts are now configurable. However, currently only via the configuration file `config/shortcutsConfig.json`.

# New homepage
With version 1.5.0 we have also published our new homepage. Apart from the newer, more modern design, it also offers useful functions for players, modders and developers.

Documents such as instructions and technical documentation are now available directly on the website. You can also find informations and pictures of the individual mods in our mod repository.

## And much more
In addition, many other features and fixes have been integrated, which were requested by the community. For example: tavern hero inviting (requires mod to enable), optional unlimited replay, option to disable cheats, immediate end of the battle, dimension door & summoning mechanics fixes. See the complete [changelog](https://github.com/vcmi/vcmi/blob/master/ChangeLog.md#145---150)

We are delighted that you are entering the world of Enroth via VCMI. The journey has been a long one, but we are far from finished and will continue to improve VCMI.