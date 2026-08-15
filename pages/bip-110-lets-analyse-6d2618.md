---
source: https://rogerprice.me/bip-110-lets-analyse
clipped: '2026-08-15T15:11:08+00:00'
title: 'BIP-110: Let''s analyse'
site: Letter from ...around the world
published: '2026-08-11T17:02:13.000Z'
---

# BIP-110: Let's analyse

# BIP-110: Let's analyse

![BIP-110: Let's analyse](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/08/Screenshot-2026-08-11-at-18.00.18.png)

Click [here](https://github.com/bitcoin/bips/blob/master/bip-0110.mediawiki?ref=rogerprice.me) to read the source document

The pro-BIP-110 text is, at its core, a **jurisdictional argument disguised as a technical specification**. Where [Saylor’s essay](https://rogerprice.me/110-objections-analysed/) frames the proposal as a constitutional crisis of neutrality, the BIP text reframes Bitcoin itself as a **single-purpose monetary network under siege by a polluting externality**. Every technical limit is anchored not to engineering preference, but to a teleological claim about Bitcoin’s “intended function.”

Below is the Robert Dilts pattern analysis applied to the pro-BIP-110 document.

---

### 1. Chunking Up (Move to Higher Purpose)

The BIP does not debate bytes; it debates the mission.

- **“In order to protect Bitcoin’s intended function as the Internet’s native money”** (Motivation). This chunks up from “limiting scriptPubKeys” to Bitcoin’s cosmological purpose.
- **“Set Bitcoin back on the path to becoming the world’s money”** (Motivation). The proposal is framed not as a change, but as a *return*.
- **“Bitcoin should ‘do one thing, and do it well’”** (Motivation). This invokes Unix philosophy to elevate “simplicity of purpose” above “generality of function.”
- **“Liberates Bitcoin developers from endless scope creep”** (Motivation). A project-management abstraction is used to justify consensus-level coercion.

The master chunk-up is monetary teleology: *if a transaction structure does not serve immediate monetary settlement, it is out of scope for the protocol.*

---

### 2. Redefinition (Semantic Reframe)

The document systematically renames the phenomena under dispute to strip legitimacy from data embedding.

- **Data embedding → Abuse / Hack / Spam.** It is called an “inscription hack,” “unsupported use case,” “data abuse,” and “spam injection.” What opponents call “permissionless innovation” is redefined as a “misinterpretation” of script meaning (Rationale: “what matters is that Bitcoin has a well-defined meaning that is distinct from the unsupported one”).
- **Consensus restriction → Restoration of principle.** “These rules may be new at the consensus level, but they are merely enshrining long-standing principles of Bitcoin.” The radical act of changing validity rules is redefined as conservative preservation.
- **Breaking user space → Intentional communication.** The taboo of breaking user space is reframed as a feature: *“this proposal intentionally breaks user space… necessary in order to communicate that data storage is not supported.”*
- **55% threshold → Ideal urgency.** Rather than a degraded standard, the lowered threshold is “ideal” because the change is temporary and urgent. The deviation from BIP 9 is renamed a tailored optimization.
- **OP\_IF / OP\_NOTIF → Redundant spam vector.** A general-purpose opcode is redefined as “commonly abused today to inject spam” and “redundant for Tapscript” because conditions “can instead be evaluated off-chain.”

---

### 3. Consequence (Outcome Reframe)

The text redirects every objection toward a feared secondary effect of *inaction*.

- **“Development to grind to a standstill”** (Motivation). The consequence of tolerating data is not cultural annoyance, but developmental collapse.
- **“Data storage competes unfairly with payments, making Bitcoin payments unnecessarily costly. This encourages reliance on third-party payment processors, making Bitcoin payments easier to censor.”** This is a multi-link consequence chain: data → high fees → custodial payment processors → censorship. The outcome of not restricting data is the destruction of censorship resistance itself.
- **“The miner accepts a one-time fee, and in exchange, the priceless service of highly-available, uncensorable data storage is provided in perpetuity for free by node operators.”** This reframes data transactions as **theft of infrastructure**.
- **Against fund-loss fears:** The text does not deny the risk; it dilutes it through combinatorial improbability. Funds are lost *only if* the UTXO is Taproot, *and* pre-signed, *and* confirmed during deployment, *and* spent via a deep leaf/OP\_IF, *and* keypath unavailable, *and* no other leaf works. The negative outcome is chunked down until it feels like a logic puzzle rather than a real danger.

---

### 4. Hierarchy of Criteria

The BIP establishes an explicit value stack, with monetary purity at the apex.

| Subordinate Value | Superior Value |
| --- | --- |
| Data embedder convenience | Node operator cost / decentralization |
| Complex contracting (BitVM) | Speed of deployment / urgency |
| Perfect, elegant rules | Simple, reviewable rules |
| General-purpose utility | “Sound, permissionless, borderless money” |
| Future upgrade elegance | Immediate crisis mitigation |

- **“A more complicated proposal… delaying deployment when the change is already urgent”** establishes Speed > Perfection.
- **“This proposal… represents the strongest possible rejection of the arbitrary data storage use case, while minimizing complexity”** establishes Strength of Signal > Feature Completeness.

---

### 5. Meta-Frame (Framing the Debate Itself)

The document repeatedly steps outside the technical argument to define the rules of acceptable argumentation.

- **On the slippery slope:** “This softfork does not attempt to impose restrictions on monetary activity… This clear distinction between mitigating a systemic risk from non-monetary data abuse and interfering with actual monetary use cases provides a strong barrier against future overreach.” It draws a bright line and declares the debate bounded: *money* is protected; *data* is fair game.
- **On policy vs. consensus:** “It remains true that policy is still the best place to fight spam. However, it is also true that policy cannot guarantee 100% effectiveness…” It absorbs the opponent’s frame (policy first), then carves out a narrow exception for consensus as the “worst-case” backstop.
- **On precedent:** “The explicitly temporary nature of the softfork further reinforces that this is a targeted intervention to mitigate a specific crisis, not a commitment or proposal of a new direction of development.” It meta-frames the 1-year sunset as a self-erasing precedent.

---

### 6. Model of the World

The BIP rests on a specific epistemological and economic framework that it asserts as fact.

- **Bitcoin has an intended function.** It is not an empty protocol; it is “the Internet’s native money” with a “fundamental purpose.”
- **Blockspace contains two non-fungible markets.** The text explicitly rejects the fungibility of blockspace: “The market for data storage on the blockchain is a completely different market from the market for payments, with completely different incentives.”
- **Miner-node externality is structural theft.** The model assumes miners and nodes are in conflict: miners privatize fees while nodes socialize storage costs forever.
- **Node operators are non-consenting hosts.** The text treats node operators as bearing an “unexpected cost” and being forced to serve “objectionable content.” This is partly an ethical appeal about consent, not just engineering.

---

### 7. Change Frame Size (Temporal & Scope Manipulation)

This is perhaps the text’s most important defensive weapon.

- **Temporal shrinkage (1-year expiry):** The entire proposal is wrapped in a self-destruct timer. “Once the softfork expires, UTXOs of all heights are once again unrestricted.” This shrink-wrap makes the “precedent” argument feel like an overreaction to a temporary speed bump.
- **Scope shrinkage:** “Inputs spending UTXOs that were created before the activation height are exempt… The new rules apply only to UTXOs created at or after the activation height.” The affected universe is narrowed to *future* data storage.
- **Temporal expansion (for safety):** “Any future upgrade, however, would need more than a year of coordination, so this softfork will not actually restrict it.” The future timeline is expanded to prove no collision with upgrade hooks.

---

### 8. Chunking Down (From Principle to Mechanism)

When abstractions like “decentralization” or “risk” are invoked, the text descends into granular technicality.

- **Byte-level boundaries:** It justifies 34 bytes vs. 83 bytes vs. 256 bytes vs. 257 bytes with specific physical arguments (UTXO set storage, RAM cost, image compression thresholds, 2048-bit cryptography).
- **Conditional risk anatomy:** The fund-loss section is a masterpiece of chunking down. It breaks “YOUR FUNDS COULD BE FROZEN” into five nested preconditions (P2TR, pre-signed, confirmed during deployment, deep leaf/OP\_IF, keypath disabled, no alternate leaf). The abstraction of danger is dissolved into a Venn diagram of near-impossibility.
- **Exhaustive witness taxonomy:** The distinction between script argument witness items, control blocks, annexes, keypath signatures, etc., chunks down “witness limits” into surgical precision to counter claims of overreach.

---

### 9. Intent Reframe

The text assigns moral roles to the actors.

- **BIP authors:** Defenders. “Protect Bitcoin’s intended function,” “safeguard against abuse,” “restore focus.”
- **Node operators:** Victims of forced labor. They “never received even a part of the fee, yet are forced to continue downloading, storing, and serving the data forever.”
- **Data storers:** Malicious free-riders. “Senders usually wants to explicitly force the content on non-consenting node operators.” This is not framed as experimentation but as aggression.

---

### 10. Counter-Example

The text preemptively attacks generalizations made by opponents.

- **Against “this is unprecedented”:** Points to the “long-established 83-byte policy limit on OP\_RETURN” and the historical fact that “the Bitcoin community has historically treated techniques for embedding arbitrary data… with antagonism.”
- **Against “fee market alone suffices”:** Provides the externality counter-example: the fee pays the miner, not the node. This breaks the generalization that fees align all incentives.
- **Against “256 bytes is arbitrary”:** Counters with the image-compression counter-example (300–400 byte images possible) and 2048-bit cryptographic numbers.

---

### 11. Another Outcome

Rather than simply prohibiting data storage, the text redirects the demand.

- **“Users storing arbitrary data… should start looking for other places to store their data, such as Nostr, IPFS, BitTorrent, cloud storage, etc.”** It offers an alternative venue for the use case rather than leaving it homeless.
- **“Over the next year, interested developers can implement and propose a longer-term solution.”** It redirects the need for a perfect rule into a future development pathway.

---

### 12. Apply to Self

The text absorbs its strongest criticisms and wears them.

- **“Yes, this proposal intentionally breaks user space”** (Alternatives/Alsos). It accepts the accusation and uses it as proof of seriousness.
- **“It remains true that policy is still the best place to fight spam”** (Alternatives/Alsos). It agrees with the anti-consensus purists, then immediately limits the agreement: *but policy fails against malicious miners.*
- **“Are there any tradeoffs? Yes”** (Tradeoffs). By openly admitting tradeoffs (BitVM delay, OP\_IF limits), it inoculates itself against accusations of dishonesty, then reframes each as acceptable.

---

### Summary: The Master Reframe

The BIP-110 text executes one overriding Sleight of Mouth maneuver:

> **It reframes a consensus restriction on transaction forms as an externality tax on a polluting industry.**

By chunking up to “Bitcoin as money,” it makes data storage no longer an unapproved *use* but an *abuse* of infrastructure. By shrinking the temporal frame to one year, it neutralizes the “precedent” and “slippery slope” objections before they can gain momentum. By redefining the fee market as two separate markets, it destroys the neutrality argument that fees alone should ration block space.

Where Saylor’s essay asks, *“Who gets to decide what Bitcoin is for?”* the BIP answers, *“Bitcoin’s intended function was already decided: it is money. We are merely enforcing the property lines.”*

In Dilts’s terms, the text does not defend a rule change. It **redefines the rule change as boundary maintenance**.
