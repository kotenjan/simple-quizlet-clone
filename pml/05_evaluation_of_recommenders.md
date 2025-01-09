### Personalizované Strojové Učení: Hodnocení Doporučovacích Systémů

---

#### **Základní Rámec Doporučovacích Systémů**
- **Hlavní Paradigmy Hodnocení:**
  - **Offline Analytika:** Posuzování algoritmů bez interakce s reálnými uživateli.
  - **Case Study (Případová Studie):** Detailní analýza konkrétního případu nebo implementace.
  - **Online Experiment:** Testování algoritmů v reálném čase s reálnými uživateli.

---

#### **Offline Analytika**
- **Cíle:**
  - Posoudit doporučovací algoritmy.
  - Filtrace nevhodných algoritmů a zachování potenciálních kandidátů.
- **Postup:**
  - Předběžné shromáždění dat o chování uživatelů (např. volby nebo hodnocení položek).
  - Simulace interakcí mezi uživateli a doporučovacími systémy pomocí datasetu.
- **Výhody:**
  - Nevyžaduje interakci s reálnými uživateli.
  - Nákladově efektivní a umožňuje rychlé testování různých algoritmů.
- **Nevýhody:**
  - Omezená schopnost hodnotit serendipitu nebo novost.
  - Může neodrážet změny v distribuci preferencí uživatelů.
- **Metody Hodnocení:**
  - **Křížová Validace (Cross-Validation):** Rozdělení datasetu na tréninkovou a testovací sadu pro hodnocení výkonu algoritmů.

---

#### **Studie Uživatelů (User Study)**
- **Postup:**
  - Nábor testerů, kteří budou vykonávat úkoly s doporučovacími systémy.
  - Zohlednění distribuce testerů (např. demografické faktory).
  - Pozorování a zaznamenávání chování testerů během úkolů.
- **Sběr Dat:**
  - Které úkoly byly dokončeny?
  - Kolik času bylo stráveno na jednotlivých úkolech?
  - Přesnost výsledků úkolů.
- **Kvalitativní Dotazování:**
  - Preference týkající se uživatelského rozhraní (UI).
  - Vnímání složitosti úkolů.
- **Výhody:**
  - Poskytuje hlubší pochopení uživatelského chování a preferencí.
- **Nevýhody:**
  - Vysoké náklady na provedení.
  - Potřeba velkého počtu testerů.
  - Nutnost dokončení mnoha interakčních úkolů.
- **Trade-off:**
  - Náklady × Statistická významnost × Kvalita dat.

---

#### **Online Experiment**
- **Definice:**
  - Provádění rozsáhlých testů na nasazeném doporučovacím systému s reálnými uživateli.
- **Výhody:**
  - Nejrealističtější výsledky hodnocení.
  - Hodnocení celkového výkonu systému, včetně dlouhodobého zisku a udržení uživatelů.
- **Aplikace:**
  - Vliv algoritmů na uživatelské chování (např. počet kliknutí).
- **Metody:**
  - **Randomizované A/B Testy:** Náhodné přiřazení uživatelů k různým verzím doporučovacích systémů.
- **Výzvy:**
  - Zajištění náhodného vzorkování uživatelů.
  - Udržení konzistentních faktorů (např. jednotné UI).
  - Rizika:
    - Návrhy nesouvisejících položek během experimentu.
    - Etické otázky spojené s experimentováním na reálných uživatelích.
- **Poznámka:**
  - Online experimenty jsou často posledním krokem v hodnocení doporučovacích systémů.

---

#### **Nejlepší Praktiky v Hodnocení Doporučovacích Systémů**
1. **Offline Analytika:**
   - Používání křížové validace pro hodnocení a porovnání různých algoritmů.
2. **Studie Uživatelů:**
   - Zaznamenávání a analyzování interakcí uživatelů s doporučovacím systémem.
3. **Online Experiment:**
   - Nasazení nejvhodnějšího algoritmu a jeho hodnocení v reálném prostředí pomocí A/B testů.

---

#### **Strojové Učení Perspektiva**
- **Cíle Hodnocení:**
  - Předvídání uživatelských hodnocení pomocí strojových učebních algoritmů.
- **Metody Hodnocení:**
  - **Přesnost Předpovědí:** Měření schopnosti systému předpovídat chování uživatelů.
- **Hodnotící Metriky:**
  - **Mean Absolute Error (MAE):**
    $$
    \text{MAE}_{\text{test}} = \frac{1}{|\Omega_{\text{test}}|} \sum_{i,j \in \Omega_{\text{test}}} |r_{ij} - \hat{r}_{ij}|
    $$
  - **Root-Mean-Squared Error (RMSE):**
    $$
    \text{RMSE}_{\text{test}} = \sqrt{ \frac{1}{|\Omega_{\text{test}}|} \sum_{i,j \in \Omega_{\text{test}}} (r_{ij} - \hat{r}_{ij})^2 }
    $$
  - Kde \( |\Omega_{\text{test}}| \) je velikost testovací sady.

---

#### **Perspektiva Informačního Vyhledávání (Information Retrieval Perspective)**
- **Definice:**
  - Doporučovací systémy jsou považovány za specializovanou podmnožinu systémů informačního vyhledávání.
- **Hodnocení:**
  - Zaměření na podporu rozhodování a pořadí doporučených položek spíše než na přesnou numerickou přesnost.
- **Hlavní Metriky:**
  - **Confusion Matrix:**
    - **TP (True Positives), FP (False Positives), FN (False Negatives), TN (True Negatives)**
    - **Výpočty:**
      - **Recall (REC) / True Positive Rate (TPR):**
        $$
        \text{REC} = \text{TP} / N^+
        $$
      - **False Positive Rate (FPR):**
        $$
        \text{FPR} = \text{FP} / N^-
        $$
      - **True Negative Rate (TNR):**
        $$
        \text{TNR} = \text{TN} / N^-
        $$
      - **False Negative Rate (FNR):**
        $$
        \text{FNR} = \text{FN} / N^+
        $$
      - **Accuracy (ACC):**
        $$
        \text{ACC} = (\text{TP} + \text{TN}) / N
        $$
      - **Precision (PR):**
        $$
        \text{PR} = \text{TP} / \hat{N}^+
        $$
      - **F1-Score (F1):**
        $$
        \text{F1} = \frac{2}{\frac{1}{\text{PR}} + \frac{1}{\text{REC}}}
        $$
  - **Precision@K a Recall@K:**
    - **Precision@K:**
      $$
      \text{Precision@K} = \frac{\text{TP ve Top K}}{K}
      $$
    - **Recall@K:**
      $$
      \text{Recall@K} = \frac{\text{TP ve Top K}}{\text{Celkový počet relevantních položek v datasetu}}
      $$
  - **Normalized Discounted Cumulative Gain (NDCG):**
    - **Definice:**
      - Metrika hodnotící kvalitu řazených seznamů doporučení s ohledem na relevanci a pozici položek.
    - **Formule:**
      $$
      \text{NDCG@K} = \frac{\text{DCG@K}}{\text{IDCG@K}}
      $$
      - **DCG@K (Discounted Cumulative Gain):**
        $$
        \text{DCG@K} = \sum_{i=1}^{K} \frac{rel_i}{\log_2(i + 1)}
        $$
      - **IDCG@K (Ideal DCG):**
        $$
        \text{IDCG@K} = \sum_{i=1}^{K} \frac{rel'_i}{\log_2(i + 1)}
        $$
      - Kde \( rel'_i \) je relevance ideálního (perfektního) řazení na pozici \( i \).

---

#### **Coverage (Pokrytí)**
- **Definice:**
  - Pokrytí položek představuje podíl doporučených položek z celkového počtu dostupných položek.
- **Význam:**
  - Indikuje schopnost systému doporučovat širokou škálu položek.
- **Formule:**
  - Kde \( I \) je množina všech položek a \( |A| \) je velikost množiny \( A \).
    $$
    C = \frac{|\bigcup_{i} I(i)|}{|I|}
    $$
  - Kde \( I(i) \) je množina doporučených položek pro uživatele \( i \).

---

#### **Perspektiva Lidské Interakce**
- **Otázka:**
  - Můžeme považovat systém za dokonalý, když \( \text{NDCG} = \text{Recall} = C = 1 \)?
- **Problémy:**
  - Recommender systémy fungují v dynamických prostředích.
  - Příklad:
    - Uživatel právě koupil nový smartphone. Doporučení příslušenství by mohla být aktuálnější než doporučení dalších smartphonů.
- **Další Metriky:**
  - **Diverzita (Diversity):**
    - Opak podobnosti, zajišťuje rozmanitost doporučených položek.
    - Pomáhá předcházet tvorbě "filter bubbles".
  - **Důvěra (Trust):**
    - Úroveň důvěry uživatelů v doporučení.
    - Zvyšuje se, když doporučené položky jsou relevantní a uživatelé je oceňují.
    - Transparentní a rozumná vysvětlení zvyšují důvěru.
  - **Novost (Novelty):**
    - Doporučování neznámých nebo málo známých položek.
    - Zvyšuje se tím, že se doporučují méně populární položky.
  - **Serendipita (Serendipity):**
    - Kvalita překvapení a nepředvídatelnosti v doporučeních.
    - Přináší příjemné překvapení uživatelům s nečekanými doporučeními.

---

#### **Perspektiva Softwarového Inženýrství**
- **Klíčové Body:**
  - Doporučovací algoritmy mohou být přesné, ale příliš náročné na výpočet pro reálný čas.
  - Systémy musí být vysoce dostupné a spolehlivé.
- **Hodnotící Dimenze:**
  - **Real-Time Výkon:** Rychlost doporučování nových položek a na základě uživatelského chování.
  - **Robustnost:**
    - Schopnost systému odolávat falešným informacím a útokům.
    - Stabilita při extrémních událostech, jako je nával uživatelských požadavků.
  - **Škálovatelnost a Správa Zdroju:**
    - Efektivní využití zdrojů při rozšiřování databáze uživatelů a položek.
    - Schopnost systému udržet výkon při rostoucí velikosti datasetu.

---

#### **Perspektiva Podnikání**
- **Cíle:**
  - Úspěch v podnikání je klíčovým cílem doporučovacích systémů.
- **Podnikové Metriky Hodnocení:**
  - **Conversion Rate:** Podíl uživatelů, kteří na doporučení reagovali (např. nákup).
  - **Revenue Generation:** Přímý vliv doporučení na prodeje a příjmy.
  - **Customer Lifetime Value (CLV):** Dlouhodobá hodnota uživatelů získaných prostřednictvím doporučení.
  - **Retention Rate:** Schopnost doporučení udržet a zapojit uživatele v průběhu času.
- **Další Aspekty:**
  - Soulad doporučení s podnikatelskými cíli.
  - Uživatelské zapojení a spokojenost.

---

#### **Shrnutí**
- **Hodnocení Doporučovacích Systémů** zahrnuje různé perspektivy:
  - **Offline Analytika:** Rychlé a nákladově efektivní hodnocení algoritmů bez interakce s reálnými uživateli.
  - **Studie Uživatelů:** Detailní analýza interakce uživatelů s doporučovacími systémy.
  - **Online Experiment:** Realistické hodnocení výkonu doporučovacích systémů v reálném čase.
- **Metriky Strojového Učení:** MAE, RMSE pro hodnocení přesnosti předpovědí.
- **Metriky Informačního Vyhledávání:** Precision@K, Recall@K, NDCG@K, Coverage pro hodnocení kvality a relevance doporučení.
- **Perspektiva Lidské Interakce:** Diverzita, důvěra, novost, serendipita pro zajištění uživatelské spokojenosti a zapojení.
- **Softwarové Inženýrství:** Real-time výkon, robustnost, škálovatelnost pro technickou efektivitu a spolehlivost systému.
- **Podniková Perspektiva:** Conversion Rate, Revenue Generation, CLV, Retention Rate pro měření obchodního úspěchu doporučovacích systémů.