---
source: https://rogerprice.me/sap-migration-scandal
clipped: '2026-10-08T03:16:20+00:00'
title: SAP Migration scandal
site: Letter from ...around the world
published: '2026-09-20T11:46:42.000Z'
---

# SAP Migration scandal

# SAP Migration scandal

![SAP Migration scandal](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/The-SAP-Migration-Scandal-Nobody-Is-Talking-About.jpg)

## Background: How SAP Became Unavoidable

- Founded in 1972 by **Hasso Plattner** and four ex-IBM engineers who left after IBM scrapped their real-time financial accounting project for ICI (Imperial Chemical Industries). SAP stands for the German *Systemanalyse und Programmentwicklung*; ICI became their first customer.
- Their innovation: **real-time financial visibility** rather than overnight batch processing.
- **R/3 (1992)** moved SAP off mainframes onto standard computers, opening it to companies of almost any size; the **Y2K scramble** then won SAP thousands of contracts.
- Today: **425,000+ customers**, including **90% of the Fortune 500**.

> [!image]
> [![Click for a rather clear explanation - notes and summary plus checks below](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-28.png)](https://www.youtube.com/watch?v=tku46fHjgx4&ref=rogerprice.me)
> Click for a rather clear explanation - notes and summary plus checks below

## Lock-In by Design

- Implementations took **18–36 months**, cost tens of millions, and SAP encouraged heavy customisation — deepening customer dependency.
- Roughly **80% of large enterprises' core transactional data** lives inside SAP; annual maintenance fees of **22% of net licence value**; full switching costs of **$500m to several billion dollars**.

## The Lawsuits Against Customers

- **Diageo (2015)**: SAP claimed ~**£55m** because Diageo's distributors accessed SAP-derived data via Salesforce without logging into SAP directly. The **UK High Court ruled for SAP in February 2017**; Diageo settled.
- **Anheuser-Busch InBev**: SAP sought **over $600m** for the same type of indirect-access violations; settled out of court in 2018.
- Both companies accelerated their moves to SAP's newer cloud system under legal threat. Analysts called the practice "predatory" and a "licensing time bomb".
- **2018 "Digital Access" licensing**: SAP moved from counting users to counting **nine document types** (sales orders, invoices, purchase orders, etc.) — critics called it "the same problem with a different name".

## The 2027 Deadline

- Support for **ECC** ends **31 December 2027** — no security patches, regulatory or compliance updates afterwards.
- No free extensions; extra time requires a **2% premium** and committing to the new system by 2027.
- Migration to **S/4HANA** costs large enterprises **$50m–$500m+**; Halliburton disclosed **$46m in a single quarter (2025)**; the SAP consulting market hit **$16bn in 2025**, projected **$39bn by 2035**.
- With ~17 months left, **~65% of customers (~17,000 organisations)** haven't completed migration; German customer group **DSA** found **61% hadn't even started**.
- Consultant day rates have risen **30–100%**; **over 60% of migrations** run over budget or late.
- The **"clean core" mandate** forbids customising S/4HANA's core as customers did with ECC — all customisation must move to the separately-priced **BTP (Business Technology Platform)**.
- Big-firm architects charge **$1,800–$3,000/day**, with consulting fees consuming **60–80% of total migration cost** — and hourly billing creates incentives to stretch projects. SAP also takes a fee via its **Partner Edge programme** regardless of success.

## Historical Implementation Failures

| Company | Year | Outcome |
| --- | --- | --- |
| Hershey | 1999 | $112m project compressed to 18 months; order failures before Halloween; ~$100m lost revenue; stock dropped 19% |
| Nike | 2000 | Bad demand forecasts from SAP supply-chain system; $90m excess inventory; ~$100m lost sales; 20% stock decline |
| Lidl | 2011 | Abandoned after 7 years and ~€500m, mostly written off |
| Revlon | 2018 | Couldn't fulfil **$64m** of orders in one quarter; **$70m net loss**; shareholder class action |

## Restructuring and AI

- **January 2024**: €3bn restructuring, up to **10,000 job cuts**, citing AI. CFO **Dominik Asam** described annual job cuts as routine, "like brushing your teeth".
- At-risk staff were told to pitch an AI-powered version of their own role. By April 2025 only ~3,000 of 10,000 had been let go.
- German labour law protections meant cuts fell harder abroad: **82 employees cut at SAP's Palo Alto research facility in November 2025**.
- CEO **Christian Klein** calls AI a "once-in-a-lifetime opportunity", but independent analysts describe the **Joule** AI tool as useful for simple queries yet immature on complex processes and behind **Microsoft Copilot**.

## SAP's Paradoxical Financial Health

- **2025 revenue: €32.5bn**; cloud revenue up **27% YoY**; cloud backlog **€23bn** (up 27%); 2026 free cash flow projected ~**€10bn**; market cap ~**$244bn (September 2026)**.
- **July 2026**: the European Commission closed an antitrust investigation after SAP agreed **10-year binding commitments** — abolishing reinstatement fees, allowing split support contracts, removing all-or-nothing policies — but the 2027 deadline and cloud pricing were untouched.
- Both bearish and bullish analysts agree: customers have **no realistic alternative**, and complaints coincide with record revenue.

## Is There an Exit?

- Full exits to Oracle, Microsoft Dynamics or Workday take **5–10 years** and hundreds of millions to billions — unrealistic for most.
- Shifts are emerging: smaller firms choosing cloud-native alternatives from the start; some large enterprises keeping SAP only for core finance while Microsoft handles everything else.

## The Video's Central Argument

In a healthy market, a vendor that sues loyal customers, forces billion-dollar upgrades and treats layoffs as routine would lose customers — but SAP hasn't, because switching costs engineered over decades work exactly as intended. The closing question posed to viewers: will SAP's customers still be on SAP in 20 years, or is this the beginning of the end of its dominance?

---

Here are external references for the two claims from the video.

## 1. The 2027 upgrade requirement (ECC end of maintenance)

**SAP's own announcements:**

- SAP announced (February 2020) that mainstream maintenance for core applications of SAP Business Suite 7 / ECC ends **end of 2027**, with optional extended maintenance (for an additional fee) until **end of 2030**, and a maintenance commitment for S/4HANA until 2040 [1], [2], [3].
- SAP confirms that continuing on-premise paths still require a shift to S/4HANA by 2027 or 2030, otherwise customers fall into customer-specific maintenance with limited support [4].

**Independent commentary on what it means for customers:**

- Analysis of the four post-2027 options (migrate, extended maintenance, third-party support, or customer-specific maintenance) and why none is cost- or risk-free [5], [6].
- Detail on extended maintenance pricing — reported as an additional ~9% premium for ECC 6.0 EHP 6–8 through 2030 [7] (note: some sources cite different figures for the premium, so treat the exact percentage with caution).
- Reports that 60%+ of ECC customers had not yet migrated as of 2026 [8].

## 2. The court cases against customers

**SAP v Diageo (UK High Court, February 2017):**

- The High Court ruled in SAP UK Ltd's favour on 16 February 2017, finding Diageo liable for additional licence and maintenance fees — commonly reported as **in excess of £54m**, with SAP's calculation reaching ~£55m on top of the ~£50–60m Diageo had already paid [9], [10], [11], [12].
- Legal analysis: Diageo's customers and distributors accessed SAP-derived data via Salesforce (the "Gen2" system), which the court held went beyond the licence scope; the exact damages were to be set at a later quantum trial unless settled [13], [14].
- The case was widely described as the UK's first major "indirect access" ruling and a warning for all SAP customers [15], [16], [11:1].

**SAP v AB InBev (US arbitration, 2017; settled 2018):**

- AB InBev disclosed in an SEC filing that SAP was seeking **US$600m** for unlicensed direct and indirect use of its software, filed as a US arbitration claim against an AB InBev unit [17], [18], [19].
- The parties **settled out of court in March 2018** (some reports date the settlement to 30 June 2017 per AB InBev's annual report), without clarifying SAP's indirect-access position [17:1], [19:1].
- The case echoed the Diageo dispute — Salesforce integration with SAP data was again the trigger [20], [21].

**Aftermath:**

- Reuters reported that SAP revised its pricing (introducing the Digital Access model) after the crackdown on large customers backfired [18:1], [22].

### Verification notes

- The video's claim of "£55m" for Diageo matches SAP's own calculation in court filings [10:1]; most press reported "over £54m" [9:1], [15:1].
- The video's "over $600m" claim for AB InBev is confirmed by the SEC filing disclosure [17:2], [19:2].
- One correction to the video's framing: extended maintenance to 2030 exists as an official paid option [1:1], rather than there being "no extensions" — though it does carry a premium.

**References**

---

1. [SAP Extends Its Innovation Commitment for SAP S/4HANA, ...](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/?ref=rogerprice.me) (12%) ↩︎ ↩︎
2. [Updated SAP S/4HANA Transition Policy](https://news.sap.com/2020/02/sap-s4hana-transition-updated-policy/?ref=rogerprice.me) (4%) ↩︎
3. [Interview on Extended Maintenance for SAP S/4HANA | SAP News Center](https://news.sap.com/2020/02/interview-extending-maintenance-for-sap-s4hana/?ref=rogerprice.me) (11%) ↩︎
4. [Guided Paths to the Cloud with SAP | SAP News Center](https://news.sap.com/2024/01/navigating-the-future-guided-cloud-journey-with-sap/?ref=rogerprice.me) (7%) ↩︎
5. [SAP ECC End of Life: What Happens After 2027? | Rialtes](https://www.rialtes.com/insights/blogs/sap-ecc-end-of-support-what-happens-after-2027?ref=rogerprice.me) (4%) ↩︎
6. [SAP ECC End Of Support: A 2027 Decision Framework](https://www.panorama-consulting.com/18-months-to-the-sap-ecc-cliff-and-half-of-customers-still-havent-moved/?ref=rogerprice.me) (6%) ↩︎
7. [SAP S/4HANA Migration Strategies for Customers After 2027](https://www.tjc-group.com/blogs/beyond-2027-strategic-options-for-sap-customers-for-s-4hana-migration/?ref=rogerprice.me) (1%) ↩︎
8. [SAP ECC Support End Date 2027: What Businesses Need to Know | SAVIC](https://www.savictech.com/insights/ecc-end-of-maintenance-2027/?ref=rogerprice.me) (7%) ↩︎
9. [The Scope Of 'Indirect Access' To Software: SAP UK ...](https://www.legal500.com/en/intelligence/united-kingdom/intellectual-property/the-scope-of-'indirect-access'-to-software-sap-uk-limited-v-diageo-great-britain-limited?ref=rogerprice.me) (2%) ↩︎ ↩︎
10. [The SAP v. Diageo decision – a realistic approach to ...](https://www.dentons.com/en/insights/articles/2017/may/17/the-sap-v-diageo-decision-a-realistic-approach-to-indirect-access?ref=rogerprice.me) (5%) ↩︎ ↩︎
11. [SAP's Licensing Time-Bomb](https://www.pillsburylaw.com/en/news-and-insights/saps-licensing-time-bomb.html?ref=rogerprice.me) (2%) ↩︎ ↩︎
12. [Drinks company Diageo loses battle with SAP, indirect ...](https://itassetmanagement.net/2017/02/21/diageo/?ref=rogerprice.me) (2%) ↩︎
13. [SAP v Diageo – the UK’s first software over-deployment case: takeaways ...](https://kempitlaw.com/insights/sap-v-diageo-the-uks-first-software-over-deployment-case-takeaways-for-business-2-2/?ref=rogerprice.me) (4%) ↩︎
14. [Software licensing - ‘direct and indirect access and use’ SAP UK ...](https://www.lexology.com/library/detail.aspx?g=b72a7719-044a-4971-bbd1-34a27b4aa63d&ref=rogerprice.me) (2%) ↩︎
15. [Indirect Software Licensing: SAP v Diageo – 3 Years Later](https://kempitlaw.com/insights/indirect-software-licensing-sap-v-diageo-3-years-later/?ref=rogerprice.me) (2%) ↩︎ ↩︎
16. [Five Shades Darker? – What The Diageo “Indirect Access” ...](https://www.forrester.com/blogs/17-02-21-five_shades_darker_what_the_diageo_indirect_access_judgement_really_means_for_sap_customers/?ref=rogerprice.me) (2%) ↩︎
17. [AB InBev settles out of court in $600m SAP licensing dispute](https://www.computerweekly.com/news/252437245/AB-InBev-settles-out-of-court-in-600m-SAP-licensing-dispute?ref=rogerprice.me) (9%) ↩︎ ↩︎ ↩︎
18. [SAP revises pricing after crackdown on big customers ...](https://www.reuters.com/article/technology/sap-revises-pricing-after-crackdown-on-big-customers-backfires-idUSKBN1HH1ML/?ref=rogerprice.me) (2%) ↩︎ ↩︎
19. [A List of SAP Implementation Failures - Brightwork Research & Analysis](https://www.brightworkresearch.com/list-of-sap-implementation-failures/?ref=rogerprice.me) (6%) ↩︎ ↩︎ ↩︎
20. [SAP goes after world’s largest brewing company in $600m licence dispute](https://www.computerweekly.com/news/450418295/SAP-goes-after-worlds-largest-brewing-company-in-600m-licence-dispute?ref=rogerprice.me) (2%) ↩︎
21. [When the World's Largest Brewer Faced a $600 Million SAP Bill](https://www.linkedin.com/pulse/when-worlds-largest-brewer-faced-600-million-sap-bill-edward-heyburn-wkose?ref=rogerprice.me) (2%) ↩︎
22. [SAP vs. AB InBev: What Every SAP Customer Needs to Know Now](https://thirdstageconsulting.com/blog/sap-vs-ab-inbev-licensing-dispute/?ref=rogerprice.me) (6%) ↩︎
