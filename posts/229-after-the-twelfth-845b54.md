---
source: https://rogerprice.me/229-after-the-twelfth
clipped: '2026-08-15T15:27:07+00:00'
title: 229 - After the twelfth
site: Letter from ...around the world
published: '2026-07-17T16:01:10.000Z'
---

# 229 - After the twelfth

[grand solar minimum](/tag/grand-solar-minimum/)

# 229 - After the twelfth

🇬🇧 Insights from solar physicist Valentina Zharkova. Plus: Bitcoin payments in Signal, why Monero tops privacy charts, Immich backup strategy, Gold Clearing in Hong Kong and decoding the 2012 Olympics opening ceremony.

- [![Roger Price](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w100/2022/07/highres_253585337.jpeg)](/author/roger/)

#### [Roger Price](/author/roger/)

18 Jul 2026
• 11 min read

[Share](#/share)

![229 - After the twelfth](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/07/IMG_4564.jpeg)

Holywood this week - at the library

🇬🇧 Strangely enough, the weather has continued to be [rather good](https://rogerprice.me/july-in-belfast-2/) this week and the outlook for the coming week is not bad either! We had a very busy weekend with family visiting from Belgium and all of V's planned activities. They have now gone home and we are settling back into our normal daily routine here.

I am in contact with a few local Bitcoiners and we are planning some meetups - there are lots of interesting developments to discuss - see this week's project updates. I also expect to meet up with a few former school friends - if you are around and fancy meeting up, just reach out.

I have also had some time for hands-on project work, setting up the computers that I got here recently. For this I am using anonymous AI - it is amazing how good this has got. If you are not making use of these tools, you are going backwards - more on this in the [Project Updates](#🛠️-project-updates) section below.

Among all the other things this week I had time to get out to the Botanic Gardens, Bangor Walled Garden and Crawfordsburn Country park for a nice walk along the beach and an ice cream (aka poke). What have you been up to?

### Interview of the week

Recall that I have recommended James Delingpole's book [Watermelons](https://rogerprice.me/r/83f208c1?m=aee19331-9c07-433c-b232-71e8bfd62006) before. In this book (originally from 2011 and recently updated and republished) [he dismantles](https://rogerprice.me/watermelons/) the Global Warming and Climate Change scam. James demonstrates that climate activism is driven by **flawed science**, misanthropic elite agendas, and policies that impose severe **economic costs** on society.

ICYMI: The Club of Rome's 1993 publication *The First Global Revolution* explicitly stated: *"In searching for a new enemy to unite us, we came up with the idea that pollution, the threat of global warming, water shortages, famine and the like would fit the bill… the real enemy, then, is humanity itself."*

I found this interview that he recently did with Professor Valentina Zharkova to be fascinating. Listen and you will learn much. She tells her story of coming from the former Soviet Union to the West (and that should already shock you) and then talks through her decades of research that independently corroborates James' findings.

> [!bookmark]
> [Valentina Zharkova](https://rogerprice.me/valentina-zharkova/)
> This is a transcript of an interview between James Delingpole (host of The Delingpod) and Professor Valentina Zharkova, a solar physicist originally from Ukraine who has worked in UK academia for over two decades. The interview covers her personal background, her solar research, and her predictions about an impending period
> — Letter from ...around the world | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/Valentina-Zharkova-Delingpole-4a31ee0a-49dc-478c-866a-ad05162766a4.png)

Click for full information and to listen to the discussion

So, while the mainstream story of man-made climate change and CO2 is fake there is *man-made climate manipulation* in the form of Chemtrails and HAARP, as we have discussed before. That, however, pales into insignificance compared to the larger changes due to variation in Solar Radiation - this is self-evident if you think rationally for a few minutes but mainstream propaganda distracts you and prevents you from looking here.

I highly recommend that you bookmark and research her website. She provides a wealth of academic research, documentation and data.

> [!bookmark]
> [General description – Valentina Zharkova’s GSM](https://solargsm.com/general-description/?ref=rogerprice.me)
> ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/cropped-p8jXfLipzvdkz84qwpQXx8-10f3156d-7c8a-41c5-9fd4-d1e68221a632.jpg)

Click for Valentina's website - a wealth of information

Valentina utilizes *principal component analysis* to predict an ongoing modern *grand solar minimum* that she expects will lead to significant *global cooling through the 2030s*. She further challenges anthropogenic climate models by attributing historical climate shifts to solar inertial motion and solar activity cycles.

As a minimum, you should be aware of this information as an [*Ethical Skeptic*](https://rogerprice.me/76-holywood-cafe/#:~:text=Ethical%20Skepticism,or%20disprove%20it.).

## **More in this issue**

- Photo memories - Out and about this week
- Project Updates - Hands-on backups, Radar in Signal and Monero
- Plenty of useful links - don't say nobody told you!
- Closing out - All the world is a stage - can you see it now?

> [!image]
> ![Out and about this week - Bangor Walled Garden, Crawfordsburn and Botanic Gardens](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/07/IMG\_4627.jpeg)
> Out and about this week - Bangor Walled Garden, Crawfordsburn and Botanic Gardens

# 🛠️ Project Updates

Some hands-on updates this week and a couple of informational ones you ought to know about. These are all part of the *Parallel Systems* that we need to build and use. What are you doing?

### Disaster Backup

I have explained to you several times the ***3-2-1 rule*** for your backups:

- **3** copies of your data: primary + two backups.
- **2** different media or locations: eg local external Btrfs drive + another machine or cloud target.
- **1** offsite copy: cloud storage (Backblaze or a remote server) for real resilience.

So, with time on my hands this week I set to work to set up a proper Active-Passive recovery configuration for my Immich server and all my photos. The approach is:

Keep one primary Immich server running (Prime). On a second machine (Secondary), keep the Docker compose files and directory structure ready, but **do not start Immich** there normally.

- Immich runs normally on Prime machine.
- A scheduled job on Prime:
  - Dumps the database.
  - Syncs the`upload/` folder and database dumps to the secondary.
- Secondary: Immich stays off. **In a disaster:**
  - Restore the latest database dump.
  - Ensure the synced upload directory ownership is correct.
  - Start Immich on the secondary.
- Periodically, back up all data to a third machine or offsite service

BTRFS is a better choice for filesystem than the usual linux EXT4 for an Immich setup because it offers instant snapshots, transparent compression, data corruption detection and efficient incremental replication to a backup machine.

This is a simple, safe and well-tested configuration and one that you should consider. An additional benefit is that you can use this setup to complement your existing offsite backup arrangements. Well worth it for something like your photos and other valuable data. Of course - you want the external disks to be encrypted and the encryption key needs to be safely stored.

### How great is this!

*Radar* is a Bitcoin-integrated messaging app built on top of the ***Signal*** network, allowing users to send payments directly within existing chats. It aims to remove friction by combining messaging and payments without the need for centralized custodians or bank-linked KYC processes.

> [!bookmark]
> [Radar - payments in Signal](https://rogerprice.me/radar-payments-in-signal/)
> Click below to listen to the full interview - Stephan’s new “Fast format” 1. Motivation: Why Build a Bitcoin Messenger? \* The core observation is that private messaging and payments have remained artificially separated. Existing combined platforms (WeChat Pay, Facebook Messenger payments, Cash App messaging) all rely on central custodians, banks,
> — Letter from ...around the world | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/Bitcoin-in-Your-Signal-Chat-----Radar---s-Bold-Move-with-Seth-for-Privacy-\_-SLP754-488b92e1-3c7f-47c1-8008-30ba60d98e62.jpg)

Click for key points and to listen to the full discussion

- Radar is self-custodial, allowing users to manage their own keys via a 12-word seed phrase or utilize automatic encrypted backups stored on their Signal profile.
- It leverages the Spark protocol to facilitate payments, allowing compatibility with Lightning-enabled services like Wallet of Satoshi, Cake Wallet, Phoenix, and Zeus.
- Privacy is maintained through a separation of concerns: Signal handles messaging without knowledge of payment data, while Spark operators process transactions without access to user identities or Signal-specific data.

Radar is positioned for mass adoption by meeting users in an environment they already use (Signal), rather than requiring them to adopt standalone Bitcoin wallets.

Particularly interesting is that the project maintains a positive and constructive relationship with Signal, operating as an alternative client similar to Molly and it currently supports the Signal Foundation through monthly donations.

> [!bookmark]
> [Radar — Chats and sats in one place](https://radar.chat/?ref=rogerprice.me)
> End-to-end encrypted chat with self-custodial Bitcoin Lightning payments. Settle in under a second.
> — Radar | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/og-27db5115-03db-4601-b8b7-d90b82d3e4a7.jpg)

Click to know more, get the app and get started

### Monero still tops the chart

You have likely been following the payment chart for nano-GPT. This is a fabulous, anonymous AI aggregator that gives you easy access to all of the latest AI models with a simple (and very reasonable) pay-as-you-go setup.

Most interesting from their six-monthly review is that Monero continues to top the charts in terms of payment choice. Bitcoin over Lightning is solid second place. These really are your best choices for private payments, both for products and services that you use and for payments between individuals.

> [!bookmark]
> [2026 Mid-Year Crypto Payment Statistics: Monero Still Leads, Bitcoin Rails Grow, Stablecoins Broaden | NanoGPT](https://nano-gpt.com/blog/2026-midyear-payment-stats?ref=rogerprice.me)
> NanoGPT’s first-half 2026 crypto payment data across XMR, XNO, BTC, Lightning, USDC, USDT, LTC, ZEC, ETH, SOL, TON, and more.
> — NanoGPT | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/june-2026-payment-pie-chart-09a8b8d2-07ba-4b71-8ff4-01b59c5f3bc7.png)

Click for the blog post with all the details

I have given you lots of suggestions on how to get started. Just do it and feel free to reach out if you have questions or want help to do some test payments.

### Others think similarly

I came across this rather interesting interview this week. DHC is a pseudonymous investor and his take on Monero confirms what most should already know. Monero really does behave as the best money, being private by default and having many other attributes that focus on being money, rather than speculation or even store-of-value. Read details below or listen and learn

> [!bookmark]
> [Monero: A Peer-to-Peer Electronic Cash System](https://www.dhcfund.com/p/monero-a-peer-to-peer-electronic?ref=rogerprice.me)
> Investment Thesis
> — DHC Research | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/https-3A-2F-2Fsubstack-post-media.s3.amazonaws.com-2Fpublic-2Fimages-2Fc33d24e9-6be5-44fe-b0e2-20313ecae249\_1200x630-ce685ffc-b02c-4ad3-9344-dc3907d931db.jpeg)

Click to read his article or [here to listen](https://www.monerotalk.live/monerotalk-389?ref=rogerprice.me) to the discussion with Doug

# 🔗 Links for your edification

The following are links from my *Liferea* RSS feeds - learn, enjoy and share.

### It's time - or so it seems

You might have missed the opening of Hong Kong’s central clearing system for gold ([link](https://www.thestandard.com.hk/finance/article/336541/Hong-Kong-launches-central-gold-clearing-system-boosting-worlds-gold-hub-status?ref=rogerprice.me)) – enhancing the gold trading ecosystem for global investors and institutional capital seeking safe-haven assets. You should also be aware that the mainstream message is that "*everything is fine"* until one day it is not.

Andre Jikh explores a potential structural shift toward gold as a neutral global reserve asset. Drawing on research from Luke Gromen and US Treasury Secretary Scott Bessent, the analysis suggests that central banks are increasingly accumulating gold to navigate economic rebalancing.

> [!bookmark]
> [Gold - it’s time](https://rogerprice.me/gold-its-time/)
> Andre Jikh argues that a structural shift is underway toward gold as a neutral global reserve asset. The video draws heavily on the macro research of Luke Gromen of FFTT (Forest for the Trees) and on a June 2026 Wall Street Journal op-ed by US Treasury Secretary Scott Bessent.
> — Letter from ...around the world | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/China-Is-Buying-A-LOT-of-Gold-4c57d125-6b80-4ed0-af0f-eaf4baf6a5d5.jpg)

Click for a full walk-through and to listen to Andre's analysis

His analysis is very thorough and checks out well. This transition reflects Hamiltonian economics, prioritizing domestic industrial capacity over traditional financialization. Ultimately, Jikh highlights that while global systems may face significant adjustments, gold is positioned to play a critical role in future monetary stability.

### Micro$lop - just when you thought it couldn't get worse

Project Aion, also known as Co-Pilot OS, is an internal Microsoft prototype that attempts to replace the traditional Windows interface with a web-based agentic operating system running on Edge. The concept has faced sharp criticism for its reliance on an always-on internet connection, the removal of local files, and an invasive AI integration - all the things that users said they did not want and yet Micro$lop did them anyway!

> [!image]
> [![Click for laugh of the week](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/07/image-16.png)](https://www.youtube.com/watch?v=psWcdE1pieA&ref=rogerprice.me)
> Click for laugh of the week

💡

If it is in the news - it is a ruse. There are no coincidences.

# 🤔 Closing Thoughts

I think that by now most of you who are still here understand that "all the world is a stage" and events are being played out on the global stage in a way that keeps people distracted and divided into groups that fight with each other rather than building things or pushing back on those who are the puppet-masters.

All of this has been shown to you many times and each time you likely missed the deeper meaning, at least the first time you saw it.

So it is that everything that is currently going on in the world has been shown to you in advance. This serves not only to absolve those behind the actions from *Karma* but also it is a required part of the *Manifestation of the events*. It is necessary to "*plant the seed*" in the *minds of the masses* so that they will not only accept it but their subconscious plays a part in the manifestation of the events themselves.

I already explained this to you back in [August 2024](https://rogerprice.me/127-older-and-wiser/#:~:text=%F0%9F%A4%94%20Closing%20Thoughts,the%20same%20again.). Recently Jason has edited his explainer video to be shorter with just what you need to know. Everything, from *Covid* onwards has been laid out for you to see in advance. Were you paying attention to the *2012 Olympics Opening Ceremony*?

> [!bookmark]
> [Olympiad - do you see it yet?](https://rogerprice.me/olympiad-do-you-see-it-yet/)
> Jason (of the “Archaix” channel) presents a scene-by-scene esoteric breakdown of the 2012 London Olympic Opening Ceremony, arguing that it encodes a hidden narrative about the Phoenix phenomenon — a cyclical civilisational reset — and the subsequent re-initiation of society by an underground elite. He identifies five sequential “scenes”
> — Letter from ...around the world | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/Olympiad-Oracle\_-Breaking-of-the-Seals-8137937e-9593-4588-8e1c-2834c865e018.jpg)

Click for a full walk-through and to listen to Jason's superb explanation

For those with eyes to see and ears to hear. Don't say that nobody told you.

### MAGICK and manifestation

Some of you may have been wondering what I was referring to above about "*involving the masses in the manifestation*" of events. I recently came across this excellent explainer. Watch, listen and you will know.

> [!bookmark]
> [Magick - now you know](https://rogerprice.me/magick-now-you-know/)
> The speaker discusses the book Magick by Aleister Crowley, which he first read nearly 20 years ago. He explicitly cautions viewers against Crowley the man, while arguing that the understanding Crowley reached about how reality responds to the mind is both genuine and important — and that its danger lies precisely
> — Letter from ...around the world | ![](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/thumbnail/The-Most-Dangerous-Book-Ever-Written-On-Reality-c7f19135-c46e-4959-883f-c603c933cfd8.jpg)

Click to learn what you need to know

*Magick* is a commentary on Aleister Crowley's work that explores how the *Law of Manifestation* operates neutrally and continuously, arguing that our lived reality is shaped by the attention we habitually feed to our subconscious thoughts rather than occasional deliberate intentions.

# ❤️ Enjoy this newsletter?

**Forward to a friend** and let them know where they can subscribe

> ***No one can be told what The Matrix is.** **You have to see it for yourself.***  
> - Morpheus to Neo in [The Matrix](https://lookmovie2.to/movies/view/the-matrix-1999?ref=rogerprice.me)

> [!image]
> [![How to exit the matrix - do you see it yet?Click here: Morpheus will explain it to you](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2025/11/How-to-exit-the-matrix-2.png)](https://www.youtube.com/watch?v=ax2bQOZy6Sc&t=78s&ref=rogerprice.me)
> How to exit the matrix - do you see it yet?Click here: Morpheus will explain it to you

**Any questions or anything else?** Feel free to **comment below!**  
You can also email me at: LetterFrom@rogerprice.me

🤔

"99% of all subjects accepted the program if they were given a choice - even if they were only aware of the choice at an unconscious level"  
- The Architect

*💡Enjoy the newsletters in **your own language**:* [Spanish](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me), [*Dutch*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=nl&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*French*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Italian*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=it&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*German*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Serbian*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=sr&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Croatian*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=hr&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*, Chinese* [*Traditional*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=zh-TW&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me) *&* [*Simplified*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Burmese*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=my&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Irish (Gaelic)*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=ga&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)*,* [*Russian*](https://rogerprice-me.translate.goog/?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me) *and*[*Thai*](https://rogerprice-me.translate.goog/?_x_tr_sl=auto&_x_tr_tl=th&_x_tr_hl=en-US&_x_tr_pto=wapp&ref=rogerprice.me)
