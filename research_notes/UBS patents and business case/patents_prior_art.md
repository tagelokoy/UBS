# UBS patent landscape: prior art, freedom-to-operate risk, patentability, and patents in open standards

Scope note: these are research notes, not legal advice. Patent status data below comes mostly from Google Patents pages, which give "anticipated expiration" and "Active" flags computed by Google, not legal status from the EPO Register or Patentstyret. For a European patent (EP...B1), "Active" on Google Patents does not tell you in which countries it was validated or whether renewal fees are paid in Norway. Any decision should rest on a register check by a European patent attorney. The research session had about 25 tool calls, so coverage is a sample of the landscape, not a search.

## Q1. For each UBS feature (a)–(g), what prior art and notable patents exist?

### Takeaway
Almost every building block of UBS already exists in prior art: smart batteries with fuel gauges and data (1994–95), authentication in fuel gauge chips, cylindrical cells with NFC/RFID antennas on a ferrite shield (Duracell, 2013 priority), polarity-correcting converters (1999), per-cell DC/DC converters on a shared bus, and USB-rechargeable cells with indicators in the cap. The cluster with the most live patent risk is feature (d), the in-cell NFC "passport", because Duracell holds an active family covering antennas wrapped on cylindrical cells over a ferrite shield and battery-status communication.

### Cited Findings

**(a) Fixed outer dimensions, in-cell protection, button top / (c) mandatory protection circuit / cap electronics**
- Patent applications already cover lithium-ion cylindrical cells with a PCB and LED charging indicator in the top cap, inside a PET sleeve, with the cell fixed to the PCB through a support frame and steel sleeve ("Lithium battery with cap charging indication function", US 2022/0200072) — [Justia](https://patents.justia.com/patent/20220200072)
- Older prior art covers rechargeable cylindrical battery assemblies (AAA/AA/C/D) with a USB plug, recharging circuitry and a cap (US 7,375,494; US 8,067,923) and "Rechargeable battery with USB inputs" (US 8,314,590B2) — [USPTO 7375494](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375494); [USPTO 8067923](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8067923); [Google Patents US8314590](https://patents.google.com/patent/US8314590)
- "Portable light and keyed rechargeable USB battery" (US 11,639,789) describes a battery case with a cylindrical main part, a rechargeable cell and a cap that encloses a circuit board — [USPTO 11639789](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11639789)

**(b) Chemistry by wrap color plus raised tactile bands**
- No patent or prior art specific to tactile bands encoding cell chemistry was found in this session (see Gaps).

**(d) "Passport": NFC tag plus fuel gauge in the cell, antenna on ferrite under the wrap, signed identity, readable by phone**
- Smart Battery Data (SBD) and SMBus were announced by Duracell and Intel on 21 April 1994. SMBus 1.0 was released on 15 Feb 1995. SBD defines the data a smart battery reports: remaining capacity, full charge capacity, manufacturing data, current, voltage, temperature and so on. This is decades-old prior art for "a battery that stores and reports its identity, rating and live state" — [Wikipedia: Smart Battery System](https://en.wikipedia.org/wiki/Smart_Battery_System); [SMBus 1.0 spec](https://www.smbus.org/specs/smb10.pdf)
- TI fuel gauges (e.g. bq27350) already combine a single-cell Li-ion fuel gauge with SHA-1/HMAC pack authentication. Newer TI parts (BQ41zxx) use ECC key pairs and TI ships key-programming tools. Signed cell identity is therefore a commodity feature at the chip level — [TI bq27350 datasheet](https://www.ti.com/lit/gpn/bq27350); [TI app note](https://www.ti.com/document-viewer/lit/html/SLUAAQ0/GUID-8A9D2DF1-20E9-4792-9132-8E923490E02B); [Electronic Design](https://www.electronicdesign.com/technologies/power/article/21758555/battery-ics-charge-gauge-and-authenticate)
- **Duracell "Omni-directional antenna for a cylindrical body" family**, priority 23 May 2013:
  - US 9,887,463 B2 claims a battery status circuit with a flexible ferrite shield on a cylindrical battery, a loop antenna printed on that shield, and an IC (which may include an ADC and an RFID/NFC chip) that senses battery condition and reports it to a reader. Assignee Duracell U.S. Operations Inc. Status Active, anticipated expiry 23 May 2033.
  - Family: US 9,478,850 B2 (parent), US 10,916,850 B2 (continuation), EP 3000152 B1, JP 6178002 B2, CN 110165363 B, WO 2014/189831.
  - [Google Patents US9887463B2](https://patents.google.com/patent/US9887463B2/en)
- **EP 3000152 B1** (same family): granted 27 Dec 2023 according to Google Patents. Status Active, anticipated expiry 19 May 2034. Claim 1 covers a flexible substrate on a cylindrical body with two symmetric rectangular antenna loops about 180° apart, wrapping around the ends and along the length, connected to an IC, giving omni-directional RFID/NFC reception. Google Patents did not show which countries it was validated in — [Google Patents EP3000152B1](https://patents.google.com/patent/EP3000152B1/en)
- **Duracell "Battery including an on-cell indicator"**, US 10,297,875 B2, priority 1 Sep 2015. Status Active, anticipated expiry 26 Apr 2037. Claim 1 covers a battery with an electrochemical cell, an on-cell indicator, a PCB, conductive traces, and an IC for remote wireless communication. Family includes EP 16760327.3 / EP 3345242 A1, JP, CN 107851859 A, AU, WO 2017/040282 — [Google Patents US10297875B2](https://patents.google.com/patent/US10297875B2/en)
- **Duracell "Positive battery terminal antenna ground plane"**, US 10,483,634 B2, priority 1 Nov 2016. Status Active, expiry 1 Feb 2037. Claim 1 uses the battery's positive terminal and can as the antenna ground plane, with an impedance-matching circuit, for battery status communication. Family: **EP 3535795 B1**, AU 2017355386 B2, CN 109891648 B, JP 7064492 B2, US 11,031,686 B2, WO 2018/085343 — [Google Patents US10483634B2](https://patents.google.com/patent/US10483634B2/en)
- Further Duracell patents that cite the antenna family, in the same field: US 10,184,988 B2 "Remote sensing of remaining battery capacity using on-battery circuitry"; US 10,416,309 B2 "Systems and methods for remotely determining battery characteristic"; US 10,608,293 B2 "Dual sided reusable battery indicator"; US 10,818,979 B2 "Single sided reusable battery indicator". Their statuses were not checked — [Google Patents US9887463B2, cited-by list](https://patents.google.com/patent/US9887463B2/en)
- A Korean patent covers a battery protection circuit package with an NFC antenna, and a battery pack including it (KR 101602832 B1) — [Google Patents](https://patents.google.com/patent/KR101602832B1/en)

**(e) Two-digit energy/power rating code**
- No patents were found on a rating code for cells. This is a labelling convention, and labelling and marking schemes are generally hard to patent (see Inferences).

**(f) Universal multi-size bays with a per-slot DC/DC converter feeding a shared bus; polarity-independent slots with active MOSFET bridges**
- Polarity independence:
  - US 6,023,418 A, "Low voltage polarity correcting DC to DC converter", lets a single-cell device work with the battery in either orientation, using two solid-state switches in series instead of a diode bridge to avoid the voltage drop. It also covers a holder that accepts the battery either way. Priority 29 Apr 1999. Status: **Expired, fee related, 8 Feb 2008**. Assignee Lohman Technologies LLC — [Google Patents US6023418A](https://patents.google.com/patent/US6023418A/en)
  - US 5,431,575 "Bi-directional battery holder" notes that a diode bridge gives the right polarity either way at the cost of a voltage drop — [USPTO 5431575](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5431575)
  - US 3,887,393 is an even older battery holder assembly — [Google Patents](https://patents.google.com/patent/US3887393A/en)
  - EP 1456925 B1 and US 7,126,801 B2, "Polarity protection implemented with a MOSFET" — [Google Patents EP1456925B1](https://patents.google.com/patent/EP1456925B1/en); [US7126801B2](https://patents.google.com/patent/US7126801B2)
  - A published "polarity-correcting circuit protects battery-powered devices" design idea exists in EDN — [EDN](https://www.edn.com/polarity-correcting-circuit-protects-battery-powered-devices/)
- Per-cell DC/DC converters and mixed cells on a shared bus:
  - US 5,656,915, "Multicell battery pack bilateral power distribution unit with individual cell monitoring and control", was issued 12 Aug 1997 — [Justia](https://patents.justia.com/patent/5656915)
  - WO 2011/015900 A1, "A battery pack with integral DC-DC converter(s)" — [Google Patents](https://patents.google.com/patent/WO2011015900A1/en)
  - US 2012/0194133 A1 covers active cell balancing with isolated bidirectional DC/DC converters on an independent DC energy-transfer bus. It notes that batteries may differ in chemistry — [Google Patents](https://patents.google.com/patent/US20120194133A1/en)
  - US 8,237,407 B2, "Power supply modules having a uniform DC environment", allows different chemistries — [Google Patents](https://patents.google.com/patent/US8237407)
  - US 9,461,482 B2, "Multi-chemistry battery pack system" (lead-acid plus Li-ion) — [Google Patents](https://patents.google.com/patent/US9461482B2/en)
  - Recent US patents on mixed-chemistry pack power transfer use multilevel inverters as DC/DC converters (US 12,506,432 and US 12,397,658) — [USPTO 12506432](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12506432); [USPTO 12397658](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12397658)
  - The fact that ONE built a commercial "dual-chemistry" EV pack shows that mixed-chemistry packs are an active, commercial area — [Charged EVs](https://chargedevs.com/features/ones-hybrid-battery-pack-combines-the-best-aspects-of-two-chemistries-to-deliver-600-miles-of-ev-range/)
- Tool battery platform interfaces, relevant to the screwdriver and the modular power bank:
  - Makita owns US 6,350,149, "Structure of electrical terminals for establishing electrical contact between a battery pack and an electrical device".
  - Milwaukee holds EP 4379904 A3 on a battery pack terminal (terminal walls forming a gap with a coil spring).
  - Milwaukee sued Makita and Hitachi in 2009 (both settled), and later sued Hilti, Snap-on, Festool and Chervon.
  - [Search summary with EPO and RPX sources](https://insight.rpxcorp.com/news/7947); [EP4379904 A3](https://data.epo.org/publication-server/rest/v1.2/patents/EP4379904NWA3/document.html); [Makita EP2149433 A3](https://data.epo.org/publication-server/rest/v1.2/patents/EP2149433NWA3/document.html); [EPO Board of Appeal T 0225/23 (Battery pack/MAKITA), 30 Jan 2025](https://www.epo.org/en/boards-of-appeal/decisions/t230225eu1); [US11945094B2 Battery pack interface](https://patents.google.com/patent/US11945094)

**(g) Return credit, where a shop verifies the cell by NFC and marks it returned**
- No battery-specific patent was found in this session. The building blocks are already prior art: RFID/NFC on cells (Duracell family above) and authentication in the gauge (TI above).

### Inferences
- Features (a), (c) and (e) are standard engineering and labelling choices. Protected 18650 cells, cells with indicators or USB in the cap, and smart-battery data sets are all long-established. These features are unlikely to be patentable and are not obvious FTO risks, apart from specific cap or PCB constructions such as US 2022/0200072 if granted.
- Feature (d) is the hot spot. Duracell's family covers *how* the antenna is built on a cylindrical cell: loops on a flexible ferrite shield, and the positive terminal or can used as ground plane. A UBS design that puts a loop antenna on ferrite under the wrap, read by a phone, sits close to these claims. Whether it infringes depends on the exact claim wording, such as the "two rectangular loops about 180° apart" in EP 3000152 B1. Only a claim-by-claim review by a patent attorney can settle that.
- Feature (f): the generic ideas (polarity correction with switches, per-cell converters on a shared bus) have expired or very old prior art. The 1999 polarity patent expired in 2008, and per-cell bus converters go back to 1997. Specific implementations may still be patented, especially recent mixed-chemistry converter topologies and tool-pack terminal geometries. If UBS bays use a Makita, Milwaukee or similar style slide-rail terminal, check the terminal designs.
- Feature (g) is a business method. Business methods are largely excluded from patentability at the EPO as such. US patents in this area exist in general, but none were found here.

### Gaps
- No search was done on tactile chemistry markings on cells (b) or on multi-size battery compartments and adapters (for example, AA-to-C or 18650/21700 adapters and spring-loaded multi-length holders). These need a dedicated Espacenet search.
- Patents from Energizer, Panasonic or Sony on batteries with NFC were not checked. Neither were Apple or Dell battery authentication patents.
- The status of the Duracell cited-by patents (US 10,184,988 and the others) and any EP equivalents was not checked.
- Assignees and status of US 12,506,432, US 12,397,658 and WO 2011/015900 were not checked.
- EU Battery Regulation (EU) 2023/1542 "battery passport" technical implementations were not researched here. My background knowledge is that the digital passport applies from Feb 2027 to EV, LMT and industrial batteries over 2 kWh, and is QR-code and database based rather than an in-cell chip. This was not verified in this session.

## Q2. Which patents appear active and in force in Europe/Norway, and who owns them?

### Takeaway
The clearest active European patents relevant to UBS are Duracell's EP 3000152 B1 (antenna on a cylindrical cell, anticipated expiry May 2034) and EP 3535795 B1 (positive terminal as antenna ground plane, 2016 priority, likely expiry around 2037). Their US counterparts run to 2033–2037. Whether they are validated and in force in Norway was **not confirmed**.

### Cited Findings
| Patent | Owner | Priority | Status (Google Patents) | Expiry (anticipated) | UBS feature |
|---|---|---|---|---|---|
| EP 3000152 B1 | Duracell US Operations Inc | 23 May 2013 | Active, granted 27 Dec 2023 | 19 May 2034 | (d) antenna on cell |
| US 9,887,463 B2 (and US 9,478,850, US 10,916,850) | Duracell U.S. Operations Inc | 23 May 2013 | Active | 23 May 2033 | (d) |
| US 10,297,875 B2 / EP 3345242 A1 | Duracell US Operations Inc | 1 Sep 2015 | US active. EP grant status not checked | 26 Apr 2037 (US) | (d) indicator plus wireless IC |
| US 10,483,634 B2 / EP 3535795 B1 / US 11,031,686 B2 | Duracell US Operations Inc | 1 Nov 2016 | Active | 1 Feb 2037 (US) | (d) can as ground plane |
| US 6,023,418 A | Lohman Technologies LLC | 29 Apr 1999 | Expired, 8 Feb 2008 (fees) | n/a | (f) polarity |

Sources:
- EP 3000152 B1: [Google Patents](https://patents.google.com/patent/EP3000152B1/en)
- US 9,887,463 B2 and family: [Google Patents](https://patents.google.com/patent/US9887463B2/en)
- US 10,297,875 B2 / EP 3345242 A1: [Google Patents](https://patents.google.com/patent/US10297875B2/en)
- US 10,483,634 B2 / EP 3535795 B1 / US 11,031,686 B2: [Google Patents](https://patents.google.com/patent/US10483634B2/en)
- US 6,023,418 A: [Google Patents](https://patents.google.com/patent/US6023418A/en)

- Milwaukee EP 4379904 A3 (battery pack terminal, priority family from Dec 2017) is a published application. Its grant and status were not checked — [EPO publication](https://data.epo.org/publication-server/rest/v1.2/patents/EP4379904NWA3/document.html)

### Inferences
- A European patent only takes effect in Norway if it was validated there after grant, and only stays in force while Norwegian renewal fees are paid. Norway is an EPC member; this is general knowledge and was not verified in this session. EP 3000152 B1 was granted in Dec 2023, so the Norwegian validation deadline has passed and its status can be read from Patentstyret's register. Duracell's main markets are likely to be covered (DE, FR, GB and others), and that matters if UBS sells EU-wide.
- The Unitary Patent (since June 2023) does not cover Norway. Norway is not an EU member. Background knowledge, not verified here.
- Duracell is a large, active brand in the same consumer battery shelf space. It also co-founded the Smart Battery standard (with Intel, 1994). That makes it both a plausible enforcer and a plausible partner or licensor.

### Gaps
- Validation and renewal status in Norway (NO), Germany, France and the UK for EP 3000152 B1 and EP 3535795 B1 was not available from Google Patents. It needs a check in the EPO Register and Patentstyret's database (search.patentstyret.no).
- Panasonic, Sony, Energizer, Samsung SDI and LG patents on NFC or ID in cells were not checked.

## Q3. What does freedom to operate (FTO) mean, what does it cost, and when should the founder pay for one?

### Takeaway
An FTO analysis checks whether a specific product, in specific countries, would infringe someone else's in-force patents. It is different from a patentability search, which asks whether your idea is new. A professional FTO typically costs about €5,000–20,000 in Europe, and a fuller legal opinion runs $15,000–30,000 or more. It is worth paying for once a concrete product design is frozen and before tooling or volume launch, not at concept stage.

### Cited Findings
- An FTO analysis usually has two parts: the search, and a clearance report or legal opinion, often written by patent attorneys — [IamIP: Freedom to Operate](https://iamip.com/wiki/freedom-to-operate-fto/)
- Typical FTO analysis costs about €5,000–20,000, depending on the number of documents reviewed and the level of detail — [IamIP](https://iamip.com/wiki/freedom-to-operate-fto/)
- A basic FTO opinion costs around $5,000, and a more comprehensive legal analysis $15,000–30,000 or more. Cost rises with product complexity, the number of components and technologies, and the number of jurisdictions — [Search summary citing tryandai / ipiry patent-search cost guides](https://www.tryandai.com/blog/patent-search-cost); [ipiry](https://www.ipiry.com/guides/patent-search-cost)
- Finnegan (a US IP firm) discusses when an FTO opinion is cost-effective. It weighs product investment and launch risk against the cost of the opinion — [Finnegan](https://www.finnegan.com/en/insights/articles/when-is-a-freedom-to-operate-opinion-cost-effective.html)

### Inferences
- UBS spans several technology areas (cell construction, NFC antenna, fuel gauge firmware, power electronics, tool interfaces) and several products. A full multi-product FTO would sit at the high end of the range or above. A cheaper route is a staged FTO: first a narrow one on the in-cell passport (feature d, where the Duracell family is), then one per product before each launch.
- Buying chips and modules from established suppliers (TI fuel gauges, NFC tag ICs) does not transfer the supplier's patent position for the whole system. Supplier patent licences or indemnities are worth asking about. Background reasoning, not sourced.
- Norwegian-specific FTO pricing was not found. Norwegian patent firms' rates are likely to be in line with Western European rates.

### Gaps
- No Norwegian source (Patentstyret, Norwegian firms such as Zacco, Onsagers, Bryn Aarflot or Acapo) giving FTO prices was found.
- No source was found on Patentstyret or Innovasjon Norge support schemes for IP costs, such as IPR advice vouchers. Worth checking.

## Q4. Could the founder patent anything, would it help or hurt an open standard, and what does publishing on the website mean?

### Takeaway
Under European law (EPC Art. 54/55), anything the founder has already published on the public website is prior art against the founder's own later European or Norwegian application. There is no general grace period, only narrow exceptions for evident abuse and officially recognised international exhibitions within 6 months. The US gives the inventor a 12-month grace period from their own disclosure. Most UBS features are probably not patentable anyway given the prior art above. For an open standard, defensive publication (cheap or free) is usually the better fit than patenting.

### Cited Findings
- Art. 55 EPC: a disclosure is ignored for novelty only if it occurred no earlier than six months before filing **and** was due to (a) evident abuse against the applicant or (b) the applicant displaying the invention at an official or officially recognised international exhibition — [EPO Case Law, Non-prejudicial disclosures under Art. 55 EPC](https://epo.org/en/legal/case-law/2019/clr_i_c_2_5.html); [EPC Art. 55](https://www.epo.org/law-practice/legal-texts/html/epc/2020/e/ar55.html)
- The six months are counted from the actual filing date of the European application, not the priority date (G 3/98, G 2/99) — [EPO Case Law](https://epo.org/en/legal/case-law/2019/clr_i_c_2_5.html)
- In Scandinavian patent law, novelty is absolute and objective. Publishing the invention or lecturing about it before filing can destroy novelty — [Lawline (Swedish legal Q&A)](https://lawline.se/answers/vilka-krav-galler-for-patent)
- US: 35 U.S.C. §102(b)(1) gives a one-year grace period. An inventor-originated disclosure made one year or less before the effective filing date is not prior art against the inventor's own application — [USPTO MPEP 2153](https://www.uspto.gov/web/offices/pac/mpep/s2153.html); [MPEP 2151](https://www.uspto.gov/web/offices/pac/mpep/s2151.html)
- Defensive publication is a deliberate public disclosure to create prior art that blocks anyone, the discloser included, from patenting the idea — [CASRAI](https://casrai.org/guides/defensive-publication)
- Technical Disclosure Commons is free to publish on and free to read, and its documents are indexed by search tools including Google Patents — [IPWatchdog](https://ipwatchdog.com/2020/05/25/defensive-publications-cost-effective-tool-supplement-patent-strategy/)
- IP.com's Prior Art Database is a paid service that distributes to patent offices, at about $109 per document according to one source. Publishing a technical disclosure costs under about $300, compared with $20,000 or more per patent application in key countries — [IP.com defensive publishing](https://ip.com/defensive-publishing/); [Richard Poynder](https://www.richardpoynder.co.uk/On%20the%20defensive.htm); [Igor International](https://igorinternational.com/blog/?p=2869)

### Inferences
- **Effect of the website.** Every feature already described on https://tagelokoy.github.io/UBS/ (and in the public GitHub repo with its commit history) is very likely novelty-destroying prior art in Europe and Norway against a later application by anyone, including the founder. In the US the founder still has 12 months from the first publication date to file on what was disclosed. The commit history and GitHub Pages deploy dates can be used to establish when that clock started. A patent attorney should confirm this and the exact dates.
- **What might still be patentable:** only new, unpublished technical details that are not obvious given the prior art above. Examples might be a specific polarity-agnostic contact geometry combined with the MOSFET bridge, a specific way to put a gauge plus NFC in a cap within 18650/21700 tolerances while avoiding Duracell's antenna geometry, or a specific multi-size bay mechanism. Inventive step against SBS (1995), TI authentication and the Duracell family will be a high bar. The rating code, the color and band scheme and the return credit scheme are presentation or business-method features and are weak candidates at the EPO.
- **Help or hurt.** A patent held by the founder could be pledged royalty-free to UBS implementers. That gives some defensive leverage and credibility with partners and can deter copycats who might file around the standard. But it costs money: roughly €5k–10k+ to file and prosecute per family and more to validate, and the source on this is limited (see Gaps). It also adds friction and suspicion for an "open" standard. Defensive publication of every new detail before showing it publicly is cheaper and matches an open standard. It prevents others from patenting the published details, but it does not stop anyone using them.
- A practical sequence: (1) keep publishing openly, adding dated technical detail to the repo or website (GitHub timestamps are good evidence) and mirroring key disclosures to TDCommons for indexing in Google Patents; (2) if a genuinely new mechanism appears that a partner might value, talk to a patent attorney *before* publishing it.

### Gaps
- No Patentstyret page was retrieved stating its novelty and grace-period rules directly. The Norwegian Patents Act is understood to mirror the EPC (absolute novelty, Art. 55-style exceptions), but this was not verified here.
- Filing and prosecution costs at Patentstyret and the EPO were not retrieved (official fee schedules: patentstyret.no, epo.org fees).

## Q5. How do open standards handle patents, and what are the "submarine" risks?

### Takeaway
Standards bodies use one of two models. In royalty-free models (W3C, Bluetooth SIG's reciprocal member licence), participants commit to license essential claims without royalties. In FRAND models (ETSI), owners commit to license essential patents on fair, reasonable and non-discriminatory terms, which can include royalties. Both commitments bind only *participants*. A third party who never joined, such as Duracell for UBS, is not bound, which is where submarine risk comes from.

### Cited Findings
- W3C's stated aim: "W3C seeks to develop Specifications that can be implemented on a Royalty-Free (RF) basis." Working Group participants commit to RF licensing of their Essential Claims — [W3C Patent Policy](https://www.w3.org/policies/patent-policy/)
- W3C defines Essential Claims as those "necessarily infringed" by implementing the specification, where "there is no non-infringing alternative." Participants may exclude specific patents during defined windows (150 days after the first public draft, among others) by naming the patent and the affected spec sections. Disclosure "does not require that the discloser perform a patent search" — [W3C Patent Policy](https://www.w3.org/policies/patent-policy/)
- Bluetooth SIG: the Bluetooth Patent/Copyright License Agreement is a reciprocal, royalty-free licence among members to IP that is "necessary" for Bluetooth. Members rely on it when adopting Bluetooth — [Bluetooth SIG governing documents](https://bluetooth.com/about-us/governing-documents); [PCLA](https://www.bluetooth.com/wp-content/uploads/2019/03/PCLA-ESign-Version-Version-11.pdf)
- ETSI IPR Policy clause 6.1: when an essential IPR comes to ETSI's attention, the Director-General asks the owner for an irrevocable written undertaking, within three months, to license on FRAND terms. Members must use reasonable endeavours to disclose essential IPR in a timely way. ETSI does not check essentiality or validity — [ETSI IPR Policy](https://www.etsi.org/images/files/IPR/ETSI-ipr-policy.pdf)
- FRAND commitments are enforceable but can still lead to injunctions in Europe and the UK. In Optis v Apple (UK Court of Appeal 2022), the implementer had to undertake to take a FRAND licence or face an injunction — [EWCA Civ 1411](https://caselaw.nationalarchives.gov.uk/ewca/civ/2022/1411); [Bird & Bird](https://cm.twobirds.com/en/patenthub/shared/insights/2022/global/frand-injunction-bites-even-if-a-rate-is-yet-to-be-set)
- Prior standards in this exact space exist: Duracell and Intel's Smart Battery System and SMBus (1994–95) were managed by an industry forum (SBS-IF, later SMIF) of about ten promoter companies — [Wikipedia: Smart Battery System](https://en.wikipedia.org/wiki/Smart_Battery_System)

### Inferences
- For UBS, a light structure would be a written UBS patent policy modelled on W3C RF. Anyone who contributes to or implements the spec and wants the "UBS" mark would commit to RF licensing of essential claims, and the founder would pledge any patents they ever own the same way. This only binds those who sign up.
- Submarine risk means patents unknown at standardisation time, often pending applications published 18 months after filing, held by non-participants. For UBS this risk is concrete for the in-cell NFC/gauge passport (Duracell, and possibly others not yet checked). Mitigations:
  - design the spec so the antenna and gauge implementation is *not normative*: specify the data and protocol (for example NFC Forum Type 5 / ISO 15693 and a data schema), not the antenna geometry, so implementers can design around;
  - list known patents in an informative annex;
  - re-run a watch search periodically.
- A trademark and certification programme ("UBS-compatible" logo), not patents, is the usual lever for enforcing compliance with an open standard (USB-IF and WPC/Qi logo programmes are the analogues). Background knowledge; USB-IF and WPC policies were not fetched.

### Gaps
- USB-IF and WPC (Qi) patent and licensing policies, and the Open Invention Network licence terms, were not fetched in this session.
- Patent pools (for example Via LA or Avanci) were not researched. They are less relevant at UBS's scale.
- Where a patent attorney is needed:
  1. a claim-level FTO on the in-cell NFC/gauge design against the Duracell EP and US families, plus a Norway/EU validation check;
  2. a check of the bay and terminal design against the power-tool interface portfolios (Makita, Milwaukee and others) if a slide-on pack interface is used;
  3. advice on whether any not-yet-published detail is worth filing before it is published, and on the US 12-month window measured from the website's first publication date;
  4. drafting the UBS patent policy and trademark and certification terms.
