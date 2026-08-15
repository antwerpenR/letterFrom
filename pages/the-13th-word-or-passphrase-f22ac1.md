---
source: https://rogerprice.me/passphrase
clipped: '2026-08-15T15:15:51+00:00'
title: The 13th word or Passphrase
site: Letter from ...around the world
published: '2025-05-25T13:05:23.000Z'
---

# The 13th word or Passphrase

# The 13th word or Passphrase

![The 13th word or Passphrase](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/05/bitcoin.jpg)

Explaining the "13th word" or "BIP39 passphrase"

Okay, let's clarify something crucial first: the standard Bitcoin wallet recovery phrase is typically **12 words**, not 13. A "13th word" usually implies an extension to the standard BIP39 mnemonic seed. I'll explain both the standard 12-word phrase and then how a 13th word might be used and interpreted.

**1. The Standard 12-Word Recovery Phrase (BIP39 Mnemonic)**

- **What it is:** This is a set of 12 words drawn from a specific dictionary (the BIP39 wordlist) that serves as the human-readable representation of your wallet's *seed*. The seed is a long, random number that's used to generate your private keys (and therefore your Bitcoin addresses).
- **Why it's important:** It's the *only* way to recover your Bitcoin if you lose access to your wallet (e.g., your phone is lost, your computer crashes, etc.). If you lose your 12-word phrase, you lose your Bitcoin.
- **How it works:**
  - **Randomness:** The 12 words are chosen in a way that encodes a high degree of randomness.
  - **Wordlist:** The words are selected from a defined list of 2048 words. This wordlist is standardized across many Bitcoin wallets. This standardization makes it easier for you to restore your wallet in a different wallet application if necessary.
  - **Checksum:** The 12th word isn't purely random. It's a checksum, which is calculated based on the first 11 words. This helps to detect errors if you've written down the phrase incorrectly. If the checksum is invalid, your wallet won't be restored.
- **Example:** `abandon ability able about above absent absorb abstract absurd abuse access accident` (This is just an example; *never* use this phrase for a real wallet. Anyone who sees it can steal your Bitcoin).

**2. The 13th Word (and Beyond): Passphrases/Seed Extension**

This is where things get more complex. The concept of a 13th word, or more generally a *passphrase*, is often used as a form of added security on top of the 12-word recovery phrase. It's sometimes referred to as a "25th word" if using the 24 word variant.

- **What it is:** A passphrase is a *string* (sequence of characters) that you add *on top of* your 12-word recovery phrase. It can be anything you want: a word, a sentence, a random string of characters, or even left completely blank. Be careful - it is case sensitive and it consists of every character that you type.
- **How it works:**
  - The passphrase is used to further *derive* the seed. The 12-word phrase generates a primary seed. That primary seed is then combined (typically using a cryptographic hash function like PBKDF2) with the passphrase to generate a *new* seed.
  - This new seed is then used to generate your private keys and addresses.
- **Key implications:**
  - **Creates a separate wallet:** Using a passphrase effectively creates an entirely *separate* wallet, even though it's derived from the same 12-word recovery phrase. If you restore your wallet with the 12-word phrase *without* the correct passphrase, you will not see your Bitcoin. You'll get a completely different set of addresses (and therefore an empty wallet).
  - **Increased security (but also increased responsibility):** A passphrase provides an extra layer of security. Even if someone obtains your 12-word recovery phrase, they can't access your Bitcoin without knowing the passphrase. *However*, if you forget your passphrase, you lose access to your Bitcoin just as surely as if you lost your 12-word phrase. There is no recovery if you forget the passphrase.
  - **"Hidden" wallets:** You can use different passphrases with the same 12-word phrase to create multiple "hidden" wallets. This can be useful for organizing your Bitcoin or for plausible deniability.
- **Example:**
  - 12-word phrase: `abandon ability able about above absent absorb abstract absurd abuse access accident`
  - Passphrase (13th word or string): `"MySecretPhrase"`
  - Restoring the wallet with *only* the 12-word phrase will show a different (empty) wallet.
  - Restoring the wallet with the 12-word phrase *and* the passphrase `"MySecretPhrase"` will show your correct Bitcoin balance.

**Important Considerations:**

- **Wallet Support:** Not all Bitcoin wallets support passphrases. Make sure your wallet does before using this feature.
- **Record Carefully:** If you use a passphrase, you *must* record it accurately and securely. Treat it with the same (or even greater) care as your 12-word recovery phrase.
- **Testing:** *Always* test your recovery process (both with and without the passphrase) with a small amount of Bitcoin before storing significant funds. This ensures that you understand the process and that you have correctly recorded your phrase and passphrase.

**In Summary:**

The 13th word is more accurately understood as a *passphrase* that adds an extra layer of security to your Bitcoin wallet. It's a powerful feature, but it comes with the responsibility of remembering it perfectly. If you're new to Bitcoin, it's best to thoroughly understand the basics of the 12-word recovery phrase before experimenting with passphrases. Always test your recovery process before committing significant funds.
