---
source: https://rogerprice.me/john-woods-on-monero
clipped: '2026-08-15T15:11:52+00:00'
title: John Woods on Monero
site: Letter from ...around the world
published: '2026-06-24T08:30:36.000Z'
---

# John Woods on Monero

# John Woods on Monero

![John Woods on Monero](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/06/Screenshot-2026-06-24-at-10.30.08.png)

This is a rich discussion between **John Woods** and **Douglas (Monero Talk host)** covering Monero, Zcash, privacy architecture, and Woods' current project Nillion. Here's a structured breakdown of the key themes:

---

> [!bookmark]
> [Monero’s influence on the privacy industry w/ John Woods | EPI 387](https://www.monerotalk.live/monerotalk-387?ref=rogerprice.me)
> TODAY’S SHOW: Douglas Tuman chats with John Woods, the CEO of Nillion - a company focused on building decentralised privacy. Their discussion focuses on Monero’s current position within the privacy ecosystem and the growing debate between Monero and Zcash. John explains how concerns around fungibility and privacy led him from Bitcoin to Monero before examining the health of the Monero community, emerging privacy technologies, and the implications of Zcash’s recent Orchard vulnerability. The conversation explores the tradeoffs between privacy and auditability, differing trust assumptions in cryptocurrency design, and Monero’s future roadmap, including FCMP++, Seraphis, Jamtis, and post-quantum considerations.
> — Monero Talk | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/cover\_medium-f172452a-f018-4434-9ff9-86c67d1f352b.jpg)

## John Woods' Background

- Software engineer with a security focus (worked at Ericsson, banks)
- Exposed to Bitcoin very early (received ~9-10 BTC when they were worth a few dollars each) — **lost them on Mt. Gox**
- Got into Monero in late 2015/early 2016 after Googling "most private cryptocurrency"
- Professional crypto career: worked on **Ethereum** (consensus), **Cardano** (led architecture & applied crypto), **Algorand** (CTO)
- Currently works at **Nillion**, a much smaller privacy compute project

---

## Monero vs. Zcash — The Core Argument

Woods' thesis rests on **two architectural philosophies**:

|  | **Monero** | **Zcash** |
| --- | --- | --- |
| **Privacy model** | Layered "pancake stack" — ring signatures, stealth addresses, Bulletproofs, RingCT, (soon FCMP++) each doing a specific job | One massive ZK circuit handling sender, receiver, and amount privacy all at once |
| **Privacy default** | **Mandatory** — every transaction is private | **Optional** — most transactions are transparent, destroying the anonymity set |
| **Bug impact** | If one primitive fails, others still provide protection ("five smaller guys at the door") | A single bug in the monolithic circuit can be **catastrophic** |
| **Anonymity set** | Even pre-FCMP, the crowd you hide in is large; with FCMP++ it becomes the entire blockchain | The Orchard shielded pool contains a **tiny fraction** of total Zcash supply |
| **Production readiness** | Battle-tested, 100% uptime through multiple upgrades | Not ready for serious privacy use in Woods' view |

---

## The Zcash Orchard Exploit — Woods' Detailed Critique

The most substantive part of the discussion. Woods explains the bug in lay terms:

1. **The flaw**: The ZK circuit failed to properly validate that elliptic curve points used during spending were from the allowed small set. Instead, **any point on the curve** could be used, allowing an attacker to effectively **print new Zcash**.
2. **The communication problem**: Woods is most critical of how Zcash leadership downplayed it:
   - "Don't worry, most Zcash is transparent anyway" — which **entirely contradicts** the project's stated purpose of peer-to-peer private cash
   - "The turnstiles will protect you" — but turnstiles only limit what can exit the pool to what entered; they **cannot reveal whether forged Zcash was spent on goods/services inside the pool**
3. **The unresolved risk**: The Orchard pool never drained to zero. Until it does and someone potentially gets **blocked by the turnstile**, we can't know if counterfeit Zcash was created and quietly liquidated. Woods uses a hypothetical: an attacker forges ~$2M of Zcash, exits to transparent, sells on exchanges — the only artifact would be a slightly lower pool balance.
4. **First-out-the-door dynamics**: If you hold Zcash in the shielded pool, you want to exit **before** the pool balance approaches your holdings, because if there's counterfeit Zcash, the turnstile will block the last ones out.
5. **Ironwood (new pool)**: Woods sees it as a cleaner slate — forcing Orchard to wind down, disabling internal Z-to-Z transactions, and letting the turnstiles reveal the truth as the pool drains. But he's skeptical of claims that Ironwood is "more provably secure," noting he's seen **no formal methods proof** of correctness, and such proofs take years (citing Cardano's consensus proof as an example).

---

## Nillion — Woods' Current Project

- **Not a blockchain** — a semi-decentralized private compute network with an ERC-20 token on Ethereum
- Combines TEEs, homomorphic encryption, MPC, and various signature schemes into a "smorgasbord of cryptography"
- Users submit Docker containers; the network runs them with cryptographic assurance of privacy
- **Similar philosophy to Monero**: mandatory privacy (not optional), privacy-in-depth (layered primitives, not one giant circuit)
- Comparable to **Venice AI** (private AI inference) but broader in scope — aims to be a general private compute platform
- Currently building a **Monero swap product**: non-custodial, atomic, trustless swaps between BTC/ETH ↔ XMR, currently going through legal review
- **Ultimate aspirational goal**: fully homomorphic encryption running the Linux kernel across a distributed network where compute nodes don't even know what they're working on

---

## Monero's Future — FCMP++, Carrot, and Post-Quantum

- **FCMP++ (Full Chain Membership Proofs)**: Woods calls this the most exciting Monero upgrade he's seen — anonymity set becomes the entire blockchain rather than a ring of outputs. Compares its significance to when RingCT hid transaction amounts.
- **Carrot (wallet address/view key reform)**: Supports it, pushes back on community fears that it's a "Fed operation" — argues it doesn't reduce privacy, just makes wallet syncing more efficient
- **Post-quantum resistance**: Woods sees this as critical and urgent given the pace of AI/tech advancement. Notes that Algorand has already rolled out a PQ signature scheme (Falcon, lattice-based). Acknowledges it's "open heart surgery" on Monero but absolutely doable, though worried about the timeline relative to when quantum attacks become viable
- **Zcash's "quantum secure" claim**: Woods dismisses this as misleading — while shielded spends don't publish public keys, the t-addresses, consensus mechanism, and parts of the ZK proofs themselves still rely on classically vulnerable cryptography

---

## Key Quotes / Memorable Lines

- *"Optional privacy is bullshit"* — Woods, on why both Monero and Nillion mandate privacy
- *"Monero is the Linux of the cryptocurrency space"* — Woods
- *"After all this time, it only took me shitting on Zcash to get on the show"* — Woods, self-deprecatingly
- *"It's not even my opinion... it's just the hard mathematical reality"* — on the turnstile exit dynamics
- *"We have to think of it as quantum resistance, like water resistance rather than waterproofing"* — on post-quantum crypto

---

Overall, Woods comes across as a technically rigorous, philosophically aligned Monero advocate whose criticisms of Zcash are grounded in specific architectural arguments (monolithic ZK circuit vs. layered primitives) rather than tribal partisanship. He credits Zcash's engineers for working hard on the fix but is sharply critical of the project leadership's communication around the exploit's real-world implications.

---

## Going deeper: THORChain + Monero

THORChain is a decentralized cross-chain liquidity protocol that enables native asset swaps without wrapped tokens, bridges, or KYC. Monero integration has been one of the community's most long-awaited features, and it **went live on THORChain mainnet in May 2026** [1].

This means you can now swap **native BTC, ETH, USDC, and dozens of other assets directly to XMR** — no wrapping, no pegging, no centralized intermediary, no KYC [2].

## How It Works — The Technical Breakthrough

The integration was a years-long challenge because Monero's privacy architecture (ring signatures, stealth addresses) made standard multisig approaches fail. Previous attempts using Monero multisig had "too many issues to release to prod" [3].

The breakthrough came from a **community developer named Boone**, who used AI coding tools (OpenAI Codex) to wire together:

- **Luke Parker's audited FROST Rust package** (from the Serai project / Monero-Oxide) — a threshold signature scheme (TSS) for Monero
- **THORNode** — THORChain's node software

Boone spent roughly **two months** building the integration, translating between the FROST TSS code and THORNode using Codex. The FROST-based approach replaces the older failed multisig method with a threshold signature scheme that works with Monero's privacy primitives [4].

---

## What John Woods Says About It

In the discussion document, Woods shares his perspective:

- He **hasn't done a deep dive** into THORChain's architecture or cryptographic primitives himself
- But anecdotally, "smart people in my circle" are **quite excited** about Monero launching on THORChain
- His key criteria for any swap service are:
  1. **Trustless** — mathematical guarantee you can't get robbed
  2. **Non-custodial** — no one holds your funds during the swap
  3. Decentralization is nice but **not strictly required** — trustlessness is the priority

Woods says: *"Once whatever THORChain does, once it kind of tends towards those characteristics, I think it'll be exciting"* [5].

He also notes that **Nillion is building its own competing Monero swap product** (BTC/ETH ↔ XMR) that is non-custodial, atomic, and trustless — currently going through legal review [5:1].

---

## Current Status (June 2026)

| Detail | Status |
| --- | --- |
| **Mainnet launch** | ✅ Live since May 2026 |
| **Supported pairs** | BTC↔XMR, ETH↔XMR, USDC↔XMR, and more |
| **KYC required** | No |
| **Wrapped tokens** | No — fully native swaps |
| **XMR swap volume** | Becoming the first measurable DEX liquidity metric for Monero [6] |
| **RUNE price** | ~$0.43 (significantly below previous highs) [1:1] |
| **THORChain trading** | Currently showing "temporarily paused" on the main site [7] |

---

## Why This Matters

Monero has been systematically **delisted from centralized exchanges** (Binance, Kraken in many jurisdictions, etc.), making it difficult to acquire. THORChain's native integration is a landmark because it provides:

- **Permissionless access** to XMR without going through a CEX
- **Privacy by default** — no account or identity required
- A real test of whether **DEX demand can replace CEX volume** for privacy coins

Woods' view (shared by many in the Monero community) is that **the more swap options the better** — whether THORChain, Nillion's product, Wagyu, Haveno, or others — because each reduces the friction of entering and exiting Monero privately.

**References**

---

1. [What Is THORChain? How Cross-Chain Swaps... - PegasusSwap Blog](https://pegasusswap.com/blog/what-is-thorchain?ref=rogerprice.me) (22%) ↩︎ ↩︎
2. [How THORChain is Making Monero More Accessible... | Bitget News](https://www.bitget.com/news/detail/12560605374129?ref=rogerprice.me) (11%) ↩︎
3. [To set the record straight, TC devs spent a lot of time to making XMR ...](https://x.com/THORChain/status/1740925205390983270?ref=rogerprice.me) (16%) ↩︎
4. [How Boone Used AI to Build THORChain's Monero Integration | THORChain](https://thorchain.org/blog/how-boone-used-ai-to-build-thorchains-monero-integration?ref=rogerprice.me) (18%) ↩︎
5. a72d5dd80deb-JohnWoods (21%) ↩︎ ↩︎
6. [Monero (XMR) Price Prediction 2026, 2027–2030 | CoinEx Academy](https://www.coinex.network/en/academy/detail/2953-monero-xmr-price-prediction?pId=2&sId=10&ref=rogerprice.me) (6%) ↩︎
7. [THORChain: Crypto DEX | Swap BTC, ETH, & XMR | No KYC](https://thorchain.org/?ref=rogerprice.me) (6%) ↩︎
