---
source: https://rogerprice.me/scott-and-sideswap
clipped: '2026-08-15T15:13:52+00:00'
title: Scott and Sideswap
site: Letter from ...around the world
published: '2026-03-10T09:04:45.000Z'
---

# Scott and Sideswap

# Scott and Sideswap

![Scott and Sideswap](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/03/cd194.png)

Source: [CD194: SIDESWAP - LIQUID PREDICTION MARKETS](https://noderunners.network/en/media/podcasts/ungovernable-misfits/cd194-sideswap-liquid-prediction-markets/197409)

Scott, co-founder of **SideSwap**, joined Matt on Citadel Dispatch to discuss their non-custodial wallet and swap infrastructure built on the **Liquid sidechain**. The interview covers SideSwap's growth, technical architecture, privacy features, and their new prediction market initiatives using **Simplicity** smart contracts.

[Citadel Dispatch - CD194 Sideswap-transcript

Click for the full transcript

Citadel Dispatch - CD194 Sideswap-transcript.txt

51 KB

download-circle](https://rogerprice.me/content/files/2026/03/Citadel-Dispatch---CD194-Sideswap-transcript.txt "Download")

## What Is SideSwap?

**SideSwap is a non-custodial wallet** built on the principle of "your keys, your coins." The platform enables **atomic swaps** between counterparties on Liquid, functioning as a bulletin board system where users find each other and trade without intermediaries [1].

Key capabilities include:

- **Peg-in/peg-out services** between Bitcoin main chain and Liquid at **0.1% fees** (previously, competitors charged much higher rates)
- **Order book markets** where anyone can participate as market makers—not just "black box" instant swaps
- Swaps between **Liquid Bitcoin (L-BTC)**, **Liquid Tether**, and other Liquid assets

Scott emphasized they operate with minimal marketing, growing organically and cash-flow positive [1:1].

---

## Significant & Surprising Points

### 1. **Depix Surpasses Tether in Transaction Volume on Liquid**

While **Tether remains larger by total value**, **Depix**—a Brazilian stablecoin issued by Ulam—has become the **most-traded asset by transaction count** on SideSwap [1:2].

- Depix adoption is driven by local Brazilian payments
- This growth came organically without direct outreach from SideSwap
- Demonstrates Liquid's low barriers to entry: no listing fees, no gatekeepers

### 2. **Tether on Liquid Has Unique Censorship-Resistance Properties**

A critical and underappreciated point: **USDT on Liquid is the only Tether issuance where the issuer cannot selectively confiscate balances** [1:3].

- Due to **Confidential Transactions**, Tether cannot identify which UTXOs hold USDT
- On other chains (Ethereum, Tron, Solana), Tether can freeze specific addresses
- On Liquid, Tether's only option would be to shut down the entire asset—cannot pick and choose

Despite this advantage, Liquid Tether circulation remains negligible (~$95 million) compared to Ethereum ($92 billion) and Tron ($85 billion) [1:4].

### 3. **PayJoin Privacy on Liquid**

SideSwap uses **PayJoin transactions** extensively:

- For users without Liquid Bitcoin to pay network fees
- For swaps between two non-Bitcoin assets (SideSwap pays the fee)
- Combined with **Confidential Transactions** and **Confidential Assets**, this creates strong privacy even with smaller usage volumes [1:5]

The **peg-in/peg-out process** adds additional privacy: the Liquid Federation selects UTXOs for peg-outs, breaking direct correlation between peg-in and peg-out transactions [1:6].

### 4. **Order Book Accessible via Mobile and CLI**

Unlike typical "instant swap" services, SideSwap offers **proper order books** with transparent pricing. Market makers can:

- Use the mobile app to participate
- Download **dealing software from GitHub** for programmatic access
- Compete on pricing, with spreads currently around **0.2–0.3%** from midpoint [1:7]

### 5. **Swapsion: First Simplicity-Powered Prediction Market Prototype**

SideSwap recently launched **Swapsion** (swapsion.io), their first product using **Simplicity** smart contracts on Liquid [1:8]:

Current offerings:

- Binary contracts on Bitcoin price direction (up/down in 2/5/10 minutes)
- Binary contracts on Bitcoin price movement magnitude (1%, 2%, 3%, 4%, 10%)

**Technical approach**: Uses SideSwap's order book infrastructure adapted for prediction markets. Bids represent "yes" outcomes, offers represent "no" outcomes. The price point indicates the prediction probability (e.g., bid at 30 = 30% probability). Both parties fund the contract simultaneously via atomic swap [1:9].

**Liquid Connect**: A wallet connection protocol (similar to MetaMask) allowing web pages to connect to SideSwap mobile/desktop wallets for transaction signing [1:10].

### 6. **Revenue Sharing Model for Integrations**

SideSwap offers partners a **50-50 revenue split** on trading fees. This powers integrations with:

- **Aqua Wallet** (Samson Mow's wallet—Liquid at rest for Lightning)
- **Bull Wallet** (Bull Bitcoin's self-custody wallet)
- Various Brazilian ecosystem wallets around Depix [1:11]

### 7. **Six-Month Roadmap: Polymarket Competitor MVP**

Scott committed to having a **proof-of-concept for a full prediction market** within six months, including:

- Order book structure (0-100 scale for binary outcomes)
- Improved Liquid Connect functionality
- Oracle infrastructure with integrity guarantees
- Additional betting-style markets (Satoshi Dice structure) to test edge cases [1:12]

---

## Key Technical & Philosophical Themes

| Theme | Discussion |
| --- | --- |
| **Self-custody vs. federation trust** | Scott acknowledged the ongoing debate about Liquid's federation model, noting that practical decentralization may be sufficient for regulatory purposes even if not philosophically pure |
| **Oracle problem** | Both agreed the oracle problem is fundamentally unsolvable—requires trusted third parties, but can be mitigated through multiple oracles, reputation systems, and DLC-style approaches |
| **Simplicity advantages** | Contracts are mathematically verifiable before signing; more conservative/safety-oriented than Ethereum's approach |
| **Privacy momentum** | Matt noted growing mainstream awareness (Ray Dalio, Chamath Palihapitiya mentioning financial privacy), potentially creating tailwinds for Liquid |
| **Agentic payments** | Matt raised the possibility of Liquid as infrastructure for AI agents needing USD token + Bitcoin support without node management |

---

## Call to Action

Scott encouraged listeners to:

1. **Download the SideSwap app** (sideswap.io)
2. **Try pegging Bitcoin into Liquid** and experiment with swaps
3. **Test the order books** and understand the mechanics
4. **Visit Swapsion** to try Simplicity-powered binary contracts
5. **Analyze their own transactions** on liquid.network (mempool.space's Liquid explorer) to observe privacy properties [1:13]

---

## Conclusion

SideSwap represents a **quietly bootstrapped, technically rigorous approach** to building non-custodial financial infrastructure on Bitcoin. Their work demonstrates that Liquid—despite years of being overlooked—offers unique properties for privacy, stablecoin usage, and now prediction markets that compete with "shitcoin" alternatives while maintaining Bitcoin-native values. The coming six months will test whether this infrastructure can achieve the user adoption and liquidity necessary to fulfill its potential.
