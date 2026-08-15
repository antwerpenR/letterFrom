---
source: https://rogerprice.me/tailscale-to-netbird
clipped: '2026-08-15T15:13:04+00:00'
title: Tailscale to NetBird
site: Letter from ...around the world
published: '2026-04-28T08:35:15.000Z'
---

# Tailscale to NetBird

# Tailscale to NetBird

![Tailscale to NetBird](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/04/netbird.png)

Here are the step-by-step instructions to install NetBird server on your remote Ubuntu server over SSH:

## Pre-Installation: SSH Into Your Server

```
ssh your-user@your-server-ip
```

## Step 1: Stop Tailscale Temporarily

```
sudo tailscale down
```

This prevents any routing conflicts during setup. The NetBird server components don't conflict with Tailscale, but stopping it ensures clean network state.

## Step 2: Install Docker (If Not Already Installed)

```
# Remove any old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
sudo docker run hello-world
```

[1][2]

## Step 3: Install Docker Compose Plugin

```
sudo apt-get install -y docker-compose-plugin
docker compose version
```

[3]

## Step 4: Run NetBird Quickstart Script

```
curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started.sh | bash
```

This script:

- Creates a `netbird` directory with Docker Compose configuration
- Generates a **built-in identity provider** (no external IdP needed) [4][5]
- Configures management server, signal server, and TURN relay
- Sets up automatic Let's Encrypt certificates (requires public domain pointing to this server)

## Step 5: Configure Your Domain

You need a domain/subdomain pointing to this server's public IP. The quickstart will prompt you for it.

If you don't have a domain yet, you can use a free subdomain service or purchase one. The server must be accessible on ports 80 and 443 for Let's Encrypt.

## Step 6: Access the Dashboard

Once complete, open in your browser:

```
https://your-domain
```

Create your admin account — the embedded IdP handles authentication automatically [4:1].

## Step 7: Generate Setup Key

In the dashboard:

1. Go to **Setup Keys**
2. Click **Create Setup Key**
3. Copy the key for client installation

## Step 8: Re-enable Tailscale (Optional)

```
sudo tailscale up
```

Your server now runs NetBird coordination services while maintaining Tailscale connectivity temporarily.

## Verification

Check NetBird server status:

```
cd netbird
docker compose ps
```

All containers should show `healthy` or `running`.

**Next:** Proceed to install NetBird clients on your devices using the setup key, then remove Tailscale from each.

---

1. [How to Install Docker on Ubuntu – Step-by-Step Guide | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04?ref=rogerprice.me) (1%) ↩︎
2. [Ubuntu | Docker Docs](https://docs.docker.com/engine/install/ubuntu/?ref=rogerprice.me) (1%) ↩︎
3. [Install the Docker Compose plugin](https://docs.docker.com/compose/install/linux/?ref=rogerprice.me) (< 1%) ↩︎
4. [Self-Hosting Quickstart Guide (5 min) - NetBird Docs](https://docs.netbird.io/selfhosted/selfhosted-quickstart?ref=rogerprice.me) (75%) ↩︎ ↩︎
5. [Self-Hosted Overview - NetBird - Mintlify](https://mintlify.com/netbirdio/netbird/deployment/self-hosted?ref=rogerprice.me) (23%) ↩︎
