---
source: https://rogerprice.me/silent-payments-and-frigate
clipped: '2026-09-20T09:44:14+00:00'
title: Silent Payments and Frigate
site: Letter from ...around the world
published: '2026-09-16T18:54:41.000Z'
---

# Silent Payments and Frigate

# Silent Payments and Frigate

![Silent Payments and Frigate](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/Sparrow-Wallet_-Craig-Raw---Silent-Payments.jpg)

**Watchman Privacy — recorded 2 July 2026** (their third conversation; the previous one was March 2025). Craig Raw is the developer of Sparrow Wallet, a desktop (PC) Bitcoin wallet, formerly notable as one of the few wallets to implement Whirlpool before the Samourai situation.

> [!image]
> [![Click to listen to the full interview and discussion - notes and summary below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-20.png)](https://www.youtube.com/watch?v=tWrmpfLHSgY&ref=rogerprice.me)
> Click to listen to the full interview and discussion - notes and summary below

## Key Topic: Silent Payments

- **The problem**: Address reuse is "almost unsolved" since the Bitcoin white paper. Despite HD wallets (seed words, introduced ~2013) making fresh addresses trivial to derive, roughly **70% of spendable outputs on-chain today go to reused addresses**, and the trend is rising.
- **What silent payments are**: A static, off-chain payment code/address; every payment to it generates a unique on-chain address derived partly from the transaction's inputs. Only sender and recipient can see the linkage — address reuse is eliminated *by design*.
- **Send vs receive split**: The design deliberately separates sending from receiving. Sending is easier, so most wallets start there; receiving requires scanning the chain.
- **Sparrow's scanning solution (via a separate server component called "Frigate")**:
  - Reduce the blockchain to one value per transaction, then compute *inside* the database — ~10x speed-up.
  - Move computation to a **GPU** — which Craig believes is the first GPU use in Bitcoin since GPU mining — another 10x.
  - A further optimised GPU implementation contributed by another developer gave a third 10x, for a total **~1000x reduction** — scanning two years of history in seconds on a reasonably powerful machine.
  - A **free public scanning server** has been live for about a month, making silent payments usable without running your own infrastructure. Craig argues this is essential (Metcalfe's law) for adoption beyond privacy-conscious hobbyists — ideally even as a default in wallets like Trust Wallet or on exchanges like Binance.
- **Status in Sparrow (as of 2 July 2026)**: Sending and receiving both work. Create via *File → New Wallet* and select "silent payments" as the policy type. Software wallets only for now; hardware wallet support is not yet in, but all standards are written and Sparrow is ready for vendors to integrate. Hardware-wallet correctness is verified via a **discrete log equivalence proof**.
- **Dust attacks**: A theoretical concern. Craig raised Sparrow's dust limit from 1,000 to **5,000 sats**, suggesting users freeze payments below that threshold.
- **Future ambition**: Silent payments could eventually become the *default* wallet type Sparrow creates.

## Other Discussion Points

- **Maintenance**: Ongoing work on weak points, dependency patching and verification takes ~20–30% of Craig's time.
- **Apple App Store incident**: Scam "Sparrow" mobile apps on the App Store defrauded users. Craig submitted (unpublished) a warning app stating Sparrow has no mobile apps; Apple's automated processes then flagged his developer account, threatening macOS releases. After a social-media response and appeal, Apple resolved it and added a note to his account.
- **Samourai developers imprisoned — chilling effect**: Craig says running servers that let people build transactions jointly now sits at the edge of the Overton window in the US, even though non-custodial developers shouldn't be liable. CoinJoin as a general tool is "too edgy" to promote; he suggests Silent Payments as a serverless workaround.
- **Regulatory warning**: He has seen draft language proposing that users be required to use a single fixed on-chain address — building better privacy systems *before* address-reuse norms become regulation is urgent.
- **Ordinals**: Zero interest; Sparrow was simply used as a capable tool.
- **Fiat price display**: Open to adding it, with caveats about source accuracy; it "should never be taken as financial truth."
- **Lightning**: Not coming to Sparrow — "servers should be servers and clients should be clients"; Sparrow is meant to be closed when not in use. He personally runs Lightning nodes and finds it very usable.
- **Other wallets**: Praises **Zeus** and **Phoenix**.
- **Base-layer privacy**: Opposes radical new address types with cryptographic complexity; prefers application-level changes and supports **cross-input signature aggregation**, which could erode the common-input-ownership heuristic.
- **Physical attacks**: 11 of 14 known 2026 physical attacks on crypto holders occurred in France. Advice: don't publicise your holdings — the best defence is criminals never learning about you.
- **Mobile vs PC**: Mobiles aren't privacy-focused at the baseband level; best practice is a clean Linux machine dedicated to interacting with your savings.
- **Other interests**: Watching FROST (multi-sig) standards, which have been slow; Bitcoin **inheritance** remains a big unsolved problem; some miniscript-based inheritance concepts have self-sovereignty issues.

## Practical Privacy Tips from Craig

- Don't discuss your holdings — the classic mistake behind most attacks.
- Use a wallet that generates a fresh address per payment, and always fetch a new address for each incoming payment.
- Avoid round amounts; slight overpayments obscure which output is change.
- Use Sparrow's privacy tab on the send screen (two same-amount outputs — one a decoy) to defeat change-detection heuristics.

## Links Mentioned

- Sparrow Wallet website: [sparrowwallet.com](https://sparrowwallet.com/?ref=rogerprice.me) (given in the transcript as "Sparrow Wallet22WS.com" with two W's)
- Gabriel's site: [escapethetechnocracy.com](https://escapethetechnocracy.com/?ref=rogerprice.me)
