---
source: https://rogerprice.me/self-custody-vs-custodial
clipped: '2026-10-08T03:16:18+00:00'
title: Self-custody vs custodial
site: Letter from ...around the world
published: '2026-09-23T09:01:50.000Z'
---

# Self-custody vs custodial

# Self-custody vs custodial

![Self-custody vs custodial](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/Institutional-Custody--Multisig---the-War-on-Cash-_-Mike-Belshe-SLP773-1.jpg)

Mike Belshe is a "huge fan of self-custody": if self-custody is lost (e.g. via regulation), Bitcoin ends up with gatekeepers deciding who is "in or out".

However, the asset class has grown large enough that security requirements have reached the point where many people ask whether they can secure it themselves. He receives monthly calls from long-term holders whose Bitcoin is now a large share of net worth and who worry about inheritance and spousal access.

He draws a parallel with traditional finance: people once kept assets at home; banks emerged; some early "banks" were rugs; layers of regulation, law and insurance eventually built trust. A mix of custody and self-custody is inevitable — like carrying some cash in your wallet vs. banking the rest.

> [!image]
> [![Click for the full interview and discussion - notes and summary below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-36.png)](https://www.youtube.com/watch?v=7bstGBiem7Y&ref=rogerprice.me)
> Click for the full interview and discussion - notes and summary below

## The BitGo model

| Aspect | Detail |
| --- | --- |
| Multisig model | 2-of-3, protects against both theft and loss; done on every supported chain |
| Key distribution (self-custody) | BitGo holds 1 key (HSM, generation ~4); user holds 2 — browser-generated key, optional third-party provisioning (Coincover), or bring-your-own third key |
| Backup | Key card material; no single breach point; recovery possible if BitGo disappears |
| Open-source recovery | "Wallet Recovery Wizard" on GitHub — recovers any BitGo self-custody wallet with no BitGo involvement; institutional clients audit/test it |
| Custody offering | Regulated, AML/KYC, insured, 100% cold storage (BitGo holds all 3 keys); 24/7 withdrawals via hot buffers — hot wallet risk sits with BitGo, not the client |
| Fees | Free for individuals; monetised via trading, staking, lending. Institutional custody fees vary by use case |
| Multi-user | Spouse/accountant roles: administrators (dual approval for policy changes), spenders, viewers |
| Policies | Spending limits, delays, IP/location/timing restrictions, velocity limits |

## On retail exchange fees

- He argues the industry "failed retail" on lower fees and fewer middlemen: the largest US retail exchange charges roughly **160 basis points** on retail trading (per its public financials), while institutions pay tens of basis points.
- BitGo is not an exchange — it uses a smart order router across all market makers and exchanges globally for best execution, akin to securities brokers' best-execution duty (which has no crypto equivalent).
- Claims everyone in the industry knows you don't get best price unless trading on Binance, Bybit, or OKX; US prices are higher.

## Recent hacks and trust in "trustless"

- People set up security when holdings were small ($10k-level), then holdings grow to $1M+ and the security level no longer matches.
- On the Coldcard RNG issue: self-custody is never actually trustless — there's always trust (developers, hardware, supply chains, RNG). Multisig helps because you need three independent random numbers rather than one, and BitGo's keys are generated in different places with different implementations, making failure probabilities multiplicative (e.g. $0.001% \times 0.001%$).
- On Bybit/Lazarus (Safe blind-signing hack): don't put $1.5 billion in one wallet. BitGo splits a $1B client across ~10–15 wallets; the Bybit loss would have been ~$150M instead of $1.5B. Wallet segregation also means zero correlation between client breaches.

## 2-of-3 vs other schemes (3-of-5, FROST, Miniscript)

- 2-of-3 balances security and usability; users effectively handle one key while BitGo co-signs; the third key is a backup in a vault.
- Casa's 3-of-5 works but is "a level up" in complexity — five keys to protect, more locations, more recovery routines. Every added key means more ops, recovery routines and people.
- Miniscript/on-chain timelocks are interesting but users lock coins and regret it; BitGo handles policy at the application layer instead. Chain-specific schemes (FROST) are awkward for BitGo's multi-chain support.

## MPC vs multisig

- BitGo supports more of the top 100/250 tokens than Fireblocks, Anchorage or Coinbase; many chains (including Ethereum) don't support on-chain multisig, so MPC is used there.
- **Multisig is strictly better than MPC**: independent keys, asynchronous signing, works in cold storage, and allows independent implementations (which mitigates RNG-type bugs). MPC is a single vendor's protocol requiring parties online simultaneously.
- Early MPC was 2-of-2/3-of-3 (theft protection but no loss protection); competitors still haven't upgraded to 2-of-3 MPC. Documented cases exist of 3-of-3 MPC users losing coins through loss of one share with no backup.

## PII, KYC/AML and the "war on cash"

- On the Revolut KYC leak (staff tricked by someone impersonating government): Revolut "screwed up", but the deeper issue is that AML/KYC mandates create **honeypots** of personal data — see also Equifax, and two French incidents (an insider selling the Bitcoin-holder list to criminals, then a hack).
- Belshe's view: PII collection has never really worked for stopping crime; it's mostly about tax enforcement. The government wants money in institutions it can see — a "war on cash".
- In France it's illegal to spend more than €1,000 in cash. He met Treasury Secretary Bessent, who "hadn't really thought about" the war on cash. Erosion of cash rights will eventually erode gold and Bitcoin rights too — vote for property-rights defenders.
- Loss of privacy (tying identity to holdings) is "one thing you lose when you go into custody"; France's requirement to report where and how much Bitcoin you hold is what enabled physical attacks.
- Industry should apply money-grade controls to PII storage and support authentication, but the problem is structurally hard: compliance tech (third-party fintechs like Persona, Sub, Sardine) creates more leakage points.

## Confiscation and jurisdiction risk

- BitGo moved wrapped Bitcoin (WBTC) to multi-jurisdictional key storage a couple of years ago amid US regulatory fears; fears have subsided, and global legislation lowers ban/confiscation odds — but it "could happen" (Executive Order 6102 cited). Self-custody at least leaves you choices. Money is power; the state needs money to maintain power.
- Multisig makes multi-jurisdictional protection straightforward.
- Counterpoint on splitting custody: splitting BlackRock's ~$50B across two custodians halves the catastrophic loss but increases the chance of a $25B failure — "everything's risk at some level."

## Quantum resistance

- BitGo lets clients see how much is quantum-exposed (UTXOs with revealed public keys) and auto-sweeps exposed outputs; ~30% of UTXOs currently use exposed public keys. If all wallets followed this unspent-output hygiene, everyone would be resistant to long-range quantum attacks now.
- Recent report cited: a 20,000-qubit computer might break a key in ~73 days — multisig doubles that (two 73-day sequences). Short-range (in-flight mempool) attacks still need mitigation.
- Satoshi's exposed coins remain a separate, unsolved issue.

## Insurance

- Total global underwriting capacity for crypto is only ~$5–7 billion against a ~$1.6+ trillion asset class — 100% coverage will never happen.
- Insurance still matters: (a) architecting uncorrelated risk (wallet splitting, geographic key separation — BitGo's three custody keys sit ~1,000 miles apart, qualifying for natural-disaster coverage he believes is unique), and (b) underwriters putting a $250M cheque behind you implies deep diligence on governance, tech and operations.
- Coincover sells retail insurance on multisig wallets.

## Multi-institution custody (Onramp, Anchorwatch)

- These are "elaborate self-custody solutions", not qualified custodians; they use some BitGo tech. Belshe feels BitGo's model captures most of the benefit, but choice is good.

## Takeaway

There is no one-size-fits-all: some will self-custody, some will DIY multisig, some will use custodians or blends (e.g. self-custody wallet for DeFi activity plus custodial savings). Belshe's (tongue-in-cheek) closing: "there's one that's best — just use BitGo and it'll be fine," while acknowledging everyone should be educated and choose what lets them sleep at night.
