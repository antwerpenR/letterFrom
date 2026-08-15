---
source: https://rogerprice.me/fastmail
clipped: '2026-08-15T15:13:53+00:00'
title: Fastmail
site: Letter from ...around the world
published: '2026-03-09T06:07:24.000Z'
---

# Fastmail

# Fastmail

![Fastmail](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/03/The-Email-Provider-Google-Doesn-t-Want-You-to-Know-About--Fastmail-Interview-.jpg)

Source: [The Email Provider Google Doesn't Want You to Know About (Fastmail Interview)](https://www.youtube.com/watch?v=FByPnomEh5o)

Here is a summary of Henry's interview with Ricardo Cignas, Chief Engineer at FastMail, highlighting significant and surprising points.

## Summary

Ricardo Cignas has spent **20 years** in email—10 at Pobox.com, which FastMail acquired a decade ago. He remains driven by FastMail's four core values: being **stewards of your data**, **good internet citizens**, and prioritizing user empowerment. These values, he emphasizes, are lived daily, not just marketing slogans.

[![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/03/image-14.png)](https://www.youtube.com/watch?v=FByPnomEh5o&ref=rogerprice.me)

### FastMail vs. Gmail and Proton

**Against Gmail**, Ricardo argues FastMail wins on both ethics and experience. Gmail's business model—large-scale data analytics—means "if you're not the customer, you're the product." More personally, he finds Gmail creates "friction" in daily use, while FastMail offers "no friction" productivity 1.

**Against Proton/Tutanota**, FastMail deliberately avoids native end-to-end encryption. Ricardo explains this is a principled technical stance, not a limitation:

- Email standards (RFC 822) transmit messages **in the clear**
- Key distribution for strangers remains unsolved
- "Walled garden" encryption breaks when emailing outside the ecosystem, creating "weird stuff"—signed-but-unencrypted messages, or emails that say "you have an email" and redirect to web portals 1

> **"I don't ever want to see [email] go away. I'd like to see it continue to evolve."**

### Surprising Technical Revelations

| Point | Detail |
| --- | --- |
| **Phone number resistance** | Ricardo: "I don't want to know your phone number. I don't want to know anybody's phone number who's using FastMail." Required only for fraud prevention, not identity 1 |
| **VOIP workaround was intentional** | Mobile signup bypasses phone verification—"at least somewhat on purpose" 1 |
| **JMAP origins** | FastMail created JMAP ~2014 to replace IMAP's inefficiencies; now an IETF standard (RFC 8620/8621) 1 |
| **Offline architecture** | Browser runs a "tiny JMAP server inside of the tab" for caching—enabling offline without native apps 1 |
| **Support staff see "lorem ipsum"** | Customer service sees structural placeholders, not actual content, unless users explicitly opt in 1 |

### Open Source Philosophy

FastMail maintains **Cyrus** (92% of commits in last 10 years), the leading open-source IMAP/JMAP/CalDAV/CardDAV server. However, Ricardo defends **not** open-sourcing everything:

- "Every extra button is a problem"
- Open-sourcing creates "enormous" maintenance overhead
- "How do we produce the most benefit for the most people?" sometimes means standards work over code dumps 1

### JMAP: The Hidden Speed Engine

FastMail's name predates JMAP by over a decade, but modern speed comes from layered engineering:

1. **Ajax UI (2013-14)**: Shifted to browser-based application with local caching
2. **JMAP**: HTTP/JSON protocol replacing IMAP's "Shakespearean" complexity
3. **Optimistic UI**: Delete appears instant; server catches up after 1

**Security benefit**: JMAP uses standard **web push** (RFC 8030) instead of persistent connections, eliminating the need for cloud services to store OAuth tokens for push notifications—a significant improvement over how IMAP clients handle Gmail on iOS 1.

### The "Good Internet Citizen" Ethic

Ricardo's most passionate argument: the internet's federated, decentralized nature is fragile. Being a "good citizen" means:

- Building tools that let users **separate life contexts** ("you might as well be two strangers communicating with yourself")
- Supporting **open standards first**, proprietary APIs only when unavoidable
- **"Don't be a dick"**—explicitly stated as corporate and personal responsibility 1

### Future Directions

- **Teams/small business expansion**—carefully adding features without "fruit salad" complexity
- **JMAP for calendars/contacts**—standards finalized, implementation polishing
- **Automatic OAuth configuration**—eliminating "IMAP server name" setup friction entirely 1

### Key Quote on Privacy Trade-offs

> **"There's always that slider between... convenience and secrecy. And people make their choice on that front."**

FastMail's position: they provide **privacy** (data stewardship, no analytics) and **security** (infrastructure hardening, zero-trust goals), but not **secrecy** (mathematical unavailability of data). For that, they explicitly recommend **Signal** 1.
