---
source: https://rogerprice.me/surveillance-report
clipped: '2026-08-15T15:11:39+00:00'
title: Surveillance Report
site: Letter from ...around the world
published: '2026-07-02T09:03:59.000Z'
---

# Surveillance Report

# Surveillance Report

![Surveillance Report](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/Apple-Just-Downgraded-Privacy.-Google-Did-Too.jpg)

*Review of the weekly Techlore Surveillance Report transcript, dated around late June 2026. The episode covers threats to security, privacy, and digital freedom.*

> [!image]
> [![Click to listen to Henry talk you through the week's updates](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/06/image-47.png)](https://www.youtube.com/watch?v=4sJJtd1LgL8&ref=rogerprice.me)
> Click to listen to Henry talk you through the week's updates

## 1. Apple — Hide My Email Domain Downgrade

**Significant points:**

- Apple's **Hide My Email** feature currently generates alias addresses under the **icloud.com** domain, forwarding emails to your real Apple account while hiding your actual address from services.
- Apple has notified developers that, in the coming weeks, generated email addresses will move to a new subdomain: **private.icloud.com**.
- The stated purpose is to make it 'easier for apps and websites to know that an email address is private and block users from signing up'.
- This does not change the underlying privacy or security of the service, but it makes alias addresses **easily identifiable and blockable** — a known problem for users of privacy tools (e.g., alternative phone number providers like MySudo or Google Voice are frequently rejected by services).
- Henry argues for a **right to use any provider** — that rejecting non-Gmail/non-iCloud addresses is discriminatory against people who don't use Big Tech providers, tying this to concepts like the DMA and interoperability.
- **TechCrunch reported** that Apple turned over the real account information of a user who generated an anonymised email address — a reminder that aliasing services are **not end-to-end encrypted**; you are trusting Apple as the intermediary.
- **Workaround:** Open-source alternatives (e.g., SimpleLogin, Addy.io) offer multiple domains and support custom domains, which are much harder to block.

**Additional Apple story:**

- An **unpatchable flaw** was found in older Apple chips (A12, A13 — released 2018–2019), affecting phones from the iPhone XS/XR up to the iPhone 11. It opens the door for a potential jailbreak (and thus also represents a vulnerability). Henry frames this as a reminder that older devices are reaching end-of-life, and recommends upgrading (second-hand to avoid e-waste).

---

## 2. Google — IP Address Tracking & Fingerprinting

**Significant points:**

- Google is notifying advertisers that it will begin **using IP addresses for ad measurement and personalisation** across the **EEA, the UK, and Switzerland**, on or shortly after **3 August 2026**.
- The primary concern is **fingerprinting**.
- In **2019**, Chrome engineering director **Justin Schuh** wrote that 'fingerprinting subverts user choice and is wrong because users cannot clear it the way that they can clear cookies.' Henry reverses this stance: Google dropped its prohibition on fingerprinting for advertisers in **December 2024**, explaining why Chrome lacks strong fingerprinting resistance and why Google is open to IP-based tracking.
- Henry notes this aligns with Google's core business model (advertising) and expresses disappointment that there appears to be no floor to how far Google will go.

**Actionable mitigations mentioned:**

- Decline non-essential cookies / engage with consent prompts
- Review ad personalisation settings in your Google account
- Hide your IP address using a **VPN** or **Tor** (more advanced)

---

## 3. Chrome — Killing Ad Blockers (Manifest V3 & MV2 Removal)

**Significant points:**

- **Manifest V2 (MV2)** is the underlying extension technology that has historically powered effective ad blockers. **Manifest V3 (MV3)** is the newer, more restrictive update that limits what extensions can do.
- Google claims MV3 is for better security and permissions; critics argue the decisions were designed to **make ad blocking harder** — a conflict of interest given Google's advertising business and ownership of Chrome, YouTube, etc.
- **uBlock Origin** has had to retire its old extension on Chrome; **uBlock Origin Lite** is MV3-compatible but 'nowhere near as powerful.'
- Chromium until now retained a flag (`ExtensionManifestV2Disabled`) that allowed MV2 extensions to still run. A **new Chromium commit removes that flag entirely**; a Googler confirmed they intend to let it go.
- **9to5Google** notes this will impact other Chromium-based browsers like **Edge and Opera**.
- **Brave** and **Vivaldi** have committed to supporting MV2 for as long as they can. Henry speculates on whether they relied on the flag workaround (now being removed) or found a sustainable alternative path. Brave at least builds ad blocking directly into the browser, bypassing the need for an extension.

---

## 4. Sponsor Segment — Easy Optouts

- A data removal service Henry personally uses to remove personal information from data brokers and people-search websites.
- **$20 per year** (not per month).
- Verified by **Consumer Reports** as tied for the most effective data removal service alongside **Optery**.

---

## 5. Canada — Surveillance Bill (C-22)

**Note:** Henry refers to the bill as 'BC-22' in the transcript; this appears to be a verbal error for **Bill C-22** (the bill is consistently referenced as a Canadian surveillance bill). This is flagged here for accuracy.

**Key concerns of the bill:**

- Requirements for **metadata retention**
- Expanded **information sharing with foreign governments**
- A mechanism to **demand companies create backdoors**, effectively breaking encryption

**Broad opposition from:**

- Citizen Lab
- Canadian Civil Liberties Association
- EFF
- Signal
- Big tech companies (Apple, Google)
- VPN providers

Henry stresses that this is a global issue — 'every domino that falls' matters internationally. The bill has not yet passed but is moving forward without serious debate. Canadians are urged to contact their representatives.

---

## 6. UK — Social Media Ban for Under-16s

**Significant points:**

- The UK plans to **ban social media for under-16s**, inspired by **Australia's failed ban** — which has been 'catastrophic': children get around it, it hasn't demonstrated effectiveness, and it creates internet gatekeeping while ignoring root issues with exploitative companies.
- A quote from **Prime Minister Keir Starmer**: 'This is not something I do lightly, and I will not present it as cost-free, as if social media has brought no benefits to young people, because clearly that is wrong. But government is always about choices, and it's clear to me that a total ban is the right choice.'
- Henry strongly disagrees, arguing:
  - The right choice is **allowing parents to decide** whether their children use these platforms.
  - People should have the choice to use platforms that don't exploit them.
  - The government's framing presents a false dichotomy: either ban platforms + require age verification (a privacy nightmare for children and adults alike), or hold companies accountable and make them safer.
  - The **real problem is the companies**, not children — they should be held liable and forced to create safe environments.
  - Comparison: banning children from parks because parks are dangerous, rather than making the parks safer.
  - Uses Techlore's own **PeerTube server (Techlore.tv)** as an example of safe, non-exploitative video sharing — accessible via RSS, no account required, open source, self-hosted, no advertising surveillance economy.
- The implementation would require **ID or face scans** before accessing social media accounts — which Henry finds deeply concerning.

---

## 7. Arch Linux — AUR Malware Attacks

**Significant points:**

- The **AUR (Arch User Repository)** is a user-contributed, open repository (like an app store but completely open) where anyone can publish packages.
- On **12 June 2026**, what was initially thought to be ~400 compromised packages turned out to be **more than 1,500 packages** containing malware.
- On **14 June 2026**, a **second, more obfuscated sophisticated malware attack** hit the AUR.
- Henry expresses genuine alarm and argues this highlights the **risk of purely community-maintained repositories** without a well-resourced gatekeeper.
- **F-Droid** is cited as a good middle ground — it's on the user's team but also verifies apps (open source, no suspicious domain contacts, flags suspicious behaviour).
- **Recommendation:** Reconsider relying strictly on community-based sources; obtain software from official developers where possible. Henry applies the same philosophy to **Flatpak** — he does not consider a Flatpak a trustworthy way to run Signal on desktop Linux because he won't trust a random community maintainer to push updates for Signal.
- Users who may have installed affected packages should consult show notes for remediation steps.

---

## 8. Defence Bulletin — Data Breaches

| Entity | Details |
| --- | --- |
| **Texas government** | Hackers stole **3 million** driver's licences and passports. Texas residents should check if they were affected. |
| **LastPass** | New breach via a **3CLUE supply chain attack**. No vault data compromised, but customer **names, phone numbers, email addresses, physical addresses, and support case information** were leaked. Concern: downstream phishing and social engineering attacks. LastPass's history is described as 'not the strongest.' |
| **iRhythm** | Cardiac monitoring service disclosed a data breach. Has analysed **2 billion hours** of curated heartbeat data from **12 million** patients. |
| **Kodak** | Confirmed a breach claimed by the **ShinyHunters** extortion gang. Kodak stated only a limited amount of data was accessed. |
| **Madison Square Garden** | Covered by 404 Media; appears to be more of a business/internal data breach rather than customer data. Limited impact expected. |
| **FIFA World Cup portal** | A researcher gained access to **everything** inside the portal — all streams, analytics, internal workings. Could have started/stopped streams, potentially broadcasting to live television. Documented in a blog post; FIFA fixed it quietly after being contacted. Henry describes this as highly entertaining and shareable. |

---

## 9. Defence Bulletin — Threats

| Threat | Details |
| --- | --- |
| **Fortinet 40 sandbox flaw** | Now being exploited in attacks. Fortinet users should investigate. |
| **WordPress — Gravity SMTP plugin** | Flaw addressed in the newest version; users should update. |
| **WordPress — Shared Plugin (supply chain attack)** | Updating to the newest version also affected other plugins: **Product Slider Pro, WooCommerce, Real Testimonials, and Smart Post Show Pro.** |
| **Microsoft Defender — Rogue Planet zero-day** | Patch being worked on (vulnerability disclosed the prior week; fix expected soon). Flagged for friends and family. |
| **Secure Boot keys expiry** | Deadline was **24 June 2026**. Three certificates that cryptographically verify firmware/software during boot expired. Machines that don't update will still function but lose protection against new threats. Windows: check via Windows Security > Device Security > Secure Boot (green checkmark = updated). Most Windows machines auto-update via monthly patches; older machines may need manual attention. Linux users should watch for new shims. |
| **Microsoft Copilot critical vulnerability** | Allowed hackers to steal **2FA codes** from users. Described as one of countless Copilot issues. Must-read for Copilot users. |
| **Apple Beats Studio Buds flaw** | Let hackers spy on conversations. Already patched; fix automatically delivered when headphones are paired and within Bluetooth range of an iPhone, iPad, or Mac. |
| **AMD TSME reversal** | AMD was going to strip **TSME** (memory encryption against physical attacks) from consumer CPUs. After backlash, **reinstated** memory encryption. Henry notes it's handled but 'weird that it had to get that far.' |

---

## 10. Defence Bulletin — FOSS / Open Source Updates

| Project | Version / Update |
| --- | --- |
| **Tor Browser** | 15.0.16 — security updates. |
| **Mozilla Firefox** | 152 — revamped settings, JPEG XL support, easier tab muting. UI overhaul looks good. Also launched a **Firefox Roadmap** detailing future work: tab groups on mobile, PDF editor improvements, VPN on mobile, private window update, containers, ad blocking, 'AI done differently.' Praised for transparency. |
| **Tails** | 7.9 — includes the Tor Browser update; all Tails users should update. |
| **GrapheneOS** | Fully ported to **Android 17**; available soon. Supported devices: Pixel 6a, 7, 7a(?), 8, 8a(?), 10a, and 10 Pro Fold. *(Note: transcript lists '7, 7, 8, 8, 10a' which likely contains transcription errors for device model names.)* |
| **postmarketOS** | 26.06 — GNOME 50, KDE Plasma 6.6, Phosh 55, improved booting. |
| **KDE Plasma** | 6.7 — per-screen virtual desktops, unified theming system, Wayland updates. |
| **AltStore PAL** | Now available in **Brazil** as Apple enables alternative app marketplaces there (matching what Europeans have had). |
| **Proton** | Released **Easy Switch for Business** to help companies migrate away from Google. A similar tool for individuals was previously released. |

---

## 11. Closing Notes

- Supporters can become a 'Techlorian' via the link in show notes — gaining access to an exclusive **Signal community**, Henry's private **RSS feed** (updated throughout the week, including while travelling), and other perks.
- Alternatively, listeners can help by leaving a rating, sharing the episode, or leaving a comment on Spotify, YouTube, etc.
