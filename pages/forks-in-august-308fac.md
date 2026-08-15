---
source: https://rogerprice.me/forks-in-august
clipped: '2026-08-15T15:11:34+00:00'
title: Forks in August
site: Letter from ...around the world
published: '2026-07-09T10:09:21.000Z'
---

# Forks in August

# Forks in August

![Forks in August](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/Perception-and-Reality.jpg)

As background and introductions, read this excellent article by Jimmy Song.

> [!bookmark]
> [On Overconfidence](https://primal.net/jimmysong/on-overconfidence?ref=rogerprice.me)
> ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/media-cache-7ecb6626-b7af-4d60-8a1f-c07a353f1b82)

A most interesting analysis by Jimmy Song

### 1. BIP-110 "Reduced Data Temporary Soft-fork" (RDTS) — early August 2026

- **Author:** Dathon Ohm (draft proposed December 2025)
- **Activation window:** Mandatory signaling begins at **block 961,632** (estimated **August 7, 2026**), running through block 963,647
- **Purpose:** A 1-year temporary soft fork aimed at restricting Ordinals-style arbitrary data inscriptions at the consensus level. Restrictions automatically lift after 52,416 blocks
- **Mechanism:** Uses a modified BIP9 deployment with a lowered **55% miner signaling threshold** (instead of the usual 95%). If that threshold isn't met naturally, enforcing nodes will reject any block in the mandatory window that fails to signal bit 4
- **Status (late June 2026):** Miner signaling is around **0.31–0.80%** — far below the 55% threshold — raising concerns about a potential persistent chain split. Adam Back and Jameson Lopp have called the activation parameters reckless and technically flawed

### 2. eCash hard fork (Paul Sztorc) — August 2026

- **Proposer:** Paul Sztorc (LayerTwo Labs CEO, long-time Drivechain advocate)
- **Target:** **Block 964,000**, August 2026 - **Mechanism:** A near-copy of Bitcoin Core using the same SHA-256d mining algorithm, with a one-time difficulty reset at launch. BTC holders receive **eCash tokens 1:1** based on balances at the fork block (hold 4.19 BTC, get 4.19 eCash)
- **Key feature:** Activates **BIP300/BIP301 Drivechains** — a sidechain architecture Sztorc first proposed in 2015. Seven Layer 2 Drivechains are reportedly ready for deployment at launch
- **Controversy:** Sztorc has framed it as both an "exit plan" and a pressure tactic — he says he'll call it off if Bitcoin Core activates BIP300/301 before August, which is considered unlikely. The proposal has drawn strong criticism from the Bitcoin Core community, with some developers calling it a "theft" or "hazardous airdrop," though the fork does not actually move Satoshi's BTC
- **Institutional angle:** This would be the first major fork where the largest holders are ETF sponsors, corporate treasuries (e.g., Strategy's ~818,334 BTC), and regulated custodians rather than retail — creating novel questions about how forked assets must be handled under ETF prospectus language

## Recently Completed (for context)

### Bitcoin Cash "Layla" upgrade — May 15, 2026 (completed)

The BCH network underwent its scheduled annual hard fork on May 15, 2026, implementing four CHIPs (Bitcoin Cash Improvement Proposals): P2S (Pay to Script), Bounded Looping Operations, Functions, and Re-Enable Bitwise Operations — giving the BCH "Bitcoin VM" support for loops and functions for more complex smart contracts

## Things to keep in mind

- **Bitcoin forks historically fail to gain meaningful traction** (Bitcoin Cash, Bitcoin Gold, Bitcoin SV, etc.), and developers have explicitly warned that the eCash airdrop should not be treated as "free money" [8:1][12]
- **Splitting forked coins is risky** — using a "coin-splitter" tool exposes your private keys and BTC to potential theft. Never enter seed phrases into untrusted software.
- **BIP-110** is technically a *soft fork* but the very low miner support and mandatory-signaling enforcement mechanism make an actual chain split a real possibility — worth watching closely around August 7.
- **Timelines are block-height-based, not date-based**, so the "August" estimates can shift if block production deviates from the ~10-minute average.

If you hold BTC and care about claiming any forked coins, the standard advice applies: control your own private keys (not on an exchange) well before the fork block, and wait for the dust to settle before interacting with splitter tools.

---

# The Risk of a "Separate Minority Chain" — How It Would Unfold

## The Core Mechanism

When a UASF-style activation like BIP 110's mandatory signalling kicks in, **two sets of nodes are running different rules**. BIP 110 nodes will reject any block that doesn't signal bit 4; non-BIP 110 nodes will accept those same blocks. If miners don't overwhelmingly comply with the signalling requirement, the network **diverges into two separate blockchains** — each with its own history from the split point forward [1].

Jameson Lopp explains the consequence bluntly:

> "This greatly increases the chances of a 'chain split,' in which there are 2 competing chains vying to be 'the real Bitcoin.' During a chain split scenario you should expect the entire ecosystem to grind to a halt as a result of uncertainty around which fork will win and resulting double-spend risks." [1:1]

Adam Back's prediction is even more specific: with miner signalling at only ~0.3% of hash power as of late June 2026, he says there is "virtually no chance" the proposal achieves activation through consensus. Instead, he predicts supporters would simply **"fork off and find out"** — creating a **low-hashrate minority chain** while Bitcoin continues operating unchanged on the original chain [2][3].

---

## How It Would Appear: A Timeline of Events

### Phase 1 — The Split Point (Block ~961,632, ~August 2026)

BIP 110's mandatory signalling begins. From this block onward, BIP 110-enforcing nodes **reject any block that doesn't signal bit 4** [4]. If the vast majority of miners (who control ~99.7% of hash power) ignore this requirement:

- The **original chain** continues normally — miners produce blocks every ~10 minutes, non-BIP 110 nodes accept them.
- The **BIP 110 chain** stalls — its nodes reject those blocks and must wait for a miner (any miner) to produce a block that *does* signal bit 4.

### Phase 2 — The Difficulty Wall

This is the most critical mechanical problem. Bitcoin adjusts its mining difficulty only **every 2,016 blocks** (~2 weeks). If the BIP 110 chain captures only a tiny fraction of hash power, its blocks will take **enormously longer to produce** — potentially hours, days, or even weeks per block — until the next difficulty retarget [5].

As Bitcoin.com warned during the 2017 BCH fork era:

> "A minority chain with a minuscule amount of hashrate that goes up against bitcoin's current difficulty will have a tough time surviving. It means that the hashrate minority will have to wait for 2016 blocks until the difficulty can be adjusted. With no mining power, a chain in this state facing bitcoin's difficulty could very well come to a screeching halt." [5:1]

Bitcoin Cash survived this only because its developers implemented an **Emergency Difficulty Adjustment (EDA)** — a special algorithm that rapidly lowered difficulty outside the normal 2,016-block cycle [5:2]. **BIP 110 does not include such a mechanism.** The BIP 110 chain would use Bitcoin's standard difficulty adjustment, meaning it could face **weeks of near-paralysis** before blocks speed up.

### Phase 3 — Exchange Halting

Exchanges are the first to react. Lopp warns the **"entire ecosystem" will "grind to a halt"** [1:2]. In practice, this means:

- Exchanges **freeze BTC deposits and withdrawals** to avoid crediting coins from the wrong chain.
- Trading may continue on existing balances, but **no new deposits can be confirmed** — because exchanges cannot determine which chain's confirmations are valid.
- This happened during the 2017 BCH/BSV hash war: Coinbase suspended BCH trading and took weeks to enable withdrawals of the new BSV coin [6].

### Phase 4 — Replay Attacks and Double-Spend Risk

After a split, **the same UTXOs exist on both chains**. A transaction signed and broadcast on one chain can be **"replayed"** (copied) onto the other chain, because the signatures are valid on both [7].

This means:

- If you send 1 BTC on Chain A, an attacker (or anyone observing the transaction) can broadcast the same signed transaction to Chain B, **spending your 1 BTC on that chain too** — without your consent.
- This is a form of **unintended cross-chain double-spending** [8].
- Users may **accidentally transact on the wrong chain**, leading to permanent losses [9].

### Phase 5 — Security Vulnerability of the Minority Chain

A low-hashrate chain is **trivially vulnerable to 51% attacks**. If the BIP 110 chain has, say, 1% of Bitcoin's total hash power, then any miner controlling even a small fraction of the original chain's hash power could **rent or redirect enough hash power to overpower the BIP 110 chain entirely** [10].

This enables:

- **Deep reorganisations** — an attacker secretly mines a longer chain and then publishes it, erasing transactions that were previously confirmed.
- **Double-spending on the minority chain** — the attacker can spend coins, get confirmations, then rewrite the history.
- **Complete chain destruction** — a sufficiently motivated attacker could render the minority chain unusable.

Jimmy Song noted this risk during the 2017 UASF debate: *"Whoever has the minority hashing power chain may get attacked and their fork will be less stable, less usable and risk having an embarrassing or..."* outcome [11].

---

## Historical Precedents — What Actually Happened

| Fork | Year | Outcome for Minority Chain |
| --- | --- | --- |
| **Bitcoin Cash (BCH)** | Aug 2017 | Survived only due to Emergency Difficulty Adjustment; became a permanently separate altcoin with a fraction of BTC's value and hash power [5:3] |
| **BCH → BSV split** | Nov 2018 | "Hash war" between BCH (ABC) and BSV; exchanges halted trading; BSV became a separate, low-value chain [6:1] |
| **BIP 148 (UASF)** | Aug 2017 | **No split occurred** — miners blinked and signalled via BIP 91 before the deadline [12] |
| **SegWit2x** | Nov 2017 | Cancelled before activation — no chain was produced [13] |

The critical difference: **BIP 148 worked because it was a credible threat that miners took seriously** — major exchanges, businesses, and node operators signalled intent to run it, and miners chose to comply rather than risk a split [12:1]. BIP 110, by contrast, has **~0.3% miner signalling** and lacks the broad ecosystem backing (exchanges, wallet providers, major businesses) that made BIP 148's threat credible [1:3].

---

## What Happens to Ordinary Users

| Scenario | What It Means for You |
| --- | --- |
| **You hold BTC on an exchange** | Deposits/withdrawals frozen for days or weeks; you cannot move your coins until the exchange determines which chain is "real Bitcoin" [1:4] |
| **You hold BTC in your own wallet** | Your coins exist on **both chains** simultaneously. Any transaction you broadcast may be replayed on the other chain without your knowledge [7:1] |
| **You run a BIP 110 node** | You follow the minority chain. Your node sees the original chain's blocks as invalid. You may wait hours or days for each block confirmation [5:4] |
| **You run a standard node** | You follow the original chain, which continues normally. You may not notice anything happened unless you check |
| **You're a merchant** | You cannot reliably accept payments — you don't know which chain your customer's transaction will settle on, and confirmations may be unreliable on both chains during the uncertainty period [1:5] |
| **You're a Lightning Network user** | Channel states depend on on-chain transactions for enforcement. If the chain you're watching stalls or reorganises, your channels may become **unsafe to keep open** — you might not be able to force-close or punish a cheating counterparty |

---

## The Most Likely Outcome (Based on Current Data)

With miner signalling at **0.3%** and prominent figures like Adam Back and Michael Saylor publicly opposing the proposal [2:1], the most probable scenario if BIP 110's UASF mechanism triggers is:

1. **The original Bitcoin chain continues essentially unchanged** — ~99.7% of hash power keeps mining it.
2. **A BIP 110 minority chain emerges** with negligible hash power, producing blocks extremely slowly (potentially hours or days apart) until difficulty adjusts.
3. **Exchanges freeze all BTC movements** temporarily, causing market uncertainty and possible price volatility.
4. **The BIP 110 chain becomes a de facto altcoin** — listed separately on exchanges (if at all), with its own price far below BTC's, similar to how BCH or BSV became separate assets [2:2].
5. **Most BIP 110 supporters eventually abandon the minority chain** and return to the original chain — or hold both, treating the BIP 110 coin as a separate speculative asset.

Back's summary is concise: the proposal's supporters would simply **"fork off and find out"**, creating a low-hashrate minority chain while Bitcoin continues operating unchanged [2:3].

---

## Why BIP 148 Succeeded Where BIP 110 May Fail

| Factor | BIP 148 (2017) | BIP 110 (2026) |
| --- | --- | --- |
| **Miner signalling at deadline approach** | Rising — miners were feeling the pressure | ~0.3% — near zero [1:6] |
| **Exchange/wallet backing** | Broad — major businesses signalled intent to run UASF nodes | Limited — no major exchange or wallet has publicly committed |
| **Credible threat** | Yes — miners believed a split would happen and complied via BIP 91 [12:2] | Weak — with ~0.3% hash power, miners face little pressure to comply |
| **Prominent opposition** | Minimal from major industry figures | Adam Back, Michael Saylor, and multiple developers publicly opposed [2:4] |
| **Outcome** | No split — SegWit activated cleanly | Split appears likely if UASF triggers |

The key insight: **a UASF only works as a credible threat**. BIP 148 never actually split the chain because miners capitulated. BIP 110's problem is that, without enough economic weight behind it, miners have **no incentive to comply** — and the UASF becomes not a threat but an actual fork, producing the very minority chain its critics warn about.

**References**

---

1. [BIP-110 Pushes Bitcoin Toward August Fork Deadline With Only 5 EH/s Signaling](https://news.bitcoin.com/bip-110-pushes-bitcoin-toward-august-fork-deadline-with-only-5-eh-s-signaling/?ref=rogerprice.me) (26%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
2. [Adam Back Rejects BIP-110 as 'Technically Defective'](https://coinedition.com/adam-back-calls-bip-110-technically-defective-as-bitcoin-governance-debate-heats-up/?ref=rogerprice.me) (12%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
3. [BIP-110 Supporters Push for Activation as Adam Back Warns of...](https://cryptonews.net/news/bitcoin/33061225/?ref=rogerprice.me) (6%) ↩︎
4. [BIP-110 / Knots Designed To Fork Off From The Beginning (and fail)](https://bitcointalk.org/index.php?topic=5583540.0&ref=rogerprice.me) (2%) ↩︎
5. [Fork Watch: The Chain With Less Hashrate Could Come to a Screeching Halt](https://news.bitcoin.com/fork-watch-the-chain-with-less-hashrate-could-come-to-a-screeching-halt/?ref=rogerprice.me) (22%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
6. [Updated: What to Expect During the Bitcoin Cash Hard Fork](https://www.coinbase.com/blog/what-to-expect-during-the-bitcoin-cash-hard-fork?ref=rogerprice.me) (5%) ↩︎ ↩︎
7. [How Do Replay Attacks Impact My Assets after a Blockchain Split?](https://encrypthos.com/question/how-do-replay-attacks-impact-my-assets-after-a-blockchain-split/?ref=rogerprice.me) (7%) ↩︎ ↩︎
8. [What Are the Security Implications of Replay Attacks after a Blockchain ...](https://encrypthos.com/question/what-are-the-security-implications-of-replay-attacks-after-a-blockchain-hard-fork/?ref=rogerprice.me) (1%) ↩︎
9. [What is What is a fork in blockchain? Exploring chain... | CoinTracker](https://www.cointracker.io/learn/fork?ref=rogerprice.me) (2%) ↩︎
10. [BIP-110 Pushes Bitcoin Toward August Fork Deadline With Only...](https://cryptonews.net/news/bitcoin/33074358/?ref=rogerprice.me) (5%) ↩︎
11. [UASF BIP148 Scenarios and Game Theory | by Jimmy Song - Medium](https://jimmysong.medium.com/uasf-bip148-scenarios-and-game-theory-9530336d953e?ref=rogerprice.me) (4%) ↩︎
12. [BIP 148 (UASF) | LearnBitcoin](https://www.learnbitcoin.com/glossary/bip-148-uasf?ref=rogerprice.me) (8%) ↩︎ ↩︎ ↩︎
13. [Major Bitcoin Forks: What Split the Chain and What Changed](https://blofin.com/en/academy/blofin-courses/major-bitcoin-forks?ref=rogerprice.me) (1%) ↩︎
