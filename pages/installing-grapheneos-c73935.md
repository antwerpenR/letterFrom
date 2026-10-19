---
source: https://rogerprice.me/installing-grapheneos
clipped: '2026-09-04T16:54:33+00:00'
title: Installing GrapheneOS
site: Letter from ...around the world
published: '2026-09-02T17:56:26.000Z'
---

# Installing GrapheneOS

# Installing GrapheneOS

![Installing GrapheneOS](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/How-to-install-GrapheneOS-on-Google-Pixel-7_7a_8_8a_9_9a----Setup-for-new-users_1.jpg)

## Prerequisites

Before beginning the installation, the following requirements must be met:

- **Supported device**: A Google Pixel (the video uses the Pixel 7, but the process is similar for other supported Pixels).
- **Supported operating system**: e.g., macOS, Windows, or Linux.
- **Supported browser**: Avoid using Chromium on Ubuntu, as it is broken and will not work — use an alternative such as Google Chrome.
- **Do not use Incognito or private browsing mode** — the installer requires normal browsing mode.
- **Reliable USB cable**: Use the stock cable that came with the device if possible; plug directly into the computer, not through a dongle. Faulty cables are the most common cause of connection issues.
- **Windows users**: Must install the fastboot driver before proceeding.

The presenter strongly advises always consulting the official documentation at **grapheneos.org** rather than relying solely on a video or blog post.

> [!image]
> [![Click to watch the step by step guide - 20 minutes is all you need](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-4.png)](https://youtu.be/ZAZlmYKrwfk?si=aELH8GuKAtGA2Jep&ref=rogerprice.me)
> Click to watch the step by step guide - 20 minutes is all you need

## Key Steps in the Installation Process

### 1. Initial Device Setup (if brand new)

- Power on the device and complete the initial setup **offline** (skip mobile network and Wi-Fi).
- Accept the limited warranty and additional legal terms.
- Optionally set a PIN (good practice, though the phone will be erased shortly).
- Skip Face Unlock and the navigation tutorial.

### 2. Check for System Updates (recommended but optional)

- Connect to Wi-Fi → go to **Settings → System → System update**.
- Install any pending updates before continuing.

### 3. Enable OEM Unlocking

- Enable **Developer Options**: Settings → About phone → tap **Build number** repeatedly until prompted for PIN.
- Go to **Settings → System → Developer options** and toggle **OEM unlocking**.

> **Important caveat**: If the phone was purchased brand new, it must first connect to the internet so it can check whether the serial number is carrier-locked. Devices locked by carriers (typically Verizon-based) **cannot** enable OEM unlocking — the only option is to return or sell the device and buy a factory-unlocked one. If buying a used device, ask the seller to send a photo confirming OEM unlocking is available before purchasing.

### 4. Boot into the Bootloader Interface

- Reboot the phone and **hold the volume down button** while it restarts.
- If successful, the bootloader interface screen will appear; if not, the phone boots normally — try again.
- **Windows users**: Install the fastboot driver if not already present.
- **Common issue**: If the computer does not see the phone, try a different USB cable (the stock cable is best) and plug directly into the computer (no dongles).

### 5. Connect the Phone

- Plug the USB cable into the device and computer.
- On the web installer page, select **Connect** when prompted (the device should appear in the list).

### 6. Unlock the Bootloader

> **Warning**: Unlocking the bootloader **wipes all data** on the device. Back up everything (contacts, calendar, photos, messages) beforehand — it is unrecoverable.

- Select **Unlock bootloader** on the web page.
- On the phone screen, use volume buttons to change the selection from 'do not unlock' to **unlock the bootloader**, then press the power button to confirm.
- Device state should change to **red — unlocked**.

### 7. Download the Factory Images

- Select **Download release** on the web installer.
- Download time varies with internet speed (could take minutes to an hour).

### 8. Flash the Release

- Select **Flash release**.
- **Do not interact with the device at all** until flashing completes — the script replaces the existing OS and wipes all data.
- Once complete, the screen will say 'flashed' and the phone returns to the bootloader interface.

### 9. Lock the Bootloader (Critical)

This step is described as **extremely important** for security.

- Select **Lock bootloader** on the web page.
- On the phone, use volume buttons to change to **lock the bootloader**, then press power to confirm.
- Device state should change to **green — locked**.

### 10. Boot the OS

- With 'start' selected in the bootloader interface, press the power button to boot.
- A warning screen about loading a different operating system is **normal** for non-stock OS installations.
- The Google splash screen and GrapheneOS boot animation are also normal. Initial boot takes a minute.

### 11. GrapheneOS Initial Setup

- Select **Start**, choose language and time zone.
- Optionally skip Wi-Fi, SIM, and location services.
- **Set a PIN** (use something other than 0000 or 12345).
- Optionally set up fingerprint.
- Skip backup restore for a new installation, then press **Start**.

### 12. Disable OEM Unlocking and Developer Options

- Re-enable Developer Options (Settings → About phone → Build number → enter PIN).
- Go to **Settings → System → Developer options**.
- **Disable OEM unlocking** — a restart is required.
- **Disable Developer options** — a restart is required.

### 13. Verify the Boot Key Hash

- On the boot warning screen, **press the power button to pause the boot**.
- Verify that the **boot key hash string** displayed on the device matches the one shown on the GrapheneOS web page.
  - This applies to Pixel 6 and newer devices.
- Once confirmed, press the power button again to resume booting.

---

## Post-Install: Setting Up Sandboxed Google Play Services (for New Users)

GrapheneOS offers **sandboxed Google Play services**, which run as standard apps with no special access or privileges — unlike stock Android, where Play services bypass the app sandbox with highly privileged access. This is the recommended simplest approach for users new to GrapheneOS.

### Steps

1. Connect to Wi-Fi.
2. Open the **Apps** app → select **Google Play Store**.
3. This also installs **Google Services Framework** and **Google Play Services** — select **Install all**.
4. Wait approximately five minutes for completion.
5. Once installed, the Play Store appears in the app drawer and functions as on stock Android.
6. Sign in (consider creating a separate Google account for additional privacy).
7. Download your apps and get started.

The presenter recommends reading the official GrapheneOS documentation on sandboxed Play services and the usage guide, which cover how it works, configuration, and limitations.

> For users wanting more privacy, Play services can alternatively be installed in a **separate user profile** (covered in a separate video by the same creator).

---

## Final Advice

The presenter's closing guidance:

- **Privacy and security is a journey** — don't try to do everything at once.
- If you change too much at once, it becomes hard to maintain the habit.
- Take it step by step; every little bit helps.

---
