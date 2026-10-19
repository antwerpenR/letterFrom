---
source: https://rogerprice.me/f-droid-2-0
clipped: '2026-10-08T03:16:12+00:00'
title: F-Droid 2.0
site: Letter from ...around the world
published: '2026-09-29T14:56:29.000Z'
---

# F-Droid 2.0

# F-Droid 2.0

![F-Droid 2.0](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/F-Droid-2.jpg)

F-Droid is an **open-source alternative app store** for Android — but also a **repository system and toolset** for distributing Android software, far friendlier to developers than Google Play.

- Unlike Play Store publishing, F-Droid requires **no registration fee, no terms agreement, no government ID, no signing-key evidence, no listing of app identifiers**, and takes **no 30% cut** of in-app purchase profits.
- Despite the lack of gatekeeping, it sees **far less malware** than the Play Store. The official repository focuses on free and open-source apps, but the client can connect to other F-Droid repositories too — no Google account needed.

> [!image]
> [![Click for the full walk-through and explanation](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-43.png)](https://www.youtube.com/watch?v=i\_T9ARBP3nw&pp=0gcJCS8MAYcqIYzv&ref=rogerprice.me)
> Click for the full walk-through and explanation

## Notable apps only realistically available outside Play

- **NewPipe** — lightweight alternative front end for YouTube, SoundCloud and other ad-heavy sites, without login.
- **Aurora Store** — an open-source alternative client for Google Play itself, so you can install Play apps without signing into a Google account.
- **Termux** — a terminal for power-user/Linux work on Android. The Play Store build comes from a separate code base with missing functionality due to Google policies, so developers recommend the F-Droid (or GitHub) version.

## Why 2.0 happened

The old official client felt dated; many users had switched to third-party clients like **Droid-ify** and **Neo Store** for cleaner interfaces and better filtering. Version 2.0 is the official client catching up with its own ecosystem.

## Key changes in 2.0

- **Interface rebuilt from scratch** with **Kotlin Compose** (Google's modern Android UI toolkit). Looks far more modern than the old 2014-era UI — though the current beta has no proper tablet UI (a large "2.0" banner dominates the screen, with no setting to remove it).
- **Improved search** — now searches descriptions, translations and discovery pages to highlight popular downloads, instead of requiring exact app names.
- **Anti-feature filters** — hide apps with tracking, non-free code, etc.
- **Parallel installs and updates** — multiple apps can download/update simultaneously.
- **Better repository handling, install information, signer details**, and **migration of settings** from the old client, including proxy and Tor settings.

## Alternatives

- **Droid-ify** and **Neo Store** are not competing repositories but alternative *clients* browsing F-Droid-compatible repos. Droid-ify adds automatic background updates and custom repositories; Neo Store offers extensive filters, reproducible-build indicators, privacy info and ~100 built-in repositories.
- **Obtainium** skips the repository model: point it at a GitHub/GitLab/Codeberg release page (it also supports F-Droid repos, direct APK links and many other sources) for bleeding-edge builds. Trade-off: you take on the trust decisions yourself, and web-scraping sources can break when sites change.

## The context: Google's lockdown

- Google's new **Android developer verification** requires developers to pay a fee and clear multiple hurdles to publish on Play, ostensibly to fight malware.
- Side-loading is not being blocked outright, but will require **developer mode, several warning screens, a restart, and a 24-hour wait** — so on a new device you can't install your apps until the next day.
- Per **keepandroidopen.org** (cited in the video), this flow runs through **Google Play services**, meaning Google could extend the delay to a week or block side-loading entirely at will. The creator's view: "Google wants to be like Apple so bad."
- **ADB from a computer** remains a workaround in the first 24 hours — ironically similar to how iOS side-loading works, and too cumbersome for most users.

## Verdict

The F-Droid ecosystem's weakness was never lack of apps — it was user experience. Version 2.0 delivers better search, faster updates, better discovery and clearer security information just as alternative app distribution becomes a bigger fight. Recommendation: try the 2.0 beta now, but tablet/large-screen users should wait for the finished release.
