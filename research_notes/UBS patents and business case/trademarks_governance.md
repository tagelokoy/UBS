# Trademarks, copyright and governance for an open hardware standard (UBS / Anodyne)

Scope: how a private founder in Norway can keep "UBS" (Universal Battery System) open and royalty-free while protecting its name, quality and safety, and how the separate commercial brand "Anodyne" fits in. Norway/EEA first, then EU and US. Researched 7 October 2026. Not legal advice: points marked **[attorney]** need a trademark or IP attorney.

Note on method: the official trademark databases (EUIPO eSearch, TMview, WIPO Global Brand Database, USPTO search, Patentstyret search) are JavaScript applications that could not be queried from this research environment, and Justia's trademark search returned HTTP 403. The clearance findings below come from web search and are **not** a clearance search. A real search in those databases is the first practical task (see the last section).

---

## 1. Trademark conflicts: "UBS", "Universal Battery System", "Anodyne", and which classes matter

### Takeaway
"UBS" is very likely unusable as a trademark or logo for a consumer hardware standard. UBS Group AG holds a mark that is registered worldwide and that dispute panels have repeatedly called famous, so a registration would probably be opposed and the brand would be weak. "Universal Battery System" is a descriptive phrase that others already use for battery platforms, so it is hard to register on its own and impossible to make exclusive. "Anodyne" has at least one active user in a nearby field (ANODYNE infrared light-therapy devices, US) and is an ordinary English word. It needs a proper search in classes 9, 11 and 8 before any money is spent on it.

### Cited Findings
**UBS (the bank)**
- UBS has used the UBS mark since at least 1962 for financial services. It owns many registrations for UBS in the US, the EU, Switzerland, China and through WIPO. — [ADR Forum UDRP decision](https://www.adrforum.com/DomainDecisions/1832240.htm)
- UDRP panels have repeatedly found the UBS mark "well known and famous", and UBS actively pursues domain names that contain "UBS" plus generic words (ubs-bank.net, ubspremium.com, ubsofficial.com). — [ADR Forum decisions](https://www.adrforum.com/DomainDecisions/1742275.htm); [WIPO UDRP D2005-0993](https://www.wipo.int/amc/en/domains/decisions/html/2005/d2005-0993.html)
- A search summary indicates that UBS AG's global portfolio includes class 9 (software/electronics) as well as class 36 (finance). The exact EUTM class 9 coverage could not be confirmed. — [IP Australia records for UBS AG](https://search.ipaustralia.gov.au/trademarks/search/view/957291/details); [Gleanmark owner page, UBS Group AG](https://gleanmark.com/owner/ubsgroupag)

**"Universal Battery System" / "Universal Battery"**
- "Universal Battery" is a trademark and brand of Universal Power Group (UPG), which has sold sealed lead-acid batteries since 1968. — [Ace Hardware listing (UPG Universal Battery)](https://www.acehardware.com/p/8258964)
- A US application for UNIVERSAL BATTERY (serial 77162835, filed 2007, sealed lead-acid batteries) was abandoned in 2008. — [Justia Trademarks](https://trademark.justia.com/771/62/universal-battery-77162835.html)
- The phrase is already used descriptively for battery platforms. Black & Decker Canada launched VersaPak as a "universal battery system", and Canadian Tire markets PWR POD as "Canada's Universal Battery System". — [Strategy Online](https://strategyonline.ca/?p=13605); [Canadian Tire, PWR POD](https://canadiantire.ca/en/all-brands/pwr-pod.html)
- US patents also use the phrase, for example "Universal battery and modular power system" (US 10,753,761). — [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10753761)

**Anodyne**
- Anodyne Therapy, LLC (US) sells "Anodyne Therapy" infrared light-therapy devices, which are registered in the FDA's GUDID device database. — [AccessGUDID](https://accessgudid.nlm.nih.gov/devices/00859101006004)
- In a published lawsuit resolution, the ANODYNE mark was described as "valid and enforceable", which shows the owner has litigated over it. — [Rehab Management, "Resolution of lawsuit"](https://rehabpub.com/pain-management/chronic/resoultion-of-lawsuit/)
- An old US mark, JOHNSON'S AMERICAN ANODYNE LINIMENT (reg. 427494), is dead. — [Trademarkia](https://www.trademarkia.com/johnson-s-american-anodyne-liniment-71498891)
- No ANODYNE registration in classes 8, 9 or 11 turned up in web search. That is **not** evidence that none exists. — (search result: none found)

**Which classes matter (Nice classification)**
- Class 9 covers electrical and scientific apparatus: batteries, chargers, electronics and software. — [Nolo, Class 9](https://www.nolo.com/legal-encyclopedia/trademark-class-9-computers-scientific-devices.html); [USPTO, Goods and services](https://www.uspto.gov/trademarks/basics/goods-and-services)
- Patentstyret requires applicants to choose their goods and services at filing: "it is not possible to add new ones later". — [Patentstyret, Anna's guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- Patentstyret recommends checking name availability in TMview and the WIPO Global Brand Database before filing. — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)

### Inferences
- **UBS:** Under EU and Norwegian law, a mark with a *reputation* can be protected against later marks for dissimilar goods when the later use takes unfair advantage of, or harms, the earlier mark. The CLAUDE.md for this repo already uses "UBS" in that way (EUTMR Art. 8(5)/9(2)(c) and the Norwegian equivalent; this is general legal knowledge and was not sourced in this research **[attorney]**). Combined with UBS's documented enforcement, this means a "UBS" logo on batteries invites an opposition or a letter, and probably also domain and search-visibility problems ("UBS battery" will surface the bank). The practical recommendation is to treat "UBS" as an internal working name only and choose a different public name before anything is filed or launched.
- **"Universal Battery System"** is descriptive (it says what the thing is), so registering it alone would probably be refused for lack of distinctiveness, and others already use it. It can still serve as a plain descriptive tagline next to a distinctive name, for example "[NewName] – a universal battery system".
- **Anodyne:** Light therapy (medical devices) is likely class 10, so it may not conflict directly with class 9/11/8 goods. But Anodyne plans lighting (class 11), and "anodyne" means "painkiller", so the risk has to be checked on the register. An attorney's clearance opinion is worth paying for here **[attorney]**.
- **Classes to consider:**
  - Standard and certification mark: class 9 (rechargeable cells, battery packs, chargers, battery management electronics), possibly class 42 (testing and certification services), and class 41/16 if publishing the spec matters.
  - Anodyne: class 9 (cells, chargers, power banks), class 11 (lamps, torches, lighting), class 8 (hand tools), class 7 if powered tools (power-operated tools are class 7, while hand-operated tools are class 8), and class 35 if retail services matter.
- **How to evaluate alternative names:**
  1. Generate invented or arbitrary names, not descriptive ones.
  2. Knock-out search on TMview, WIPO GBD, USPTO and Patentstyret in classes 7/8/9/11/42.
  3. Check domains (.com/.org/.no), app stores and the big retail platforms.
  4. Check the name's meaning in major languages.
  5. Order a Patentstyret preliminary examination or an attorney clearance opinion on the 1–3 finalists.

### Gaps
- Exact EUIPO, Norwegian and US register results for "UBS", "Universal Battery System" and "Anodyne" in classes 7/8/9/11/42 could not be retrieved because the databases are JavaScript-only and Justia returned 403. A manual search is needed.
- Whether UBS AG's EU or Norwegian registrations cover batteries in class 9 is unconfirmed.

---

## 2. Costs, process and timeline: Norway (Patentstyret), EU (EUIPO), international (Madrid), US

### Takeaway
A Norwegian word mark in 3 classes costs NOK 5,800 in official fees. An EU trade mark in 3 classes costs €1,050. A Norwegian filing gives a 6-month priority window to extend abroad through Madrid. Patentstyret's own worked example puts an international portfolio in the region of NOK 75,000 before attorney fees. Certification and collective marks cost somewhat more (Norway NOK 4,000 for the first class; EU €1,500 online) and also need written regulations of use.

### Cited Findings
**Norway (Patentstyret)**
- Ordinary trademark application: NOK 3,800 including one class, plus NOK 1,000 per additional class. Renewal every 10 years: NOK 3,400 plus NOK 1,300 per additional class. Opposition is free. Administrative review costs NOK 4,000. — [Patentstyret fees](https://www.patentstyret.no/en/about-us/how-we-work/prices-trademark-patent-design)
- Worked example: 3 classes cost NOK 5,800. — [Patentstyret, How much does a trademark cost?](https://www.patentstyret.no/en/trademark/how-much-does-a-trademark-application-cost)
- Collective and guarantee (certification) marks: NOK 4,000 for the first class plus NOK 1,650 per additional class. Renewal: NOK 5,150 plus NOK 2,100 per additional class. — [Patentstyret fees](https://www.patentstyret.no/en/about-us/how-we-work/prices-trademark-patent-design)
- Patentstyret charges NOK 800 to process an international (Madrid) application filed through Norway. — [Patentstyret fees](https://www.patentstyret.no/en/about-us/how-we-work/prices-trademark-patent-design)
- Optional preliminary examination (a search plus an assessment before filing): NOK 4,750, or NOK 3,500 for one class plus NOK 625 per extra class. Normally delivered within 5 working days, or 48 hours on the express service. — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection); [Patentstyret fees](https://www.patentstyret.no/en/about-us/how-we-work/prices-trademark-patent-design)
- After filing in Norway, "you have six months to extend the protection" abroad with the Norwegian filing date as priority. — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- Patentstyret's example of international protection through Madrid (3 classes, several markets): about NOK 8,000 in WIPO fees, about NOK 55,000 in country fees and about NOK 5,000 in fixed surcharges, "around NOK 75,000" in total, with adviser fees on top. — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- Third parties can oppose a registration within three months of its publication (varemerkeloven § 26). — [Norsk varemerketidende](https://search.patentstyret.no/tidende/varemerke/2020/varemerketidende-nr04-2020.pdf)

**EU (EUIPO)**
- EU trade mark, online filing: €850 for one class, €50 for the second and €150 for each class from the third on. — [TMarkMetric, EU trademark cost 2026](https://tmarkmetric.com/insights/eu-trademark-cost)
- EU collective and certification marks: €1,800 basic fee, or €1,500 online, with the same €50/€150 additional-class fees. — [EUIPO, Fees and payments](https://www.euipo.europa.eu/en/trade-marks/before-applying/fees-payments); [EUIPO, Certification and collective marks](https://www.euipo.europa.eu/en/trade-marks/before-applying/certification-and-collective-marks)
- SME Fund 2026 (open 2 February–4 December 2026): 50% reimbursement of basic trademark and design application fees, up to €1,500 per SME. It is open to SMEs established in the EU and in Ukraine. — [Dudkowiak, SME Fund 2026](https://www.dudkowiak.com/blog/sme-fund-2026-funding-for-eu-national-and-international-ip-filings/)

**International (WIPO Madrid)**
- Madrid basic fee: CHF 653 (black and white) or CHF 903 (colour). Complementary fee: CHF 100 per designated country unless that country charges an individual fee. Supplementary fee: CHF 100 per class beyond three. Many offices, including the EU and Norway, charge individual fees instead. — [WIPO, Madrid schedule of fees](https://www.wipo.int/madrid/en/fees/sched.html)

**US (USPTO)**
- Since 18 January 2025 there is a single base application at $350 per class. Surcharges apply: $200 for free-form descriptions of goods and services, and $200 per 1,000 extra characters. — [Buchanan Ingersoll & Rooney](https://bipc.com/uspto-set-to-change-trademark-fees-alongside-patent-increases-in-2025)

### Inferences
- **Indicative official-fee budget (3 classes, word mark only):**
  - Norway: NOK 5,800.
  - EU: €1,050.
  - US: $1,050.
  - Madrid add-ons: on the order of NOK 50–75k for several countries.
  - Certification-mark versions cost more.
  - Attorney fees typically come on top. No reliable Norwegian attorney fee figures were found.
- The SME Fund appears **not** to cover a Norway-established company, since it is limited to the EU and Ukraine. If the founder later forms an EU entity, that changes. **[verify]**
- **Typical sequence:**
  1. File a Norwegian national application, which is cheap and starts a priority date.
  2. Within 6 months, extend to the EU (EUTM directly or through Madrid) and to the US if relevant.
  3. Alternatively, file the EUTM first and use it as the Madrid base.
- **Timeline:** examination, publication and a 3-month opposition period, so several months to registration in Norway or the EU. No official Patentstyret processing-time figure was found.

### Gaps
- Patentstyret's current average processing time and EUIPO's average time to registration were not retrieved.
- The exact Norwegian and EU individual fees under Madrid in CHF were not retrieved; only Patentstyret's aggregate example is available.
- USPTO certification-mark fees were not specifically confirmed (they are believed to follow the same per-class base fee).

---

## 3. Certification and collective marks, and how logo programs enforce compliance on a free spec

### Takeaway
The standard pattern is to let anyone read and implement the spec, and to require a licence, testing and a listing before anyone may use the **logo or name**. Trademark law is what lets the owner stop non-compliant products from carrying the mark. This is how USB-IF, Bluetooth, Wi-Fi, Qi, Thunderbolt and Matter work.

A true **certification (guarantee) mark** in the EU or Norway may not be owned by anyone who sells the certified goods. So if Anodyne (or the founder's trading company) sells cells, the UBS-style mark has to sit with a separate neutral entity (foundation or association), or else be an ordinary trademark or collective mark under a licence program.

### Cited Findings
**Legal framework**
- EU certification marks (EUTMR Art. 83) can be applied for by any person "provided that such person does not carry on a business involving the supply of goods or services of the kind certified". — [IPPT, EUTMR Art. 83](https://www.ippt.eu/legal-texts/eu-trade-mark-regulation-2017/article-83); [EUIPO guide to certification and collective marks (PDF)](https://euipo.europa.eu/knowledge/pluginfile.php/164955/mod_label/intro/Certification%20and%20Collective%20marks.pdf)
- EU certification marks need regulations of use, filed within two months of the application. They must state the conditions of use, any fees, and the sanctions for misuse, and must be clear enough for a reader to understand the requirements. — [EUIPO, Regulations of use for EU certification marks (PDF)](https://euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/trade_marks/RoU_EU_certification_marks/RoU_EU_certification_marks_en.pdf)
- Norway, collective marks: available to associations and organisations of producers or traders and to public bodies.
- Norway, guarantee or certification marks: any entity may apply, but "the holder of the mark is not allowed to conduct commercial activities involving the sale of the goods or services covered". The regulations must cover user eligibility, terms of use, enforcement, and the owner's duty to monitor compliance. Applications use a special form in Altinn. — [Patentstyret, Collective and guarantee/certification marks](https://www.patentstyret.no/en/trademark/collective-marks-and-guarantee-or-certification-marks)

**How the industry programs work**
- **USB-IF:**
  - Membership costs $5,000 a year and includes a vendor ID. A vendor ID bought separately costs $6,000.
  - Non-members can take a logo licence for $3,500 per two years, which is waived for members.
  - Logos may be used only on products that have passed USB-IF compliance testing and are on the Integrators List. Without the logo licence agreement you may not use the logo, "regardless of their testing status".
  - Sources: [USB-IF](https://www.usb.org/node/1809); [USB-IF Logo Trademark License Agreement](https://usb.org/node/1811)
- **Bluetooth SIG:**
  - Adopter membership is free.
  - The product qualification fee for Adopters is $12,000 per new design, effective 1 March 2026.
  - A Company Identifier costs $1,250.
  - Sources: [Bluetooth SIG fee schedule](https://www.bluetooth.com/fee-schedule/)
- **Wireless Power Consortium (Qi):**
  - Regular membership costs $20,000 a year plus a $10,000 ecosystem fee, so $30,000 in total. Associate membership was discontinued on 1 January 2024.
  - Qi interoperability testing costs $1,500–2,000.
  - Certification listing costs $750 per new product and $250 per substantially similar product.
  - Sources: [WPC, Cost of certification](https://www.wirelesspowerconsortium.com/knowledge-base/testing-and-certification/cost-of-certification/); [WPC pricing PDF](https://www.wirelesspowerconsortium.com/media/qp4l2yiu/pricing-information-page-102023.pdf)
- **Connectivity Standards Alliance (Matter, Zigbee):**
  - Membership tiers: Associate (free), Adopter ($7,000 a year), Participant ($20,000) and Promoter ($105,000 plus an initiation fee).
  - Matter certification costs $3,000 per product for Adopters ($2,500 for derivative products) and $2,000 for Participants and Promoters ($1,500 for derivatives).
  - Adopters may use the Alliance logos on certified products.
  - Sources: [CSA, Become a member](https://csa-iot.org/become-member/); [Matter Alpha](https://www.matteralpha.com/industry-news/connectivity-standards-alliance-confirms-membership-tiers-for-iot-development)
- **Wi-Fi Alliance:** a company must be a member and achieve certification to use the Wi-Fi CERTIFIED logo and certification marks. — [Wi-Fi Alliance](https://www.wi-fi.org/node/61)
- **Thunderbolt (Intel):** certification is mandatory before a product may use the Thunderbolt logo and branding, and only products that have passed certification may show the Thunderbolt icon. Intel holds the trademark rights. — [Intel Thunderbolt messaging guide (PDF)](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2023-09/thunderbolt-messaging-guide.pdf); [AppleInsider (trademark transfer to Intel)](https://forums.appleinsider.com/discussion/124630)

### Inferences
- **For UBS, the €3 return credit "as a condition of using the mark" is legally the kind of condition that can go into regulations of use or a logo licence.** EUIPO explicitly expects the regulations to state conditions, fees and sanctions. Whether a take-back or deposit obligation is acceptable as a certification *characteristic*, and how it interacts with the EU Batteries Regulation's producer-responsibility rules, needs advice **[attorney]**.
- **Three structural options:**
  - **(a) Ordinary trademark plus a logo licence:** like USB-IF, Bluetooth, Intel and CSA. The owner may also make products. This is simplest and the most common in the industry, but conflict-of-interest optics apply if Anodyne owns it.
  - **(b) Certification or guarantee mark:** owned by a neutral foundation that sells nothing. This is the strongest signal of independence and is consistent with "Anodyne is a separate brand", but Anodyne must be fully separated from the owner.
  - **(c) Collective mark:** owned by an association of implementers and used by its members.
- **Recommended direction:** a neutral foundation or association owns the standard's name and logo (as a certification mark, or as an ordinary mark under a licence program). Anodyne is just one licensee or member, on the same terms as everyone else.
- **Fee levels:** the big programs charge thousands to tens of thousands of dollars a year. A small new standard has to charge little or nothing, as Bluetooth Adopter membership is free, or nobody will join. Testing can be self-declared at first, with audits and random market sampling later.

### Gaps
- Examples of certification marks that certify conformity with a *technical* standard (as opposed to origin or quality schemes), and EUIPO refusals in that area, were not retrieved because the Fieldfisher article returned 403.
- No source was found on whether USB-IF, Bluetooth and similar programs register their logos as certification marks or as ordinary marks in each jurisdiction. They appear mostly to be ordinary marks under licence, but this is not verified.

---

## 4. Copyright on a specification versus patents on ideas; licensing options

### Takeaway
Copyright protects the *text and drawings* of the spec, not the technical idea. Anyone may implement the functionality without a copyright licence. EU case law confirms that functionality, interfaces and data formats are ideas, not protected expression. The real "openness" risk is **patents**, so a spec licence should combine an open copyright licence for the document with a royalty-free patent commitment from contributors. The Community Specification License and OWFa 1.0 do both. CC BY 4.0 covers the text only.

### Cited Findings
- In *SAS Institute v World Programming* (CJEU, 2 May 2012), the court held that the functionality of a computer program, its programming language and its data file formats are not protected by copyright. Manuals can be protected as literary works where the choice, sequence and combination of their content is the author's intellectual creation. — [SCL report](https://www.scl.org/2451-sas-institute-inc-v-world-programming-ltd-report-and-analysis/); [Computerworld](https://www.computerworld.com/article/2504590/eu--programming-languages-can-t-be-copyrighted.html)
- **Community Specification License:**
  - It is a repository-based framework, created through the Joint Development Foundation, with contributor agreements, governance and contribution rules.
  - It includes royalty-free patent commitments that extend "to implementations of the entire specification, regardless of who made the actual contribution".
  - It drew on the Open Web Foundation agreements and the Alliance for Open Media patent licence.
  - It is designed to scale and later transition to formal standards bodies.
  - Source: [Community Specification on GitHub](https://github.com/CommunitySpecification/Community_Specification)
- **OWFa 1.0:**
  - Grants a perpetual, worldwide, royalty-free copyright licence to "reproduce, prepare derivative works of… distribute, and implement the Specification".
  - Adds a patent non-assert and a commitment to a "no charge, royalty free license to my Granted Claims", limited to claims necessarily infringed by implementing the spec.
  - Expressly grants no trademark rights.
  - Source: [Open Web Foundation, OWFa 1.0](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0)
- **CC BY 4.0** licenses copyright and similar rights in the material. The legal code states that patent and trademark rights are not licensed. — [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode)

### Inferences
- **Recommended stack for UBS:**
  - Publish the spec text under CC BY 4.0, or under the Community Specification License if multiple companies will contribute.
  - Have every contributor sign a patent commitment (the CSL or OWFa-style royalty-free grant).
  - Keep the **name and logo out of the copyright licence**, and say so explicitly, so that copying the spec gives no right to call a product "UBS-certified". Both OWFa and CC BY already exclude trademarks.
- A **CC BY-ND** or "no-derivatives" spec licence is sometimes used to prevent forks. Forks are better handled through the trademark: anyone may fork the text, but only the official version can use the name.
- **Patents:** the founder's own inventions can be (a) patented and licensed royalty-free (defensive), or (b) published openly as prior art to block others from patenting them. Publishing before filing destroys novelty for the founder's own patent in Europe, where there is no general grace period (general legal knowledge, not sourced here) **[attorney]**. This is covered in more depth by the separate patents research.

### Gaps
- No direct source was retrieved comparing CC BY 4.0 with the CSL for hardware specs, or describing hardware standards that use the CSL. The CSL's own documentation is software- and spec-oriented.

---

## 5. Governance models and what they cost to run

### Takeaway
The options run from a single owner (cheap, fast, but not trusted as "open"), through a founder-led alliance (Power for All, CAS), to a membership standards body (USB-IF, WPC, CSA), which needs paying members, staff and a test program. Hosted foundations (Linux Foundation's JDF) cost nothing to start. Formal standardisation (Standard Norge, CEN-CENELEC, IEC) is open and cheap to join but slow, and it gives up control of the text.

For a solo founder, the realistic path is to start as a JDF-hosted project or a Norwegian foundation (stiftelse) that holds the mark, with free implementer access, and to consider a formal standard later.

### Cited Findings
**Single company**
- **Ryobi ONE+:** launched in 1996 and kept backward compatible, so the newest 18V ONE+ batteries fit the original 1996 tools. The range has grown to well over 300 tools. It is a single-company, closed platform. — [Ryobi, Celebrating 30 years](https://uk.ryobitools.eu/footer-links-en/information/celebrating-30-years/); [SlashGear](https://www.slashgear.com/2207521/what-is-ryobi-one-plus-promise-which-tools-does-it-apply-to/)

**Founder-led alliances**
- **Bosch Power for All Alliance:** founded in 2020 and now includes 10 brands (Bosch, Gardena, Gloria, Wagner, Rapid, Flymo, Steinel, Husqvarna, Kübler Workwear, PerfectPro) on one 18V battery and charger. — [Bosch press release](https://www.bosch-presse.de/pressportal/de/en/maximum-added-value-for-users-three-new-partners-for-the-power-for-all-alliance-241984.html)
- **Metabo Cordless Alliance System (CAS):** founded in 2018 with 9 brands on Metabo's 18V LiHD technology, and has since grown to 50 partners (Exact Tools was the 50th) and more than 300 devices. — [Handwerksblatt (2018)](https://www.handwerksblatt.de/betriebsfuehrung/auf-dem-weg-zur-akku-norm); [Torque Expo](https://www.torque-expo.com/node/20992); [Toolbrothers](https://www.toolbrothers.de/en/blogs/news/cas-battery-system-manufacturer-independent-flexible-future-proof)

**Membership standards bodies** (fees as in section 3)
- **USB-IF:** $5,000 a year. — [USB-IF](https://www.usb.org/node/1809)
- **Bluetooth SIG:** free Adopter tier plus a $12,000 qualification fee. — [Bluetooth SIG](https://www.bluetooth.com/fee-schedule/)
- **WPC:** $30,000 a year. — [WPC](https://www.wirelesspowerconsortium.com/knowledge-base/testing-and-certification/cost-of-certification/)
- **CSA:** $0 to $105,000 a year. — [CSA](https://csa-iot.org/become-member/)

**Open foundations**
- **Joint Development Foundation (Linux Foundation):** "There's no cost to start and run your project", using the JDF's legal agreements and its 501(c)(6) structure. Bank accounts, project management and meeting logistics are available at extra cost. The JDF says it has cut the time to set up a standards project from months to days. — [JDF Projects, About](https://jdfprojects.lfprojects.linuxfoundation.org/about); [Linux Foundation blog](https://linuxfoundation.org/blog/accelerating-open-standards-development-with-community-specifications)
- The JDF is recognised as an ISO/IEC JTC 1 PAS submitter, which gives a route from a JDF spec to an international standard. That route is for JTC 1 (information technology), not batteries. — [Linux Foundation](https://www.linuxfoundation.org/blog/joint-development-foundation-recognized-as-an-iso-iec-jtc-1-pas-submitter-and-submits-openchain-for-international-review)
- **RISC-V International membership:**
  - Community (individuals, academic and non-profit organisations): free.
  - Strategic Startup (fewer than 10 employees and under 2 years old): $2,000.
  - Strategic: $5,000, $15,000 or $35,000 by headcount.
  - Premier: $100,000 or $250,000.
  - Source: [RISC-V International, Membership](https://riscv.org/membership)

**Formal standardisation**
- **Standard Norge:** according to a 2025 course document, participating in a Norwegian standardisation committee is free. The time commitment is 40+ hours a year for a national mirror committee (1–4 meetings a year) and 100+ hours a year for international work, plus travel. — [Standard Norge course material 2025](https://standard.no/globalassets/generelt-horisontalt/standardisering/standardiseringskurs/trinn-i-varen-2025---del-b.pdf)
- **IEC:** the first IEC standards for battery sizes were issued in 1957, and IEC 60086 has defined the alphanumeric battery coding since 1992. US battery standardisation dates back to 1919 (National Bureau of Standards) and continues in ANSI C18 (NEMA). — [Wikipedia, Battery nomenclature](https://en.wikipedia.org/wiki/Battery_nomenclature)

### Inferences
**Cost per model for a solo founder**
- **Single company (Anodyne owns UBS):**
  - Cost: only trademark fees.
  - Upside: fastest.
  - Downside: competitors won't adopt a rival's standard, so "open" isn't credible. This fails the stated goal.
- **Alliance led by Anodyne (CAS/PfA model):**
  - Works when the founder already has market power, which Metabo and Bosch had and Anodyne does not.
  - CAS and PfA are effectively brand-licensing programs around one company's battery, not open specs.
- **JDF-hosted Community Specification project:**
  - Cost: $0 to start, plus trademark fees.
  - Gives a neutral US non-profit home for the spec and its IP policy.
  - Who would hold a certification mark under it is unclear and needs checking with the Linux Foundation **[verify]**.
- **Norwegian stiftelse or forening owning the mark:**
  - Gives local control and makes the neutrality requirement for a guarantee mark easy to meet.
  - Setup cost includes registering with Stiftelsestilsynet and Brønnøysund, with minimum capital required for a stiftelse **[verify]**.
- **Full membership SDO (USB-IF style):**
  - Needs staff, a test lab or authorised test labs, and a legal budget.
  - Only feasible once several manufacturers pay dues.
- **Formal standard (Standard Norge → CENELEC/IEC):**
  - Committee seats are cheap, but the process takes years, the text becomes a paid standard, and control is shared.
  - Best treated as a later step, once there is a working spec and products (the SBMC path; see section 6).

### Gaps
- No total running-cost data (staff, legal, test lab) was found for small standards bodies.
- No source was found for the minimum capital or setup cost of a Norwegian stiftelse.
- Membership terms for Power for All and CAS (fees, licence conditions) are not public in the sources found.
- Formal IEC TC 21 / CENELEC TC 21X participation routes and costs were not researched in detail.

---

## 6. Lessons from successful and failed consumer hardware standards

### Takeaway
Standards win when the parties that control demand (phone makers, the dominant OEMs) sign up and the certification program is cheap enough to join. Technical superiority alone loses. Fragmented, competing consortia slow adoption until one absorbs the others. Battery standards that last (AA/IEC 60086, SBS) are the ones that went through neutral bodies or multi-company forums. Power-tool batteries stay proprietary or alliance-bound, and motorcycle makers are now taking a consortium-to-CEN/IEC route.

### Cited Findings
- **Qi versus PMA and A4WP/AirFuel:**
  - WPC had the phone makers.
  - PMA (Procter & Gamble and Powermat) won Starbucks and McDonald's, creating a "chicken and egg" split.
  - A4WP's Rezence was arguably technically superior but less efficient and needed larger coils.
  - The war ended in 2017, when Apple joined WPC and put Qi in the iPhone, and Powermat then joined WPC.
  - Sources: [GSMArena, Counterclockwise: the wireless charging format wars](https://www.gsmarena.com/counterclockwise_the_wireless_charging_format_wars-news-34143.php); [Wikipedia, Wireless Power Consortium](https://en.wikipedia.org/wiki/Wireless_Power_Consortium)
- **Swappable Batteries Motorcycle Consortium (SBMC):**
  - Honda, Yamaha, KTM and Piaggio signed a letter of intent and started work in May 2021, aiming to define common swappable battery specs and push them into European and international standardisation.
  - It has grown to 21 members, including Kawasaki, Suzuki, KYMCO, Niu, Samsung and Swobbee.
  - It has agreed technical specifications and become a formal liaison member of CEN, CENELEC and ETSI.
  - Sources: [Piaggio Group press release](https://www.piaggiogroup.com/en/archive/press-releases/swappable-batteries-motorcycle-consortium-agreement-signed-between-piaggio); [MCNews](https://mcnews.com.au/?p=404724); [Carole Nash](https://www.carolenash.com/news/bike-news/detail/swappable-batteries-motorcycle-consortium-grows-in-stature)
- **Gogoro (context):** runs its own battery-swap network, with about 2,000 stations in Taiwan at the time of the SBMC launch. — [Jalopnik](https://jalopnik.com/honda-yamaha-ktm-and-piaggio-are-working-together-on-1846383571)
- **Smart Battery System (laptop batteries):**
  - Originated with Duracell and Intel in 1994 and was developed further by an industry forum.
  - The SBD spec 1.1 (December 1998) carried joint copyright from Benchmarq, Duracell, Energizer, Intel, Linear Technology, Maxim, Mitsubishi, National Semiconductor, Toshiba and Varta.
  - The *electronic interface* (SMBus data) standardised; the *physical pack* did not.
  - Sources: [Wikipedia, Smart Battery System](https://en.wikipedia.org/wiki/Smart_Battery_System); [SBS Forum spec PDF](https://www.sbs-forum.org/specs/sbsel110.pdf)
- **AA/AAA and IEC 60086:** the formal route through IEC (first battery-size standards in 1957) and ANSI C18 produced interchangeable cell sizes worldwide, although IEC and ANSI designations are still not fully harmonised. — [Wikipedia, Battery nomenclature](https://en.wikipedia.org/wiki/Battery_nomenclature)
- **Power tools:** CAS (2018) and Power for All (2020) are founder-company alliances around Metabo's and Bosch's own 18V packs. — [Handwerksblatt](https://www.handwerksblatt.de/betriebsfuehrung/auf-dem-weg-zur-akku-norm); [Bosch press release](https://www.bosch-presse.de/pressportal/de/en/maximum-added-value-for-users-three-new-partners-for-the-power-for-all-alliance-241984.html)

### Inferences
- **Lessons for UBS:**
  1. Recruit a few anchor device makers before launch. Demand-side adoption decided Qi.
  2. Keep certification cheap for small makers, or offer a free tier as Bluetooth does for Adopters.
  3. Avoid splitting the market with a second competing standard. Joining or aligning with an existing effort can beat starting a rival.
  4. Make sure the standard's owner is neutral, or competitors will treat it as Anodyne's proprietary platform, the way CAS and PfA are seen as Metabo's and Bosch's.
  5. Plan a later hand-off to IEC/CENELEC so the cell format can become a "real" standard like AA.
- SBS shows that a forum can standardise the electronics and data while form factors stay proprietary. UBS's value is the *physical cell plus protection*, so it needs a mechanical spec and a testing regime, which is harder.
- The AA precedent suggests that if UBS cells succeed, the eventual home is IEC TC 21/TC 35 or CENELEC. A JDF or foundation spec is a stepping stone. This is an inference: no source was found describing such a route for a new cell format.

### Gaps
- No good source was found on failed or abandoned early laptop-battery *form-factor* standardisation attempts, beyond SBS's electronic standard.
- No source was found on Gogoro's open-platform licensing terms or on the SBMC's IP or licence policy.
- No published SBMC specification or formal standard number was found as of October 2026.
- The PMA/AirFuel governance details (fees, IP policy) were not retrieved.

---

## 7. Practical first steps and order; what to avoid; when to involve an attorney

### Takeaway
1. Fix the name problem first: pick a new, distinctive name for the standard.
2. Run a clearance search and get a professional opinion.
3. File the name and logo in Norway, or as an EUTM, to secure a priority date.
4. Then extend within 6 months.
5. Set up the neutral owner entity (foundation or JDF project) before launching the logo program.
6. Publish the spec under an open copyright licence plus a patent commitment.
7. Keep Anodyne as a separate company that licenses the mark like anyone else.

Avoid publicly launching the "UBS" name and logo, and avoid publishing patentable details, before getting advice.

### Cited Findings
- Patentstyret recommends searching existing marks, contacting its free customer centre for guidance, optionally ordering a preliminary examination, and then filing with the chosen classes. — [Patentstyret, Anna's guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- A Norwegian filing date gives 6 months of priority for foreign filings, and "maintaining Norwegian filing date provides advantage if others file similar marks". — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- The goods and services list cannot be extended after filing. — [Patentstyret guide](https://www.patentstyret.no/en/articles/guide-trademark-protection)
- A guarantee or certification mark owner may not sell the certified goods, under both Norwegian and EU law. — [Patentstyret](https://www.patentstyret.no/en/trademark/collective-marks-and-guarantee-or-certification-marks); [EUTMR Art. 83](https://www.ippt.eu/legal-texts/eu-trade-mark-regulation-2017/article-83)
- EU certification mark regulations of use must be filed within 2 months of the application. — [EUIPO RoU guidance](https://euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/trade_marks/RoU_EU_certification_marks/RoU_EU_certification_marks_en.pdf)
- The JDF can host a spec project at no cost, using its legal agreements. — [JDF Projects](https://jdfprojects.lfprojects.linuxfoundation.org/about)

### Inferences (suggested order; not legal advice)
1. **Now, at low cost:** stop expanding public use of "UBS" as a brand. The site currently says "UBS" in the open. Shortlist 3–5 invented names for the standard. Search TMview, WIPO GBD, USPTO and Patentstyret for each, plus "Anodyne", in classes 7/8/9/11/42. Check domains.
2. **Attorney, step 1 [attorney]:** a clearance opinion on the finalists and on "Anodyne", a few thousand NOK upward (no source for exact fees). Also ask about the UBS reputation risk and the €3-return-credit wording.
3. **File** the chosen standard name (word mark, plus the logo later) in Norway (NOK 5,800 for 3 classes) or as an EUTM (€1,050), and "Anodyne" separately. Use the 6-month priority to extend to the EU, UK and US as needed.
4. **Decide the owner of the standard's name:**
   - (a) A Norwegian stiftelse or forening, which can hold a guarantee or certification mark because it sells nothing.
   - (b) A JDF/Linux Foundation project.
   - (c) An interim holding by the founder personally, assigned to the foundation later.
   - The guarantee or certification mark version must be filed *by* the neutral entity, so set it up first or file an ordinary mark now and add a certification mark later **[attorney]**.
5. **Spec licensing:** CC BY 4.0 or the Community Specification License for the text, plus a royalty-free patent pledge. State explicitly that the name and logo are licensed only through the certification program.
6. **Certification program v0:**
   - Free or low-cost licence.
   - Self-test against a published checklist (cell protection, honest capacity ratings, the €3 return credit).
   - A public listing of certified products, as with USB-IF's Integrators List.
   - Sanctions, including the right to withdraw the mark.
   - Third-party testing can come later.
7. **Anodyne:** form a separate AS (aksjeselskap) for the commercial brand, take a licence to the standard's mark on the same terms as others, and keep separate trademarks.
8. **Avoid before advice:**
   - Publishing undisclosed inventive details you might want to patent, since publication destroys novelty.
   - Using ® before registration. Marking an unregistered mark as registered is generally prohibited (general knowledge, not sourced here).
   - Promising "certified safe" claims that could create liability.
   - Using "UBS" in domains or social handles.
9. **When an attorney is needed:**
   - Name clearance and the UBS reputation risk.
   - Drafting the certification-mark regulations of use and the logo licence.
   - Patent strategy and defensive publication.
   - The foundation structure and its relationship with Anodyne.
   - Product liability and battery-regulation compliance (EU Batteries Regulation, CE). Those regulatory aspects are outside this note.

### Gaps
- Typical Norwegian trademark attorney fees for clearance and filing were not found.
- No source was found for the setup cost or minimum capital of a Norwegian stiftelse or forening, or for whether a JDF project can own a certification mark.
- The interaction between the €3 return credit and EU Batteries Regulation producer-responsibility rules was not researched here.
