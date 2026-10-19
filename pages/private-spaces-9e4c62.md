---
source: https://rogerprice.me/private-spaces
clipped: '2026-09-04T16:54:32+00:00'
title: Private spaces
site: Letter from ...around the world
published: '2026-09-02T18:02:38.000Z'
---

# Private spaces

# Private spaces

![Private spaces](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/GrapheneOS-Private-Space-Explained.jpg)

## Overview

GrapheneOS fully supports the **Private Space** feature introduced in Android 15. Private Space is described as a separate user profile nested inside a parent user profile. The presenter walks through the official GrapheneOS forum announcement and then provides a hands-on demonstration on a Pixel 7 running GrapheneOS.

> **Note:** Since the original announcement, one key change has already occurred — Private Space is now available in **all user profiles**, not just the Owner profile.

> [!image]
> [![Click for step by step guide and explanation of the benefits](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-5.png)](https://youtu.be/G94V5I2xH1E?si=pJNEoTx91RB4omRh&ref=rogerprice.me)
> Click for step by step guide and explanation of the benefits

## What Private Space Is

- A **separate, isolated workspace profile** for apps and data, similar to both **user profiles** and **work profiles**.
- The GrapheneOS team **strongly recommends** it as a replacement for a work profile managed by a local profile admin app (e.g. **Shelter**), citing better OS integration and isolation.

---

## Key Features & Comparisons

### Three forms of profiles share these properties:

| Feature | Details |
| --- | --- |
| **Separate VPN configurations** | Each profile (user, work, private space) has its own VPN settings. Even if connected to the same VPN service, exit IPs can differ per profile. |
| **Separate encryption keys** | Each profile uses its own encryption keys. |
| **Can be put at rest** | A private space can be locked (put at rest) while the parent/owner user remains logged in — previously only possible with secondary user profiles. |

### Advantages over a secondary user profile:

- **Easier data sharing** — the clipboard is shared between the parent user and the private space (though a setting has since been added to control this).
- **More convenient access** — apps in the private space are accessible within the same user profile you already use, rather than requiring a full user switch.
- **Same isolation benefits** as a separate user profile, but without the inconvenience of switching between users.
- **Full support** for GrapheneOS-specific features: **contact scopes**, **storage scopes**, and **sandboxed Google Play Services** all work within Private Space.

### A key use case:

Users who currently run a **separate user profile** for sandboxed Google Play can instead install Play Store and Play Services inside Private Space — achieving the same isolation while being able to **lock the space** when not in use (something not possible with apps installed directly in the Owner profile without powering off the device).

---

## Setup Walkthrough

1. Open **Settings → Security & Privacy → Private Space** (works in any user profile).
2. Enter your user PIN.
3. Read the details and warning on screen.
4. Tap **Setup**.
5. Choose a **lock method**: either reuse your screen lock or set a new separate lock.
6. Once complete, Private Space appears at the bottom of the app drawer with a **lock icon** on the right.
7. Tap the lock icon and enter your PIN/password to unlock.

### Critical Warning (stated twice)

> Private spaces are **not suitable for apps that need to run in the background or send critical notifications** (e.g. medical apps). When the space is locked, notifications and background activity are stopped. If the space is unlocked, notifications should work — but the presenter advises **testing independently** before relying on this for anything health-critical.

---

## Private Space Settings

| Setting | Default | Description |
| --- | --- | --- |
| **Private Space Lock** | — | Change the lock method (screen lock or a separate lock). |
| **Lock automatically** | Every time device locks | Options: lock every time the device locks, or **only after device restarts** (choose the latter if you want it running continuously in the background). |
| **Hide Private Space** | Off | Hides the private space from the app drawer. To access it, you must go to Settings → Security & Privacy → Private Space and unlock it. The presenter keeps this off, noting he doesn't rely on obscurity for security. |
| **Cross-profile shared clipboard** | Follow defaults (allow sharing) | Controls whether the clipboard is shared between the parent user and the private space. Can be changed per personal preference. |
| **Install available apps** | — | Shows a list of all apps installed in the current user profile; installing into Private Space is done by toggling next to each app. |
| **End session immediately on lock** | — | Prevents delayed locking of storage when locking the private space, making it behave like ending a session on a secondary user (requires strong authentication to re-unlock). The presenter admits he doesn't fully understand this option but assumes enabling it is harmless. |

---

## Installing Apps into Private Space

- **Method 1:** Tap the **Install** button inside the private space — this opens the **GrapheneOS app store**, from which you can install Google Play Store, Play Services, and other apps.
- **Method 2:** Use **Install available apps** in settings — presents a list of apps already installed in the current user profile; toggle each one to install a copy into the private space.

### Identifying private space apps

- Each app installed in Private Space displays a **shield-and-key icon** in the bottom-right corner of its app icon.
- When searching apps by name (e.g. "Molly"), this icon lets you distinguish the private space version from the main profile version.
- When an app is open, a **private space icon appears in the top-right corner**, confirming you're in the private space instance.

### Practical example

You could have **Signal** installed in both your main profile (with one phone number) and in Private Space (with a different phone number), and the icons make it easy to tell which instance you're using.

---

## VPN Configuration per Profile

- VPN apps installed in the **owner/main profile do not apply** to the private space.
- To verify: connect a VPN in the main profile, check your IP (e.g. via Vanadium), then check the IP in the private space's Vanadium — it will show a different IP (your home/cellular IP, not the VPN exit IP).
- To use a VPN in the private space, you must **install the VPN app separately** within it, sign in, and connect.
- This is the same behaviour as secondary user profiles on GrapheneOS — each profile needs its own VPN installation.
- **Benefit:** you can set different countries or exit IPs per profile.

---

## Presenter's Personal Experience

- Has been testing Private Space for **several weeks** with generally good results.
- Finds it **more convenient** than a separate user profile.
- Noted some **oddities with the MySudo app** — some calls, texts, and notifications behaved unexpectedly. MySudo's team stated it should be supported in any profile type, so he's continuing testing before fully committing and deleting his secondary user.
- Recommends Private Space as a **great option, especially for newcomers**, as it makes the transition easier than managing a separate user profile.

---

## Summary of Significant Points

1. **Private Space is available in all user profiles** (updated since the original announcement).
2. It is the **recommended replacement** for work profiles managed by apps like Shelter.
3. It provides the **same isolation** as secondary user profiles but is **more convenient**.
4. **Sandboxed Google Play, contact scopes, storage scopes** all have full support.
5. **VPN configurations are entirely separate** per profile — each must be set up independently.
6. **Notifications and background activity stop** when the space is locked — unsuitable for critical/medical apps.
7. Apps can be installed via the **GrapheneOS app store** or by toggling from the **Install available apps** list.
8. Private space apps are identifiable by a **shield-and-key icon**.
9. Settings include **auto-lock behaviour**, **hide private space**, **clipboard sharing**, and **immediate session end on lock**.
