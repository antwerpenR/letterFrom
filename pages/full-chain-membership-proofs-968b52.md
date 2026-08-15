---
source: https://rogerprice.me/full-chain-membership-proofs
clipped: '2026-08-15T15:11:44+00:00'
title: Full Chain Membership Proofs
site: Letter from ...around the world
published: '2026-07-01T13:40:27.000Z'
---

# Full Chain Membership Proofs

# Full Chain Membership Proofs

![Full Chain Membership Proofs](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/monerossreorg-760x428.png)

### The Technical Picture (from Monero's official documentation and community sources)

Since launch, Monero has used **ring signatures** to provide sender privacy. Each transaction input is mixed with a small set of **decoy outputs** (currently **16**), making it ambiguous which output is actually being spent [2].

However, ring signatures have known vulnerabilities:

- **EAE attacks** (a specific chain analysis technique)
- **Chain reorganisation difficulties**
- **Statistical analysis** (mitigated but not eliminated by the decoy selection algorithm) [2:1]

The core issue: an anonymity set of only 16 leaves room for sophisticated surveillance tools (such as those from Chainalysis or Elliptic) to narrow down possibilities over time [3].

### The Solution: Full Chain Membership Proofs

**Full Chain Membership Proofs (FCMPs)** replace ring signatures entirely. Instead of proving that a spent output is one of 16 decoys, an FCMP proves that the spent output is **one of *any* output on the entire chain** [2:2].

This means every input's anonymity set jumps **from 16 to approximately 100,000,000** (and growing as the chain grows) [2:3].

### How It Works (High-Level)

| Component | Description |
| --- | --- |
| **Anonymity set expansion** | Instead of 16 decoys, the proof covers the entire set of unspent outputs on the chain (millions and growing) — a '1-of-N' proof where N is enormous [3:1] |
| **Spend authorisation** | The proof confirms the user controls the output without revealing which one, using cryptographic commitments and signatures [3:2] |
| **Linkability prevention** | Mechanisms ensure double-spending is detectable without linking unrelated transactions [3:3] |
| **Underlying cryptography** | Based on **Curve Trees** and Eagen's work with **elliptic curve divisors** [2:4] |
| **Zero-knowledge proofs** | Uses advanced ZKPs to verify transaction validity without revealing which specific output is being spent [3:4] |

### Two Proposals

There have been **two proposals** under the FCMP banner [2:5]:

1. **Original FCMPs** — announced at **MoneroKon 2023**, intended to be deployed with or after **Seraphis** (a broader protocol upgrade that would require migration to a new address format, invalidating all prior addresses).
2. **FCMP++** (originally 'FCMPs+SA+L') — proposed in **March 2024** in response to spam attacks at the time. It independently adds **Spend Authorisation + Linkability**, **removing the dependency on Seraphis**. This means it can be deployed **without** a disruptive migration to a new address format [2:6].

### New Features Introduced by FCMP++

FCMP++ adds several features beyond just replacing ring signatures [2:7]:

- **Transaction Chaining** — allows signing a transaction spending another transaction *before* the spent transaction is published on-chain. This enables certain **layer-two designs** (such as payment channel protocols).
- **Outgoing View Keys** — anyone with the outgoing view key can detect with **100% certainty** when received outputs are spent. Currently Monero only offers incoming view keys, which detect spends with high likelihood but not certainty. This makes cold wallet setups and multi-signature wallets much more efficient.
- **Forward Secrecy** — an adversary with a discrete log oracle (such as a quantum computer) cannot break the privacy of the protocol.

**Important caveat:** The deployed protocol would *support* all of these features, but the **wallet code** to take advantage of them would be **delayed** — the initial focus is on achieving full sender privacy as quickly as possible. Wallets could then adopt these features on their own timeline, without further hard forks [2:8].

### Efficiency Improvements

| Metric | Before (Ring Signatures) | After (FCMP++) |
| --- | --- | --- |
| Anonymity set | 16 | ~100,000,000+ (entire chain) |
| Proof generation (multi-input) | 5+ minutes | ~1 minute |
| Privacy against chain analysis | Vulnerable to EAE attacks, statistical analysis | Computationally infeasible to correlate |

Speedups of **95% and 22%** were achieved through community optimisation contests for the `helioselene` and `ec-divisors` libraries [3:5].

### Timeline and Activation

| Milestone | Detail |
| --- | --- |
| First proposed (original FCMPs) | MoneroKon 2023 [2:9] |
| FCMP++ proposal | March 2024 [2:10] |
| Security proofs (Generalised Bulletproofs) | Published by Aaron Feickert (sarangnoether), July 2024 [4] |
| Beta stress net live | Around the time of Tuman's interview [1:5] |
| Tuman's estimate at interview | 'Months away' from going live [1:6] |
| Network activation (per community sources) | **Q1 2026** via hard fork [3:6] |
| Final optimized version | Shipped in the **August 2026 hard fork** (per one source, which refers to the '++' as the final optimised version) [5] |

> **Note on timeline discrepancy:** The transcript (recorded before the interview was published) has Tuman saying the upgrade was 'months away.' Community sources indicate FCMP++ activated network-wide in **January 2026** via hard fork [6], with a final optimised version in **August 2026** [5:1]. This is consistent with Tuman's 'months away' estimate if the interview was recorded in mid-to-late 2025.

---

## Why This Matters — Summary

1. **Quantum leap in privacy:** From 16 decoys to the entire chain's unspent output set — correlation attacks become computationally infeasible [2:11].
2. **Removes known vulnerabilities:** EAE attacks, chain reorganisation issues, and statistical analysis vulnerabilities inherent to ring signatures are eliminated [2:12].
3. **Forward secrecy:** Future-proofing against quantum computing threats [2:13].
4. **No disruptive migration:** Unlike the Seraphis path, FCMP++ can be deployed without invalidating existing addresses [2:14].
5. **Enables layer-two designs:** Transaction chaining opens the door to payment channels and other scaling solutions [2:15].
6. **Privacy strengthens over time:** Unlike fixed ring sizes, the anonymity set grows as the blockchain grows — privacy gets *better* with scale [3:7].

As Tuman put it in the interview, this is why he is 'more excited than ever' about Monero from a technical perspective [1:7].

---

*Note: The transcript references are drawn verbatim from the interview document. Technical details are sourced from Monero's official getmonero.org documentation and community blog posts. Where community sources give slightly differing dates, I have noted the discrepancy rather than choosing one over the other.*

**References**

---

1. 4f427d880359-Douglas Tuman\_ Leading the Monero Charge (18%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
2. [Full-Chain Membership Proofs Development | Monero - secure, private, untraceable](https://www.getmonero.org/2024/04/27/fcmps.html?ref=rogerprice.me) (47%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
3. [Monero FCMP++ Upgrade Explained: What It Means for XMR Users](https://xgram.io/blog/monero-fcmp?ref=rogerprice.me) (24%) ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎ ↩︎
4. [r/Monero - Full-Chain Membership Proofs (FCMP)](https://www.reddit.com/r/Monero/comments/1ch0oje/fullchain_membership_proofs_fcmp_the_next/?ref=rogerprice.me) (2%) ↩︎
5. [Why I’m Betting on FCMP++: How Monero’s 2026 Upgrade Redefined...](https://xgram.io/blog/why-im-betting-on-fcmp?ref=rogerprice.me) (4%) ↩︎ ↩︎
6. [Beyond Ring Signatures: How Monero’s FCMP++ Upgrade Redefined...](https://xgram.io/blog/beyond-ring-signatures?ref=rogerprice.me) (5%) ↩︎
