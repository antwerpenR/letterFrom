---
source: https://rogerprice.me/evgeny-on-simplex
clipped: '2026-08-15T15:12:48+00:00'
title: Evgeny on Simplex
site: Letter from ...around the world
published: '2026-05-14T13:57:07.000Z'
---

# Evgeny on Simplex

# Evgeny on Simplex

![Evgeny on Simplex](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/05/simplex.webp)

This is a detailed summary of Matt Odell's interview with Evgeny Poberezkin, founder of SimpleX, on Citadel Dispatch (episode CD196), recorded on 20 March 2025.

---

## What SimpleX Is and Why It Exists

**SimpleX is an encrypted messaging protocol and app built on two foundational principles: sovereignty and trustlessness.** Evgeny came to this project not from the cryptocurrency or privacy communities, but from publishing — he worked as an executive in publishing, owned a magazine, and later served as head of engineering at Mail Online. His motivation was observing people losing jobs for stating truths, which he saw as fundamentally corrosive to society.

The core insight is that **users should own everything**: their conversations, channels, connections, and identity. Unlike almost all other networks, SimpleX has no network-wide user identity. Your identity is what your contacts see, not something registered on any server. This makes it architecturally impossible for a single provider to act against users, even if they want to.

Evgeny distinguishes his approach from traditional privacy messengers. When privacy and sovereignty conflict, SimpleX chooses sovereignty. For example, SimpleX refuses to let senders delete messages from recipients' devices — because "I have files on my computer. I have to allow somebody else to delete those files. It's just wrong".

---

## The Technical Architecture: Connection-Based Addressing

**SimpleX's key innovation is flipping internet addressing upside down.** Instead of assigning addresses to endpoints (devices), it assigns addresses to connections between endpoints. This solves two problems simultaneously: endpoint security (no fixed address to attack) and mobile battery life (no need for constant polling).

The network consists of routers that forward packets between endpoints. Each conversation uses four routers — two in each direction — with clients programmed to use routers from different operators. This makes collusion to correlate traffic technically difficult: "If each conversation uses four different companies, and those companies are rotated on a weekly basis, then your dependence on each particular company is extremely low".

Critically, **there are no persistent circuits** (unlike Tor). Each packet is anonymous in its path — forwarding routers cannot determine how many addresses exist because of encryption between sender and receiving router. This provides packet-level anonymity rather than session-level anonymity.

---

## Privacy of Participation vs Content Privacy

**A major theme is the distinction between content privacy and participation privacy.** Evgeny argues that in large public groups, content privacy is impossible to guarantee and dangerous to rely on — "if you expect privacy, but there is no privacy, then you may be saying something as if it is a private conversation".

What matters more is **participation privacy**: protecting who is reading or listening, even when content is public. He cites real-world cases where people were fined simply for liking controversial content, or where authorities extracted membership lists from Telegram channels to target individuals. "We currently live in a world when some powers believe that they have to regulate not just what's being said, but also what's being listened to".

SimpleX achieves this by giving users new keys and addresses for every community they join. "Every time you join a community, it's the next set of keys, it's the next set of addresses, it's the next set of credentials. And your participation remains private".

---

## Criticism of MLS (Message Layer Security)

**Evgeny delivers scathing criticism of MLS, the specification Signal plans to adopt.** His core argument: MLS requires a trusted authentication server to protect against providers, which is logically incoherent — "we need a trusted provider to protect from provider... it's like a logical impossibility".

He argues MLS solves the wrong problem. For corporate groups hosted on corporate servers, infrastructure security suffices — "why do they need MLS for this case?... They just need security of infrastructure, they need discipline, they need proper ops at Google." For public groups, content cannot be protected regardless. MLS occupies an awkward middle ground that adds complexity without solving the actual trust problem.

---

## Scalable Channels and the "Next Web"

**SimpleX is weeks away from launching scalable channels** — large broadcast communities that compete with Telegram channels but with censorship resistance and participation privacy. These differ from Nostr in a crucial way: "to publish on Nostr, you have to connect to a relay. To publish on SimpleX channel, there would be no direct connection, the connection to a relay is through the messaging network, which means the privacy is preserved on a transport layer".

The channel design uses "chat relays" — special clients that cosplay as servers but are reached only through SimpleX addresses, never via direct IP connection. Multiple relays per channel provide redundancy and censorship resistance. Critical commands (like removing members) are signed; ordinary messages are not, preserving deniability.

---

## Monetisation and Business Model

**The planned monetisation model is novel and caused significant controversy.** Rather than user subscriptions (which Evgeny argues fragments networks and makes apps unusable, citing Telegram Premium), SimpleX will make messaging free forever and charge large channels for infrastructure — analogous to how the web subsidises small sites via big ones.

This requires:

- A registry of servers discoverable by all clients
- A global namespace for channel names
- Programmatic revenue sharing between channel owners, server operators, software developers, and governance

These functions require network-wide state, which SimpleX currently lacks. Hence the decision to use smart contracts on a blockchain — not for transferring value alone, but as "a global distributed computer that can perform arbitrary computations and arrive to consensus about things".

**Evgeny explicitly states they will NOT create tokens:** "We're not going to create any digital asset class. All we want is a scheme that allows people to deposit some existing asset." The model is compared to prepaid telephone cards — users deposit existing assets (possibly USDC, possibly others), which are held in smart contracts and assigned to communities via zero-knowledge proofs for privacy.

---

## Governance: Consortium Model

**SimpleX is transitioning from company-controlled to consortium governance**, inspired by how the World Wide Web was governed (by agreement between four entities in different countries) until W3C became a US non-profit in 2023. Lawyer Heather Meeker (author of Mozilla and Elastic licences) is drafting the agreement.

The company will retain IP ownership but license it irreversibly to consortium members. Multiple non-profits in different jurisdictions will run the network together, avoiding jurisdictional capture. Evgeny argues this is necessary because "any organisation that wants to be independent has to make profit. Otherwise it becomes dependent on whoever gives its money" — and donor dependence leads to capture, as seen with Linux Foundation's silence on California's SB 1047-like legislation.

---

## Significant and Surprising Points

- **Founder came from publishing, not crypto or privacy**: Evgeny's background is in media and free speech, not cypherpunk culture. He "didn't know [privacy communities] even exist"
- **SimpleX and Nostr invented simultaneously**: "SimpleX protocol was created, invented, pretty much at the same time when Nostr protocol was invented" — around 2019
- **No database required for default servers**: "Our default implementation doesn't use any database layers... a single executable that keeps the state in memory with a full backup state in append-only logs"
- **Internet-to-Tor routing built in**: Messages to Tor-hidden routers can be delivered even from non-Tor users, keeping the network interconnected
- **Repudiation as deliberate cryptographic feature**: Unlike signed systems, SimpleX messages are cryptographically deniable — "there is no way to prove to a third party that you actually ever sent this message." Evgeny defends this despite no legal precedents, noting Signal pioneered this only ~10 years ago
- **Rejection of "pick a lane" thinking**: Evgeny explicitly refuses false trade-offs between privacy and convenience, fast and compliant, for-profit and ethical — citing his JavaScript validation library (now ~1 billion monthly downloads) as proof that eliminating artificial choices works
- **Venture capital without control provisions**: The company took VC money via SAFE agreements with "no boards, no control" — investors must be chased for advice. Evgeny argues this is post-Facebook VC culture
- **Community equity crowdfunding planned**: Within ~3 months, SimpleX intends to sell actual company equity (not tokens) to users via modified SAFE agreements
- **Adoption itself as privacy feature**: "We effectively see adoption as a privacy feature" — mainstream usage is necessary for privacy technology to protect anyone
- **All privacy tech combined reaches maybe 2% of people**: "If you think about it, it's crazy. All privacy technology together are used by maybe like, what, 2% of people in the world? Nobody"
