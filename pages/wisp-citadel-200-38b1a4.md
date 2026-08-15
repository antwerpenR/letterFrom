---
source: https://rogerprice.me/wisp-citadel-200
clipped: '2026-08-15T15:13:01+00:00'
title: Wisp - Citadel 200
site: Letter from ...around the world
published: '2026-04-28T12:25:16.000Z'
---

# Wisp - Citadel 200

# Wisp - Citadel 200

![Wisp - Citadel 200](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/04/citadel200.png)

This Citadel Dispatch interview from 21 April 2026 features **Matt Odell** speaking with developer **UTXO** about his new Android Nostr client **Wisp**, the challenges of Nostr adoption and the intersection of AI with decentralised social media.

> [!image]
> [![Click for the full interview and discussion](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/04/image-38.png)](https://serve.podhome.fm/episodepage/CitadelDispatch/cd200-utxo--wisp--better-nostr?ref=rogerprice.me)
> Click for the full interview and discussion

[citadel200-wisp-transcript

Click for full transcript of the interview

citadel200-wisp-transcript.txt

70 KB

download-circle](https://rogerprice.me/content/files/2026/04/citadel200-wisp-transcript.txt "Download")

### **Wisp: A New Approach to Nostr Clients**

UTXO built **Wisp** (wisp.mobile) after becoming frustrated with existing Android Nostr apps that lacked basic features like gift keyboards and suffered from instability. His core strategy centres on **UX stability and speed**—competing with big tech apps without taking shortcuts like centralised servers. Wisp implements the **Outbox model**, allowing it to find notes even when users publish to their own relays, which paradoxically makes the app faster by responding from the quickest relay rather than waiting for a single slow server.

The app targets both power users and mainstream adoption. For normies, it offers seamless onboarding: users receive Bitcoin immediately without managing Lightning wallets or understanding relays or private keys. Wisp integrates **Spark Wallet** for easy Lightning onboarding—users can receive Bitcoin without prior holdings, and backups are interoperable with Primal. UTXO made a distinctive UX choice: **seeds are automatically backed up to relays encrypted with the user's NSEC**, meaning users only need their NSEC to recover both their identity and funds.

### **The "Send Money" Experiment: Denominating in Dollars**

One of Wisp's most controversial decisions is **renaming "zaps" to "Send Money"** and **denominating them in dollars** for new users (those signing up with fresh NSECs rather than existing signers like Amber). UTXO's thesis: many people reflexively hate Bitcoin due to associations with "crypto scams" and political figures. By showing dollar amounts with a ₿ symbol (not the Lightning bolt), he hopes to reduce friction for mainstream users.

Matt notes this could increase zap amounts psychologically—sending "21 cents" feels more substantial than "1.5 cents worth of sats," which might appear insulting. However, he flags the risk of confusion when Bitcoin's price fluctuates, citing **Samourai Wallet** removing dollar displays entirely after support complaints about shrinking balances. The "normie mode" remains unreleased pending Google Play approval.

### **Follower Counts and Network Metrics**

The interview delves deeply into **follower count methodology**. UTXO argues accurate counts are impossible on Nostr—what constitutes a "follower" when bots and throwaway NPubs can be generated instantly at zero cost? Wisp's solution: **only show followers within your network** (people you follow who also follow that account). This creates a personalised, reputation-based metric rather than a global number.

Matt suggests this resembles a **reputation score** more than traditional follower counts. He defends Primal's upper-bound approach as necessary for competing with X and TikTok, where users expect inflated numbers. Both agree the "web of trust" concept is more useful than raw counts, though Matt notes the tension between philosophical purity and growth metrics needed to attract users accustomed to mainstream platforms.

### **Nostr Adoption Challenges**

The discussion addresses why **40-50% of the Bitcoin X community actively dislikes Nostr**. UTXO suspects some fear losing follower counts built on Twitter; Matt acknowledges diminished reach but values Nostr's censorship resistance. Both express frustration that high-value Bitcoiners like **Saifedean** post infrequently on Nostr despite its benefits.

Matt highlights **survivorship bias**: the remaining Nostr users love it precisely because 97-98% of early triallists left. To attract that lost majority, the product experience must improve. UTXO notes his own past aggressiveness may have alienated some potential adopters.

### **AI Integration and Local Models**

UTXO reveals heavy use of **AI for development**, calling **Claude "absolutely insane"** for coding tasks. He runs **Qwen 3.6 locally on four RTX 3090 GPUs** (a ~$15,000 build purchased cheaper years ago), serving it via VLLM for Nostr users to access. This local setup handles lighter tasks while Claude manages complex development.

For spam detection, Wisp runs **lightweight local models on-device** to identify bot replies without relying on centralised services. This "end spam" system only filters notifications, preserving feed posts from legitimate bots like **Recbot**.

Matt and UTXO discuss AI's economic implications. UTXO believes **LLMs are approaching capability limits**—future gains will be in speed, cost, and consistency rather than 10x intelligence improvements. He predicts **job creation** around AI implementation rather than mass unemployment. Matt disagrees, foreseeing significant disruption at big tech companies where AI could replace substantial portions of 190,000-employee workforces like Google's.

### **Significant and Surprising Points**

- **Automatic seed backup to relays**: Wisp backs up encrypted seeds automatically, saving users who forget to manually save recovery phrase
- **Dollar-denominated "Send Money"**: Renaming zaps and showing dollar amounts for new users to reduce Bitcoin stigma
- **Network-relative follower counts**: Wisp only displays followers within your existing network, creating a personalised reputation metric
- **Local AI spam filtering**: On-device lightweight models filter bot replies without centralised dependencies
- **Qwen 3.6 local deployment**: Four RTX 3090 GPUs running open-source models comparable to Claude for chat tasks
- **Spark Wallet integration**: Seamless Lightning onboarding where users receive Bitcoin without prior holdings or liquidity management
- **Kick.com streamer outreach**: UTXO's strategy to attract banned Twitch streamers to Nostr as a viable uncensorable alternative
- **Recbot's relay solution**: Creating a personal relay to bypass rate limits during price spikes, demonstrating Nostr's unstoppable architecture
- **Nostr's "lurker" problem**: 90% of users may be non-posting readers, complicating active user metrics
- **Claude Max value proposition**: UTXO estimates $300/month provides $5,000-30,000 worth of developer output

### **Future Outlook**

UTXO hints at **potential iOS development** ("stay tuned") and continues refining Wisp's marketing. Both agree Nostr needs **content creators with existing audiences**—even occasional cross-posting from figures like **IShowSpeed** could drive massive adoption. The interview concludes with mutual appreciation for philosophical discussion and an invitation for user feedback on Wisp.
