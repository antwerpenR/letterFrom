---
source: https://rogerprice.me/lex-and-dhh
clipped: '2026-09-20T09:44:24+00:00'
title: Lex and DHH
site: Letter from ...around the world
published: '2026-09-08T15:52:08.000Z'
---

# Lex and DHH

# Lex and DHH

![Lex and DHH](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/size/w2000/2026/09/DHH_-Future-of-Programming--AI--Agentic-Engineering--Vibe-Coding---Linux-_-Lex-Fridman-Podcast--501.jpg)

## 1. Overview

Thirteen months after his previous appearance, DHH — creator of Ruby on Rails, CTO of 37signals, race car driver and now creator of the Omarchy Linux distribution — describes a complete reversal on AI. Once skeptical of AI coding tools, he now runs "100% agent-accelerated" development, calling the past nine months "decades of progress" and quoting (with attribution) Lenin's line: *"There are decades where nothing happens and weeks where decades happen."* His framing: "If you're not recognising the gravity of the moment, that's the delusion."

> [!image]
> [![Click to listen to the full interview and discussion](https://storage.ghost.io/c/9c/2a/9c2aa86d-156e-419f-9a0f-38bf91aebf15/content/images/2026/09/image-12.png)](https://www.youtube.com/watch?v=NYFGCESmikA&ref=rogerprice.me)
> Click to listen to the full interview and discussion

## 2. The pivot: four phases of the agentic era

DHH structures the transformation as distinct phases:

- **Pre-agentic era (to late 2025):** AI as autocomplete and chatbot — useful as a tutor, but he was still "chiselling code" by hand.
- **The dividing line — 24 November 2025 (Opus 4.5):** He tried it on the 26th and found the output "uncannily close" to what he would have written; agents could use tools, check their own work and instrument the computer. Adoption exploded over the Christmas break (he cites Shopify).
- **Early spring: sub-agents.** Harnesses that subdivided tasks across ~8 sub-agents cut times to a fifth or a tenth.
- **This summer (Opus 5, Fable, GPT Sol):** He now states the *problem*, not the path. "I've become optional in the part that produces the code that picks the route." He likens it to GPS: nobody gets driven into the harbour any more.

## 3. Key numbers and claims

| Item | Detail as stated in the episode |
| --- | --- |
| Omarchy Quattro | Released the Friday before recording; "tens of thousands" of downloads; ~3,000 hours of DHH's effort over ~1 year |
| AI-written code in Quattro | 100% of shipped code for the last two months; he reviewed shapes and critical model-layer lines only |
| Install time | World record 45 seconds (target: ~12-second "turbo images" for Dell XPS); ISO shrunk from 7.5 GB to 5.8 GB; JetBrains font slim package saved 180 MB; re-compressed NVIDIA drivers saved ~200 MB |
| Pull requests | 1,000+ merged in three months; ~400 unmerged (double the previous week); agents pre-review PRs and validate fixes in a VM |
| Plugins | 330 community plugins within three days of launch |
| Fable's Python→Rust translation (Terminal Text Effects → "TTFX") | ~45 minutes, one-shot; startup 86 ms → 2 ms; 9.6× execution speed-up; 3 MB binary; ~$550 in per-token cost. Sol: ~1.5 hours, ~$46. Grok 4.6: ~$55. DeepSeek Pro: 2 h 45 m, ~$23. GPT Luna and DeepSeek Flash failed. After two "auto research" runs: 46× improvement over the original |
| Shopify study (per DHH, by CTO Mikhail) | Agent-reviewed PRs caused far fewer production incidents than human-reviewed ones |
| Machine setup | ~16 parallel agent threads across 4–5 machines via GL.iNet Comet KVMs and Tailscale; Neovim, tmux → Herdr (tmux + agent notifications); Fireworks inference for open-weight models |
| Bad Mac/PC set-up anecdotes | New Mac: 42 minutes before Lightroom could be installed; new Windows PC: 1 hour 35 minutes |
| Opus 5 system prompt | Shrunk by ~80% (per DHH citing Boris on Claude Code) — over-prescriptive instructions were harming agents |

## 4. Work, architecture and vibe coding

- **Basecamp 5** was 37signals' first agent-accelerated product, but an early "let the designers vibe" surge produced PRs that, taken together, "destroyed the architecture" and required manual clean-up. He says the lesson: on substantial existing code bases, retaining architecture still needs a programmer's judgement.
- **Beautiful code still matters — for now** — because tokens are scarce and agents re-learn context on messy codebases ("ball of mud"). But he sees the economic case for hand-crafted beauty as diminishing.
- **The bottleneck isn't implementation** — it's human bandwidth, communication, vision and taste. Direct human–agent interaction, without intermediaries, is where 10×–1000× gains come from.
- **On terminology:** he dislikes "agentic engineering" as "marketing slob speak" and thinks "vibe coding" smells like script kiddies; he distinguishes it from agent-accelerated development, and argues non-programmers can now out-perform mediocre programmers because product sense matters more than implementation skill.
- **Bash, Rust, C++:** agents write excellent Bash except for "early exits" he must correct; he "hates Rust with a passion" yet ships Rust for its output; he wrote Omawrite (a C++/Qt Typora replacement) without reading a line of it.

## 5. Models, harnesses and the industry

- Current ranking: **Fable best, Opus 5 second**; Sol, Grok 4.6 close behind; Codex his favourite "checker"; Copilot has "actually gotten good".
- His workflow: one model drives, another (Codex xHigh) reviews; Copilot adds a further pass.
- Claude Code remains his harness of choice despite reservations about Anthropic (cutting OpenCode off from subscriptions; Claude refusing to read `AGENTS.md`; a model refusing to translate an essay into Italian — which he compares to HAL 9000).
- A Kimi open-weight model served via Fireworks answered a Tiananmen Square question bluntly, which he finds ironic given the Italian-translation refusal.
- Security: latest models find exploitable vulnerabilities so well that (he claims) one Fable release was held back as "not safe"; 37signals' security team faces a "seemingly endless parade" of real vulnerabilities — but end results are "vastly more secure systems". Offence and defence are symmetric ("spy versus spy").
- Anecdotes: an agent filed a mise bug report *before release* (after GitHub banned the bot for filing 28 issues in ~12 seconds); a crash watcher ships in Quattro to diagnose app crashes from source.

## 6. Advice, work and society

- Advice to programmers: don't try to anticipate two model hops ahead ("you will literally go crazy"); the frontier is catchable — a programmer who backpacked for a year "can catch up in two weeks".
- Jobs: cites the Jevons paradox and the ATM/bank-teller example for optimism; the Luddites and mechanised farming as historical parallels; productivity gains as the engine of progress, with real, individual suffering that shouldn't be made light of.
- Cites **David Graeber's *Bullshit Jobs*** (his UK poll; ~a third of workers felt their jobs were fake) and Tobi Lütke's Formula 1 anecdote as an image of post-drudgery employment.
- Falling birth rates worry him: without "skin in the game", he fears societal nihilism; he name-checks Peter Thiel's stagnation argument and *The Fourth Turning* (recommended by Lex).
- **AGI:** not "in the general definition", but "glimmers" he calls AGI-like; on consciousness, he finds agents' expressions of regret "uncannily human-like" and notes his own writing behaves like next-token prediction plus temperature.

## 7. Politics and controversy (as stated by DHH)

- Unrepentant about the drama from his immigration commentary: "The Overton window does not open itself." He recounts Denmark's early debate (crediting Mogens Glistrup), his childhood Brønshøj (≈99% ethnic Danish in 1984, which he says is now ~60–70% — a mid-point figure in the transcript is garbled), and London's demographic change since the late 1990s (59–60% → ~34% "ethnic Brits", per his recollection).
- He endorses merit-based immigration, citing a Danish tally he says came out the previous week: UK/France/US immigrants ≈ **$25,000 net annual benefit** to the Danish state; Somalis ≈ **$28,000 net cost**.
- On assimilation: his American wife (of Scandinavian heritage) struggled to assimilate in Denmark; he contrasts America's "optional assimilation" culture.
- On discourse: praises the lost Buckley-style *Firing Line* format; notes 2020-era drama has shrunk (Bluesky/Mastodon as a "honeypot"); he re-followed Theo (of t3) despite their TypeScript dispute.

## 8. Personal and philosophical

- Racing gave him a template: exhaustion as exhilaration ("I'm alive"), and Omarchy began between Le Mans sessions.
- The pursuit of excellence: quotes Mitchell Hashimoto — *"The pursuit of excellence deserves no explanation"* — and admires McLaren's gram-shaving; his summary: "I want the fastest car breaking the speed limits. I want the diver watch that can go down the Mariana Trench. I want the operating system that can install in less than 60 seconds."
- He embraces finitude: Omarchy ships a *memento mori* Easter egg (his life bar at 62%, default lifespan 90); he respects Bryan Johnson while disagreeing with "don't die"; he defends alcohol's social lubricant role (Chesterton's fence).
- Fatherhood: "Creating life with another human that you love is literally the peak experience of being on the planet."
- Food: Danish 7-Eleven croissants beat anything he's found in 20 years in the US; the Louisiana museum cafeteria near Copenhagen is his favourite lunch (the whipped butter, especially); favourite dinner is the seafood restaurant at Puente Romano, Marbella.
- If uploaded to a simulation, he chooses the 1980s — the 1990s he calls a turn to nihilism ("grunge and Nirvana… Seattle grey").

## 9. Notable quotes

- "Who would not get delirious if suddenly a genie pops out of the bottle…?"
- "The psychosis is believing that the world is barely different."
- "If there is one programming language more beautiful than Ruby, it is the English language."
- "I live for the long argument."
- "The terminal was actually one of the most impressive and productive user interfaces we can have."
- "You don't know what a program should do until you play with it." (invoking the agile movement's critique of up-front specification)

## 10. People and works referenced in the episode

| Reference | Context |
| --- | --- |
| Tobi Lütke (Shopify) | Early AI adopter; DHH ignored his warning memo; partner on Omarchy; source of the "brains and hands" VM pattern, F1 anecdote and agent-shopping story |
| Linus Torvalds | Recent comments welcoming AI in the kernel ("if you think Linux is an anti-AI project, think again"); DHH defends his spiciness |
| Boris (Claude Code) | Opus 5 prompt-shrinking anecdote; Claude Code's multi-agent view as enduring advantage |
| Mikhail (Shopify CTO) | Agent-review-vs-human-review production study |
| Mitchell Hashimoto | Ghostty terminal; "pursuit of excellence" quote |
| David Graeber | *Bullshit Jobs* essay/poll |
| Gad Saad (named "Gad") | Phrase "suicidal empathy" |
| Peter Thiel | Stagnation argument (physical vs digital progress) |
| William F. Buckley / *Firing Line* | Model of civilised disagreement (Black Panther interview) |
| Elon Musk | Admiration for goal-setting; the four-minute-mile analogy (DHH dates it to "1952"; the famous Bannister run was 1954) |
| PewDiePie | Arch Linux, "Chernobyl rice", AI clusters — an inspiration for non-programmers |
| Palmer Luckey / ModRetro | Recreated Game Boy and N64; the Chromatic Tetris re-implementation ("hit up and the brick slams… speeds the game by ~400%") |
| Books/other | *The Fourth Turning* (recommended by Lex); *One Flew Over the Cuckoo's Nest*; *Requiem for a Dream*; *Bullshit Jobs*; Black Mirror's San Junipero-style upload episode |
