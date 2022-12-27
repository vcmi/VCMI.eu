+++
title = "Frequently Asked Questions (FAQ)"
+++

**This article has been verified for VCMI 1.1.0 (release date 23.12.2022)**

* Again, what is VCMI?

> In simple words: Remake of Heroes of Might and Magic 3. We use original Heroes 3 graphic, sound and text assets and make new game that is supposed to work 100% same as H3. Everything in VCMI is made from scratch - loading game files, drawing graphics, AI, game mechanics etc. We have a plan to support popular features from WoG and HD mod as well as some brand-new features, but there are also other areas that need our attention as well.

* What is the purpose of VCMI? Why to play or develop it if Heroes 3 is already there?

> Our goal is to make "better" heroes 3 that overcomes various H3 engine limitations and allows way easier extensibility / modding than original game. Also VCMI is cross-platform so it works on Windows, Linux, MacOS, iOS and Android.

* Is HotA / WoG compatible with VCMI?

> HotA and WoG are mods that work with original Heroes 3, VCMI is basically new game. Still, they were ported by enthusiatsts as VCMI mods, offering limited range of their features. When more VCMI features come, they may be used to re-implement missing parts of mods. For example VCMI scripting (planned future feature) while not being WoG focused work, will be replacement for WoG's scripting feature.

* Is HD Mod compatible with VCMI?

> HD Mod is not designed for VCMI. VCMI provides its own options for high resolutions and quality-of-life GUI improvements, some of them being re-make of HD Mod features. More of them will come as project evolves.

* Where to get latest version?

> We recommend downloading latest release from <https://github.com/vcmi/vcmi/releases/latest> - scroll to the bottom and download installer from your system. Currently as of VCMI version 1.1.0 we do not have up-do-date build available on google play for Android users, but we plan to fix that. When that happens play store will be our recommended way to download VCMI on Android.

* How do I install VCMI (Windows)?

> Easiest way: Download release from <https://github.com/vcmi/vcmi/releases/latest> and install VCMI into Heroes 3 folder. Cleaner way: Download release and install VCMI into new folder, then copy "data", "maps" and "mp3" folders from some folder with installed Heroes 3 into main VCMI folder (OR %USERPROFILE%\Documents\My Games\vcmi folder). More detailed information about currently recommended setup process is available in download section on this website after you choose your system.

* Who works on this?

> Volunteers in their free time. VCMI is non-profit project. Unlike most other Heroes 3 related projects VCMI is open-source, which means it is public and everybody can contribute. That also means project future doesn't depend on "team members" abandoning it or deciding not to publish source code.

* Can I donate?

> No, at the moment we do not accept donation as we do not have any good idea how to spend potential money from donation.

* Where do I report bugs?

> Report bugs on <https://github.com/vcmi/vcmi/issues>, we strongly recommend using english language.

* How do I contact you?

> We recommend using [our forums](https://forum.vcmi.eu/) or [our Slack](https://slack.vcmi.eu/). Alternatively you can send e-mail to team@vcmi.eu to contact some of core contributors. If you are not comfortable with english language - we also have polish and russian sections on forums and slack.

* I like VCMI, how can I help to make it better?

> It would be best if you could join [our Slack](https://slack.vcmi.eu/). We mostly need C++ developers, QA/testing helpers and native mobile developers for improving mobile ports, but there may be other areas, where we could use some help. Alternatively you can create VCMI mods to try increasing popularity of VCMI platform.

* Is VCMI Mod Design Team (MDT) part of VCMI Team?

> No, they are separate group of modders, but we have some cooperation with them.

* When is VCMI final / 2.0 / whatever version going to be released?

> Open source projects never stop growing, and they tend to drift in different directions over years. As long as contributors like to add new features, VCMI will continue to evolve. There's no point in waiting for a "final" version. It's hard to estimate any sort of achieving big milestones like "100% original H3 compatibility" since work on VCMI is distributed between fixing bugs, adding missing features, developing AI, creating new features that do not exist in Heroes 3 etc. We are not very close to getting rid of every single bug and having every single missing feature implemented, but if VCMI was just about that then we would probably finish long ago. Extensibility of VCMI engine requires doing various things "better" than original Heroes 3 developers did, for example no doing things easiest way - engine building with extensibility in mind, no hardcoding various mechanics (such as creature abilities). VCMI also provides more robust engine architecture for multiplayer than Heroes 3, but is also harder to develop because of that.

* When is feature X going to be released?

> If the feature you wait is on [our issues list](https://github.com/vcmi/vcmi/issues) then you can use emote to upvote it, if not - report it so we know that feature we might be not aware about is wanted. Everybody has different expectations and things that should be priority for him. We also have our own idea on what should be higher priority and what not, based on various factors, including temporary state of project. We also do not have any page with "what is currently being made" etc. simply, because such pages would require manual management, there are some pages like that on wiki, but they are out of date.

* When will it be possible to play online in multiplayer?

> As of VCMI 1.1.0 multiplayer reached fair level of stability and is playable. You can play via local network using any supported device. There is also lobby to play online with anyone across the world, but as of VCMI 1.1.0 it doesn't support Android yet. We know that multiplayer lobby on Android is potentially one of top wanted features, but also hard to get done. Further evolution of multiplayer is definitely on our priority list.

* How close is VCMI emulating H3 gameplay?

> VCMI follows original Heroes 3 mechanics as close as possible and should be fully compatible with it. However, some obvious bugs were fixed, while some features were made optional. The AI is brand new and completely different.

* Higher resolution / random map generator is not working!

> Get "VCMI Extras" mod from our launcher. Workaround for Android devices, while embedded mod management is not available yet as of VCMI 1.1.0, would be downloading mod on PC and moving Mods folder to android to same folder that has Heroes 3 data.

* Game screen resolution is glitchy! Mouse goes beyond window / fullscreen is not properly stretched!

> Situation written here is accurate as of VCMI 1.1.0 - On PC: Try real fullscreen mode, you can activate it in VCMI launcher. If it happens on mobile platform then it may be yet unfixed bug, if changing resolution won't fix it.

* Is there any way to boost adventure AI? I want harder opponent.

> As of VCMI 1.1.0 the default adventure map AI algorithm is VCAI. Nullkiller AI is alternative, more recent AI that you can choose in VCMI launcher settings. That is generally more challenging, if you want more, check out Resourceful AI mod, which provides options for empowering AI and to speed up it. Ability to swap AI is new feature in Android version of game since VCMI 1.1.0 so if you played on older version it's worth to check it out.
