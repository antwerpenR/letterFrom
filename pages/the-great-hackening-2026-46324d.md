---
source: https://rogerprice.me/the-great-hackening-2026
clipped: '2026-10-08T03:16:15+00:00'
title: The Great Hackening - 2026
site: Letter from ...around the world
published: '2026-09-24T08:11:03.000Z'
---

# The Great Hackening - 2026

# The Great Hackening - 2026

![The Great Hackening - 2026](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/The-Great-Hackening-of-2026.jpg)

This episode frames the Coldcard hack as "the gun that kicked off the race to hack everything." The presenter argues this is an ongoing, ecosystem-wide event — not a time to assume anything is safe — and ultimately claims it may be one of the best things for Bitcoin security in the long run.

> [!bookmark]
> [The Great Hackening of 2026 – Bitcoin Audible](https://bitcoinaudible.com/the-great-hackening-of-2026/?ref=rogerprice.me)
> ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/BA-Secondary-Logo-Blkpng-d0f32719-e6c8-4863-a5d0-0df7c5365da9.png)

Click to listen to the full explanation - notes and summary below

## Coldcard

- Incident dated 30 July; the bulk of funds were drained within the first 2–3 days, though higher-entropy "bounty" addresses are still being hit (credit to James O'Bern for ongoing tracking work).
- Root cause: the firmware protection mode checked that the true random number generator was **defined** rather than **enabled** — so it was defined but never executed. Seed generation fell back to a pseudo-random number generator, reducing entropy from "an atom in the universe" to "a blade of grass in a football field."
- Likely consequence: key collisions — users may have generated keys already in use by others.
- Evidence suggests a frontier AI model was used to find the entropy vulnerability; multiple researchers independently reproduced the find by simply prompting an AI (referred to as "Kimmy K3") with a pointer to the affected firmware window.
- **Action:** move any funds on a Mk IV/V or multisig involving Coldcards immediately; Mk III holders are out of luck.

## Liquid Network (Blockstream)

- Drained of 4,200 BTC; 3,600 returned with a "we are a white hat" message; the attacker kept 600 BTC — which the presenter calls **grey hat** behaviour (a rational bargain, since laundering 4,200 BTC would be slow, costly and risky).
- Mechanism: a "key cache" bug in confidential transactions. Range proofs (expensive) are cached; a fix for one bug apparently introduced another. The attacker obtained a valid proof from vulnerable clients, then swapped in an inflated transaction — minting ~4,000 new LBTC out of thin air (fractionalising the network) — and the peg-out/swap service verified it against cached proofs without rechecking critical details, releasing the Bitcoin.
- Broader lesson: privacy at the base layer carries serious trade-offs — supply and transaction details can't be independently verified, and privacy mechanisms "have a shorter shelf life."

## Other incidents (mostly patched, largely not exploited in the wild)

| Project | Issue |
| --- | --- |
| BitBox (older devices) | USB bug allowing malicious firmware installation via a compromised machine/phishing; a buffer-overflow-style bug allowing malicious execution; a silent payments verification flaw that could let an attacker hold funds hostage. The Nova is unaffected; all found internally by the team, not by outside attackers. |
| Core Lightning (CLN) | Two DoS-style bugs: flooding the gossip protocol to exhaust node memory, and a crafted message that crashes nodes. Found largely via AI agents (credited to "Chand"); patched quickly; one was reportedly exploited within hours of disclosure. |
| LND | Reorg vulnerability in channel closes (13 August); zero-timestamp gossip DoS (June). |
| Eclair (ACINQ) | Multiple exploitable bugs found by Rob Hamilton during scanning, involving a malicious bitcoind RPC; patched quickly, never exploited. |
| Sparrow Wallet | Security hardening (anti-klepto related to BitBox 02, credential redaction, PayNJoin). **Warning:** there is no Sparrow mobile wallet — iOS/Android versions are malware/scams. |
| Data breaches | Trezor's shipping provider (names, addresses, emails — physical targeting risk); Ledger's payment partner (global e-order data, no keys). |

## Why this is happening now

- AI has collapsed the economics of attack: a million times more people with the skill, at a millionth of the time cost. Anyone with a Claude subscription or a little Bitcoin for ppq.ai can run an AI agent against firmware.
- Bitcoin is hit **first** — the "canary in the coal mine" — not because it's weakest, but because it offers the most irreversible reward. Next in line: wider crypto, then the general web (whose stolen value is more reversible and traceable).
- Roughly 1,500–1,700 bug reports have been submitted across the Bitcoin ecosystem in the past month; the overwhelming majority never exploited.
- Security research may need to become more private during finding/patching stages; red-teaming efforts (Rob Hamilton, James O'B[e]rn, "Cali" and others) are dedicating serious resources.

## Why it's good for Bitcoin long term

- Anti-fragile systems don't avoid stressors — they adapt. This wave will "brute force" the ecosystem toward rock-solid, AI-hardened code, plugging the "Swiss cheese" holes of the duct-taped internet.
- AI is compared to introducing **gunpowder into a world of bows and arrows** — those who don't adapt become the victims.
- He cites Julian Assange's remark that "for some reason the universe smiles upon cryptography" — verification remains cheap while breaking remains hard.
- Digital evolution: what isn't secure enough dies; what is secure survives.

## Practical advice

- Update everything promptly (CLN, LND, Eclair, Sparrow, older BitBox firmware via official sources only).
- Never click links in emails — expect phishing waves after any data breach.
- Get a PO Box (~$22/month) for hardware orders instead of using your home address.
- Physical security: a dog, a visible security system, and (where legal) a firearm — together eliminating most home-invasion targeting risk. He also flags France's "crypto mafia" problem and suggests avoiding travel there until it's addressed.
- Set up AI agents to monitor security newsletters and deliver a daily morning report; demand independent audits and constant vigilance.
- He shares his own habit of having an agent (running via ppq.ai) trawl security reports for his specific stack each morning.
