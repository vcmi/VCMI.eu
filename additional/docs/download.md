---
hide:
  - navigation
  - toc
---

# Download

[ :fontawesome-solid-download: Download for your platform](#){ .md-button .md-button--primary id=dl-button style="font-size:1.2em; padding:0.6em 2em; margin-bottom:0.3em;" }

<script>
(function(){
  var ua = navigator.userAgent;
  var link = document.getElementById('dl-button');
  var url = '';
  var name = '';
  if (/Windows/.test(ua)) {
    url = 'https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Windows-x64.exe';
    name = 'Windows (x64)';
  } else if (/Mac/.test(ua)) {
    url = 'https://formulae.brew.sh/cask/vcmi';
    name = 'macOS (Homebrew)';
  } else if (/Android/.test(ua)) {
    url = 'https://play.google.com/store/apps/details?id=is.xyz.vcmi';
    name = 'Android (Play Store)';
  } else if (/iPad|iPhone|iPod/.test(ua)) {
    url = 'https://testflight.apple.com/join/pJWHSbmu';
    name = 'iOS (Testflight)';
  } else if (/Linux/.test(ua)) {
    url = 'https://flathub.org/apps/eu.vcmi.VCMI';
    name = 'Linux (Flathub)';
  } else {
    link.style.display = 'none';
    return;
  }
  link.href = url;
  var nodes = link.childNodes;
  for (var i = nodes.length - 1; i >= 0; i--) {
    if (nodes[i].nodeType === 3 && nodes[i].textContent.trim()) {
      nodes[i].textContent = ' Download for ' + name;
      break;
    }
  }
})();
</script>

## Other platforms

| Platform | Package Sources | Direct |
|:---|:---|:---|
| :fontawesome-brands-windows: **Windows** | — | [:fontawesome-solid-download: x64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Windows-x64.exe) &nbsp;&nbsp;·&nbsp;&nbsp; [:fontawesome-solid-download: x86](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Windows-x86.exe)<br /><br />[:fontawesome-solid-download: ARM64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Windows-arm64.exe) |
| :fontawesome-brands-apple: **macOS** | [:fontawesome-brands-apple: Homebrew](https://formulae.brew.sh/cask/vcmi) | [:fontawesome-solid-download: ARM64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-macOS-arm.dmg) &nbsp;&nbsp;·&nbsp;&nbsp; [:fontawesome-solid-download: Intel](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-macOS-intel.dmg) |
| :fontawesome-brands-linux: **Linux** | [:fontawesome-brands-linux: Flathub](https://flathub.org/apps/eu.vcmi.VCMI)<br /><br />[:fontawesome-brands-ubuntu: Ubuntu PPA](https://launchpad.net/~vcmi/+archive/ubuntu/ppa) | [:fontawesome-solid-download: AppImage x64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Linux-x64.AppImage)<br /><br />[:fontawesome-solid-download: AppImage ARM64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Linux-arm64.AppImage) |
| :fontawesome-brands-android: **Android** | [:fontawesome-brands-google-play: Play Store](https://play.google.com/store/apps/details?id=is.xyz.vcmi)<br /><br />[:fontawesome-brands-android: F-Droid](https://f-droid.org/de/packages/is.xyz.vcmi/)<br /><br />[:fontawesome-solid-store: Obtainium](https://apps.obtainium.imranr.dev/redirect?r=obtainium://add/https://github.com/vcmi/vcmi) | [:fontawesome-solid-download: ARM64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Android-arm64-v8a.apk) &nbsp;&nbsp;·&nbsp;&nbsp; [:fontawesome-solid-download: ARM32](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Android-armeabi-v7a.apk)<br /><br />[:fontawesome-solid-download: x64](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Android-x86_64.apk) |
| :fontawesome-brands-apple: **iOS** | [:fontawesome-brands-apple: Testflight](https://testflight.apple.com/join/pJWHSbmu) | [:fontawesome-solid-download: IPA](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-iOS.ipa) |
| :fontawesome-solid-gamepad: **Handheld** | [:fontawesome-solid-gamepad: PortMaster](https://portmaster.games/detail.html?name=vcmi) | — |

## Required files

| File | Source |
|---|---|
| :fontawesome-solid-gamepad: Heroes III: Complete | [:fontawesome-solid-cart-shopping: Buy on GOG.com](https://www.gog.com/en/game/heroes_of_might_and_magic_3_complete_edition) |

## Optional files

| File | Source |
|---|---|
| :fontawesome-solid-gamepad: Heroes Chronicles | [:fontawesome-solid-cart-shopping: Buy on GOG.com](https://www.gog.com/en/game/heroes_chronicles_all_chapters) |
| :fontawesome-solid-gamepad: Heroes of Might & Magic III - HD Edition | [:fontawesome-solid-cart-shopping: Buy on Steam](https://store.steampowered.com/app/297000/Heroes_of_Might__Magic_III__HD_Edition) |
| <small>*Optional as extension — Complete/SoD files still required.*</small> | |

## Help

| Platform | Guide |
|---|---|
| :fontawesome-brands-windows: Windows | [:fontawesome-solid-book: Installation Guide](../players/Installation_Windows/) |
| :fontawesome-brands-apple: macOS | [:fontawesome-solid-book: Installation Guide](../players/Installation_macOS/) |
| :fontawesome-brands-linux: Linux | [:fontawesome-solid-book: Installation Guide](../players/Installation_Linux/) |
| :fontawesome-brands-android: Android | [:fontawesome-solid-book: Installation Guide](../players/Installation_Android/) |
| :fontawesome-brands-apple: iOS | [:fontawesome-solid-book: Installation Guide](../players/Installation_iOS/) |

## Other downloads

| Download | Link |
|---|---|
| :fontawesome-brands-github: GitHub Releases | [:fontawesome-solid-link: see on GitHub](https://github.com/vcmi/vcmi/releases/latest) |
| :fontawesome-solid-wrench: Daily Builds | [:fontawesome-solid-link: download.vcmi.eu](https://download.vcmi.eu/) |
| :fontawesome-solid-code: Source Code | [:fontawesome-solid-download: GitHub](https://github.com/vcmi/vcmi/releases/latest/download/VCMI-Sources.tar.gz) |
