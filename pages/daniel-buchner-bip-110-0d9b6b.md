---
source: https://rogerprice.me/daniel-buchner-bip-110
clipped: '2026-08-15T15:11:19+00:00'
title: Daniel Buchner - BIP 110
site: Letter from ...around the world
published: '2026-07-29T13:23:40.000Z'
---

# Daniel Buchner - BIP 110

# Daniel Buchner - BIP 110

![Daniel Buchner - BIP 110](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/Daniel-Buchner_-Why-BIP-110-Cannot-Stop-Bitcoin-Spam-_-SLP758.jpg)

## Overview

Daniel Buchner and Stefan Livera discuss BIP 110, a proposed soft fork aimed at restricting on-chain data (commonly referred to as "spam") on Bitcoin. Both participants are **anti-BIP 110**. The interview covers what BIP 110 is, why it cannot achieve its stated goals, the technical and economic arguments against it, and the likely outcomes around the mandatory signalling date of 8–9 August 2025.

> [!image]
> [![Click for a ver clear explanation](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/07/image-33.png)](https://www.youtube.com/watch?v=KFcFonaYKiw&t=28s&pp=0gcJCaMLAYcqIYzv&ref=rogerprice.me)
> Click for a ver clear explanation

## What Is BIP 110?

According to the text on **bipont.org**, BIP 110's stated purpose is to 'temporarily limit the size of data fields at the consensus level in order to correct distorted incentives caused by standardising support for arbitrary data and to refocus priorities on improving Bitcoin as money'.

Stefan outlines the following key details:

- There are **seven documented consensus changes**, plus **one additional undocumented consensus change** that Merch spoke about — totalling approximately **eight consensus changes**.
- One change restricts **OP\_RETURN at the consensus level to 83 bytes** (not merely at the relay/policy level).
- Other changes include **blocking the Taproot annex** and **blocking the inscription envelope**.

Daniel frames the broader context:

- On other chains, NFTs and 'monkey JPEGs' and 'silly shitcoins' have been driven by speculators and scams, and these narratives eventually 'burned out'.
- The move of this content onto Bitcoin was **not caused by any reference implementation change or settings change** — it was a **narrative shift** by people who 'exhausted their marks' on other chains. Bitcoin's durability made it attractive as 'a place where if we put data here, it's really going to stay for all time'.
- Bitcoin's purpose is monetary — 'it wasn't better coffee payments, it wasn't to inscribe monkey pics, it was money, to change the foundation of money'.

---

## Significant Points and Arguments

### 1. Consensus rules vs. node policy (standardness/relay)

Daniel draws a sharp distinction:

- **Consensus rules** are the rules that, if violated, cause a node to fork off onto a different coin. **Core never changed these.**
- What Core changed was a **node preference** — relay policy/standardness. Daniel dislikes even calling it 'standardness' or 'policy' because it makes it sound more consequential than it is. He compares it to **'horse blinders'** — 'you can put horse blinders on your own node and maybe not see the spam coming, but it's still there'.
- In the early days (Daniel got into Bitcoin in 2011), policy worked because the network was smaller and 'full of a lot of us fanatical people' who 'all ran the same stuff'. Since then, tools like **Libre Relay** and **direct-to-miner APIs** have made per-node relay preferences 'meaningless in many areas' because spammers can route around them.

### 2. Spam can be hidden anywhere there is a public key or hash

Daniel's central technical argument:

> 'You can hide data in Bitcoin anywhere there is a public key or hash, anywhere, and there's many op codes and many areas of Bitcoin where you can do that.'

He notes, in jest, that the only way to eliminate all spam would be to **remove all public keys and hashes from Bitcoin** — but 'you literally can't have Bitcoin without all those things'. The seven consensus changes merely address **specific shapes** of spam (tall/fatter transactions like deep tap trees or large OP\_RETURN blobs). The effect is merely to **flatten** spam into more, smaller transactions:

> 'It's like you have water in a glass and you're putting your hand down... it'll move around some fluid, but it's still going to be the same amount of fluid.'

The choice is therefore: 'do you want 3,000 transactions a block that are spam or would you like four?'

### 3. The asymmetry of effort (the 'whack-a-mole' problem)

Daniel compares the situation to the principle that 'it takes 10 times the amount to refute' a falsehood — gaining community consensus to fork and patch out op codes or hobble features takes **orders of magnitude more effort** than spammers need to route around it. With AI, 'some of these things to patch around take like a couple of lines of code and can be done in minutes'. He calls it 'a dragon chase. You'll never catch it.'

Spammers, he notes, 'get a kick out of it' — watching the community spend months on a fork only to route around it 'in a day'.

### 4. The need for continual forking (and the TVA analogy)

If the goal is truly to stop spam, 'you've got to keep forking'. To chase spammers down to a flat transaction space of just hashes and public keys, 'you would have to fork dozens of times'. This would require 'a regime for fast forking to put our finger in all these holes of the leaky ship'.

Daniel compares this to the **Time Variance Authority (TVA)** from the Loki series — 'who is going to be this regime that's put in place to constantly fork? I don't want that.' He wants forks to be 'few and far between' because each one creates opportunities for 'bad motion in the ecosystem'.

### 5. The inconsistency exposed in the Bitcoin Mechanic exchange

Daniel recounts a cordial debate with **Bitcoin Mechanic**, a leading BIP 110 proponent. He pointed out:

- BIP 110 was originally framed as countering spam, but 'it's already been routed around'.
- It **only increases the price of spam by about 0.5%** (less than 1%), which spammers don't care about.
- A 'first step' implies further forks. He asked Mechanic to go on record about whether he would push for more forks.

Mechanic **went on record saying 'no'** — they would not push for further forks. Daniel sees this as **inconsistent**: if the goal were truly to harass spammers into being dissuaded, 'you would have to relentlessly fork to go after them maybe once a month'. This 'undermines the idea that this is effective against spam or really about spam'.

### 6. What BIP 110 might actually achieve

Daniel's candid assessment:

> 'The only thing BIP 110 would actually be effective at is potentially changing the centre of gravity for Bitcoin reference implementation development and putting that in the hands of a different set of people, primarily Luke or maybe Mechanic and others being the outsized "authority" in what this reference implementation is, who gets to check in code.'

He adds: 'if you want that, at least be upfront about it.'

### 7. Known bugs and undocumented changes

Stefan notes there have been **at least two consensus bugs** noted in the implementation, **one undocumented consensus change**, and **one workaround found by Voytech** for yet another spam method — all requiring further fixes.

### 8. The SegWit discount point (from Moonsettler)

Stefan raises a point attributed to **Moonsettler**: as long as Bitcoin Script and the **SegWit discount** exist, spammers will find cheap ways to put data in the witness. The SegWit discount (from the 2017 soft fork) means witness data is treated as **25% of the cost**, making it a natural vector for large-scale spam. Banning one inscription envelope simply leads to another.

Daniel agrees and notes that removing the discount would harm legitimate uses like **tap trees**. The cycle would continue: restrict to seven depths, spammers chain transactions with seven-deep trees; restrict further, eventually it's all flat — 'an endless series of whack-a-moles until you've shot Bitcoin script with a shotgun so much that it just looks like Swiss cheese'.

### 9. The house/door analogy and why it breaks down

Pro-BIP 110 arguments often use analogies like email filtering, water filtering, or 'leaving the front door open'. Daniel explains why the house analogy fails:

- The 'door' in Bitcoin is used by **both invited and uninvited guests** — the same features (public keys, hashes, script) serve monetary purposes.
- Restricting entry forces **everyone** to 'climb through your second-storey window'. The building still ends up with the same number of people inside — 'you're going to contort yourself to get it to happen and the outcome's going to be the same'.
- 'That one window represents public keys and hashes, and if you don't get rid of them in Bitcoin, the window's there and everyone's going to crawl through.'

Stefan adds that these analogies mislead because 'it just doesn't work like that in a digital, decentralised, permissionless system'.

### 10. Node costs will not 'blow out'

Daniel calls this 'the easiest one' to address:

- The **4 megabyte block weight** has been the known tolerance for about a decade — 'nothing's changed'.
- As an engineer, 'when you set tolerances, you assume the worst case'. The 4 MB limit should have been assumed to be hit every block.
- A **Bitfury paper** found that around **6 megabyte weight**, nodes start dropping off — and that was at older storage/bandwidth prices.
- Even if every block were filled to 4 MB with spam starting today, Bitcoin's **linear growth** 'well undershoots the cost and capacity curve' (Moore's law-type compounding for storage and bandwidth). 'Bitcoin nodes would get cheaper and cheaper every single year.'
- Future technologies like **holographic storage** could increase capacity by orders of magnitude.

Stefan summarises: 'the chain can only grow linearly at maximum, and the technology price deflation over time is compounding at a rate faster than that.' He notes there may be temporary spikes (e.g. an current AI-related SSD price bump), but the trend outpaces chain growth.

### 11. Current block sizes are well under the limit

Stefan notes that before the Ordinals explosion (~2023), average block size was around **1.5–1.6 MB**. With spam, it rose by perhaps **30–40%**, bringing it to around **2 MB or a little over** — still well under the 4 MB limit, 'except for rare occasions'.

Daniel uses a car engine red-line analogy: tolerances are set below the comfort level; 'even if it was revving at four megabytes per block, every block, you're not going to blow a cylinder. You're fine.'

### 12. Illegal/abhorrent data on chain

Stefan notes that as of **Bitcoin Core version 28, blocks are exorcised by default** (referring to data-stripping of inscriptions/Ordinals). Daniel addresses the concern:

- No one wants terrible content on chain, but 'if you flatten the spam, it can always just be more transactions to get you to that same outcome'. Such content has already been anchored on Bitcoin.
- **Legal case law** is reassuring: there are decided cases establishing that an operator is **not liable** for obscured content in a system they run, because liability requires **specific intent** to view and to send such content to someone else for the purpose of them viewing it — not merely general intent to run a system that happens to contain something.

### 13. The greater legal threat: the All Writs Act and the filter regime

Daniel's **more serious legal concern** is the precedent created by a fast-forking filter regime. He references the **All Writs Act** (a couple of hundred years old), which says that if compliance with a government demand (for national security or other serious matters) is **not an undue burden**, you must comply.

He cites the **San Bernardino terrorist case involving Apple**, where the government demanded backdoors and data extraction. Apple won by arguing they had **no existing engineering staff or mechanism** to do it — building such a regime would be a major undertaking. Other cases have tested similar principles.

Daniel's fear: if Bitcoin shifts its dev centre to people willing to build a fast-forking filter regime, then a government could say 'we want our filter in there in consensus rules' — and it would **no longer be an undue burden** because the regime already exists. The government would go to economic nodes (e.g. Coinbase) and say 'you're going to run that one because that's the sanctioned one'. This would 'start degrading Bitcoin's really great neutrality'.

### 14. Centralisation of development

Stefan notes that the **only client compatible with BIP 110 is Knots** (not Bitcoin Core) — a PR into Bitcoin Core did not get through, and no other client is compliant. Proponents see themselves as assisting decentralisation, but 'in the development of Bitcoin it's arguably a centralising factor'.

Daniel elaborates:

- Knots has **far fewer reviewers** and **far fewer people who can push code**.
- Reviews are 'often dubious' — Luke is pushing 'sizable' changes 'with seemingly little review in comparison to something like Core'.
- If BIP 110 became dominant, it would displace dev gravity to Knots, centring on 'a couple of people'.
- He references Luke Dashjr's history, including that he 'managed to lose his own Bitcoin' and 'then involved three-letter agencies as a result', and questions whether that person should be 'the de facto leader' of Bitcoin development.

### 15. Miners should not be relied upon as 'good guys'

Daniel is emphatic: 'we can't have a system that's built on people being good guys'. The system must be 'actively adversarial' and 'repellent of bad guys' — not through an authority regime, but because 'the technicals we believe in can endure'. He doesn't care whether miners are good actors; 'they just have to play by the rules. And the economic rules are what really lead here.'

### 16. Economic nodes and influence

Daniel defines **economic nodes** broadly — miners, exchanges, wallet app operators, and anyone participating in value transfer. These matter 'far more' than other types of nodes.

Key points on influence:

- The SegWit narrative that 'a small tiny percentage contingent running this one fork overthrew everyone' is false — 'there was broad support... the majority of exchanges supported it, the majority of miners, most users — it was like 80–85% of users supported it.'
- BIP 110, by contrast, is supported by 'maybe 20–25% of node runners, which is in the tens of thousands of people'.
- Around **350 million people** have bought Bitcoin (most custodially). A single individual running a node in their basement is 'not worth anything close to Coinbase or some exchange that represents 10 million active buyers'.
- Influence comes from **monetary velocity, transaction volume, and demand** — not from running a node. A great developer who produces PRs everyone likes is influential even if they 'divested themselves completely of Bitcoin, didn't run a node, and participated in nothing involving nodes at all.'
- 'You're not going to spin up 5,000 nodes on Amazon and think that that matters. It doesn't matter at all.'

### 17. The current landscape (as of 22 July 2025)

| Metric | Status |
| --- | --- |
| Hash rate signalling (pro-BIP 110) | Under 1% |
| Node runners on Knots/BIP 110 | 6%–20% (depending on how counted) |
| Large economic actors signalling pro-BIP 110 | Zero |
| Prediction/futures markets (à la Bitfinex B1X/B2X in 2017) | None |

Stefan recalls that in the 2017 NYA/2x saga, Bitfinex ran **B1X coin and B2X coin** futures — roughly **0.15 for the 2x coin and 0.85 for B1X** — which helped people 'put their money where their mouth is'. No equivalent exists for BIP 110.

Daniel adds that there are no 'large-scale signatory campaigns' against exchanges demanding BIP 110 support. 'The apathy or the lack of care is actually a signal.' He finds it reassuring that a small minority cannot flip Bitcoin's protocol — 'if that group could flip the consensus rules of Bitcoin, I would be much more worried about that'.

### 18. Game theory is against BIP 110

The pro-BIP 110 'game theory' argument: miners should signal pro-BIP 110 because it's 'free' (wipeout risk), leading to a ramp-up near the end.

Daniel's counter:

- Miners are **net sellers** of Bitcoin — they sell primarily to **OTC desks and exchanges**. If that demand side isn't asking for BIP 110 coins, miners have no incentive to signal for them.
- There is 'no good reason to believe there's a silent majority'.
- For economic actors, taking a position creates **alienation risk** on either side, but 'you're going to alienate far more if you're pro-BIP 110 because there's just more people on that [anti] side'.
- The most sound game-theoretical outcome is for **all economic actors to sit on their hands, look the other way, and let it fade away** into its inability to produce blocks.

### 19. Luke Dashjr's 'rejecting BIP 110 is a hard fork' claim

Stefan quotes Luke Dashjr's tweet from **13 July 2025**:

> 'Removing rules is a hard fork that includes scheduled rules like subsidy halvings and yes, even BIP 110. Rejecting BIP 110 is a contentious hard fork attempt. And unlike soft forks, hard forks need consensus to succeed. There is no consensus on rejecting BIP 110.'

Daniel's response is blunt:

> 'We have changed nothing with Bitcoin on the consensus rule level, but somehow we're forking. That is so beyond batshit that it should be comical. You can't claim that the party who's changing zero consensus rules and just kind of likes Bitcoin as it is is forking. That's absurd.'

He says the burden is entirely on the pro-BIP 110 side: 'you're the one trying to change Bitcoin... you've got to convince economic nodes, you've got to convince all the Bitcoin holders, convince the miners... and you have failed to convince them and that's why your fork is failing.'

### 20. The 100-block maturation delay and inertia

Stefan raises an additional point favouring inertia: miners face a **100-block delay** before they can spend block rewards. In a chain split, a miner would need an exchange willing to list and sell BIP 110 coins, whereas on the legacy chain 'it's business as usual'. This further favours no change.

Daniel adds that pro-BIP 110 advocates are 'not putting skin in the game' — there's **no replay protection**, and no one is selling their Bitcoin ahead of time. He contrasts this with the 2017 big-block side: 'say what you will about Roger and Jihan, but they put some money where their mouth is... they burned tens of millions if not hundreds of millions of dollars.'

### 21. Closing thoughts — Daniel's humane appeal

Despite the contention, Daniel says he **doesn't want BIP 110 proponents to leave Bitcoin**:

> 'I want somehow for it to be a learning experience in the fullness of time where they come back and say, "We learned that it wasn't just a few thousand nodes that are going to change Bitcoin's protocol."'

He frames Bitcoin as 'a life raft' given 'tens of trillions of dollars of US debt' and 'an eventual spiralling collapse of the fiat monetary system', and warns that if proponents 'rage quit', they'll 'end up buying Bitcoin back at a much higher point, probably at a time of tumultuous seas'. He notes 'there are people and families behind these avatars'.

### 22. Predicted outcome around 8–9 August 2025

Daniel's prediction:

> 'I can't see them being able to produce blocks that have this chain sustaining in any meaningful way. I think it'll die with a whimper.'

He believes it will prove that changing Bitcoin's consensus rules 'requires a heck of a lot more influence and buy-in all around the ecosystem' — not miners vs. users or exchanges vs. users, but 'a sea of actors who are all economically relevant... coming together in a supermajority across them all'. On BIP 110, 'we don't have it. We're far from it.'

---

## Summary of Key Figures and Facts Cited

| Item | Value/Detail |
| --- | --- |
| Consensus changes in BIP 110 | 7 documented + 1 undocumented = ~8 total |
| OP\_RETURN restriction | 83 bytes at consensus level |
| Cost increase to spammers from BIP 110 | ~0.5% (less than 1%) |
| SegWit witness discount | Data treated as 25% of cost |
| Block weight limit | 4 MB (set ~a decade ago) |
| Bitfury paper node drop-off threshold | ~6 MB weight |
| Pre-Ordinals average block size | ~1.5–1.6 MB |
| Post-Ordinals average block size | ~2 MB (30–40% increase) |
| Hash rate signalling pro-BIP 110 | Under 1% |
| Node runners on Knots/BIP 110 | 6%–20% |
| Large economic actors signalling pro-BIP 110 | Zero |
| Bitcoin holders worldwide | ~350 million |
| SegWit user support (2017) | ~80–85% |
| Block reward maturation | 100 blocks |
| Mandatory signalling date | ~8–9 August 2025 |
| Recording date | 22 July 2025 |

---

## Key People Referenced

| Name | Role/Context |
| --- | --- |
| **Daniel Buchner** | Guest; from Proof; DID/decentralised identity experience; handle @CSU\_Wildcat |
| **Stefan Livera** | Host |
| **Luke Dashjr** | Leading BIP 110 proponent; Knots maintainer; made the 'rejecting BIP 110 is a hard fork' claim |
| **Bitcoin Mechanic** | Leading BIP 110 proponent; went on record saying no further forks would be pushed |
| **Moonsettler** | Credited with the SegWit discount argument against BIP 110 |
| **Voytech** | Found a workaround for one of BIP 110's spam restrictions |
| **Merch** | Spoke about an undocumented consensus change in BIP 110 |
| **Roger Ver & Jihan Wu** | Referenced as 2017 big-block advocates who 'put money where their mouth was' |

---

## Key External References Cited

- **bipont.org** — the BIP 110 text and description.
- **Bitfury paper** — on optimal block size and node drop-off (~6 MB weight).
- **All Writs Act** — US law on government compliance demands; tested in the San Bernardino/Apple case.
- **San Bernardino terrorist case (Apple)** — precedent for arguing that building a compliance regime constitutes an undue burden.
- **Bitcoin Core version 28** — blocks are 'exorcised' (data-stripped) by default.
- **SegWit (2017 soft fork)** — introduced the witness discount (25% cost treatment).
- **Bitfinex B1X/B2X futures (2017)** — prediction market for the NYA/2x fork (~0.15 vs 0.85).
