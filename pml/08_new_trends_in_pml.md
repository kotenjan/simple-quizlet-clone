### Personalizované Strojové Učení: Nové Trendy v PML

---

#### **Matrix Factorization (MF)**
- **Tradiční Metody:**
  - **Závislost na Interakcích Uživatel-Položka:**
    - MF rozkládá matici interakcí uživatel-položka do latentních faktorů.
  - **Optimalizační Cíl:**
    $$
    \min_{U,V} \sum_{(i,j) \in \Omega} (r_{i,j} - \mathbf{u}_i^\top \mathbf{v}_j)^2 + \lambda \left( \sum_x \|\mathbf{u}_x\|^2 + \sum_y \|\mathbf{v}_y\|^2 \right)
    $$
    - Cíl je minimalizovat rozdíl mezi pozorovanými hodnoceními \( r_{i,j} \) a predikovanými hodnoceními \( \hat{r}_{i,j} = \mathbf{u}_i^\top \mathbf{v}_j \) pro uživatele \( i \) a položku \( j \).
  - **Výhody:**
    - Velmi populární, efektivní a přesná metoda.
  - **Omezení:**
    - Tradiční MF má problémy s adaptací na nové uživatele nebo položky, zejména v dynamických prostředích.

---

#### **Inductive Matrix Factorization (IMF)**
- **Rozšíření Tradičních Metod:**
  - **Zpracování Nových Uživatelů a Položek:**
    - IMF rozšiřuje MF metody tak, aby dokázaly pracovat s novými uživateli a položkami, které nebyly přítomny během tréninku.
  - **Inkorporace Vedlejších Informací:**
    - Využívá dodatečné informace o uživatelích a položkách (např. demografické údaje, charakteristiky položek).
  - **Generalizace na Nové Případy:**
    - Umožňuje modelu generalizovat na nové uživatele a položky využitím pomocných dat během tréninku.
  - **Aplikace:**
    - Obzvláště užitečné v dynamických prostředích a nově vznikajících trzích.
  - **Zvýšení Přesnosti:**
    - Díky využití dodatečných informací může IMF zlepšit přesnost modelu pro uživatele v počáteční fázi (warm-start).

---

#### **Hybridní MF a IMF Model**
- **Komplementarita MF a IMF:**
  - **Společné Využití:**
    - MF a IMF nejsou oddělené, ale navzájem se doplňují.
  - **Abstrakce Vlastností:**
    - V ML jsou vlastnosti často abstrakcí reality. Například v predikci cen nemovitostí:
      - Cena \( p_i \) může být modelována jako plocha \( a_i \) nemovitosti krát parametr \( \omega_i \).
  - **Omezená Informace:**
    - I s kompletní sadou proměnných je stále nemožné plně predikovat.
  - **Role IMF a MF:**
    - **IMF:** Zodpovídá za extrakci příspěvku vedlejších informací k prediktoru.
    - **MF:** Pracuje na části bez vedlejších informací.
  - **Optimalizační Cíl:**
    - Kombinovat výhody obou metod pro zlepšení celkového výkonu doporučovacího systému.

---

#### **Multimodalní Doporučovací Systémy**
- **Rozšíření Tradičního Paradigmatu:**
  - **Kombinace Různých Typů Informací:**
    - Kromě uživatelsko-položkových interakcí využívají multimodalní systémy různé modality jako text, obrázky, audio a další.
  - **Výhody:**
    - **Zlepšené Porozumění Uživatelským Preferencím:** Kombinace více modalit poskytuje komplexnější pohled na preference uživatelů.
    - **Řešení Cold Start Problému:** Užitečné pro nové uživatele nebo položky s omezenou historií interakcí.
    - **Zvýšení Přesnosti Doporučení:** Využití různých zdrojů dat pomáhá zachytit jemnější zájmy uživatelů.
    - **Reálné Aplikace:** Vynikají v oblastech jako móda, umění a multimediální obsah.
  - **Implementace:**
    - Integrace různých datových modalit do jednoho modelu pro zlepšení kvality doporučení.

---

#### **Personalizované Vyhledávání (Personalized Search)**
- **Definice:**
  - Tradiční vyhledávače poskytují univerzální výsledky pro všechny uživatele.
  - Personalizované vyhledávání přizpůsobuje výsledky vyhledávání na základě informací o preferencích, chování a historii uživatele.
- **Výhody:**
  - **Zlepšená Relevance:** Uživatelé dostávají výsledky přizpůsobené jejich zájmům.
  - **Zvýšená Spokojenost Uživatelů:** Personalizace vede k uspokojivějšímu vyhledávacímu zážitku.
- **Výzvy:**
  - **Obavy o Soukromí:** Rovnováha mezi personalizací a ochranou soukromí uživatelů.
  - **Serendipita:** Udržení rovnováhy mezi relevancí a zaváděním nového obsahu.
  - **Cold Start Problém:** Výzvy při omezené historii uživatele.
- **Optimalizační Cíl:**
  - Přizpůsobit vyhledávací algoritmy tak, aby se kontinuálně zlepšovaly a adaptovaly na měnící se preference uživatelů.

---

#### **Reinforcement Learning (RL) v Doporučovacích Systémech**
- **Definice:**
  - Oblast strojového učení zaměřená na to, jak inteligentní agenti přijímají akce v dynamickém prostředí s cílem maximalizovat kumulativní odměnu.
- **Základní Setup:**
  - **Agent:** Doporučovací systém, který rozhoduje o doporučeních.
  - **Prostředí:** Dynamické prostředí uživatelů a položek.
- **Úloha RL:**
  - Vytvořit strategie (policy), které umožní agentovi učit se optimální akce pro maximalizaci odměn.
- **Příklad:**
  - **Scénář Komutace:**
    - **Agent:** Uživatel, který se snaží optimalizovat způsob dopravy.
    - **Akce:** Chůze, veřejná doprava, kolo.
    - **Odměna:** Příjezd včas (1) vs. zpoždění (0).
    - **Cíle:**
      1. Jak interagovat s prostředím pro maximalizaci počet příchodů včas.
      2. Jak by tradiční ML řešilo tento problém.
      3. Existuje nejlepší možnost?

---

#### **Exploration × Exploitation Dilemma**
- **Definice:**
  - Konflikt mezi využíváním známých informací pro dosažení vysoké odměny (exploitation) a zkoumáním nových možností pro získání více informací (exploration).
- **Příklad:**
  - **Výběr Dopravního Prostředku:**
    - **Exploitation:** Vybrat způsob dopravy, který v minulosti fungoval dobře.
    - **Exploration:** Zkoušet nové způsoby dopravy, které by mohly být efektivnější.
- **Otázky:**
  - Kdy začít využívat získané znalosti a kdy pokračovat ve zkoumání nových možností?
- **Relevance v Doporučovacích Systémech:**
  - Nabízet nové položky uživatelům pro lepší pochopení jejich preferencí vs. nabízet položky, o kterých víme, že se uživatelům líbí.

---

#### **Multi-Armed Bandit (MAB)**
- **Definice:**
  - Model představující sérii rozhodnutí mezi několika možnostmi (rameny), kde každá možnost má vlastní pravděpodobnost odměny.
- **Příklad:**
  - **Klasický Příklad:**
    - Jednoruční bandita (slot machine) má několik ramen, z nichž každé má jinou pravděpodobnost výhry.
- **Variace:**
  - **One-Armed Bandit:** Tradiční slot machine s jedním ramenem.
  - **Multi-Armed Bandit:** Slot machine s \( k \) rameny, kde každé rameno \( a_i \) má pravděpodobnost \( P(a_i) \) výhry.
- **Optimalizační Cíl:**
  - Vybrat nejlepší rameno pro maximalizaci odměny během omezeného počtu pokusů \( N \).
- **Výzvy:**
  - **Exploration vs. Exploitation:** Rozhodnout se mezi zkoumáním nových ramen nebo využíváním těch, která již přinášejí vysoké odměny.
- **Aplikace v Doporučovacích Systémech:**
  - Vybrat, zda nabídnout uživateli nové položky (explore) nebo známé populární položky (exploit).

- **Algoritmy pro MAB:**
  - **Greedy Strategy:** Vždy vybrat nejlepší známé rameno.
  - **ϵ-Greedy Strategy:** S pravděpodobností \( \epsilon \) vybrat náhodné rameno, jinak nejlepší známé.
  - **Upper Confidence Bounds (UCB):** Vybrat rameno s nejvyšší horní hranicí spolehlivosti.
  - **Thompson Sampling:** Vzorkovat z posterior distribuce pravděpodobnosti výhry a vybrat rameno s nejvyšší pravděpodobností.

---

#### **Reinforcement Learning v Doporučovacích Systémech**
- **Výzvy:**
  - **Hodnocení:** RL algoritmy jsou obtížně hodnotitelné s offline daty; často vyžadují online hodnocení.
  - **Simulace:** Pro pochopení fungování RL algoritmů se často provádějí simulace na základě offline datasetů.
- **Algoritmy:**
  - **Multi-Armed Bandits (MAB):** Jedna z základních RL technik používaných v doporučovacích systémech.
  - **Další RL Algoritmy:** Existuje široká škála RL algoritmů aplikovatelných v doporučovacích systémech.
- **Výzkumné Příležitosti:**
  - RL v doporučovacích systémech je relativně nová oblast s mnoha možnostmi pro další výzkum a inovace.

---

#### **Shrnutí**
- **Matrix Factorization (MF):** Efektivní metoda pro rozklad matic interakcí, s omezeními při práci s novými uživateli a položkami.
- **Inductive Matrix Factorization (IMF):** Rozšíření MF umožňující zpracování nových uživatelů a položek pomocí vedlejších informací.
- **Hybridní MF a IMF Model:** Kombinace MF a IMF pro zlepšení výkonu doporučovacích systémů.
- **Multimodalní Doporučovací Systémy:** Integrace různých typů datových modalit pro lepší porozumění preferencím uživatelů.
- **Personalizované Vyhledávání:** Přizpůsobení výsledků vyhledávání na základě uživatelských preferencí pro zvýšení relevance a spokojenosti.
- **Reinforcement Learning (RL) v Doporučovacích Systémech:** Použití RL a MAB pro dynamické optimalizace doporučení s ohledem na exploraci a exploitaci.
- **Exploration × Exploitation Dilemma:** Klíčový problém při rozhodování mezi využíváním známých informací a zkoumáním nových možností.
- **Multi-Armed Bandit (MAB):** Model pro řešení rozhodovacích problémů s několika možnostmi, aplikovatelný v doporučovacích systémech.
- **EM Algoritmus:** Iterativní metoda pro odhad parametrů modelů s latentními proměnnými, využitelná pro směs procesů.
- **SPoSE Model:** Model pro učení reprezentací z tripletů, zachycující latentní podobnostní struktury mezi objekty.
- **Permutational Layer:** Komponenta neuronových sítí pro zpracování vstupních sekvencí nezávisle na jejich pořadí.
