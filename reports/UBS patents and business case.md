# Rename UBS, ship products, open later

UBS is legally workable, and EU law is moving its way. As drafted, though, it has three fixable problems and one hard truth.

The first problem is the name. **"UBS" is a famous, actively defended trademark of the Swiss bank**, so it should stay an internal working name and never become the public brand or logo. The second is the passport. As written (an NFC antenna on ferrite under the cell wrap), it **sits close to active Duracell patents that run to 2034–2037**, so the spec should define the data and protocol and leave the antenna design to implementers. The third is cost. **A fuel gauge in every cell adds roughly 40–100% to the cell's bill of materials** at low volume, so it should be optional or live in the charger.

The hard truth is that no lone founder is known to have built a widely adopted battery standard. Every shared-battery platform that worked (Ryobi ONE+, Bosch Power for All, Gogoro) began as one company's product line and opened up only after it had scale. An open standard will bring in almost no licence income for years.

There is a real opportunity, but it is small. It is a premium enthusiast brand: branded protected cells already sell for about €20–30 against €4.50 for a bare name-brand cell, and fake-capacity cells are everywhere. The open spec would serve as Anodyne's credibility and marketing engine.

On patents, the founder's position is mostly defensive. The website has already disclosed most ideas, which blocks the founder's own patents in Europe. The US allows a 12-month grace period, which runs to about late September 2027. The heavy compliance burden is not the much-discussed EU battery passport, which does not cover portable cells. It is producer registration country by country, UN 38.3 and IEC 62133-2 testing for each cell model, and the fact that Posten will not carry loose cells.

The sensible route is staged:

1. Rename the standard and test demand for under NOK 20k.
2. Prototype on grant money.
3. Launch a product that ships without cells.
4. Certify cells only once there is sell-through.

My rough estimate is NOK 0.5–2 million before the first certified Anodyne cell ships. Most of that can wait until the evidence justifies it.

A note on confidence: this report summarises desk research done on 7 October 2026. The patent work looked at a sample of the landscape, not a full search, and the official trademark registers could not be queried directly. Every point flagged for a professional below really does need one.

## Patents: little to own, and one Duracell family to design around

### Most of UBS is already prior art, which helps you

Almost every building block of UBS has been public for decades, and that mostly works in your favour, because old public ideas are free for everyone to use.

- **Smart battery data.** "A battery that reports its identity, rating and live state" was standardised when Duracell and Intel announced the Smart Battery Data specification and SMBus in 1994–95 ([Wikipedia: Smart Battery System](https://en.wikipedia.org/wiki/Smart_Battery_System); [SMBus 1.0](https://www.smbus.org/specs/smb10.pdf)).
- **Signed cell identity.** This is a commodity chip feature. TI fuel gauges have combined gauging with SHA-1/HMAC pack authentication for years, and newer parts use ECC keys ([TI bq27350](https://www.ti.com/lit/gpn/bq27350); [TI app note](https://www.ti.com/document-viewer/lit/html/SLUAAQ0/GUID-8A9D2DF1-20E9-4792-9132-8E923490E02B)).
- **Any-way-round slots.** The patent on a polarity-correcting converter with two switches, US 6,023,418, was filed in 1999 and **expired in 2008** ([Google Patents](https://patents.google.com/patent/US6023418A/en)).
- **Per-cell converters on a shared bus.** These go back to at least US 5,656,915, issued in 1997 ([Justia](https://patents.justia.com/patent/5656915)).
- **Electronics in the cap.** Cylindrical rechargeable cells with charging circuits and USB in the cap are also long established ([US 8,314,590](https://patents.google.com/patent/US8314590)).

The chemistry colour bands, the two-digit rating code and the return credit are labelling conventions and a business method. These are weak candidates for patents at the European Patent Office, and nothing specific to them turned up.

### The passport is the one real patent hot spot

The UBS passport (§4 of draft 0.3) puts an NFC tag and fuel gauge in the cap, with the antenna on ferrite under the wrap. That is almost a description of Duracell's patent families.

| Patent | What it claims (simplified) | Anticipated expiry |
|---|---|---|
| **US 9,887,463 B2** | A battery-status circuit with a flexible ferrite shield on a cylindrical battery, a loop antenna printed on the shield, and an IC (which may include an NFC chip) that reports battery condition to a reader ([Google Patents](https://patents.google.com/patent/US9887463B2/en)) | May 2033 |
| **EP 3000152 B1** | European counterpart. Claim 1 covers two symmetric rectangular antenna loops about 180° apart on a flexible substrate around a cylindrical body. Granted December 2023 ([Google Patents](https://patents.google.com/patent/EP3000152B1/en)) | May 2034 |
| **US 10,483,634 B2 / EP 3535795 B1** | Uses the battery's positive terminal and can as the antenna ground plane for status communication ([Google Patents](https://patents.google.com/patent/US10483634B2/en)) | About 2037 |
| **US 10,297,875 B2** | A battery with an on-cell indicator, a PCB and a wireless-communication IC ([Google Patents](https://patents.google.com/patent/US10297875B2/en)) | About 2037 |

Whether a UBS cell would infringe depends on exact claim wording, such as the "two rectangular loops" geometry. Only a claim-by-claim review can settle that.

It is also **unconfirmed whether these European patents were validated and kept in force in Norway**. A European patent applies in Norway only if it was validated there, and Google Patents does not show this. The quick check is Patentstyret's register and the EPO Register.

Duracell sells into the same retail space and co-founded the original Smart Battery standard. That makes it both the most likely enforcer and a possible licensor or partner.

### Other areas worth a second look

- **Tool-pack interfaces.** If a UBS bay ever uses a slide-rail tool-pack interface, check the terminal patents. Milwaukee holds terminal patents such as EP 4379904 and has sued Makita, Hitachi, Hilti and others ([RPX summary](https://insight.rpxcorp.com/news/7947); [EPO publication](https://data.epo.org/publication-server/rest/v1.2/patents/EP4379904NWA3/document.html)).
- **Recent mixed-chemistry converters.** Recent converter designs for mixed-chemistry packs are also patented, for example US 12,506,432 ([USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12506432)). If your bay electronics go beyond simple per-slot buck/boost converters, they need checking.
- **Searches not done.** Nobody has yet checked NFC-in-cell patents from Energizer, Panasonic, Sony or Samsung SDI.

### Publishing the website has largely used up your own patent options

In Europe and Norway, novelty is absolute. Anything published before filing counts against your own later application. The only exceptions are evident abuse and officially recognised international exhibitions, and both apply only within six months ([EPC Art. 55](https://www.epo.org/law-practice/legal-texts/html/epc/2020/e/ar55.html); [EPO case law](https://epo.org/en/legal/case-law/2019/clr_i_c_2_5.html)).

The repository history shows the concept site went up on **25 September 2026**, and the passport and return credit were added on **27 September 2026** ([UBS repo](https://github.com/tagelokoy/UBS)). Everything described there is very likely prior art against a European or Norwegian application by you or anyone else.

The US is different. It gives inventors a **12-month grace period from their own disclosure** ([USPTO MPEP 2153](https://www.uspto.gov/web/offices/pac/mpep/s2153.html)), so a US filing on published material stays possible until roughly late September 2027. A patent attorney should confirm the exact dates.

Patenting would cost money and add friction. A patent application in key countries runs to $20,000 or more. Defensive publication fits an open standard better and is much cheaper: Technical Disclosure Commons is free and indexed by Google Patents, and IP.com charges about $109 per document ([IPWatchdog](https://ipwatchdog.com/2020/05/25/defensive-publications-cost-effective-tool-supplement-patent-strategy/); [Richard Poynder](https://www.richardpoynder.co.uk/On%20the%20defensive.htm)).

The practical rule:

- Keep publishing technical detail openly and with dates.
- If you invent a new mechanism that a partner might value, talk to a patent attorney before you publish it, not after.

### An open standard's patent policy only binds the people who sign it

Open standards handle patents in one of two ways.

- **Royalty-free.** The W3C model asks participants to license "essential claims" without royalties ([W3C Patent Policy](https://www.w3.org/policies/patent-policy/)).
- **FRAND.** ETSI requires licensing on fair, reasonable and non-discriminatory terms, which can include royalties ([ETSI IPR Policy](https://www.etsi.org/images/files/IPR/ETSI-ipr-policy.pdf)).

Either way, the commitment binds only those who join. Duracell would not be bound by a UBS patent pledge it never signed. Third-party patents of that kind are called "submarines".

The defence is drafting. Make the spec normative only for the data format and the protocol (for example, NFC Forum Type 5 / ISO 15693 plus a data schema). Leave antenna geometry and gauge implementation open so implementers can design around patents, and list known patents in an informative annex.

### Freedom to operate: a narrow check before tooling

A freedom-to-operate (FTO) analysis asks whether a specific frozen product would infringe in specific countries. It is different from asking whether your idea is new. Typical costs:

- **€5,000–20,000** for an analysis ([IamIP](https://iamip.com/wiki/freedom-to-operate-fto/)).
- **$15,000–30,000 or more** for a full legal opinion ([ipiry](https://www.ipiry.com/guides/patent-search-cost)).

It is not worth paying for at concept stage. Do a narrow FTO on the passport design once it is frozen and before any cell tooling, then a check per product before launch.

## The name belongs to a bank; the logo program is your real lever

### Choose a new public name before filing or launching anything

**UBS.** UBS has used the UBS mark since at least 1962 and holds registrations worldwide. Domain-dispute panels have repeatedly called it "well known and famous", and UBS pursues even domains that combine "UBS" with generic words, such as ubspremium.com ([ADR Forum](https://www.adrforum.com/DomainDecisions/1832240.htm); [WIPO D2005-0993](https://www.wipo.int/amc/en/domains/decisions/html/2005/d2005-0993.html)). European law protects reputed marks even against use on unrelated goods. A "UBS" logo on batteries therefore invites an opposition or a letter, and anyone searching "UBS battery" will find the bank. A trademark attorney should confirm this.

**"Universal Battery System."** This is descriptive, and others already use it. Black & Decker marketed VersaPak as a "universal battery system", Canadian Tire calls PWR POD "Canada's Universal Battery System", and "Universal Battery" is a lead-acid brand ([Strategy Online](https://strategyonline.ca/?p=13605); [Canadian Tire](https://canadiantire.ca/en/all-brands/pwr-pod.html); [Ace Hardware](https://www.acehardware.com/p/8258964)). It can serve as a tagline next to an invented, distinctive name, but it cannot be the brand itself.

**Anodyne.** "Anodyne" is an ordinary English word meaning "painkiller". At least one owner, Anodyne Therapy LLC, sells infrared light-therapy devices under the name and has litigated over the mark ([AccessGUDID](https://accessgudid.nlm.nih.gov/devices/00859101006004); [Rehab Management](https://rehabpub.com/pain-management/chronic/resoultion-of-lawsuit/)). That is probably a different class from batteries, but no proper register search has been done. Anodyne needs a clearance search in these classes:

- class 9: cells, chargers and power banks
- class 11: lighting
- class 8: hand tools
- class 7: powered tools

### Filing is cheap; picking the goods list is the step that matters

| Route | Official fees | Notes |
|---|---|---|
| Norwegian word mark | NOK 3,800 for one class + NOK 1,000 per extra class, so **NOK 5,800 for three classes** | Optional preliminary examination costs NOK 3,500 + NOK 625 per extra class and comes back in about 5 working days ([Patentstyret fees](https://www.patentstyret.no/en/about-us/how-we-work/prices-trademark-patent-design); [guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)) |
| EU trade mark | **€1,050 for three classes**, online ([TMarkMetric](https://tmarkmetric.com/insights/eu-trademark-cost)) | The EU SME Fund refund appears limited to EU and Ukraine firms, so it likely does not cover a Norwegian company |
| US | $350 per class ([Buchanan Ingersoll](https://bipc.com/uspto-set-to-change-trademark-fees-alongside-patent-increases-in-2025)) | Only needed if you sell in the US |
| International portfolio via Madrid | **About NOK 75,000** in official fees in Patentstyret's own worked example, plus adviser fees ([Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)) | |

A Norwegian filing gives you **six months of priority** to extend abroad. Patentstyret warns that you cannot add goods or services to the list after filing, which makes the class list the main thing to get right. After publication, third parties can oppose within three months.

### Keep the specification open and control the logo

Copyright protects the text and drawings of a specification, not the technical idea. The EU Court of Justice held in *SAS Institute v World Programming* that functionality and data formats are not protected expression ([SCL](https://www.scl.org/2451-sas-institute-inc-v-world-programming-ltd-report-and-analysis/)). Anyone can build to your spec without asking, which is the point of an open standard.

The usual licensing stack has three parts:

- **The text.** Publish it under CC BY 4.0, or under the Community Specification License if several companies will contribute. The Community Specification License builds in royalty-free patent commitments from contributors ([Community Specification](https://github.com/CommunitySpecification/Community_Specification)).
- **Patents.** Add a royalty-free patent pledge, such as OWFa 1.0 ([OWFa 1.0](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0)).
- **The name and logo.** Keep them out of the licence. CC BY 4.0 and OWFa already exclude trademarks ([CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode)).

Compliance is then enforced through the trademark. USB-IF, Bluetooth, Qi and Thunderbolt all let anyone read the spec, but allow the logo only on products that pass testing and sign a logo licence ([USB-IF logo licence](https://usb.org/node/1811); [Intel Thunderbolt guide](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2023-09/thunderbolt-messaging-guide.pdf)).

### Anodyne cannot own a true certification mark

Both EU and Norwegian law bar the owner of a certification (guarantee) mark from selling the certified goods ([EUTMR Art. 83](https://www.ippt.eu/legal-texts/eu-trade-mark-regulation-2017/article-83); [Patentstyret](https://www.patentstyret.no/en/trademark/collective-marks-and-guarantee-or-certification-marks)). If Anodyne sells cells, the standard's mark has to sit in one of two places:

- **A separate neutral body that sells nothing**, such as a Norwegian stiftelse (foundation) or forening (association), or a project hosted by the Linux Foundation's Joint Development Foundation (JDF).
- **An ordinary trademark under a logo licence.** This is how most industry programmes appear to work.

Certification marks cost a little more to file: in Norway NOK 4,000 for the first class, in the EU €1,500 online. They also need written regulations of use that set out the conditions, fees and sanctions ([EUIPO regulations-of-use guidance](https://euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/trade_marks/RoU_EU_certification_marks/RoU_EU_certification_marks_en.pdf)). The €3 return credit, written as "a condition of using the mark", could legally sit in those regulations. A trademark attorney and an EPR lawyer should review how it is worded.

### Governance: a neutral home is cheap; a staffed standards body comes later

Neutral homes cost little to set up:

- **JDF.** The Joint Development Foundation says it costs nothing to start and run a project there, using its legal agreements ([JDF](https://jdfprojects.lfprojects.linuxfoundation.org/about)).
- **Standard Norge.** Joining a Norwegian standards committee is free, but takes 40+ hours a year, and 100+ hours for international work ([Standard Norge](https://standard.no/globalassets/generelt-horisontalt/standardisering/standardiseringskurs/trinn-i-varen-2025---del-b.pdf)).

Membership standards bodies charge real money and only work once companies want the logo:

- **USB-IF:** $5,000 a year ([USB-IF](https://www.usb.org/node/1809)).
- **Wireless Power Consortium (Qi):** $30,000 a year ([WPC](https://www.wirelesspowerconsortium.com/knowledge-base/testing-and-certification/cost-of-certification/)).
- **Bluetooth:** $12,000 per new product design ([Bluetooth SIG](https://www.bluetooth.com/fee-schedule/)).

A new standard has to charge nothing or close to nothing, or nobody will sign up.

History points the same way:

- **Qi** won because the phone makers backed it. The format war ended in 2017 when Apple joined the Wireless Power Consortium ([GSMArena](https://www.gsmarena.com/counterclockwise_the_wireless_charging_format_wars-news-34143.php)).
- **Smart Battery System** standardised the data interface but never the physical pack ([Wikipedia](https://en.wikipedia.org/wiki/Smart_Battery_System)).
- **EnergyBus** became an IEC specification in 2019, but the dominant e-bike systems still use proprietary batteries ([Wikipedia: EnergyBus](https://en.wikipedia.org/wiki/EnergyBus)).

The lesson is that being standardised is not the same as being adopted.

The motorcycle makers' swappable-battery consortium shows the route a cell format takes if it succeeds. It went from a letter of intent between Honda, Yamaha, KTM and Piaggio to a liaison role with CEN, CENELEC and ETSI ([MCNews](https://mcnews.com.au/?p=404724)). For UBS, that kind of formal standardisation is a step for year five, not year one.

## EU law is a tailwind, but cells bring paperwork in every country

### Article 11 is close to the UBS thesis, but it does not mandate standard cells

From **18 February 2027**, the EU Battery Regulation (EU) 2023/1542 sets these rules for products containing portable batteries ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1542/oj)):

- **Removable.** The batteries must be "readily removable and replaceable by the end-user" with commercially available tools.
- **No software lock-out.** Software may not be used to block "another compatible battery" (Art. 11(8)).
- **Spare parts.** Spare batteries must stay available for five years after the last unit is sold.

That is almost the UBS manifesto written into law, and it supports a pitch to device makers: "Article 11 compliance with an open cell".

It does not force anyone to use standard cells, however:

- The obligation covers "entire batteries and not individual cells".
- There are exemptions.
- Smartphones and tablets that meet the Ecodesign rules can keep built-in batteries ([Right to Repair Europe](https://repair.eu/?p=7509)).
- Proprietary removable packs comply just as well.
- A reported Commission delegated act from July 2026 would widen the exemptions from two categories to eight. It is not confirmed in the Official Journal ([EcoComply](https://ecocomply.ai/blog/eu-batteries-regulation-removability-2027)).

The UBS spec's "signed identity" feature collides with Art. 11(8). A device may read a cell's signature, but if it refuses a compatible non-UBS cell, that could be an unlawful software lock-out. Whether a plain protected 18650 counts as "compatible" with an Anodyne device needs an EU product lawyer's opinion.

### What actually applies to an Anodyne cell

Several of the Regulation's headline obligations do not apply to portable cells:

- **Battery passport:** applies only to EV, LMT (light means of transport, such as e-bikes) and industrial batteries over 2 kWh (Art. 77).
- **Carbon footprint declaration:** EV, LMT and large industrial batteries only (Art. 7).
- **Supply-chain due diligence:** does not apply below **€40 million turnover** (Art. 47) and has been postponed to August 2027 ([Latham & Watkins](https://www.lw.com/en/insights/european-commission-unveils-two-proposals-impacting-the-eu-batteries-regulation)).
- **Performance minimums:** 14500, 18650 and 21700 are not on the list of "portable batteries of general use" (Art. 3(10)), so the minimums planned for AA-type cells do not apply.

So the NFC passport is a voluntary product feature, not a compliance tool.

What does apply:

- **CE marking with self-declared conformity.** This uses Module A ("internal production control"), and no notified body is needed for portable cells (Art. 17).
- **The crossed-out-bin collection symbol.** For cylindrical cells it must cover at least 1.5% of the surface.
- **A QR code on every battery from 18 February 2027.** It must link to the label information and the declaration of conformity (Art. 13).
- **A capacity label for rechargeable batteries.** Its start date depends on an implementing act that was still unpublished in August 2026, so it will probably land in 2027–28 ([Pryor](https://www.pryormarking.com/18-august-2026-and-the-eu-battery-regulation/)).

The two-digit rating code is a fine extra, but it cannot replace the mandated capacity label. On a 14500, some label elements will probably have to move to the packaging.

The most demanding duty is **producer registration in every country where you first make cells available**, usually through a producer responsibility organisation (PRO). This has been in force in the EU since August 2025. Direct sales into another EU state also require an **authorised representative in that state** (Art. 55–56).

The Regulation also helps the business model in one respect. PRO fees must be adjusted by chemistry and to reward re-use and remanufacturing (Art. 57), and NFC-verified state of health is exactly the evidence a re-use claim needs.

### Norway is still on the old regime, but you must join a PRO before the first sale

As of 7 October 2026, the Battery Regulation is **still "under scrutiny" for the EEA Agreement**. No Joint Committee decision has been made ([EFTA EEA-Lex](https://www.efta.int/eea-lex/32023r1542)). Norway applies avfallsforskriften chapter 3. A new batteriforskrift that adopts the EU Regulation by reference is drafted and waiting ([RENAS](https://renas.no/aktuelt/siste-nytt/status-for-eus-nye-batteriforordning-i-norge/)).

Either way, anyone who makes or imports batteries for the Norwegian market must **be a member of an approved PRO before the battery is put into circulation** ([Miljødirektoratet](https://www.miljodirektoratet.no/ansvarsomrader/avfall/for-naringsliv/batteriveilederen/hvilken-rolle-og-hvilke-plikter-har-du/)). Candidates are Batteriretur, RENAS and Norsirk; ask each for a quote. Chargers and devices also need membership in a scheme for electrical and electronic waste (WEEE). Transitional rules were still under consultation in spring 2026, so ask your PRO or a Norwegian environmental lawyer about timing.

### The €3 return credit is legal, but it cannot run through the post

**What the law already requires.** Distributors, including online sellers, must already take back waste portable batteries free of charge (Art. 62). The UBS rule "any seller takes back any cell" is therefore mostly existing law. The €3 is the new part.

**How to structure the credit.** Nothing found forbids a producer from paying an extra incentive on top of producer responsibility. The return itself must never cost the consumer anything (Art. 59(4)). Structure it as a rebate on return, not as a surcharge refunded later, which would legally be a deposit.

**Where policy is heading.** The Commission must assess battery deposit-return systems by the end of 2027 (Art. 63). In December 2025, Austria, Germany and Lithuania pressed for faster action after battery fires at waste plants ([EUWID](https://www.euwid-recycling.com/news/policy/austria-germany-and-lithuania-press-european-commission-for-swift-decision-on-battery-deposit-scheme-151225/)). The industry body EPBA opposes a mandatory scheme ([EPBA](https://www.epba.eu/news/a-deposit-refund-scheme-is-not-an-effective-instrument-for-increasing-the-collection-of-portable-batteries)). Per-cell NFC IDs answer the fraud objection, so a UBS credit could become an early, compatible model if deposits arrive.

**What still needs a lawyer.** The draft says makers fund the credit by paying €3 per cell sold into a shared pool. A consumer, VAT and EPR lawyer needs to look at that mechanism, and so do price-display rules.

**Logistics.** Returned cells are dangerous goods and possibly waste, so returns must go to retail or PRO drop-off points, not into a mailbox. Re-selling returned cells would make Anodyne a "producer" of used batteries, with relabelling duties (Art. 13(9)).

### Testing, radio rules and liability

**Cell testing.** Each cell model needs:

- **UN 38.3** to be shipped at all. It costs about $2,000–7,000 and takes 3–6 weeks.
- **IEC 62133-2**, the practical evidence of product safety for retailers and marketplaces. It costs about $5,000–12,000 and takes 6–12 weeks ([Ufine](https://www.ufinebattery.com/blog/essential-guide-to-battery-certification-types-costs-timeframes-and-standards/)). One US lab quotes $8,225 for a single cell, with 43 samples ([BatterySpace](https://www.batteryspace.com/iec62133.aspx)).

A UBS cell, with its cap electronics, is a new assembly, so it will probably need its own tests even if the cell inside is certified. Altitude testing reportedly causes about 40% of first-time UN 38.3 failures ([Tritek](https://tritekbattery.com/un38-3-certified-battery-pack-what-it-means-and-how-to-source/)). Three sizes plus a LiFePO₄ variant means four or more test programmes.

**Chargers.** Expect about $4,000–15,000 per model for low-voltage safety, EMC and RoHS ([Alibaba seller guide](https://seller.alibaba.com/blogs/2026/southeast-asia/electronics-accessories/ce-certified-charger-compliance-guide-alibaba-b2b)). The source is a seller blog, so treat it as indicative.

**NFC rules.** NFC readers in chargers and devices bring the Radio Equipment Directive (RED) into play. The Cyber Resilience Act applies in full from **11 December 2027**, with vulnerability reporting from September 2026 ([Eleos](https://www.eleoscompliance.com/en/article/european-union-repeal-red-cybersecurity-delegated-regulation-eu-202230)). Whether a passive NFC tag inside a cell makes the cell itself "radio equipment" or a "product with digital elements" is **the most novel open compliance question** in the design. Nemko in Oslo is a natural first call ([Nemko](https://www.nemko.com/it-av-equipment-certification)).

**Liability.** The new Product Liability Directive (EU) 2024/2853 keeps no-fault liability. It names firmware explicitly as a "product" and applies to products placed on the market after **9 December 2026** ([Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive)). A fuel gauge that misreports could create liability even if the chemistry is fine. Insurance has to cover lithium fires and recalls explicitly. No premium benchmarks were found, so a broker with battery experience is needed.

### Shipping is the hardest operational constraint

- **Post.** **Posten does not accept loose lithium cells.** It takes them only installed in equipment, at most two batteries or four cells ([Posten](https://posten.no/en/sending/forbidden-content)).
- **Air.** Cells shipped alone (UN3480) are forbidden on passenger aircraft and must be at **≤30% charge**. Since 1 January 2026, cells packed *with* equipment must also be at 30% or less ([IATA 2026](https://www.iata.org/contentassets/05e6d8742b0047259bf3a700bc9d42b9/lithium-battery-guidance-document.pdf)).
- **Road.** The ADR road rules give relief for cells up to 20 Wh ([DEKRA guide](https://dekra.dk/media/xaeb1omh/guide-08.pdf)). Every UBS size falls under that by simple capacity × voltage arithmetic.

**Devices sold empty are easy to post. Cells need a dangerous-goods-capable road courier and, for EU customers, probably an EU warehouse.** The NFC gauge can document each cell's charge state at dispatch, which turns a feature into compliance evidence.

No EU rule was found that requires a device to be sold with its battery. The common-charger directive already requires that phones and similar devices can be bought without a charger ([Directive 2022/2380](https://eur-lex.europa.eu/eli/dir/2022/2380/oj)).

## A real but small opportunity, and only if products come first

### Shared batteries sell, but every winner owned the battery

"One battery, many devices" is proven at scale:

- **Einhell's Power X-Change** brought in **54% of €1,157.7 million** in 2025 revenue ([Einhell](https://www.einhell.com/investor-relations/financial-news/corporate-news/detail/EQS-News_188704911_en/)).
- **Ryobi ONE+** has over 300 products on one battery ([Ryobi](https://ryobitools.com/products/33287195084)).
- **Metabo's CAS alliance** reached its 50th partner in April 2026 ([Torque Expo](https://www.torque-expo.com/node/20992)).
- **Bosch** expected more than 30 million Power for All batteries by early 2023 ([Bosch](https://www.bosch-presse.de/pressportal/de/en/maximum-added-value-for-users-three-new-partners-for-the-power-for-all-alliance-241984.html)).

Every one of these platforms is anchored by a single dominant company that makes the pack and earns from it. Gogoro ran its own swap network and scooters before licensing to Yamaha and others ([RideApart](https://www.rideapart.com/news/361449/gogoro-network-battery-swapping-standards-push/)). Framework shipped its laptop before it opened its expansion-card spec and seeded developers with $100,000 ([Framework](https://frame.work/blog/expansion-card-developer-program--canada-launch)).

Qi and USB began as consortia of large companies ([Wikipedia: WPC](https://en.wikipedia.org/wiki/Wireless_Power_Consortium)). No case was found of an individual founder creating a widely adopted battery standard.

For UBS this means three things:

- Anodyne has to be the first cell supplier and the first device maker at the same time.
- The standard's credibility depends on being neutral, which is why the mark belongs in a separate body.
- Big brands ignoring UBS is a bigger threat than big brands copying it.

### The enthusiast niche is where there is room to charge a premium

Analysts size the adjacent markets in tens of billions, for example consumer batteries at about $30 billion ([Fortune Business Insights](https://www.fortunebusinessinsights.com/industry-reports/toc/rechargeable-battery-market-101350)). Nobody publishes a figure for loose consumer cells sold together with cell-agnostic devices, and it is a small fraction of those totals.

The price ladder shows where a premium is possible:

| Product | Price |
|---|---|
| Genuine unprotected Molicel P45B 21700 cell ([NKON](https://www.nkon.nl/rechargeable/li-ion/21700-20700-size/molicel-inr21700-p45b-4500mah-45a.html)) | **€4.55** |
| Fenix protected 21700 cell ([Knivesandtools](https://www.knivesandtools.dk/en/pt/-fenix-arb-l21-5000-21700-li-ion-battery-5000-mah-XX-50362.htm)) | **about €21** |
| Nitecore NL2150HP cell ([Battery Junction](https://www.batteryjunction.com/products/nitecore-nl2150hp-21700-battery)) | $28.95 |
| XTAR 4-bay charger ([123accu](https://123accu.nl/XTAR-VC4SL-oplader-i49572.html)) | €29.50 |

Fake cells are common. Forum tests find "9,900 mAh" 18650s delivering a fraction of their claim, and rewrapped cells are common ([BLF](https://budgetlightforum.com/t/4-pack-of-18650-batteries-with-9900-mah-for-real/70839)). Verified identity and health data address a real pain point, and an Anodyne cell priced like a Fenix is plausible. Enthusiasts distrust rewraps, though, so Anodyne would need to name its cell supplier openly.

The competition is already moving: Fenix and Nitecore sell their own "smart" protected 21700s with USB-C ([Battery Junction](https://www.batteryjunction.com/nitecore-nl2150hpr)).

### The cell's bill of materials argues for a lighter spec

Component prices from distributors:

- Molicel 18650 cells from about **$3.35–3.60** at volume ([18650 Battery Store](https://www.18650batterystore.com/pages/wholesale-18650-batteries)).
- NFC tag ICs about **$0.29–2** ([Farnell](https://uk.farnell.com/nxp/nt3h2111w0ft1/rfid-read-write-13-56mhz-soic/dp/2663149); [Findchips](https://origin-www.findchips.com/search/st25dv04kc-ie8t3)).
- A TI BQ27441 fuel gauge about **€1.65** at 1,000 units ([Farnell](https://at.farnell.com/texas-instruments/bq27441drzt-g1a/battery-fuel-gauge-li-ion-4-5v/dp/3008752)).

Adding protection, a cap PCB and assembly, my estimate is **$6–12 per UBS cell at a few thousand units**. The gauge and NFC chip alone add 40–100% to the bare cell.

That points to a design change in the spec:

- Require a cheap passive NFC tag.
- Make the in-cell gauge optional.
- Let chargers write health data to the tag.

The change cuts cost and the space problem on 14500s, and it moves away from the Duracell claims.

At the device level, a four-cell power bank sold empty for €150–250 costs more than an Anker Prime at $230 list once cells are added ([9to5Toys](https://9to5toys.com/2026/01/26/26250mah-anker-prime-3-port-300w-power-bank-171/)). The pitch therefore has to be longevity and reuse, not price.

### Demand is real in surveys, but thin in sales

79% of Europeans want devices to be easier to repair, but support falls to about 4 in 10 when it would raise the price ([Restarters](https://talk.restarters.net/t/survey-8-in-10-europeans-think-digital-devices-should-be-easier-to-repair/2613); [Lewis Silkin](https://brands.lewissilkin.com/archive/2020/11)).

Fairphone, the flagship repairable brand, sold about 103,000 phones in 2024. It needed €49 million of impact investment and only turned EBITDA-positive that year ([Wikipedia: Fairphone](https://en.wikipedia.org/wiki/Fairphone)). Teenage Engineering, the design-led model for Anodyne's look, reached about €38 million turnover in 2024 with roughly 90 staff ([Largest Companies](https://largestcompanies.com/company/Teenage-Engineering-AB-502717/closing-figures-and-key-ratios)).

A premium brand is possible, but it takes years, capital and design talent. Licensing revenue from the standard is not a realistic income line.

### Early money in Norway is small and non-dilutive

**Grants.** Innovasjon Norge's market clarification grant covers up to 100%, to about NOK 150,000. Commercialisation grants go up to NOK 750,000 at 75% ([PNO Innovation](https://www.pnoinnovation.com/no/finansiering/oppstartstilskudd/)). The 2026 amounts were not confirmed on Innovasjon Norge's own site.

**Tax relief.** SkatteFUNN gives a 19% tax deduction on approved R&D, which needs an AS (Norwegian limited company) with real R&D costs ([Forskningsrådet](https://www.forskningsradet.no/utlysninger/2026/skattefunn-skattefradrag-for-forskning-og-utvikling-i-et-nyskapende-naringsliv/)).

**EU grants.** The EIC Accelerator targets technology readiness levels 6–8 (working prototypes and beyond) and is out of reach at idea stage.

**Crowdfunding.** In one study only 9% of crowdfunded hardware campaigns delivered on time and 33% never delivered ([Chalmers](https://odr.chalmers.se/handle/20.500.12380/301564)). Use it for a cell-less device, never for cells.

### Founder time is the binding constraint

Standards work and brand work are each a full-time job. The first two stages are realistic part-time; launching a product is not, without a co-founder or a partner with hardware experience.

An alternative also deserves a serious look: offer the spec to an existing enthusiast flashlight brand, or to a Nordic retailer's own brand. You would give up control, but it removes most of the capital and liability.

## Which professional you need, and when

| Specialist | What for | When | Rough cost |
|---|---|---|---|
| **Trademark attorney** | Clearance of a new standard name and of "Anodyne"; the risk from UBS's reputation; class list; regulations of use for a certification mark; wording of the €3 credit as a condition of the mark | Stage 0–1, before any filing or rebrand | Patentstyret preliminary examination NOK 3,500 + NOK 625 per extra class; attorney fees not found |
| **European patent attorney** | Check whether Duracell's EP patents are validated in Norway; confirm the US grace-period dates; decide whether any unpublished detail is worth filing; draft the patent pledge | Stage 1 (short consult); Stage 2 (FTO) | FTO €5,000–20,000 ([IamIP](https://iamip.com/wiki/freedom-to-operate-fto/)) |
| **Company lawyer** | Set up the AS for Anodyne and the stiftelse or forening for the standard, and keep them separate | Stage 1–3 | Not found |
| **EPR compliance service or environmental lawyer** | Producer responsibility membership in Norway, EEA transition timing, EU authorised representatives | Before the first sale of anything | Ask PROs for quotes |
| **EU product lawyer** | Article 11 status of devices sold without cells; whether cell authentication conflicts with Art. 11(8); the GPSR position in Norway | Stage 2, before the device launch | Not found |
| **Consumer, VAT and EPR lawyer** | Mechanics of the €3 credit and the shared pool | Before any return-credit pilot | Not found |
| **RED/CRA specialist or notified body (e.g. Nemko)** | Whether an NFC tag in a cell is radio equipment; CRA scope | Stage 1, while the spec can still change | Not sourced |
| **Accredited test lab** | UN 38.3, IEC 62133-2, CE/EMC | Stage 2 (charger); Stage 3 (cells) | See the costs above |
| **Dangerous goods safety adviser (DGSA)** | Packaging, carriers and return logistics | Before shipping cells | Not found |
| **Insurance broker with battery experience** | Product liability and recall cover | Before selling any cell | Not found |

## Conclusion and staged plan

Most of the ideas cannot be patented, and that is acceptable: the value of an open standard comes from adoption, not from patents. The real assets are a distinctive name held by a neutral body, a logo programme, and a spec drafted to avoid the known patents. The cell itself is what drives the risk and cost of the plan: three or four test programmes, dangerous-goods logistics, a PRO in every market and fire liability.

That points to a sequence. Sell the devices and chargers that take "any protected 18650/21700" first, prove that people want to keep a pool of cells, and only then put Anodyne's name on a cell. A sensible spec change follows from this: a cheap passive NFC tag in the cell, health data written by the charger, and an optional gauge. That one change addresses cost, space and the Duracell patents at the same time.

Amounts below are rough. Euro and dollar costs are converted loosely to NOK, and my own sums are built from the sourced unit costs above. Founder time and the costs that could not be found (attorney hours, insurance, PRO fees, tooling) are excluded.

| Stage | Timing | What to do | Rough cash cost | Gate to the next stage |
|---|---|---|---|---|
| **0. Rename and listen** | 0–3 months | Stop using "UBS" publicly. Shortlist 3–5 invented names and do your own searches in TMview, WIPO's Global Brand Database, USPTO and Patentstyret in classes 7, 8, 9, 11 and 42, plus "Anodyne". Change the spec: passive NFC, optional gauge, antenna non-normative. Put the spec on Technical Disclosure Commons. Add a waitlist. Interview about 20 small device brands and 3–5 Chinese protected-cell assemblers. | Under NOK 20,000 (one preliminary examination about NOK 4,750) | At least 2 device makers interested in writing, and at least 1 assembler quote |
| **1. Protect and prototype** | 3–9 months | Form an AS. Apply for the Innovasjon Norge market clarification grant. File the chosen name in Norway (NOK 5,800) and extend to the EU within 6 months (€1,050). Republish the spec under CC BY 4.0 or the Community Specification License, with a royalty-free patent pledge. Build 10–20 prototype caps and one charger or bay. Short consults with a patent attorney (Duracell validation, US window) and Nemko (RED/CRA). | About NOK 100,000–250,000, much of it grant-eligible | Prototypes work, users value the pool, and no blocking patent or radio issue |
| **2. First product without cells** | 9–24 months | Launch a charger, flashlight or power-bank shell "for any protected 18650/21700" through an ODM (MOQ about 1,000). CE, plus RED if it has NFC. WEEE membership. Product liability insurance. Pre-orders. Narrow FTO on the passport before cell tooling. | About NOK 0.4–1.2 million (CE about $4,000–15,000; FTO €5,000–20,000; inventory and grants offset part) | Sell-through and repeat buyers; a co-founder or partner on board |
| **3. First Anodyne cell, then the foundation** | 24 months and later | Certify one cell size (UN 38.3 and IEC 62133-2, about $7,000–20,000). Join a battery PRO. Set up a DG-capable carrier. Pilot the return credit via drop-off points after a lawyer has reviewed it. Move the mark to a stiftelse or forening as a certification mark (NOK 4,000 + NOK 1,650 per extra class; EU €1,500). Recruit a second cell maker. Add other sizes only with demand (about $25,000–80,000 for the full range). | About NOK 0.3–1 million for the first size and a first batch | Independent makers asking to use the mark; only then approach Standard Norge or NEK |

Stop at the end of Stage 0 if no device maker and no assembler will engage. That is the cheapest possible way to learn the idea is early. Stop again after Stage 2 if people buy the empty devices but do not keep a cell pool. Then the open spec has still done its job as public prior art and a design statement, and the founder has spent tens of thousands of kroner rather than millions.
