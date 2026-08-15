---
source: https://rogerprice.me/250412-options-to-run-a-nostr-relay
clipped: '2026-08-15T15:16:02+00:00'
title: 250412 Options to Run a Nostr relay
site: Letter from ...around the world
published: '2025-04-12T08:50:45.000Z'
---

# 250412 Options to Run a Nostr relay

# 250412 Options to Run a Nostr relay

![250412 Options to Run a Nostr relay](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/04/nostream.webp)

Nostream - one of several options

Per Grok: [https://x.com/i/grok/share/uWa9dZGKtFsVSduktS21TgWVm](https://x.com/i/grok/share/uWa9dZGKtFsVSduktS21TgWVm?ref=rogerprice.me)

Running a Nostr relay on a hosted Ubuntu system is a great way to contribute to the decentralized Nostr network. Several implementations and setup methods are available, each with its own advantages. Below, I outline the primary options, focusing on popular relay software compatible with Ubuntu, along with their setup processes, requirements, and considerations. I’ve prioritized open-source solutions and included practical details to help you choose based on your technical expertise and goals.

---

## Option 1: Nostr-rs-relay (Rust-based)

Overview: A lightweight, efficient Nostr relay written in Rust, using SQLite for storage. It’s ideal for those prioritizing performance and simplicity.Pros:

- High performance and low resource usage.
- Easy to configure with a single config.toml file.
- Active community support.
- Can run without Docker, reducing complexity for some setups.

Cons:

- Compilation requires Rust, which can take time on low-powered systems.
- Less beginner-friendly if you’re unfamiliar with Rust or systemd.

---

## Option 2: Nostream (TypeScript-based, Docker)

Full [source article here](https://www.maketecheasier.com/install-nostr-relay-linux/?ref=rogerprice.me)

Overview: A feature-rich Nostr relay written in TypeScript, typically deployed via Docker. It’s suitable for those comfortable with Docker and seeking advanced features like paid relay support.Pros:

- Docker simplifies deployment and updates.
- Supports advanced features (e.g., authentication, paid access).
- Well-documented for Docker-based setups.
- Active development.

Cons:

- Docker adds overhead, which may be unnecessary for simple relays.
- Requires familiarity with Docker and Node.js ecosystems.
- Higher resource usage compared to nostr-rs-relay.

---

## Option 3: Strfry (C++-based)

Overview: A high-performance relay written in C++, designed for scalability and minimal resource usage. Less common but great for advanced users.Pros:

- Extremely fast and lightweight.
- SQLite-based, with low disk usage.
- Suitable for high-traffic relays.

Cons:

- Less documentation compared to nostr-rs-relay or Nostream.
- Requires C++ compilation knowledge.
- Smaller community.

---

## Option 4: Umbrel Nostr Relay (Docker-based, Home Server Focus)

Overview: Umbrel offers a Nostr relay app for its home server software, which can be adapted for a hosted Ubuntu VPS. Ideal for those already familiar with Umbrel or seeking a user-friendly interface.Pros:

- Simplified setup via Umbrel’s app store.
- Web-based management.
- Integrates with other Umbrel apps (e.g., Bitcoin node).

Cons:

- Overkill for a VPS if you only need a relay.
- Requires running Umbrel’s full stack.
- Less flexible for custom configurations.

---

## Choosing the Right Option

- For Beginners: **Nostream with Docker (Option 2) is forgiving due to its clear documentation and community suppor**t. Umbrel (Option 4) is also beginner-friendly but heavier.
- For Performance: Nostr-rs-relay (Option 1) or Strfry (Option 3) are lightweight and fast, ideal for low-resource VPS or high-traffic relays.
- For Home Server Enthusiasts: Umbrel (Option 4) if you’re already running or want a full node ecosystem.
- Resource Considerations:
  - 2GB RAM suffices for nostr-rs-relay or Strfry on small relays.
  - 8GB RAM recommended for Nostream or Umbrel to handle Docker and databases.
  - Storage: Start with 20-50GB SSD; scale up if storing media or running a public relay (1TB could fill in months for busy relays, but most operators prune data).
- Security Tips:
  - Use a non-root user for running the relay.
  - Regularly update your system and relay software.
  - Backup your database (nostr.db or equivalent) to avoid data loss.
- Domain and DNS:
  - A domain is essential for wss:// connections. Use providers like Namecheap or Njalla.
  - Set an A record pointing to your VPS IP and ensure PTR records for email deliverability (if used).
- Testing and Monitoring:
  - Use nostr.watch to verify your relay’s status.
  - Monitor logs via journalctl or Docker logs.
  - Tools like websocat or Nostr clients (Damus, Nos, Primal) help test connectivity.

Enable a firewall (ufw):bash

```
sudo ufw allow 80,443,22/tcp
sudo ufw enable
```

---

Additional Notes

- Public vs. Private Relay:
  - Public relays store all events (pruning optional), requiring more storage.
  - Private relays (e.g., for you and friends) only store specified pubkey events, saving resources.
- Cost:
  - VPS costs: ~$5-20/month (e.g., DigitalOcean, Linode, Netcup).
  - Domain: ~$10-20/year.
- Maintenance:
  - Regularly check for software updates (git pull and rebuild).
  - Monitor disk usage (df -h) and prune old events if needed.
- Community Resources:
  - Join Nostr communities on Reddit (r/nostr) or Nostr itself for support.
  - Check Relay Wizard or Relay Runner for one-click scripts if you want automation.

If you’re unsure where to start, nostr-rs-relay (Option 1) is a solid choice for its balance of simplicity, performance, and community backing. Want me to dive deeper into any option or troubleshoot a specific setup issue?
