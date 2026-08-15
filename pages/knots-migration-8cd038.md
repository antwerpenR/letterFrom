---
source: https://rogerprice.me/knots-migration
clipped: '2026-08-15T15:15:09+00:00'
title: Knots migration
site: Letter from ...around the world
published: '2025-09-11T11:44:51.000Z'
---

# Knots migration

# Knots migration

![Knots migration](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/09/ePA32NfxY7k.jpg)

Watch Adam's video explainer - [here](https://www.youtube.com/watch?v=ePA32NfxY7k)

Yes, it is possible to switch from the Bitcoin Core service to the Bitcoin Knots service on Start9's StartOS without performing a new Initial Block Download (IBD).

The reason this works is that Bitcoin Knots is a derivative of Bitcoin Core. They both use the exact same format for storing blockchain data (the `blocks` and `chainstate` directories). The process involves instructing the new Bitcoin Knots service to use the existing data downloaded by the Bitcoin Core service.

Because StartOS isolates data for each service, you cannot simply install Knots and have it "find" the data. You must manually move or re-assign the data volume.

### General Procedure

The exact steps can vary slightly with StartOS updates, but the high-level process will be as follows. **Always ensure you have a backup of your wallet file (`wallet.dat`) before attempting this.**

1. **Backup Your Wallet**:
   - Navigate to your Bitcoin Core service in the StartOS UI.
   - Go to `Config` > `Show Advanced Info`.
   - Find the option to `Create new backup`. This will back up your `bitcoin.conf` and your critical `wallet.dat` file. Download and save this backup to a secure, external location.
2. **Stop Bitcoin Core**:
   - In the StartOS UI, go to your Bitcoin Core service page and stop the service. It is crucial that the service is not running when you move the data to avoid corruption.
3. **Install Bitcoin Knots**:
   - If you haven't already, go to the Marketplace and install the Bitcoin Knots service. Do **not** start it yet. If it starts automatically, stop it immediately.
4. **Transfer Blockchain Data**:  
   This is the most critical step. StartOS manages data in isolated volumes. The goal is to copy the contents of Core's `mainnet` volume to the Knots' `mainnet` volume.
   - Use the StartOS File Browser service (you may need to install it from the Marketplace if you haven't).
   - Navigate to the directory where service data is stored. This is typically `/mnt/embassy-data/package-data/volumes/`.
   - You will see directories for each of your installed services, identified by their package ID (e.g., `bitcoin` for Bitcoin Core and `knots` for Bitcoin Knots).
   - Inside the `bitcoin/data/mainnet` directory, you will find the blockchain data (`blocks`, `chainstate`, etc.).
   - Copy all the contents from `bitcoin/data/mainnet` to `knots/data/mainnet`.
     - **Important**: Do not copy the `mainnet` folder itself, but rather the contents *inside* it. The destination `knots/data/mainnet` directory should be empty before you begin the copy.
     - This copy operation can take a significant amount of time, depending on the speed of your drive. Be patient and let it complete.
5. **Transfer Wallet and Config**:
   - Copy your `bitcoin.conf` and your `wallet.dat` file from the Bitcoin Core data directory to the Bitcoin Knots data directory. If you made a backup in Step 1, you can extract these files from the backup `.s9pk` file (it's just a zip archive).
   - The `wallet.dat` file will be in `bitcoin/data/mainnet/wallets/wallet.dat` or a similar path. Copy it to the corresponding location in the `knots/data` volume.
   - Copy your `bitcoin.conf` to the `knots/data` directory.
6. **Start Bitcoin Knots**:
   - Navigate to the Bitcoin Knots service in your StartOS UI.
   - Start the service.
7. **Verify**:
   - Check the logs for Bitcoin Knots. You can access these from its service page.
   - You should see messages indicating it is loading block index and using existing block files. You should **not** see messages indicating a new IBD is starting from block 0.
   - The node will then connect to peers and sync the few blocks and transactions that have occurred since you last ran Bitcoin Core. This should be very fast.

### Important Considerations

- **Version Compatibility**: This process is most reliable when the Bitcoin Core version you were running is not drastically older than the Bitcoin Knots version you are installing. Since Knots is based on Core, major differences could potentially require a re-index.
- **Re-indexing**: If Knots fails to start correctly and mentions a corrupt `chainstate`, you may need to force a re-index. This is still much faster than a full IBD. You can do this by adding `reindex=1` to your `bitcoin.conf` file, starting the service, and then removing that line after it has successfully started once.
- **Start9 Support**: The Start9 team and community are the best resource for the most current, platform-specific instructions. If you are unsure, it is highly recommended to ask in the official Start9 community channels (e.g., Matrix, Telegram) before proceeding.
