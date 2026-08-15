---
source: https://rogerprice.me/self-custody-monero
clipped: '2026-08-15T15:11:11+00:00'
title: Self Custody & Monero
site: Letter from ...around the world
published: '2026-08-11T10:08:40.000Z'
---

# Self Custody & Monero

# Self Custody & Monero

![Self Custody & Monero](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/08/Screenshot-2026-08-11-at-11.06.19.png)

**Guest:** Seth (Seth for Privacy), COO at Cake Wallet  
**Host:** Doug Tuman  
**Show:** Monero Talk (sponsored by Cake Wallet and StealthyX)

Seth returned to Monero Talk after nearly two years away. The wide-ranging conversation covered AI and privacy, Monero vs Zcash, ASIC resistance, tail emission, quantum resistance, developer culture, hardware wallet security, and ecosystem projects.

> [!image]
> [![Click for the full interview - summary below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/08/image-14.png)](https://x.com/MoneroTalk/status/2085517046201360423?ref=rogerprice.me)
> Click for the full interview - summary below

## AI and Privacy

Seth described himself as a 'cautious enthusiast' — a tech lover who doesn't assume hyped things have substance. He found early AI tools underwhelming, but the turning point came around the start of the year when open-weight models became good enough for everyday use. He also needed a 'force multiplier' given his many responsibilities at Cake alongside young children.

He outlined three tiers of AI privacy:

1. **Hope the provider doesn't log** — Claude and ChatGPT log '100%' of your data.
2. **Zero data retention** — the provider promises not to log (a 'VPN-style promise'). This should be the minimum target. Providers like NanoGPT and Venice offer this.
3. **Secure enclave / TEE** — the 'holy grail' and 'the Monero level of AI privacy'. Open-weight models hosted in a Trusted Execution Environment with cryptographic proof the provider cannot access queries.

Seth self-hosts AI at home — roughly $10k in hardware, not financially worthwhile for individuals but providing ultimate privacy. He uses it to run sensitive security tests against Cake Wallet without any third party seeing. His recommended sweet spot for most people: host a smaller model locally for ~90% of tasks, and use a paid TEE-hosted service for complex work. He predicted that by year's end, models running on laptops could serve most people's needs.

On AI-driven security reporting, Seth was critical of the Bitcoin Red Team, who flagged Cake Wallet features like QR backup restoration as 'high severity' vulnerabilities when they are designed behaviour. The broader problem: developers lose significant time triaging floods of false positives from people running models against codebases they don't understand.

---

## Zcash vs Monero

Seth was scathing about Zcash's Ironwood pool migration. The official spec required splitting outputs into set denominations and sending them with exponential randomised delays — migrating just 10 outputs would take approximately 40 hours, impossible on mobile. Cake's developer Charak (Mr. Sionic) devised a pragmatic alternative: splitting outputs correctly but sending steadily block by block. Seth found it 'terrifying' that Cake beat dedicated, funded Zcash teams to market.

On Ironwood's formal proofs: they prove the cryptography is sound but not the implementation. Historically, inflation bugs come from implementation errors, not cryptography breaks. Monero's FCMPs will provide functionally identical privacy to Ironwood but with drastically simpler cryptography — easier to prove and lower implementation risk. Monero also has network-level protections like Dandelion++, which Zcash lacks. Seth's bottom line: 'once Monero has FCMPs, there's just no reason for Zcash to exist.'

---

## ASIC Resistance

Seth's position is nuanced and controversial within the Monero community. The best case is ASIC mining with broad distribution, but Monero cannot realistically achieve this — opening up to ASICs would likely mean one or two producers at small scale, very centralising. However, CPU mining has serious downsides: AI companies with massive data centre compute could 'flip a switch' and dominate Monero, mining empty blocks. This isn't true of ASIC-mined chains, where attackers must buy hardware they'd devalue by attacking. ASIC resistance is 'not the holy grail' but a pragmatic solution that fits Monero today.

---

## Tail Emission and Dynamic Block Size

Seth called the flat 0.6 XMR tail emission 'not properly implemented' and 'pretty useless long-term' because it will eventually be 'literally nothing' percentage-wise. He would have preferred a flat percentage of supply, ensuring a persistent security incentive. He praised dynamic block sizes as 'fantastic' with natural checks and balances, contrasting Monero's incentive for more transactions against Bitcoin's incentive for higher fees.

---

## Quantum Resistance

Monero's upcoming FCMP++ and Carrot upgrade provides forward secrecy for stealth addresses and sub-addresses. Monero's amount hiding is perfectly hiding — even a quantum break couldn't reveal historical amounts. Monero could be fully quantum resistant today, but transactions would be much larger and usability worse. Seth stressed that Monero needs a clear migration path for when a practical quantum computer arrives: 'If a quantum computer drops tomorrow and we have no migration path, Monero's dead.' He believes quantum resistance should be the top priority after FCMP++ ships.

---

## Developer Ecosystem and Community Culture

Seth praised Monero's developers as 'absolutely amazing' but highlighted structural challenges: developers must accept payment in Monero, the CCS requires constant re-pitching every 3–6 months, and it's unsustainable for people with families.

More critically, he described Monero's community immune system as 'overactive' — attacking good contributors doing good work while too few defend them. He believes a concerted psychological operation has been waged against Monero by outside entities, sending bad actors to break the culture and drive away talent: 'You can destroy Monero in every sense but the technical.' He urged the community to stand up against non-technical, character-based attacks on developers and to use common sense when evaluating people with long track records of supporting Monero.

---

## Hardware Wallet Security

A major Coldcard hack (~$90M+) resulted from a flawed random number generator. Seth confirmed Monero would be equally susceptible — privacy doesn't help when private keys are brute-forceable. His custody recommendations:

- **Small amounts:** Hot wallet (Cake Wallet)
- **Savings:** Cupcake — turn an old phone into an air-gapped signer; fully open source; no hardware purchase that flags you at customs
- **Hardware wallet:** Trezor Safe 7 — excellent Monero support, native Cake integration
- **Upcoming:** Passport Prime — Cake app with Monero support already working internally

---

## Ecosystem Projects

- **Cuprate:** Cake is testing it internally; initial block download is 'disgustingly fast' — Seth synced a full node in three hours. Needs further testing and hardening.
- **Radar:** Not a wallet but designed to get 'freedom of money into regular people's hands.' Carrot's tiered view keys will make a Monero implementation feasible.
- **Thorchain:** Seth is 'skeptical as hell' of it working long-term but hopes Serai (Luke's DEX) arrives shortly after.
- **Arbiter/Hyperliquid:** A Vic project, very early stage; Hyperliquid 'is not decentralised' despite its marketing.
- **View keys:** If governments can compel view keys, they can simply compel you not to use Monero — 'it's a moot point.'

---

## Key Quote

> 'A healthy community is one that has an immune system, not an overactive immune system... in Monero, especially over the last four or five years, that immune system has gotten way overactive and has constantly attacked and chewed on good people who are doing good things.'
