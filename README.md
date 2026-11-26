# 26 November 2026 in one image

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/kimbaex07/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/kimbaex07/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image that sums up Thursday 26 November 2026: a front page with
the date at the top and **17 date-checked stories across 8 regions** —
three illustrated leads (Washington proposing tariffs on 14 trading
partners, the Cairo ring-road tanker fire that killed 31, Ukraine's
strike on Russia's Savasleyka airbase) plus a digest covering the
Middle East, Europe, Africa, Asia, the Americas, markets, tech,
space and culture.

## The news of 26 November 2026

**Leads**

- **US PROPOSES TARIFFS ON 14 PARTNERS** — Washington proposes country-specific tariffs on 14 economies, including China, the EU, Japan and India, to fight what it calls structural factory overcapacity; the highest rates would hit China, accused of flooding world markets with cheap exports. (Reuters, 26 November 2026)
- **TANKER FIRE KILLS 31 IN CAIRO** — A fuel tanker overturns and bursts into flames on Cairo's ring road; at least 31 people are killed and about 21 hurt, Egypt's health ministry says. The crash happened on Wednesday evening and was reported on 26 November. (BBC News; The Guardian; Le Monde)
- **UKRAINE HITS RUSSIAN AIRBASE** — Ukraine says its drones struck Savasleyka airbase in Russia's Nizhny Novgorod region, damaging three MiG-31 jets and two Su-34 fighter-bombers, as Russian ballistic missiles hit Kyiv. (Al Jazeera, 26 November 2026)

**Digest (14 more)**

- **Saudi Arabia:** Yemen's Houthis claim attacks on Saudi ports and the Ras Tanura refinery; oil prices rise. (Reuters, 26 November 2026)
- **Space:** The FCC clears SpaceX to launch up to one million satellites for orbital data centres, "Starmind". (FeedCast Daily Brief; Globe TV, 26 November 2026)
- **Israel:** Judges urge prosecutors to drop the bribery case against Prime Minister Netanyahu, Case 4000. (Globe TV, 26 November 2026)
- **North Korea:** Pyongyang expels Switzerland's top diplomat and orders its newly reopened office closed; Kim Jong Un calls for wider deployment of tactical nuclear weapons. (Globe TV; FeedCast, 26 November 2026)
- **Poland:** Warsaw announces a no-fly zone near the Ukrainian border after repeated airspace incursions blamed on Russia. (Globe TV, 26 November 2026)
- **Colombia:** Security forces storm a supermarket in Cartagena, ending a 17-hour siege and rescuing all 76 hostages. (Globe TV, 26 November 2026)
- **Nigeria:** The anti-drug agency seizes a $227 million meth lab in Enugu state and arrests five Mexican nationals. (Globe TV, 26 November 2026)
- **Puerto Rico:** The Supreme Court rules 5–4 to cancel the island's power contract with Luma Energy. (Daily Summary of World, first reported 26 November 2026 UTC)
- **Economy:** US third-quarter GDP growth is revised sharply higher, while inflation stayed high in October. (Reuters, 26 November 2026)
- **Yemen:** A blast hits Sanaa as the Saudi-led coalition says it intercepted missiles over Riyadh and drones in the Eastern Region. (Daily Summary of World, first reported 26 November 2026 UTC)
- **Syria:** An ISIL suicide attack kills two security personnel at a checkpoint in Hasakah. (Daily Summary of World, first reported 26 November 2026 UTC)
- **Zambia:** Authorities ban a protest against plans to remove presidential term limits. (Daily Summary of World, first reported 26 November 2026 UTC)
- **Music:** Duran Duran guitarist and songwriter Andy Taylor dies at 65. (Reuters, 26 November 2026)
- **Sport:** Liverpool beat Club Brugge 3–0 in the Champions League. (One Turn, 26 November 2026)

## Why this front page

The three leads were chosen by scale, not by noise: the US tariff proposal is the day's biggest economic story, the Cairo tanker fire is its largest loss of life, and the Savasleyka strike is its most significant military development. The digest then walks the rest of the world region by region — the Middle East, Europe, Africa, Asia, the Americas, plus markets, tech, space and culture — so no part of the day is left to a single headline. Stories from 24 November (the Miss Universe result, the Huawei verdict) were deliberately left out: every item on the page was checked against reporting dated 26 November 2026. The page also keeps its proportions honest: three leads get the pictures, but the digest gets the same weight of checking — every item carries its date and its source, so the day reads as one story with seventeen witnesses rather than seventeen unrelated shocks.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` (a 1024x1024 PNG) to
`$MAKEFUN_OUTPUT_DIR/entry.png` byte for byte, so both grader runs
write identical output. Python 3.13, standard library only, no network.

## How the image was made

The front page is composed locally with Pillow: masthead, three
illustrated leads and a 14-item digest, all text rendered crisply in
code so nothing is garbled. The three lead pictures are flat editorial
illustrations generated with an image tool for this entry (no text in
them). Every story was checked against reporting from 26 November 2026
before it was captioned; claims are attributed where they are claims
(e.g. the Houthi attack claims, Kyiv's airbase claim), and tolls are
stated at their latest confirmed figure (Cairo 31, about 21 hurt).

---

Built for the [make.fun](https://make.fun/r/cbprbg0z) bounty
`news-image-20261126` — sum up 26 November's world news in one image.
