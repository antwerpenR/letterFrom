---
source: https://rogerprice.me/orion-brave-and-chrome
clipped: '2026-08-15T15:15:47+00:00'
title: Orion, Brave and Chrome
site: Letter from ...around the world
published: '2025-06-06T09:58:08.000Z'
---

# Orion, Brave and Chrome

# Orion, Brave and Chrome

Here's a comparison of Orion, Google Chrome, and Brave browsers based on key aspects like privacy, performance, features, and compatibility, tailored to help you decide which might suit your needs best. The information draws from various sources, including web reviews and user sentiment, while critically examining their claims.

Summary by Grok on 6 June 2025

---

1. Privacy and Security

- Orion:
  - Strengths: Orion markets itself as a zero-telemetry browser, meaning it doesn’t collect user data or "phone home." It blocks all ads and trackers (including first- and third-party) by default and uses fingerprint randomization to prevent tracking via canvas, fonts, or other identifiers. It’s built on WebKit (Safari’s engine), which some argue is less vulnerable than Chromium-based browsers due to its smaller market share and Apple’s ecosystem integration (e.g., KeyChain access).
  - Weaknesses: Orion is not currently fully open-source, which raises concerns for some privacy advocates who prefer transparency to verify security claims. Its privacy features rely heavily on blocking scripts outright, which may break some websites unless users tweak settings. They are [working on it](https://kagi.com/orion/faq.html?ref=rogerprice.me#oss:~:text=Orion%20on%20iOS.-,Is%20Orion%20open%2Dsource%3F,-We%E2%80%99re%20working%20on)
  - Unique Aspects: Offers granular control over extensions, allowing users to limit their scope to specific sites, enhancing security.
- Google Chrome:
  - Strengths: Chrome includes Google’s Safe Browsing feature to protect against malicious sites and supports privacy-focused extensions (**but only a weaker version of uBlock Origin**). It offers Incognito mode, though this only prevents local history storage, not tracking by websites or Google itself.
  - Weaknesses: Chrome is heavily criticized for its data collection practices, as Google’s business model relies on targeted advertising. It collects extensive user data (e.g., browsing history, search queries) unless users opt out or use extensions to mitigate tracking. Privacy advocates often flag Chrome as one of the least private mainstream browsers.
  - Unique Aspects: Its integration with Google services (e.g., Gmail, Drive) makes it convenient for users already in the Google ecosystem, but this comes at the cost of pervasive data tracking.
- Brave:
  - Strengths: Brave is built with privacy as a core focus, featuring default ad and tracker blocking via Brave Shields, which uses public blocklists and machine learning to identify trackers. It blocks cross-site trackers, third-party cookies, and some malware/phishing attempts. Brave also offers a Tor-powered private browsing mode for enhanced anonymity and a privacy-focused search engine (Brave Search) and full support for Manifest V2 and uBlock Origin.
  - Weaknesses: While Brave is privacy-focused, it’s not zero-telemetry like Orion, and some users question its opt-in Brave Rewards program, which involves a cryptocurrency-based ad system that whitelists certain trackers (e.g., from partners like Facebook or Twitter) - but you do not need to opt in!
  - Unique Aspects: Brave Rewards allows users to earn Basic Attention Tokens (BAT) by viewing privacy-respecting ads and tip content creators, aiming to rethink the ad-based web model.

Summary: Orion leads in privacy with its zero-telemetry policy and aggressive script blocking, but its closed-source nature is a drawback - they are [working on this](https://kagi.com/orion/faq.html?ref=rogerprice.me#oss:~:text=Orion%20on%20iOS.-,Is%20Orion%20open%2Dsource%3F,-We%E2%80%99re%20working%20on). Brave offers robust privacy with a unique ad model but isn’t as strict as Orion. Chrome lags significantly in privacy due to Google’s data collection, requiring extensions to match competitors’ protections.

---

2. Performance

- Orion:
  - Strengths: Built on WebKit, Orion is optimized for macOS and iOS, offering superior speed and energy efficiency on Apple devices. Users report it feels faster than Safari, Brave, and Chrome, with immediate page loading and lower memory usage (up to 50% less than Chrome). Its Low Power Mode further reduces battery drain, making it ideal for laptops.
  - Weaknesses: Performance is less tested on non-Apple platforms (e.g., Windows, Android), where it’s less optimized or unavailable. Some websites may load incorrectly due to aggressive blocking unless compatibility mode is used.
- Google Chrome:
  - Strengths: Chrome, built on the Chromium Blink engine, is known for fast page rendering and broad compatibility with web standards. It performs well across platforms (Windows, macOS, Linux, Android, iOS).
  - Weaknesses: Chrome is notoriously resource-heavy, often consuming 3-4GB of RAM with multiple tabs and extensions, leading to slowdowns on lower-end devices. Its energy consumption is higher than Orion or Brave, especially on mobile.
  - Unique Aspects: Recent updates have improved RAM management, but it still lags behind competitors in efficiency.
- Brave:
  - Strengths: Also Chromium-based, Brave is significantly lighter than Chrome, using about one-third the RAM (300-500MB for light workloads) due to its removal of Google’s tracking code and default ad blocking. It loads pages 3x-6x faster than Chrome in some tests, especially on ad-heavy sites.
  - Weaknesses: Benchmark tests (e.g., JetStream 2, Speedometer 2.0) sometimes show Brave slightly slower than Chrome, though real-world differences are minimal. Some websites may require disabling Shields to function properly.
  - Unique Aspects: Its ad-blocking reduces network load, saving mobile data and battery life, particularly on Android and iOS.

Summary: Orion excels in speed and efficiency on macOS/iOS, leveraging WebKit’s lightweight design. Brave outperforms Chrome in resource usage and real-world speed due to ad blocking. Chrome is fast but a resource hog, making it less efficient for heavy workloads or low-spec devices.

---

3. Features and User Experience

- Orion:
  - Strengths: Orion offers a clean, Safari-like interface with macOS-specific features (e.g., native keyboard shortcuts, one-click full-screen, KeyChain integration). It supports Chrome, Firefox, and Safari WebExtensions, providing access to a broader extension ecosystem than Safari. Unique features include Focus Mode (hides address and tab bars for distraction-free browsing), Vertical Tabs, and Floating Windows on iOS.
  - Weaknesses: Extension support is incomplete (about 70% of WebExtensions APIs), leading to occasional bugs (e.g., Bitwarden issues). As a beta browser, it can feel unpolished, with freezes or compatibility issues on some sites.
  - Unique Aspects: Its Apple-inspired design and deep macOS integration (e.g., Dock, full-screen mode) make it feel native, appealing to Mac users seeking a Safari alternative.
- Google Chrome:
  - Strengths: Chrome’s interface is simple, familiar, and consistent across platforms. It offers seamless Google account sync for bookmarks, passwords, and extensions. The Chrome Web Store provides millions of extensions, and features like automatic translation are built-in.
  - Weaknesses: Lacks advanced privacy or customization features out of the box (e.g., no built-in ad blocker). Its simplicity can feel barebones compared to Brave’s privacy tools or Orion’s macOS optimizations.
  - Unique Aspects: Chrome’s dominance (65% market share) ensures broad website compatibility and developer support, making it a reliable default for most users.
- Brave:
  - Strengths: Brave mirrors Chrome’s interface for familiarity but adds privacy-focused features like Brave Shields, Brave Search, and Brave Wallet for cryptocurrency. It supports all Chrome extensions and offers sync via a hash-based system (no email required). Brave News and Rewards integrate content and monetization options.
  - Weaknesses: The crypto-focused features (e.g., Brave Wallet, Rewards) may not appeal to all users, and some find the interface busier than Chrome’s. Shields can break websites, requiring manual tweaks.
  - Unique Aspects: Its IPFS protocol support enables access to decentralized content, and Brave Search offers a privacy-respecting alternative to Google.

Summary: Orion shines for macOS users with its native design and unique features like Focus Mode, but its beta status means occasional bugs. Chrome is the most polished and widely compatible, ideal for simplicity and Google integration. Brave balances Chrome-like familiarity with privacy tools and crypto features, though these may not suit everyone.

---

4. Compatibility and Ecosystem

- Orion:
  - Strengths: Optimized for macOS and iOS, with cross-platform support for Windows and Android (though less mature). Supports Chrome, Firefox, and Safari extensions, reducing dependence on a single ecosystem.
  - Weaknesses: Primarily designed for Apple devices, so Windows/Linux users may find it less polished. Extension compatibility is improving but not yet on par with Chrome or Brave.
  - Availability: Free during beta, but a $5/month subscription is planned post-beta, which may deter some users.
- Google Chrome:
  - Strengths: Available on all major platforms (Windows, macOS, Linux, Android, iOS) with consistent performance and full Chrome Web Store access. Syncs effortlessly with Google services across devices.
  - Weaknesses: Heavy reliance on Google’s ecosystem can feel restrictive for privacy-conscious users or those avoiding Big Tech.
  - Availability: Free, with no subscription model.
- Brave:
  - Strengths: Available on Windows, macOS, Linux, Android, and iOS, with full Chrome Web Store compatibility. Its Chromium base ensures broad website support, and Brave Sync provides a privacy-focused alternative to Google’s sync.
  - Weaknesses: Some features (e.g., Brave Rewards, Wallet) are niche and may not appeal to mainstream users. Occasional website breakage due to Shields requires manual intervention.
  - Availability: Free, with optional Brave Rewards participation.

Summary: Chrome is the most universally compatible, working seamlessly across all platforms and websites. Brave matches Chrome’s compatibility while adding privacy features, making it a strong cross-platform choice. Orion is best for Apple users but less mature on non-Apple platforms.

---

5. Community and Development

- Orion:
  - Developed by Kagi, a small company focused on privacy and user-centric design. Still in beta, with active development but limited transparency due to its non-open-source status. User feedback drives updates, but the community is smaller than Chrome or Brave.
  - Sentiment: Some X users praise Orion for macOS performance and privacy, but its beta status and limited platform support temper enthusiasm.
- Google Chrome:
  - Backed by Google, with a massive developer community and constant updates. Its dominance ensures robust support but also fuels criticism over Google’s monopolistic control and privacy practices.
  - Sentiment: Widely used but increasingly criticized for resource usage and data collection, pushing users toward alternatives.
- Brave:
  - Developed by Brave Software, an independent company founded by Brendan Eich (JavaScript creator). Open-source with a growing community, though smaller than Chrome’s. Brave’s mission to disrupt the ad-based web model resonates with privacy enthusiasts.
  - Sentiment: Popular among privacy-focused users, with strong Reddit and X support, but some criticize its crypto features and occasional website issues.

Summary: Chrome benefits from Google’s resources and ubiquity but faces privacy backlash. Brave has a dedicated privacy community and open-source transparency. Orion’s smaller, beta-stage community is promising but lacks the scale and openness of its competitors.

---

Which Should You Choose?

- Choose Orion if you’re a macOS/iOS user prioritizing privacy, speed, and native Apple integration. It’s ideal for those who want a lightweight, zero-telemetry browser and don’t mind beta-stage quirks or a potential future subscription. Best for Safari users seeking a privacy-focused upgrade.
- Choose Google Chrome if you value simplicity, broad compatibility, and integration with Google services. It’s best for casual users or those tied to Google’s ecosystem who don’t prioritize privacy or can mitigate it with extensions.
- Choose Brave if you want a privacy-focused, Chromium-based browser with Chrome-like familiarity and cross-platform support. It’s ideal for power users who appreciate ad blocking, crypto features, and open-source transparency but are okay with occasional website tweaks.

Critical Note: Orion’s zero-telemetry claim and WebKit base make it a strong privacy contender, but its closed-source nature warrants caution until verified by trusted audits. Chrome’s data collection is a dealbreaker for privacy enthusiasts, while Brave’s crypto focus and partial telemetry may not suit everyone. Test each browser based on your platform and needs, as real-world experience varies.If you want me to dive deeper into any aspect (e.g., specific features, benchmarks, or extension support), let me know!
