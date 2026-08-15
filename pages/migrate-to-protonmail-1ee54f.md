---
source: https://rogerprice.me/migrate-to-protonmail
clipped: '2026-08-15T15:15:50+00:00'
title: Migrate to Protonmail
site: Letter from ...around the world
published: '2025-05-27T08:35:02.000Z'
---

# Migrate to Protonmail

# Migrate to Protonmail

![Migrate to Protonmail](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2025/05/proton-mail-og.png)

Okay, migrating your company email from Google Workspace (formerly G Suite) to ProtonMail, especially when you're only concerned with email, is quite manageable. Here's a step-by-step guide:

**Key Assumption:** You have a custom domain (e.g., `yourname@yourcompany.com`) currently managed by Google Workspace, and you want to use this same domain with ProtonMail.

**Phase 1: Preparation & ProtonMail Setup**

1. **Choose a ProtonMail Plan:**
   - If it's just for you (one user) with a custom domain, **Proton Mail Plus** is sufficient.
   - If you have multiple users (even if it's just a couple), you'll need a **Proton Business** plan. This allows you to manage multiple users under your organization and domain.
   - Sign up for the chosen plan on the ProtonMail website.
2. **Add and Verify Your Custom Domain in ProtonMail:**
   - Log in to your ProtonMail account.
   - Go to `Settings` -> `Go to settings` -> `Organization` -> `Domain names` (or `Proton Mail` -> `Domains` if on Mail Plus).
   - Click `Add domain` and follow ProtonMail's instructions.
   - This will involve adding a **TXT record** to your domain's DNS settings (at your domain registrar, e.g., GoDaddy, Namecheap, Cloudflare) to prove you own the domain. ProtonMail will provide the specific TXT record value.
   - **Wait for verification.** This can take a few minutes to a few hours.
3. **Set Up SPF, DKIM, and DMARC Records for ProtonMail:**
   - Once your domain is verified, ProtonMail will provide you with new **SPF, DKIM, and DMARC** records.
   - Go back to your domain registrar's DNS settings.
   - **SPF:** You'll likely *replace* your existing Google SPF record (`v=spf1 include:_spf.google.com ~all`) with ProtonMail's (e.g., `v=spf1 include:_spf.protonmail.ch mx ~all`).
   - **DKIM:** Add the new DKIM records provided by ProtonMail. You might need to remove old Google DKIM records if they conflict (or just leave them if your registrar allows multiple DKIM records for different selectors).
   - **DMARC:** If you have an existing DMARC record, ensure it aligns with ProtonMail's recommendations. If you don't have one, add the one ProtonMail suggests.
   - **Important:** These DNS changes ensure your emails sent from ProtonMail are authenticated and less likely to be marked as spam.
4. **Create User Accounts in ProtonMail (if applicable):**
   - If you have multiple users (and a Proton Business plan), go to `Organization` -> `Users and addresses` in ProtonMail settings and create accounts for each user with their email address on your custom domain (e.g., `user1@yourcompany.com`, `user2@yourcompany.com`).

**Phase 2: Migrating Your Emails**

ProtonMail offers a tool called "Easy Switch" which is generally the easiest way.

1. **Use ProtonMail Easy Switch:**
   - In ProtonMail settings, go to `Import via Easy Switch` (usually on the left sidebar).
   - Select `Google`.
   - You'll be prompted to sign in to your Google Workspace account. Grant ProtonMail the necessary permissions (usually to access Gmail via IMAP).
   - Choose what you want to import: **Emails**. (You've already stated you don't use Calendar or Contacts, so deselect those).
   - Select the email address(es) you want to import *from* (your Google Workspace addresses) and map them to the email address(es) you want to import *to* (your ProtonMail addresses).
   - Start the import.
   - **Note:** This process can take a significant amount of time, from hours to days, depending on the size of your mailbox. You can close the browser window; the import will continue in the background. You'll receive an email when it's complete.

**Alternative (More Manual) Import Methods if Easy Switch Fails:**

- **Using an Email Client (e.g., Thunderbird):**
  1. Set up both your Google Workspace account and your ProtonMail account in Thunderbird.
     - For Google Workspace: Use standard IMAP settings.
     - For ProtonMail: You'll need to install and configure the **ProtonMail Bridge**. The Bridge runs on your computer and provides local IMAP/SMTP server details that Thunderbird can connect to, allowing it to access your encrypted ProtonMail mailbox.
  2. Once both accounts are set up in Thunderbird, you can drag and drop emails/folders from your Google Workspace account to your ProtonMail account. This is slower and more manual but gives you control.
- **Google Takeout & ProtonMail Import-Export App:**
  1. Go to Google Takeout (`takeout.google.com`).
  2. Deselect all services and then select only **Mail**. Choose to export all mail or specific labels.
  3. Select the export format as **MBOX**.
  4. Download the MBOX file(s) once Google prepares them.
  5. Download and install the ProtonMail **Import-Export app** from their website.
  6. Use the Import-Export app to import the MBOX file(s) into your ProtonMail account.

**Phase 3: Switching Mail Delivery (The MX Record Change)**

**CRITICAL STEP:** Do this *after* your initial email import is complete or at least significantly progressed. Once you change MX records, new emails will start flowing to ProtonMail, not Google Workspace.

1. **Get ProtonMail's MX Records:**
   - In ProtonMail settings, under your domain configuration (`Domain names`), ProtonMail will show you the MX records you need to set. They typically look like:
     - `mail.protonmail.ch` (Priority 10)
     - `mailsec.protonmail.ch` (Priority 20)
2. **Update MX Records at Your Domain Registrar:**
   - Log in to your domain registrar's control panel (where you managed the TXT, SPF, DKIM records).
   - Find the DNS or MX Record settings.
   - **Delete all existing MX records** (these will be pointing to Google, e.g., `ASPMX.L.GOOGLE.COM`, `ALT1.ASPMX.L.GOOGLE.COM`, etc.).
   - **Add ProtonMail's MX records** with their specified priorities.
   - Save the changes.
3. **Wait for DNS Propagation:**
   - MX record changes can take anywhere from a few minutes to 48 hours to fully propagate across the internet, though it's often much quicker (1-4 hours).
   - ProtonMail usually has a way to check/verify if your MX records are set correctly within its domain settings panel.

**Phase 4: Post-Migration**

1. **Test Email Flow:**
   - Send a test email from an external account (e.g., a personal Gmail, Outlook.com) to your `yourname@yourcompany.com` address. It should arrive in your ProtonMail inbox.
   - Send a test email from your ProtonMail account (using `yourname@yourcompany.com`) to an external account. Check that it arrives and isn't marked as spam (this tests your SPF/DKIM setup).
2. **Set up ProtonMail Bridge (Optional but Recommended):**
   - If you prefer to use desktop email clients like Outlook, Thunderbird, or Apple Mail, install the ProtonMail Bridge. This application encrypts and decrypts your mail locally, allowing standard email clients to work with your ProtonMail account via IMAP/SMTP.
3. **Inform Users (if applicable):**
   - If you have multiple users, inform them about the switch, how to log in to ProtonMail (web or via Bridge), and any changes to their workflow.
4. **Monitor Old Google Workspace Account (Temporarily):**
   - For a few days after the MX switch, you might still want to log in to your old Google Workspace email to catch any stragglers that were sent during the DNS propagation window (though this is less common if you waited for the import to finish).
   - You can also set up forwarding from your Google Workspace account to a temporary address *before* changing MX records if the import is very long, just as a safety net. But generally, if the import is done, you change MX, then all *new* mail goes to Proton.
5. **Cancel Google Workspace Subscription:**
   - Once you are confident that all emails are migrated and new emails are flowing correctly to ProtonMail, you can cancel your Google Workspace subscription to avoid further billing.
   - **Before canceling, consider one last Google Takeout of your mail if you want an independent archive.**

**Important Considerations:**

- **Downtime:** There shouldn't be any email downtime if you do this correctly. Emails will continue to arrive at Google Workspace until you switch the MX records, at which point they'll start arriving at ProtonMail.
- **Patience:** DNS changes and large email imports take time. Don't rush these steps.
- **ProtonMail Support:** If you run into issues, ProtonMail's support (especially for paid plans) is generally helpful.

This comprehensive guide should cover your email-only migration. Take it step by step, and you'll be set up on ProtonMail successfully!
