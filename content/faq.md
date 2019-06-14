+++
title = "Frequently Asked Questions (FAQ)"
+++

* Again, what is VCMI?

> In simple words: Remake of Heroes of Might and Magic 3. We use original Heroes 3 graphic, sound and text assets and make new game that is supposed to work 100% same as H3. Everything in VCMI is made from scratch - loading game files, drawing graphics, AI, game mechanics etc. We also plan supporting WoG mod features, but for now there are areas in VCMI that need more attention than WoG features.

* What is the purpose of VCMI? Why to play or develop it if Heroes 3 is already there?

> Our goal is to make "better" heroes 3 that overcomes various H3 engine limitations and allows way easier extensibility / modding than original game. Also VCMI works without problems on Windows, Linux, MacOS and Android.

* Is HD Mod / HotA / WoG compatible with VCMI?

> No, HD Mod, HotA and WoG are mods that work with original Heroes 3, VCMI is new game. Remaking these in VCMI would be possible, but there are bigger priorities. Note that some VCMI-specific modding features may also allow remaking some part of these mods by modders as side-effects. For example VCMI scripting while not being WoG focused work, will be replacement for WoG's scripting feature.

* Where to get latest version?

> We recommend getting daily builds from <https://builds.vcmi.download/branch/develop/>. We try to not break them up so they should work fairly well most of the time. Also google play version for Android users should be available soon.

* How do I install VCMI (Windows)?

> Easiest way: Grab daily build installer and install VCMI into Heroes 3 folder. Cleaner way: Grab daily build installer and install VCMI into new folder, then copy "data", "maps" and "mp3" folders from some folder with installed Heroes 3 into main VCMI folder.

* Who works on this?

> Volunteers in their free time. VCMI is non-profit project. Unlike most other Heroes 3 related projects VCMI is open-source, which means it is public and everybody can contribute. That also means project future doesn't depend on "team members" abandoning it or deciding not to publish source code.

* Can I donate?

> No, at the moment we do not accept donation as we do not have any good idea how to spend potential money from donation.

* Where do I report bugs?

> Report bugs on <https://bugs.vcmi.eu/my_view_page.php>, we strongly recommend using english language.

* How do I contact you?

> We recommend using [our forums](https://forum.vcmi.eu/) or [our Slack](https://slack.vcmi.eu/). Alternatively you can send e-mail to team@vcmi.eu to contact some of core contributors. If you are not comfortable with english language - we also have polish and russian sections on forums and slack.

* I like VCMI, how can I help to make it better?

> It would be best if you could join [our Slack](https://slack.vcmi.eu/). We mostly need C++ developers, but there are other areas, where we could use some help. Alternatively you can create VCMI mods to try increasing popularity of VCMI platform.

* Is VCMI Mod Design Team (MDT) part of VCMI Team?

> No, they are separate group of modders, but we do some cooperation with them.

* When will be next official release?

> For now we neglect thinking about official releases in favor of focusing on development. Since daily build became available people can play up-to-date version without need of official release.

* When is VCMI final / 1.0 / 2.0 version going to be released?

> Hard to estimate, work on VCMI is distributed between fixing bugs, adding missing features, developing AI, creating new features that do not exist in Heroes 3 etc. We are not close to getting rid of every single bug and having every single missing feature implemented, but if VCMI was just about that then we would probably finish long ago. Extensibility of VCMI engine requires doing various things "better" than original Heroes 3 developers did, for example no doing things easiest way - engine building with extensibility in mind, no hardcoding various mechanics (such as creature abilities). VCMI also provides more robust engine architecture for multiplayer than Heroes 3, but is also harder to develop because of that.

* When is feature X going to be released?

> Everybody has different expectations and things that should be priority for him. We also have our own idea on what should be higher priority and what not. We also do not have any page with "what is currently being made" etc. simply, because such pages would require manual management, there are some pages like that on wiki, but they are out of date. Maybe you wanna help us in manual pages maintaining? :P

* When will it be possible to play online in multiplayer?

> It is already possible to play multiplayer, although there are some bugs in this regard. For example there is unfixed yet bug about random map generator deynchronization when playing VCMI across multiple platforms(windows/linux), so you may see wood on adventure map but when you pick it up you collect ore etc. There are also some crashes to fix regarding player disconnection.

* How close is VCMI emulating H3 gameplay?

> We try to make VCMI as close to Heroes 3 as possible and we want to deliver 100% same game mechanics, with original heroes 3 bugs such as infinite ammo for ballista becoming toggle on/off switches. AI will not be the same, we deliver our custom adventure map and battle AI. Currently there are not many game mechanics bugs that will be noticed by people who do not have advanced knowledge about the game. Some examples are: Lack of moat in tower type town, some spell mechanics, spell hero specialties are bugged. There are  various display glitches, but they have less priority than other things.

* I updated VCMI Essential Files in VCMI launcher and I have some bugs.

> You should not do this, perform clean re-install of VCMI. We are sorry for inconvenience, reworking mods repository is on our "to do" list. We recommend getting mods from <https://wiki.vcmi.eu/Mod_list> instead of launcher.

* On Windows build I noticed crash when recruiting creatures in town. How come it is still there?

> We believe this is bug in our toolset that builds automated VCMI builds, as everything in VCMI code seems fine in place of crash. Revisiting it will be really time-consuming task. For now we recommend recruiting creatures via quick recruitment window (press fort mini-icon on panel with information about town name, income etc to show it).

* Higher resolution / random map generator is not working!

> Get "VCMI essential files mods (1.01)" from <https://wiki.vcmi.eu/Mod_list>.

* Game screen resolution is glitchy! Mouse goes beyond window / fullscreen is not properly stretched!

> On PC: Try real fullscreen mode, you can activate it in VCMI launcher. On Android: Glitchy screen borders is known bug.

* Is there any way to boost adventure AI? I want harder opponent.

> Yeah, the easiest thing to try is to use cheats for resources and/or full map reveal, using parameter that specifies target players. Typing 'ai' after cheat name causes only AI players to be affected by it, player color names are also recognized. So you can for example type 'vcmiformenos ai' to give extra resources to AI player, 'vcmieagles blue' to reveal full map for blue player etc.  Note that these cheats do not guarantee any improvement, for example revealing whole map may cause AI to overly focus on far goals, missing local details. Distance is one of factors when deciding what to do, but still. More advanced thing you can do is experimenting with AI Values for various objects / object classes by changing AI Value (exact object value) and Default AI Value (object class value) in object config JSON files. Range of effective AI Value is 0-20000. Also it's important to know that AI Values are tied to saved games by design, so you need to start new game to test effectiveness of new AI Values.