---
source: https://rogerprice.me/ibek-and-unstoppable
clipped: '2026-09-04T16:54:36+00:00'
title: Ibek and Unstoppable
site: Letter from ...around the world
published: '2026-09-02T10:51:48.000Z'
---

# Ibek and Unstoppable

# Ibek and Unstoppable

![Ibek and Unstoppable](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/Screenshot-2026-09-02-at-12.48.54.png)

This is a summary of Doug's (Monero Talk) interview with **Ibek**, a co-developer of the **Unstoppable Wallet**, a multi-coin, privacy-focused, self-hosted cryptocurrency wallet.

> [!image]
> ![Click for the full interview - summary and notes below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/08/image-33.png)
> Click for the full interview - summary and notes below

## 1. Ibek's Background

- **Ibek** is a Central Asian name of Turkic origin, common among nations such as Kazakhstan, Turkmenistan, Uzbekistan, and Turkey. He compares it to "John" in the US — a popular but not meaningfully loaded name. It is more prevalent in Central Asia than in Turkey itself.
- He has never attended MoneroKon or met Doug in person.
- He and his team are **distributed across four or five countries**, operate as a **horizontal (non-hierarchical) team**, and are **self-funded** with no external investors.

---

## 2. Crypto Scene in Central Asia

- The region's crypto usage is largely driven by **two factors**:
  1. **Cross-border commerce with China** — many Central Asian nations border China, and small-to-medium entrepreneurs use **stablecoins (USDT)** to conduct trade, because local banks increasingly cannot send or receive US dollars.
  2. **Inflation and dollar preference** — local currencies suffer significant inflation (around 10% in many countries), so people hold dollars for savings and commerce. USDT has become easier to hold and transact than physical dollars or bank-held dollars.
- **Privacy awareness is low** because the economy is still largely **cash-based**. People assume their transactions are private simply because they use cash, and many don't realise that USDT transactions are fully visible to recipients or that Tether can freeze funds.
- Real estate and car purchases are still **mostly cash-based** in many of these countries. Tax burdens are relatively light (roughly 10–20%), and much of the economy is driven by small business owners who interact with the government minimally.
- **Banks are increasingly unable to handle dollar transfers** — many explicitly tell customers they can transact in euros, yuan, rubles, or Turkish lira, but not dollars. This has fuelled the spectacular rise of stablecoins in the region.

### Key insight from Doug

As governments inevitably move to **eliminate cash** and push CBDCs or digital stablecoins, people will realise the need for a truly private cryptocurrency like Monero — because mass surveillance and censorship become trivial once cash is gone.

---

## 3. Ibek's Crypto Origin Story

| Year | Event |
| --- | --- |
| ~2011–2012 | First heard about Bitcoin through a popular consumer tech blog he was running. A contributor wrote an e-book about Bitcoin that became one of the site's most popular publications. |
| 2013 | Took a Udemy course on Bitcoin authored by **Charles Hoskinson** (later founder of Cardano), titled something like "Learn about Bitcoin and stop worrying and live free." Bought his first Bitcoin — **1 BTC for $300 in cash** from a friend's friend who was mining at home (~1 BTC/week). Spent part of it online, held the rest. |
| 2013–2016 | Left the Bitcoin untouched in a wallet (blockchain.info) for ~3 years. |
| 2016 | Running a B2B SaaS startup. The bank began aggressive KYC/due diligence, then **closed all offshore accounts** (~2017). This was the "lightbulb" moment — he understood Bitcoin's real use case: a financial system you can't be shut out of. |
| Early 2017 | Wrapped up clients and **transitioned to crypto full-time**, starting to build what became Unstoppable Wallet. |

---

## 4. Unstoppable Wallet — History and Evolution

### Naming

- Originally called **"Bank Wallet"** (~2017), but users were confused, thinking it offered fiat accounts. Renamed to **"Unstoppable"** (~2019), a name suggested by community member **untraceable**.

### Coin Integration Timeline

| Phase | Coins/Features Added |
| --- | --- |
| 2017–~2019 | **Bitcoin only** — aimed to be the most feature-complete Bitcoin wallet (everything except multi-sig), including advanced features like time-locked transactions. |
| ~2021 | Integrated **EVM/Ethereum** — initially tried to build a fully decentralised Ethereum client for iOS/Android (spent ~5 months), but it was unusable (24-hour sync times). Compromised by going through intermediary services for some chains, which opened the door to adding other blockchains. |
| ~2024 | Began adding **privacy coins**: Dash (first, closest to Bitcoin architecture), then Litecoin (with MimbleWimble), then **Zcash**, and finally **Monero** (last, due to technical complexity). |

- Monero integration was **technically intimidating** — scanning the entire blockchain on every app launch, ensuring stability and no crashes. After adding it, the team felt they "should have done it much earlier."
- The driving force was **user demand** — users repeatedly requested Monero. Ibek emphasises: if you want Monero on a platform, **go request it and get others to do the same**. Builders are motivated by people using their software.
- **No regulatory concerns** about adding Monero — Unstoppable is not an exchange and doesn't custody user funds.

### Monero was added after repeated user requests; the team regrets not adding it sooner.

---

## 5. Business Model and Revenue

Unstoppable's revenue streams have evolved through several phases:

1. **Consulting** — helping third parties integrate their products or build custody solutions for exchanges.
2. **Technical partnerships** — doing technical work for larger entities in exchange for promotion or marketing compensation (since they lack marketing budget).
3. **DeFi builds** — within the partnership model, they built DEXs, launchpads (PumpFun-style alternatives on other chains), and their own chain. This drove traffic to their projects.
4. **Premium version** of the wallet (launched ~2 years ago) — generates some revenue.
5. **Instant swaps** — most recent focus; they take a share of swap volume, particularly through their involvement with **THORChain** (since ~last year).

---

## 6. Premium Features

The premium features focus on **security**, not cosmetic changes. Key features:

### a) Duress Mode (Plausibly Deniable Wallets)

- A wallet can hold **hundreds of wallets** with **unlimited unlock PINs**.
- Different PINs unlock different subsets of wallets — one PIN opens everything, another opens only half, another opens just a couple.
- **Motivation**: real-world reports of people being robbed by police officers or subjected to "wrench attacks" (e.g., a person lost 20 BTC after being forced to unlock their phone in police custody).
- **Design challenge**: the unlocked wallet must be a **usable, real wallet** (not an obvious decoy), and the attacker must not be able to detect the feature is active.
- Now **available for free** on F-Droid (open-source Android); the team is considering making it free across all distributions.

### b) Address Poisoning Attack Protection

- Unstoppable was **the first wallet to build this** (~2 years ago).
- Protects against attacks where a user receives a small transaction from an address that closely resembles one they've recently interacted with (matching first/last few characters), tricking them into sending funds to the wrong address.

### c) Blacklist/Sanctions Address Checking

- Optionally checks whether a destination address appears on **public blacklist or sanction databases** before sending.
- **Origin story**: The team built a smart contract dealing with USDT that had a bug (related to USDT not adhering to standard token standards, as it was the earliest stablecoin). They worked with Tether to recover ~30,000 USDT (Tether burned and reminted the funds, charging a 10% fee). As part of this process, the smart contract address was **blacklisted by Tether**. Subsequently, **everyone who had ever interacted with that contract had their Binance and OKX accounts frozen** — the exchanges saw the blacklist on-chain without investigating the reason.
- This experience motivated the feature. It was initially **on by default**, but after user complaints it was made **opt-in/on-demand**.
- The checks go directly from the user's device to the databases — **Unstoppable does not see or intermediate the checks**.

---

## 7. What Makes Unstoppable a "Privacy Wallet"?

- **No accounts, no KYC** — the wallet has no knowledge of users' coins, balances, or identities.
- The only data the server sees is that **someone is requesting price/coin rates** (e.g., "Bitcoin is $67,000 today, Monero is ~$480").
- They don't even know how many people use the app — their only estimates come from **Google/Apple download counts** and rate-server requests.
- For swaps, they entered the space to fix problems with existing instant swaps (blind swaps where users had no visibility into what they'd receive). They've improved security and privacy in the swap experience.
- **Honest assessment from Ibek**: Unstoppable is **not the most private wallet**. A truly private wallet would be Monero-only, with all communication going through Tor (and even Tor has attack surfaces).

---

## 8. Why a Monero User Should Consider Unstoppable

- Monero users are typically **not single-coin users** — they also transact in BTC, USDT, and other cryptocurrencies for business and commerce.
- Unstoppable aims to be a **single wallet that covers all needs**: Monero for privacy/hodling, plus support for other chains, swaps (including DeFi swaps like USDT-ERC20 to USDT-TRC20), and more.
- They are **conservative** about adding features — no crypto cards, no gift cards — but believe users shouldn't need five different apps.
- Ibek acknowledges and credits other wallets: **Cake Wallet** ("a great wallet," thanks the team for doing difficult pioneering work), **Edge Wallet**, and **Monero Only** (a fork of Unstoppable's wallet, which they appreciate).

---

## 9. THORChain and Monero

### Ibek's perspective

- THORChain is part of the **"freedom stack"** — one of ~10 essential technologies for long-term freedom (alongside Monero, Bitcoin, Zcash, and open-source AI).
- It serves as a **decentralised bridge** between cryptocurrencies, enabling cross-chain swaps without intermediaries.
- When crypto grows (e.g., Bitcoin hitting new highs), capital flows through bridges like THORChain to other quality projects, dragging them upward too.
- Unstoppable initially wanted to work with THORChain **for free**; the relationship later became a business partnership.
- **Monero on THORChain**: the code to enable Monero pools was **published live on the 27th** (two days before the interview). Ibek expects it to go live "soon" but acknowledges "soon" has been the status for a while. Pools will likely start with **limited liquidity for 1–2 weeks**. There are expectations of a **volume surge** once privacy coins go live, partly driven by a novel fee-sharing mechanism.
- Once live, Monero swaps should be available **immediately** in all wallets that integrate THORChain, including Unstoppable.

### Doug's perspective (more critical)

- Doug is **rooting for THORChain** but disappointed by its instability (it was down the day before the interview), its over-reliance on marketing, and its handling of security researchers like **Luke Parker** (who found exploits but wasn't given proper credit).
- He notes it sometimes seems like only **one or two people** are making core decisions, despite the project's decentralised structure.
- He's also waiting for **Serai DEX** to launch as an alternative.
- Ibek responds that THORChain's decentralised nature is a double-edged sword — no single entity makes decisions, but this also makes it **less efficient** than centrally-led organisations. He advises THORChain to **focus less on marketing and more on building a good product**.

---

## 10. The Four Projects Unstoppable's Team Believes In

| Project | Role / Significance |
| --- | --- |
| **Bitcoin** | "The classic" — not perfect, not private, but the one that broke through. Big and established. |
| **Monero** | "The ethos" — the community that stays no matter what, even at personal/financial risk. Has what Bitcoin lost — the cypherpunk spirit. |
| **Zcash** | "The cryptography" — valued for inventing and advancing cryptographic techniques. |
| **RUNE (THORChain)** | "The decentralised bridge" — essential infrastructure connecting the ecosystem. |

Ibek notes some team members have different individual preferences, but this is the **general consensus**.

---

## 11. Monero vs Zcash — Long-Term Outlook

- Ibek does **not** see them as direct competitors. He believes both will grow, and if one does 10×, the other will likely do ~8×, because both have dedicated communities.
- They serve somewhat different purposes: Zcash has **optional privacy** and is exploring **shielded assets** (tokens on the blockchain, similar to Zano); Monero has **privacy by default**.
- **Zano** is also mentioned as a smaller but powerful contender in the privacy coin space.
- **Zcash recently suffered a hack** but was able to remedy it. Ibek notes that with AI advancing rapidly and computing power becoming more accessible, it's uncertain which projects will sustain their privacy promises long-term.
- He advocates against **"divide and conquer"** tribalism — being loyal to a single coin is fine, but blindly dismissing others without constructive reasoning harms everyone.

---
