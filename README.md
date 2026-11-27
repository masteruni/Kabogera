# Kabogera Beauty 美 — content studio

Motion content for our client Kabogera Beauty 美 (kabogerabeautyjapan.com), built as code with the `saas-animation` skill.

## Layout
- `brand/assets/` — logo icon, Perfect Series product shots, campaign posters and distributor portraits, taken from
  kabogerabeautyjapan.com and the Kabogera web app.
- `brand/fonts/` — Playfair Display (headlines) and DM Sans (body), the site's fonts (SIL Open Font License).
- `ads/<nn>-<name>/` — one folder per ad: storyboard, animation page, renders, sound.

## Brand kit
| Token | Value | Use |
|---|---|---|
| Plum | `#281139` | dark fields, app theme colour |
| Violet | `#482466` | headlines on light fields |
| Lilac | `#efe7f6` | light fields |
| Cream | `#faf8f5` | page background |
| Gold | `#c9a45c` | rings, accents, ticks |

Tagline: *Glow Beyond Perfect.* · Line: *The Perfect Series* (Bar Soap, Multi Action Essence, Ultimate Serum,
Illuminating UV Gel SPF 50, Renew & Resurfacing Night Cream).

## Ads
| # | Ad | Format | Status |
|---|---|---|---|
| 01 | Partners abroad: recruiting distributors and resellers internationally | 9:16 Reel, 25s, English VO + music + SFX | v1 render, waiting for notes |
| 02 | Daily ritual: the five Perfect Series steps | 4:5 feed post (1080×1350) + caption | v1, waiting for notes |

## Ad 01 · Partners abroad
- `storyboard.html/.png` — approved storyboard. `ad.html` — the animation (all beat times in the `B` block at the top).
- Decisions: English VO; CTA "Message our page to apply" → m.me/kabogerabeautyofficial; "international" (no named
  countries beyond the Philippines and Hong Kong, where shops exist today); distributor portraits approved for use.
- Audio (`audio/`): VO by ElevenLabs (Belle B – Premium Ad Narrator, take 1, `vo-lines.json` places each line);
  music "Sleeping In My Head (Instrumental Version)" by Siine and SFX from Epidemic Sound (licence must cover the
  client's channels); `build_audio.py` mixes to -14 LUFS.
- Render: `node tools/render.mjs video ad.html "out/<name>.mp4" --fps 25 --scale 1 --audio "audio/Kabogera partners abroad - mix.wav" --root ../..`
- Stills for review: `node tools/render.mjs stills ad.html out/stills 1.5 4.6 … --root ../..` then `python3 tools/sheet916.py out/stills out/sheet.jpg`.
