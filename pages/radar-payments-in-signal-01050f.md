---
source: https://rogerprice.me/radar-payments-in-signal
clipped: '2026-08-15T15:11:32+00:00'
title: Radar - payments in Signal
site: Letter from ...around the world
published: '2026-07-15T18:52:34.000Z'
---

# Radar - payments in Signal

# Radar - payments in Signal

![Radar - payments in Signal](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/Bitcoin-in-Your-Signal-Chat-----Radar---s-Bold-Move-with-Seth-for-Privacy-_-SLP754.jpg)

Click below to listen to the full interview - Stephan's new "Fast format"

> [!image]
> [![Click for the full interiew - key points are below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/07/image-14.png)](https://www.youtube.com/watch?v=WSTlsfyuHwc&ref=rogerprice.me)
> Click for the full interiew - key points are below

### 1. Motivation: Why Build a Bitcoin Messenger?

- The core observation is that private messaging and payments have remained artificially separated. Existing combined platforms (WeChat Pay, Facebook Messenger payments, Cash App messaging) all rely on central custodians, banks, and KYC — they are privacy-invasive and lack Signal-grade private messaging.
- Radar's goal is to let you pay the people you already chat with directly, removing the friction of switching between a messaging app and a separate payment app (copying Lightning invoices, asking for cash tags, etc.).
- The maturation of Lightning via Spark and the Breeze SDK made the user experience good enough that non-Bitcoin-ideologues would tolerate it.

### 2. How Radar Works for a Normal User

- Built on Signal's messaging network and protocol — contacts and chats carry over.
- A Bitcoin button sits at the bottom of the chat input where you normally type text. Tapping it, entering an amount, and hitting send completes a payment.
- Everything is **self-custodial**. Keys can be backed up via seed phrase, but they are also automatically encrypted and backed up to the user's Signal profile by default — a design choice aimed at non-Bitcoin-native users who may not manage seed phrases.

### 3. Signal Compatibility & Portability

- Radar is fully Signal-compliant. You can bring your existing Signal account, contacts, username, and group memberships into Radar.
- Migration path: create a Signal cloud backup (called "backups beta" in settings), save the recovery key, then enter that key when setting up Radar and selecting "migrating from Signal."
- Even if you skip restoring messages, you remain in all your existing group chats — they propagate as messages arrive.
- Group chats work identically, but **payments are currently limited to one-on-one DMs**. Group payment features (e.g. splitting bills, shared gift purchases) are planned.

### 4. Spark Integration — Under the Hood

- Regular payments within Radar are **Spark-to-Spark**, not technically over Lightning.
- However, Spark in Radar is Lightning-enabled, meaning users can:
  - Pay any external Lightning wallet (Wallet of Satoshi, Cake Wallet, Phoenix, Zeus) via Lightning invoices, LN URLs, or BOLT 12.
  - Top up their Radar balance from any external Lightning wallet.
- Users hold their own keys for self-custody within Spark.
- **Trust model:** You trust that at least one Spark operator is honest. If all operators plus a previous signer are dishonest, they could collude to double-spend. Multiple independent Spark operators exist to mitigate this.
- **Unilateral exit:** Not yet available directly within Radar (planned), but possible via a CLI tool in Spark currently.
- Onchain receiving is supported but automatically converted into Spark. The 12-word seed phrase is compatible across Spark-compatible wallets (e.g. Wallet of Satoshi, Cake Wallet).
- Onchain payouts are possible but slow — Seth indicates **six confirmations** are required, similar to a Liquid peg-out.

### 5. Payment Seamlessness & Offline Receiving

- Payments are near-instant — no confirmation waiting, no inbound liquidity management, no liquidity concerns for the receiver.
- Users can add a note/comment to a payment.
- **Offline receiving works** via Spark-to-Spark: you do not need to be online to receive payments. This is particularly relevant for a messaging app that users open frequently but not constantly.

### 6. Lightning Address

- Every user gets a randomly generated Lightning address (`@cake.` or `@radar.cash` domain) within the app.
- Users can customise it, subject to availability.

### 7. Positioning — Not "Another Bitcoin Wallet"

- Seth argues the market for standalone Bitcoin wallets is relatively small, while the market for messaging + payments is essentially everyone on Earth (citing Telegram, WeChat/WePay).
- The strategy is to get Bitcoin into the hands of people who would never download Cake Wallet, Zeus, or Phoenix — by meeting them where they already are (Signal).
- Users discover they can send money permissionlessly without providing ID or linking a bank account, which shifts their perspective.

### 8. Limits and Risk Categorisation

- There is **no technical maximum** on transaction size or balance.
- Radar is explicitly categorised as a **hot wallet** — users should not store more than they are willing to lose. Life savings belong in a hardware wallet with a separately backed-up seed phrase.

### 9. Backup & Recovery — Two Paths

| Path | Description |
| --- | --- |
| **Default (automatic)** | Private keys are encrypted and stored in the user's Signal profile. Not even Signal can access them — only the user, with their PIN code and phone number. If the account is compromised, the attacker already has the phone number and PIN, so the wallet loss is a secondary concern. |
| **Seed phrase (optional)** | A standard 12-word seed phrase. Once funds are first received, the user is prompted to back up and verify it in the payments tab. This seed is compatible with any Spark-compatible wallet. |

### 10. Privacy Architecture — Separation of Concerns

This is one of the most significant sections. Seth emphasises that **no single entity has full visibility** across all layers:

| Entity | What They Can See | What They Cannot See |
| --- | --- | --- |
| **Radar** | Nothing — no analytics, no visibility into user activity | Everything |
| **Signal** | Phone number and username (they host the messaging network) | Payment details — payments are sent as encrypted Signal messages. Signal cannot tell if a message is a payment, whether it is Bitcoin or MobileCoin, or who it is between. They cannot connect phone numbers/ usernames to Lightning or Spark transactions. They do not even know the user is a Spark/Lightning/Bitcoin user. |
| **Spark operators** | Spark transaction data | They do not know the user is a Radar user, do not know the user is on Signal, and never receive the user's phone number or Signal username. |

- Seth acknowledges the phone number requirement is "a little bit annoying" but notes it works well for spam prevention, which is why Signal retains it.
- He considers privacy concerns "usually a little bit overblown" given this separation.

### 11. Risk: Signal Could Block Radar

- Signal uses a **centralised server architecture** with open-source server code, but they control who can access their servers.
- In theory, Signal could block Radar's user agent strings.
- Signal has no legal claim against Radar.
- Radar is **donating monthly to the Signal Foundation** and plans to ramp up donations as it grows — framing Radar as complementary, not competitive.
- There is also a scenario where Signal adds Bitcoin natively, which Seth considers a win regardless.

### 12. Other Signal Alternative Clients

- **Molly** — a long-standing alternative Signal client, popular in the GrapheneOS / hardcore Android community. Focuses on security hardening (encrypted database at rest, so data is inaccessible without PIN/password if the phone is stolen). Has operated without issues.
- Historical animosity toward alternative clients existed years ago when "Moxy" was around, but the current Signal stance is unclear.
- Seth notes that Signal is notably inaccessible — despite nearly a decade in the privacy space with connections to every major privacy organisation, he has no contact with Signal. They "play things close to the chest," which he attributes to the scrutiny they face (e.g. fighting chat control legislation).

### 13. Fees & Monetisation

- **No monetisation model at launch.**
- The only fees are network-level:
  - **Spark-to-Spark:** approximately **2 sats per transaction**.
  - **Lightning:** standard routing fees for the specific payment.
- **Future monetisation plans:** adding fiat on-ramps (debit card, credit card, Apple Pay, Google Pay) so non-Bitcoin users can top up — this would be a revenue source.
- Other undisclosed monetisation features are in development.

### 14. Relationship Between Radar and Cake Wallet

- **Separate companies.** Radar is a new company and new product, but built by the same underlying team.
- Shared leadership: Seth is COO of both; the founder/CEO is shared.
- **Funding differences:**

|  | Cake Wallet | Radar |
| --- | --- | --- |
| **Funding** | Self-funded, bootstrapped by Vic starting in 2018, no VC | VC-backed — first investor is Ego Death Capital, with others potentially investing |
| **Approach** | Established standalone wallet | Bitcoin-integrated messaging app |

- Learnings flow bidirectionally between the two projects due to shared leadership.

### 15. Cake Wallet — Silent Payments & Frigate

- Stephan references a prior episode with **Craig Raw** about **silent payments** and **Frigate** (a GPU-accelerated Electrum server for Silent Payments, developed under the Sparrow Wallet project).
- Cake Wallet has been improving a "hardcore" client-side sync approach where tweaked data is pulled from a remote server and all computation happens locally. This gives **near-perfect privacy from the node** — the node only knows which block heights you want to sync and cannot determine which payments are yours.
- **Frigate's trade-off:** scanning happens server-side (you provide a preview key, not spending ability), so you must trust the server not to log which payments are yours — you lose some privacy from the node.
- The hardcore approach's UX is not good enough to be sustainable, so Cake Wallet is **looking deeply into Frigate** and has deployed a production Frigate server for internal testing.
- Still undecided whether to default to Frigate due to the privacy differences.
- Seth sees Frigate as a "worthwhile in-between" — not as private as full client-side computation, but far better than the current Bitcoin wallet norm (where a wallet reveals all its addresses and future addresses to a node).
- Stephan notes that without Frigate, there are higher scanning/computational costs borne by the company.

### 16. Where to Find Radar

- Website: **radar.cash** (inferred from the Lightning address domain `@radar.cash` referenced in the transcript).
- Social media: **@radarchat** on X and other platforms.

---

## Extracted Lists

### List 1: Existing Combined Messaging + Payment Platforms (Cited as Centralised/KYC Precedents)

- WeChat Pay
- Facebook Messenger (payments)
- Cash App (light messaging)
- Telegram (referenced for combined messaging + payments popularity)
- WeChat / WePay (referenced again for popularity)

### List 2: External Lightning Wallets Compatible with Radar (for Sending/Receiving)

- Wallet of Satoshi
- Cake Wallet
- Phoenix
- Zeus

### List 3: Lightning Payment Formats Supported

- Lightning invoices
- LN URLs
- BOLT 12

### List 4: Spark-Compatible Wallets (for Seed Phrase Restoration)

- Wallet of Satoshi
- Cake Wallet

### List 5: Planned Future Features

- Group chat payments (e.g. splitting bills, shared purchases)
- Unilateral exit from Spark directly within Radar (currently CLI-only)
- Fiat on-ramps: debit card, credit card, Apple Pay, Google Pay
- Other undisclosed monetisation features

### List 6: Payment Flow Steps (as Described by Seth)

1. Open the chat with the contact
2. Tap the Bitcoin button at the bottom of the message input
3. Enter the amount
4. Optionally add a note/comment
5. Hit send
6. Recipient receives it instantly

### List 7: Signal Migration Steps

1. In Signal, create a cloud backup (Settings → "backups beta")
2. Save the recovery key provided
3. Open Radar and select "migrating from Signal"
4. Enter the recovery key
5. Backup restores — contacts, groups, and username carry over

### List 8: Signal Alternative Clients Mentioned

- **Molly** — long-standing, security-hardened, popular with GrapheneOS users; encrypted database at rest; no reported issues

### List 9: Future Fiat On-Ramp Methods Planned

- Debit card
- Credit card
- Apple Pay
- Google Pay

### List 10: Privacy Separation — Entities and Their Visibility

| Entity | Sees | Does Not See |
| --- | --- | --- |
| Radar | Nothing (no analytics) | All user activity |
| Signal | Phone number, username | Payment content, payment identity, whether messages are payments, Bitcoin usage, Spark/Lightning usage |
| Spark operators | Spark transaction data | Radar usage, Signal usage, phone number, Signal username |

---

## Transcript Correction Log

The following corrections have been applied relative to the raw auto-generated transcript and my earlier review:

| Transcript (Garbled) | Corrected (Confirmed) | Basis |
| --- | --- | --- |
| "Stefan Loa podcast" | **Stephan Livera Podcast** | Official episode page at stephanlivera.com/episode/754 |
| "Craig Roar" | **Craig Raw** | Creator of Sparrow Wallet; confirmed via Citadel Dispatch CD199 and SLP748 |
| "frigot" / "Fri" / "Frigate" (inconsistent) | **Frigate** (standardised throughout) | GitHub repo `sparrowwallet/frigate`; Craig Raw's own descriptions |
| "Ego Def Capital" | **Ego Death Capital** | Known Bitcoin-focused VC; standard spelling |
| "watoshi" | **Wallet of Satoshi** | Standard Lightning wallet name |
| "Ellen URLs" | **LN URLs** | Lightning protocol standard |
| "bolt 12" | **BOLT 12** | Lightning specification (capitalised) |
| "graphine OS" | **GrapheneOS** | Standard spelling of the Android OS |
| "fungeability" | **fungibility** | Standard spelling |
| "stats" (line 238) | **sats** (satoshis) | Context: transaction fee of ~2 sats |
| "pawned" | **pwned** (compromised) | Standard term |
| "selfunded" | **self-funded** | Standard spelling |
| "timeconuming" | **time-consuming** | Standard spelling |

**Remaining items that could not be fully verified from the transcript alone:**

- **"Vic"** — referenced as the person who bootstrapped Cake Wallet starting in 2018. This appears in the transcript as a first name; the full name is not stated.
- **Radar's website domain** — Seth says "radar" without clearly articulating the full domain. `radar.cash` is inferred from the Lightning address domain stated elsewhere in the transcript but is not explicitly confirmed as the website URL.

**References**

---

1. [Bitcoin in Your Signal Chat – Radar’s Bold Move with Seth for Privacy ...](https://stephanlivera.com/episode/754/?ref=rogerprice.me) (32%) ↩︎
2. [sparrowwallet/frigate: Frigate Electrum Server](https://github.com/sparrowwallet/frigate?ref=rogerprice.me) (49%) ↩︎
3. [Silent Payments as the next st… - Stephan Livera... - Apple Podcasts](https://podcasts.apple.com/us/podcast/silent-payments-as-the-next-step-forward-slp748/id1415720320?i=1000774348577&ref=rogerprice.me) (20%) ↩︎
