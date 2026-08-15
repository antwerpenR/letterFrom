---
source: https://rogerprice.me/immich-getting-started
clipped: '2026-08-15T15:14:39+00:00'
title: Immich - getting started
site: Letter from ...around the world
published: '2025-12-19T02:09:12.000Z'
---

# Immich - getting started

# Immich - getting started

![Immich - getting started](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/12/immich.png)

Step by step guide to get going

To get started with Immich on your Linux Mint Cinnamon system, using photos exported from Google Takeout and storing everything on an external SSD, follow these steps. This assumes you're starting from scratch, have basic terminal familiarity, and your external SSD is connected (formatted as ext4 for best compatibility—use the Disks utility if needed to format it). Immich runs as a Docker-based server, so we'll install Docker first, then Immich, and use the immich-go tool for migration (it's the most reliable for handling Google Takeout's ZIP files, JSON metadata, albums, descriptions, locations, and duplicates without Node.js dependencies).

**1. Mount Your External SSD Persistently**

Immich will store uploaded photos on the SSD to avoid filling your internal drive.

- Open a terminal (Ctrl+Alt+T).
- Identify the SSD: Run lsblk -f or use the Disks utility (Menu > Administration > Disks) to find its device (e.g., /dev/sdb1) and filesystem (should be ext4).
- Get the UUID: sudo blkid /dev/sdb1 (replace with your device).
- Create a mount point: sudo mkdir /mnt/ssd
- Edit /etc/fstab for persistent mounting: sudo nano /etc/fstab
  - Add a line: UUID=your-uuid-here /mnt/ssd ext4 defaults 0 2
  - Save (Ctrl+O, Enter, Ctrl+X) and test: sudo mount -a
- Create a storage folder: sudo mkdir /mnt/ssd/immich-library
- Set permissions (for your user): sudo chown -R $USER:$USER /mnt/ssd/immich-library
- Common pitfall: If the SSD unmounts on reboot, double-check fstab syntax or UUID.

**2. Install Docker on Linux Mint**

Immich requires Docker Engine and the Compose plugin (not the old docker-compose).

- Update packages: *sudo apt update*
- Install prerequisites: *sudo apt install ca-certificates curl gnupg lsb-release*
- Add Docker's GPG key: *sudo mkdir -p /etc/apt/keyrings  
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg*
- Add Docker repository (Mint is Ubuntu-based, use "jammy" for Mint 21/22):  
  *echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null*
- Install Docker:   
  *sudo apt update  
  sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin*
- Add your user to the docker group:   
  *sudo usermod -aG docker $USER (log out/in to apply).*
- Test: *docker run hello-world*
- Common pitfall: If you had an old Docker version (e.g., from apt), uninstall it first: sudo apt remove docker docker-engine docker.io containerd runc

**3. Install and Configure Immich**

- Create a project directory: *mkdir ~/immich && cd ~/immich*
- Download files:  
  *wget https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml  
  wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env*
- Edit .env (nano .env):
  - Set UPLOAD\_LOCATION=/mnt/ssd/immich-library (this points storage to your SSD).
  - Set TZ=your/timezone (e.g., America/New\_York—find yours with tzselect).
  - Set a strong DB\_PASSWORD=yourpassword (used for the internal database).
  - Leave other defaults unless needed (e.g., IMMICH\_VERSION=release for latest stable).
- The docker-compose.yml uses ${UPLOAD\_LOCATION}:/usr/src/app/upload to mount your SSD path— no edit needed unless customizing further.
- Start Immich: *docker compose up -d*
- Access Immich: Open a browser to [http://localhost:2283](http://localhost:2283/?ref=rogerprice.me) (or your machine's IP:2283 if remote).
- Create an admin account (first user is admin).
- Common pitfalls:
  - If "name" regex error, ensure you're using docker compose (not old docker-compose).
  - Check logs if it fails: docker compose logs.
  - Firewall: If inaccessible, allow port 2283: sudo ufw allow 2283.
  - Resources: Immich needs ~4GB RAM/2 cores minimum; monitor with htop.

**4. Prepare Your Google Takeout Photos**

- Move your Google Takeout ZIP files (e.g., takeout-\*.zip) to a folder on the SSD or internal drive (e.g., /mnt/ssd/takeout)—no need to unzip them manually, as immich-go handles it.
- If already unzipped, ensure photos and JSON files are together (Google Takeout structure: folders like "Google Photos" with images and .json sidecars for metadata).

**5. Migrate Photos Using immich-go**

immich-go is ideal for Google Takeout—it processes ZIPs, matches JSON metadata (dates, locations, descriptions), recreates albums, skips duplicates/junk, and uploads directly.

- Download the Linux binary: Go to [https://github.com/simulot/immich-go/releases](https://github.com/simulot/immich-go/releases?ref=rogerprice.me), download the latest linux\_amd64 binary (e.g., immich-go\_linux\_amd64).
- Make it executable: Move to ~/immich (or anywhere), then   
  *chmod +x immich-go\_linux\_amd64*   
  (rename to immich-go for simplicity:   
  *mv immich-go\_linux\_amd64 immich-go*).
- Create an API key in Immich: Log in > User icon (top-right) > Account Settings > API Keys > Create new key (enable all permissions like asset.upload, album.create).
- Dry run first (simulates without uploading):  
  ./immich-go upload from-google-photos --dry-run --server=http://localhost:2283 --api-key=your-api-key-here /mnt/ssd/takeout/takeout-\*.zip
  - This scans for issues (e.g., duplicates, junk files like .DS\_Store). It may take hours for large libraries (100k+ photos).
- If dry run succeeds, run the real upload (remove --dry-run):  
  *./immich-go upload from-google-photos --server=http://localhost:2283 --api-key=your-api-key-here /mnt/ssd/takeout/takeout-\*.zip*
  - Add options if needed:
    - --ban-file .DS\_Store --ban-file thumbs.db (skip more junk).
    - --create-albums (explicitly recreate albums, though it's automatic).
    - --concurrency 4 (limit threads for slower machines; default is CPU-based).
- Monitor progress in terminal. Immich will process (thumbnail, face recognition) in the background—check Jobs tab in web UI.
- Common pitfalls:
  - API key errors: Ensure permissions include asset.copy/delete/upload.
  - Large libraries: Pause Immich's ML jobs (in Admin > Jobs) during upload to avoid overload.
  - Metadata issues: If some dates/locations miss, it's rare but due to Takeout inconsistencies—rerun on affected files.
  - Backups: Keep Takeout ZIPs as a safety net.

**6. Post-Migr**ation Setup

- Install Immich mobile app (Android/iOS) for auto-backups: Log in with your server URL [(http://your-ip:2283)](http://your-ip:2283/?ref=rogerprice.me) and API key.
- Enable backups in app settings (points to your SSD storage).
- Verify: Browse Immich web/app—albums, search, faces should work.
- Maintenance: Update Immich (docker compose pull && docker compose up -d). Backup database (built-in) and SSD folder regularly (e.g., with rsync or Pika Backup).
- Alternatives if issues: Use Immich's built-in CLI (docker exec -it immich\_server immich upload ...) for simple uploads, but immich-go is better for Takeout.

> This setup keeps all photos on your external SSD, gives you a Google Photos-like experience, and preserves privacy. If you hit errors (e.g., permissions, network), share logs for help!
