---
source: https://rogerprice.me/110-objections-analysed
clipped: '2026-08-15T15:11:09+00:00'
title: 110 Objections analysed
site: Letter from ...around the world
published: '2026-08-11T17:00:56.000Z'
---

# 110 Objections analysed

# 110 Objections analysed

![110 Objections analysed](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/08/Screenshot-2026-08-11-at-17.58.15.png)

Click [here](https://www.strategy.com/media/articles/110-reasons-bip-110-is-a-bad-idea) for the source document

This article is a rhetorically dense piece of advocacy. Viewed through Robert Dilts’s **Sleight of Mouth** patterns, it is not merely a technical objection to a Bitcoin Improvement Proposal; it is a systematic **reframing of the debate from an engineering trade-off into a constitutional crisis of governance and precedent**.

Below is a pattern-by-pattern analysis.

---

### 1. Redefinition (Redefine)

Saylor repeatedly redefines the language of BIP 110’s supporters to shift its semantic field.

- **“Disapproval is not invalidity” (07).** He separates the emotional/cultural judgment (“we don’t like data storage”) from the technical/legal category of consensus validity. This is a pure redefinition: *your label of “spam” does not equal my category of “invalid.”*
- **“Conservatism at the base layer should mean reluctance to alter consensus, not eagerness to alter consensus in favor of a conservative use philosophy” (10).** He seizes the word “conservative” from the proponents and redefines it. In their frame, conservatism means protecting money; in his, it means *not changing the protocol*.
- **“Bitcoin Iatrogenic Proposal” (110).** This is a masterful redefinition. He does not merely say it is a bad idea; he redefines BIP as a medical intervention whose side effects exceed the disease. The acronym remains “BIP,” but the meaning is surgically replaced.

---

### 2. Consequence (Outcome Reframe)

This is the single most frequent pattern in the text. Whenever supporters frame BIP 110 as a solution to node costs or spam, Saylor redirects attention to negative second- and third-order effects.

- **“The proposed cure is more dangerous than the condition” (110).** The classic outcome reframe: compare the stated benefit to the actual harm.
- **“Lower aggregate fee demand can weaken security at the margin” (58).** He converts a fee-market argument into a long-term security budget problem.
- **“The rules expire, but the precedent does not” (91).** He redirects from the temporary technical fix to the permanent political consequence.
- **“It establishes a precedent for using consensus restrictions to discourage a category of otherwise valid use” (What BIP 110 Proposes).** The reframe is not about what happens to data storage, but about what future “categories” can be voted out of validity.

---

### 3. Chunking Up (Move to Higher Hierarchy / Abstraction)

Saylor consistently jumps from the specific technical mechanism to first principles, making the particular dispute subservient to a universal rule.

- **“Consensus is Bitcoin’s most powerful intervention” (01).** From “should we limit scriptPubKeys?” to “what is the proper use of sovereign force?”
- **“Permissionless systems must tolerate unapproved experimentation” (09).** From a debate about image inscriptions to the definition of permissionlessness itself.
- **“Bitcoin cannot read intent” (04).** From “this particular transaction is frivolous” to an epistemological limit of distributed systems.
- **“Bitcoin does not need guardians of purity. It needs guardians of neutrality” (Closing).** From a policy fight to a mission statement for the entire network.

---

### 4. Chunking Down (Move to Specifics / Evidence)

When the opposition appeals to urgency or vague costs, Saylor chunks down to demand measurable specifics, dissolving the abstraction.

- **“The BIP itself does not quantify the node burden it would remove” (14); “does not quantify the decentralization benefit” (15); “does not quantify payment relief” (16).** He demands operational definitions for every claimed benefit.
- **“UTXO-state growth, initial-sync bandwidth, archival storage, relay burden, and validation time have different causes and may require different remedies” (17).** He decomposes the monolithic term “node cost” into distinct variables, making the bundled solution look imprecise.
- **“A historical relay-policy limit is not proof of an optimal consensus limit” (19).** He chunks down the rationale “we’ve always done it this way” to expose its logical gap.

---

### 5. Hierarchy of Criteria

Saylor does not deny that node accessibility and affordable payments are good. Instead, he subordinates them to higher values.

| Supporters’ Criteria | Saylor’s Higher Criteria |
| --- | --- |
| Keep validation cheap | Preserve hard consensus neutrality (01, 02) |
| Protect node operators | Preserve permissionless innovation (09) |
| Lower fees for payments | Maintain miner revenue / security budget (57–60) |
| Stop “spam” | Prevent precedent-based governance (91–96) |

The entire closing section, **“Guardians of Neutrality,”** is a explicit hierarchy statement: neutrality > purity.

---

### 6. Meta-Frame (Frame about Framing)

Saylor constantly steps outside the technical argument to comment on the *rules of the argument itself*.

- **“This article critiques the proposal, not the people behind it. I assume good faith” (Introduction).** He frames the debate as civil and principled, pre-emptively claiming the moral high ground.
- **“It turns protocol conservatism upside down” (10).** He frames the proponents as the ones violating their own stated ethos.
- **“Activation machinery cannot manufacture consensus” (87).** He shifts from debating the mechanism to debating what the mechanism *means* socially.
- **“A social message is not sufficient grounds for a consensus change” (06).** He meta-frames the proposal as an attempt to use code as speech, which he rules out of order.

---

### 7. Intent Reframe

He acknowledges the opponents’ positive intent, then redirects it to a different means.

- **“Many Bitcoiners I respect support BIP 110. They want to keep validation accessible, protect node operators… I share the objectives. I disagree about the remedy” (Introduction).** This is textbook intent reframe: *we want the same thing; your method is wrong.*
- **“The proposal expressly treats activation as a way to communicate that data storage is unwelcome. Consensus should be changed for compelling technical or monetary reasons, not primarily to express disapproval” (06).** He separates the intent (community signaling) from the appropriate channel (consensus code).

---

### 8. Counter-Example

He systematically finds exceptions that break the generalizations made by BIP 110.

- **“A payment channel, proof of reserves, custody policy, smart contract, or settlement commitment is both financial activity and data” (12).** A direct counter-example to the claim that “monetary” and “nonmonetary” data are cleanly separable.
- **“Private systems, unpublished contracts, experimental wallets, and future protocols are not fully observable” (40).** A counter-example to “no known use case,” proving absence of evidence ≠ evidence of absence.
- **“The same logic can be reused… Privacy tools, novel custody, stablecoin settlement, token systems, corporate applications, or other unpopular uses could face similar arguments” (95).** He turns the current target into a counter-example of a future, larger pattern of exclusion.

---

### 9. Another Outcome (Alternative Solution)

Rather than simply opposing, he redirects to a different pathway that satisfies the need without the cost.

- **Section VII (“Better Market and Policy Tools Exist”)** is entirely this pattern. Instead of consensus restriction, he proposes:
  - Relay policy (64)
  - Mining policy (65)
  - Content-neutral limits (68)
  - Pruning and optional-data designs (69)
  - Improved fee-market transparency (106)
- **Section XI (“A Better Path Is Available”)** repeats the pattern at the structural level.

---

### 10. Change Frame Size (Especially Temporal & Scope)

Saylor manipulates the time horizon and scope to alter the perceived weight of the proposal.

- **Temporary → Permanent Artifacts:** “Temporary consensus code is still consensus code” (41); “Temporary rules can leave permanent artifacts” (49); most importantly, **“The rules expire, but the precedent does not” (91).**
- **Local → Universal:** “Today’s target does not limit tomorrow’s target” (95). He expands the spatial/temporal frame from “this one-year fix” to “permanent governance culture.”
- **“A one-year closure can still disrupt development timelines” (33).** He compresses the timeframe to show that “temporary” is still too long for software ecosystems.

---

### 11. Model of the World

He imposes a different epistemological and political framework onto the same data.

- **“Miner signaling is not a referendum on all Bitcoin users” (83).** He rejects the miners-as-voters model and inserts a multi-stakeholder model (holders, exchanges, wallets, custodians).
- **“Fees price block space… They apply technical validity and resource limits rather than a semantic test” (63).** His model of Bitcoin is a content-neutral market, not a community with shared taste.
- **“Bitcoin cannot read intent” (04).** This is a model-of-the-world reframe about what a decentralized protocol is capable of knowing.

---

### 12. Analogy / Metaphor

- **“Hard consensus is Bitcoin’s immune system” (90).** Biological metaphor: the immune system (consensus) must not attack healthy tissue (valid uses).
- **“Iatrogenic Proposal” (110).** Medical metaphor extended from #01’s “intervention.”
- **“Social cohesion is a scarce asset” (97).** Economic metaphor applied to community trust.

---

### 13. Reality Strategy (How do you know?)

He systematically questions the cognitive process by which the opposition formed its conclusions.

- **“Urgency is asserted rather than operationally defined” (18).**
- **“The 256-byte line is heuristic” (20).**
- **“A historical relay-policy limit is not proof of an optimal consensus limit” (19).**

---

### 14. Apply to Self

- **“Conservatism at the base layer should mean reluctance to alter consensus…” (10).** While not a direct tu quoque, it forces the proponents’ self-identified value (“conservative”) to fold back onto their behavior (proposing a consensus change) and find it inconsistent.

---

### Summary: The Master Reframe

Strategically, the article performs one overarching Sleight of Mouth maneuver:

> **It chunks the debate up from “How do we stop data storage?” to “Who gets to decide what Bitcoin is for?”**

By doing so, Saylor shifts the burden of proof entirely. The proponents must now defend not a technical limit, but a **governance philosophy**. He redefines BIP 110 from an engineering patch into a constitutional amendment that would break Bitcoin’s content neutrality.

The sheer density of these patterns—especially **Consequence**, **Chunk Up**, **Hierarchy of Criteria**, and **Meta-Frame**—explains why the piece reads less like a code review and more like a **declaration of first principles**. It is designed not merely to disagree with the proposal, but to make adoption of the proposal *conceptually impossible* for anyone who accepts his frame.
