---
source: https://rogerprice.me/upgrade-bitcoin-core
clipped: '2026-08-15T15:15:07+00:00'
title: Upgrade Bitcoin Core
site: Letter from ...around the world
published: '2025-09-16T10:08:26.000Z'
---

# Upgrade Bitcoin Core

# Upgrade Bitcoin Core

![Upgrade Bitcoin Core](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/09/op-return.png)

### Understanding the OP\_RETURN Default

The default size for `OP_RETURN` (the data carrier size) in Bitcoin Core has been 80 bytes of data for many years. This is a network-wide standard for relaying transactions, not just a local default. It is most unfortunate that Bitcoin Core v30 changes this default value but you can retain the default when you upgrade.

The configuration parameter in Bitcoin Core is `-datacarriersize`. If you have not manually set this in your configuration, your node is already using the default. The goal of these instructions is to verify this and ensure the setting is maintained after the upgrade.

---

## Step-by-Step Upgrade Instructions

Follow these steps to safely upgrade Bitcoin Core on your StartOS device while preserving your configuration.

### Step 1: Pre-Upgrade Health Check and Backup

Before any major update, it is critical to ensure your system is healthy and backed up.

1. **Log in** to your StartOS device's web interface.
2. Navigate to **System > Create Backup**.
3. Follow the on-screen instructions to create a complete backup of your system. **Do not skip this step.** An upgrade is a major change, and a backup ensures you can restore your system if anything goes wrong.

### Step 2: Check Your Current Configuration

Verify your current `OP_RETURN` setting before you upgrade.

1. In the StartOS UI, go to **Services > Bitcoin Core**.
2. Select the **Config** tab.
3. Scroll down to the **Advanced** section and click **Properties**. This is where you can set custom startup options for Bitcoin Core.
4. Look for an entry named `datacarriersize`.
   - **If you DO NOT see `datacarriersize` listed:** Your node is using the default value (80 bytes). This is the most common scenario.
   - **If you DO see `datacarriersize` listed:** Take note of the value you have set. You will want to verify that this custom value is still present after the upgrade.

### Step 3: Perform the Upgrade (When v30 is Available)

Once the Start9 team has packaged Bitcoin Core v30 and it appears in your marketplace, you can proceed.

1. Navigate to the **Marketplace** section in your StartOS UI.
2. Under the **Updates** tab, you should see Bitcoin Core with a notification that a new version is available.
3. Click the **Update** button next to the Bitcoin Core service.
4. StartOS will now handle the entire process:
   - It will download the new Bitcoin Core v30 package.
   - It will safely stop the current version of Bitcoin Core.
   - It will install the new version and migrate your configuration.
   - Do not start Bitcoin Core - if it starts, stop it immediately
5. Be patient. This process can take several minutes. You can monitor the progress from the service's main page.

### Step 4: Post-Upgrade Verification

After the upgrade is complete you must enter your chosen value for OP\_RETURN.

1. Navigate back to **Services > Bitcoin Core**.
2. Go to the **Config > Properties** section again, just as you did in Step 2.
3. Enter your `datacarriersize` setting:
   - Ensure your desired value is present in the configuration - you will likely want to 80 and click **Save Config**. The service will restart to apply the change.
4. Finally, check the service logs for any errors.
   - Go to **Services > Bitcoin Core > Logs**.
   - Look for any red error messages or warnings, especially near the beginning of the log after the service started up. If you see errors related to configuration, double-check your settings in the `Config` tab.
