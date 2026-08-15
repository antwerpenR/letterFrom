---
source: https://rogerprice.me/numopay-with-calle
clipped: '2026-08-15T15:13:50+00:00'
title: NumoPay with Calle
site: Letter from ...around the world
published: '2026-03-11T06:30:42.000Z'
---

# NumoPay with Calle

# NumoPay with Calle

![NumoPay with Calle](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/03/Numopay.png)

Source: [NumoPay: Tap-to-Pay Bitcoin with Calle | SLP728](https://stephanlivera.com/episode/728/)

### **What is Numo Pay?**

Numo Pay is an **open-source, free Android payment terminal** that enables merchants to accept Bitcoin payments in physical stores. It can run on any Android phone or standard POS hardware. The project emerged from stealth development over several months, driven by a desire to bring **tap-to-pay functionality**—ubiquitous in fiat payments—to the Bitcoin ecosystem.

> [!image]
> [![Click to listen to the full interview](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/03/image-16.png)](https://stephanlivera.com/episode/728/?ref=rogerprice.me)
> Click to listen to the full interview

### **The Core Innovation: Tap-to-Pay for Bitcoin**

The interview's central theme is Numo Pay's breakthrough in user experience. While Bitcoin has converged around QR code scanning, Calle's team wanted to replicate the seamless fiat experience where users tap their phones and payments complete in seconds. They achieved this by **leveraging Cashu**, a Chaumian e-cash system built on Bitcoin.

Cashu operates as a custodial system where users deposit Bitcoin to receive privacy-preserving e-cash tokens stored locally on their devices. Because the e-cash lives on the payer's phone, **NFC chips can transfer tokens directly between devices**—no internet connection required for the customer. This creates a rare alignment where **the best privacy option also delivers the best UX**.

### **How It Works**

Setup takes approximately five seconds. Merchants download the app, choose a Cashu mint (where Bitcoin will be held), and begin accepting payments immediately—**no server, VPS, or additional infrastructure required**.

The terminal displays **dual QR codes**: one for Cashu payments, another for Lightning. For tap-to-pay:

- **Cashu users**: Tap their phone to the terminal; e-cash transfers offline via NFC in under a second
- **Lightning users**: Currently only Phoenix wallet supports this; the terminal broadcasts a Lightning invoice via NFC for online settlement

The system also supports **BIP 321** (November 2024), enabling unified payment payloads containing on-chain addresses, Lightning invoices, and Cashu requests in a single NFC transmission. Wallets then auto-select their preferred payment method.

### **Critical Risk Mitigation: Auto-Withdrawal**

A standout feature addresses custodial risk concerns. Merchants can configure **auto-withdrawal to a Lightning address** when balances hit a threshold (e.g., 50,000 sats). This limits exposure per device—critical for businesses with multiple terminals or employee-operated POS systems. Funds automatically flow to the owner's non-custodial wallet.

### **Significant and Surprising Points**

1. **Purely offline payments work**: The customer's phone needs no connectivity. E-cash travels device-to-device via NFC; only the merchant's terminal requires internet to later settle with the mint.
2. **Double-blind privacy**: The mint sees only that the POS performed a swap (e-cash in, e-cash out). It cannot identify who paid, what was purchased, or any payer personal information.
3. **Infrastructure minimalism**: Unlike BTCPay Server's historically involved setup, Numo Pay requires zero technical knowledge or server management. This directly addresses the "Bitcoin enthusiast owner" problem—where only the owner knows how to operate the system, leaving cashiers unable to process payments.
4. **The fiat UX gap is widening**: Calle emphasizes that post-lockdown, restaurants increasingly use QR-based web checkouts where customers pay at their tables without staff interaction. Bitcoin risks obsolescence if it cannot match these efficiency gains.
5. **AI development velocity**: Calle describes "vibe coding" as a paradigm shift comparable to "walking versus driving." He estimates **95% of developers now produce inferior code to AI agents**, which operate 100x faster. The transformation occurred within 12 months; developers not adopting these tools are "almost too late".
6. **Cashu ecosystem scale**: From two people three years ago, Cashu now encompasses **50-100 active mints**, dozens of wallets, and hundreds of contributors. Use cases extend beyond Bitcoin: Tollgate sells internet access denominated in megabytes; Portal issues privacy-preserving conference tickets that prevent double-spending without identity linkage.
7. **Corporate adoption vectors**: Organizations use Cashu for **internal fund transfers** between multinational branches and **salary payments**—enabling payroll without collecting employee on-chain addresses or Lightning node public keys.

### **Future Roadmap**

- **BTCPay Server integration**: Numo's UI/UX will become available as a frontend for BTCPay backends
- **Operational dashboard**: Centralized monitoring for multiple terminals with analytics and time-series data
- **Enhanced merchant features**: Tipping, multi-table restaurant management, basket functionality, and receipt printing already exist

### **Fundamental Philosophy**

Calle's closing argument centers on **default privacy through superior UX**. Most users won't research privacy tools; systems must embed privacy without cognitive load. Privacy "lives in numbers"—mass adoption protects everyone. The goal isn't serving "Bitcoin nerds" but creating solutions where merchants focus on sales, not infrastructure, while users gain uncensorable, untrackable payments automatically [1:14].

Numo Pay is available at **numopay.org**, requiring only an Android device to receive payments (iOS and Android can pay).
