---
source: https://rogerprice.me/fedimint-gets-real
clipped: '2026-09-20T09:44:17+00:00'
title: Fedimint gets real
site: Letter from ...around the world
published: '2026-09-09T19:29:49.000Z'
---

# Fedimint gets real

# Fedimint gets real

![Fedimint gets real](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/Fedimint-in-the-wild.png)

**Context:** Recorded Tuesday, 30 June. The conversation focused on Fedimint being used *in practice* in South Africa, rather than the protocol itself.

## Guests

| Guest | Role |
| --- | --- |
| Eric Sirion | Creator of the original Fedimint spec |
| Joscha | Long-time contributor, described by Eric as "the mastermind behind Fedimint as it is today", instrumental in the iro integration |
| Hermann | Bitcoin Ekazi; runs the South African federation in the wild |

> [!image]
> [![Click to listen to the full interview and discussion](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-11.png)](https://serve.podhome.fm/episodepage/CitadelDispatch/cd206-eric-sirion-joscha-and-hermann--fedimint-in-the-wild?ref=rogerprice.me)
> Click to listen to the full interview and discussion

## Key Highlights

### The South African federation

- It is the second federation set up by the group; the first was a 3-of-4 test federation. The live one is a **5-of-7 guardian federation** — the largest known, the first 5-of-7 running exclusively on Start9 servers and the first on iro.
- Hermann uses it "almost on a daily basis" and reported that *not a single Lightning transaction has failed*, despite several guardians being on mobile or wireless internet rather than fibre, and despite South African power cuts (guardians use UPS battery backups; the federation tolerates two nodes down).

### iro integration

- Removes the old DNS requirement and cloud/VPS complexity; communication is end-to-end encrypted with static public keys.
- The iro library uses all available network interfaces (Wi-Fi, mobile, etc.), switching and load-balancing automatically — federations have run across three continents simultaneously (Nairobi, South Africa, US), and a guardian could theoretically run in a pickup truck over Starlink.

### Setup and backups

- Setup was "a click-through process": sync the Bitcoin node (a few days to a week on poor internet), install the Fedimint package (originally sideloaded; now in the Start9 community store), exchange guardian codes via Signal chat, and confirm. Hermann: "the most complicated part was not to get confused whose code belongs to who."
- Backups are static — made once, stored on a USB stick, containing private keys. Restoring is: click restore, upload the file, "30 seconds later they are online again."
- In the test federation, one guardian accidentally deleted and uninstalled his guardian — the system kept running, and he recovered from his Start9 backup.
- If a guardian loses both machine and backup, the federation can continue as an effective 5-of-6, or guardians can configure a **shutdown date and successor federation** — users get an in-app notification and migrate with one click. This was used to migrate users from the 3-of-4 to the 5-of-7 federation.

### Federation sizes and consensus

- Recommended sizes: 4, 7, 10, then 13 guardians (e.g. 7-of-10 next). 5-of-7 is the current sweet spot; larger federations are possible (tests up to 20), limited by Bitcoin's rules for on-chain multisig, but mainly by *coordination complexity*.
- Thresholds are not arbitrary: the underlying Byzantine fault-tolerant consensus algorithm sets minimum thresholds — "5-of-7 is like the lowest threshold that is technically achievable." Going lower risks guardians disagreeing on confirmed transactions.
- Latency stays essentially constant as guardian count rises; only bandwidth increases slightly.

### Gateways and Lightning

- The gateway is a separate service connecting a Lightning node to a federation — custody (guardians) is split from servers (gateways). Multiple gateways can serve one federation, and one gateway can serve multiple federations.
- **Trust trade-off with gateways: essentially none** — the gateway is "just an extension of the Lightning network into the federation"; like any routing node, it either forwards or earns nothing. The only reliance is that it doesn't deny service, against its own fee-earning interest.
- The Fedimint project runs its own gateway to bootstrap new federations; when a federation reaches critical volume it can spin up its own. Gateways run in the cloud because Lightning nodes need high uptime and good backups.
- Guardians vote on gateways via the UI, but even a single guardian can unilaterally add a gateway to unblock a federation; clients try gateways ordered by votes.

### Wallets and South African context

- Users are on **Conduit**, a new wallet Joscha developed specifically for South Africa (in app stores a few months), supporting MoneyBadger QR codes. Joscha lived on the first federation for three months in South Africa with no failed payments.
- Hermann: "you can probably to 90% live on Bitcoin" in South Africa and Kenya; he landed in Kenya with only a Bitcoin wallet and never touched shillings. He keeps a bank account solely for visa proof-of-funds requirements.
- Zero fees for eCash transactions between federation members — a better trade-off than onboarding everyone to a fully custodial wallet.

### UTXO management (V2 wallet module)

- Hermann's federation runs the **V2 generation of modules**; the wallet V2 module **consolidates every deposit into a single UTXO** — the federation only ever holds one UTXO.
- Each user pays exactly the on-chain cost they impose, avoiding socialised fees, fee-pool exploits via dust, and management burden (zero config). The federation requires roughly next-block fee estimation — it won't let transactions sit pending 12 hours since the UTXO is a shared resource.
- Lightning transactions are effectively batched into large on-chain transactions; gateways rebalance by sending funds (e.g. via Bolt Exchange) into the federation for more eCash.

### Custody vs. chat (Fedi app)

- Only custody moves to the community federation; Fedi's chat remains cloud-hosted, using the same encryption protocol as Signal. The underlying Matrix protocol could allow decentralisation later, with MLS-based options like Whitenoise mentioned as promising.

### Broader philosophy

- Eric's original fear was that in hyperbitcoinisation, most people would simply keep Bitcoin with JPMorgan-style banks — Fedimint offers a pragmatic middle ground rather than a black-and-white self-custody debate.
- Eric argued many "fully decentralised" projects in the wider crypto space "end up with basically a federation of extra steps" — being honest about having a multisig unlocks features, e.g. Fedi's module letting users hold synthetic USD to hedge short-term Bitcoin exposure.
- On privacy: eCash gives "incredibly strong default privacy guarantees" to people who couldn't otherwise afford it.
- On education: "if we don't have to explain, we shouldn't" — users get eCash's benefits without needing the concept explained; eCash notes can be sent like chat messages or printed as paper vouchers for onboarding.

### Final thoughts

- **Hermann:** Fedimint is "probably going to be one of the most important technologies in Bitcoin going forward" for creating an *acceptable trust model* — far preferable to onboarding people to fully centralised wallets, with a great user experience.
- **Joscha/Eric:** Fedimint is as much a social experiment as a technical one — "can we form the social structures around those systems that make them work for communities?"
- **Eric:** "Bear markets are for building. More than ever before, we have to fight for our privacy, fight for our freedom. Join us."

*(Sponsor/audience-support segments at the start and end — zap leaderboards, sharing/subscription plugs — omitted as requested.)*
