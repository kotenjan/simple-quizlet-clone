### Personalizované Strojové Učení: Časová Dynamika a Popularita

---

#### **Hodnocení Doporučovacích Systémů**

---

#### **Hodit Mince (Tossing a Coin)**
- **Populární Metoda:**
  - Házení mince je celosvětově oblíbená metoda pro binární rozhodování.
- **Pravděpodobnost Výsledků:**
  - Pravděpodobnost získání hlavy (head) a orla (tail) u férové mince je \( P(\text{head}) = P(\text{tail}) = \frac{1}{2} \).
- **Příklad:**
  - Pokud hodíme férovou minci 100krát a 70krát padne hlava, jaká je pravděpodobnost, že při dalším hodu padne orel?
- **Diskuse:**
  - Možná je třeba přehodnotit, zda \( P(\text{head}) = P(\text{tail}) = \frac{1}{2} \).

---

#### **Časová Dynamika a Popularita**

---

#### **Časová Dynamika v Recommender Systémech**
- **Problém:**
  - Většina případů je obtížné určit, zda je mince skutečně férová.
  - Pravděpodobnost nalezení skutečně férové mince je velmi nízká.
- **Pozorování:**
  - Mnoho mincí má pravděpodobnosti takové, že \( P(\text{head}) \approx P(\text{tail}) \approx \frac{1}{2} \).
- **Příklad:**
  - Pokud máme férovou minci a po 100 hodech padlo 70krát hlava, je pravděpodobné, že \( P(\text{head}) = P(\text{tail}) = \frac{1}{2} \)?
  - Lze odhadnout nejpravděpodobnější hodnoty \( P(\text{head}) \) a \( P(\text{tail}) \)?

---

#### **Maximální Pravděpodobnostní Odhad (Maximum Likelihood Estimation)**
- **Formální Definice:**
  - \( Y_i \) je náhodná proměnná reprezentující \( i \)-tý hod mince.
    - \( Y_i = 1 \) indikující hlavu.
    - \( Y_i = 0 \) indikující orla.
  - \( P(Y_i = 1) = p \), \( P(Y_i = 0) = 1 - p \).
- **Pozorování:**
  - Sekvence hodů: \( Y_1, Y_2, \ldots, Y_{100} \) s 70 hlavy a 30 orlů.
- **Optimalizační Problém:**
  - Najít hodnotu \( p \), která maximalizuje pravděpodobnost:
    $$
    L(p) = p^{70} (1 - p)^{30}
    $$
- **Logaritmická Transformace:**
  - \( \ln L(p) = 70 \ln p + 30 \ln (1 - p) \)
- **Derivace a Řešení:**
  - Derivace: \( \ell'(p) = \frac{70}{p} - \frac{30}{1 - p} \)
  - Nastavení derivace na nulu:
    $$
    0 = \frac{70}{p} - \frac{30}{1 - p} \Rightarrow 100p = 70 \Rightarrow p = 0.70
    $$
  - **Nejpravděpodobnější hodnota \( p \) je 0.70.**

---

#### **Popularita v Doporučovacích Systémech**
- **Definice:**
  - Popularita odkazuje na relativní frekvenci položek mezi uživateli.
- **Měření Popularity:**
  - Počet/zastoupení zhlédnutí, hodnocení nebo nákupů.
- **Význam:**
  - Porozumění popularitě je klíčové pro vytváření efektivních doporučovacích algoritmů.

---

#### **Variabilita Popularity**
- **Výzkum:**
  - Popularita online položek se liší mezi:
    - Klidnými (normálními) obdobími.
    - Velkými sekvencemi událostí (návaly událostí).
- **Modelování Publikum:**
  - **Stabilní Publikum:** Odpovědné za klidná období.
  - **Zvědavé Publikum:** Odpovědné za návaly událostí.

---

#### **Stabilní vs. Zvědavé Publikum**
- **Zvědavost:**
  - Těžko měřitelná, návaly událostí jsou nepředvídatelné a s různou intenzitou.
  - Zvláštní zájem na rychlost událostí stabilního publika.
- **Cíl:**
  - Recommender systémy by měly rozpoznat, zda je položka ve stabilním nebo zvědavém režimu.

---

#### **Bodové Procesy (Point Processes)**
- **Definice:**
  - Matematický model pro náhodné události v čase nebo prostoru.
- **Komponenty:**
  - **Intenzitní Funkce (\( \lambda(t) \)):** Popisuje míru výskytu událostí.
  - Události mohou být závislé nebo nezávislé.

---

#### **Intenzitní Funkce**
- **Definice:**
  - Pro bodový proces s časy událostí \( T = \{t_1, t_2, \ldots, t_n\} \).
  - \( N(t) \) je počet událostí do času \( t \).
  - Intenzitní funkce:
    $$
    \lambda(t) = \lim_{\Delta t \to 0} \frac{E[N(t + \Delta t) - N(t)]}{\Delta t}
    $$

---

#### **Poissonův Proces**
- **Charakteristiky:**
  - **Homogenita:** Míra událostí je konstantní \( \lambda(t) = \lambda_P \).
  - **Paměťovost:** Čas do další události následuje exponenciální rozdělení, nemá paměť minulosti.
- **Aplikace:**
  - Modelování náhodných událostí jako příjezdy do služby, radioaktivní rozpad apod.
- **Vlastnosti:**
  - \( E[N(t + 1) - N(t)] = \lambda \) pro každou pevnou jednotku času.

---

#### **Odhad Poissonova Procesu**
- **Cíl:**
  - Najít nejpravděpodobnější hodnotu \( \lambda \).
- **Log-likelihood Funkce:**
  $$
  \ell(\lambda) = n \ln \lambda_P - \lambda_P T
  $$
- **Maximalizace:**
  - Derivace: \( \ell'(\lambda) = \frac{n}{\lambda_P} - T = 0 \)
  - Řešení: \( \lambda_P = \frac{n}{T} \)

---

#### **Zvědavé Publikum a SFP (Self-Feeding Process)**
- **Problém:**
  - Poissonův proces není vhodný pro modelování zvědavého publika kvůli nepředvídatelnosti a variabilitě událostí.
- **Řešení:**
  - Modelování zvědavého publika pomocí SFP.
- **SFP Intenzitní Funkce:**
  $$
  \lambda_S(t|H) =
  \begin{cases}
  \mu & \text{pokud } t \leq t_1, \\
  \frac{1}{t_1} + \mu e & \text{pokud } t_1 < t \leq t_2, \\
  \frac{1}{\Delta t} + \mu e & \text{jinak},
  \end{cases}
  $$
  - Kde \( \Delta t \) je rozdíl mezi posledními dvěma událostmi před \( t \).

---

#### **EM Algoritmus pro Směs Procesů (PP + SFP)**
- **Definice:**
  - EM Algoritmus je iterativní metoda pro odhad parametrů modelů s latentními proměnnými.
- **Kroky:**
  1. **Inicializace:**
     - Náhodně nastavit \( Z^{(0)} \), \( \lambda_P \) a \( \mu \). Nastavit \( N > 0 \).
  2. **Iterace do Konvergence:**
     - **E-Krok:**
       - Aktualizovat \( Z^{(j)} \) na základě předchozích hodnot.
       - Pro každého \( j \) vzorkovat \( Z^{(j)}_i \) z Bernoulli rozdělení:
         $$
         Z^{(j)}_i \sim \text{Bernoulli}\left(\frac{L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=1)}{L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=0) + L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=1)}\right)
         $$
     - **M-Krok:**
       - Odhadnout parametry \( \lambda_P \) a \( \mu \):
         $$
         \lambda_P = \frac{\sum_j (1 - z^{(j)}_i)}{T N}
         $$
         $$
         \mu = \text{Median}(\Delta T | Z^{(j)})
         $$
- **Poznámka:**
  - \( Z_{-i} \) představuje všechny \( z \) kromě \( z_i \).
  - Likelihood funkce pro směs:
    $$
    L(\lambda_P, \mu, Z) = \prod_{i=1}^n \lambda_S(t_i|H)^{z_i} \lambda_P^{1 - z_i} e^{-\int_0^T (\lambda_S(t|H) + \lambda_P) dt}
    $$

---

#### **Observace**
- **Modely:**
  - Definovali jsme modely pro stabilní (PP) a zvědavé (SFP) publikum.
- **Cíl:**
  - Na základě časové série \( T = \{t_1, t_2, \ldots, t_n\} \) určit parametry \( \lambda_P \) a \( \mu \).
- **Problém:**
  - Pozorujeme pouze smíšený proces \( T = \{t_1, t_2, \ldots, t_n\} \), nikoli jednotlivé procesy.
- **Latentní Proměnné:**
  - \( z_i \in \{0, 1\} \) označují, zda událost pochází ze stabilního (PP) nebo zvědavého (SFP) procesu.

---

#### **Popularita v Doporučovacích Systémech**
- **Definice:**
  - Popularita označuje, jak často jsou položky doporučovány mezi uživateli.
- **Měření:**
  - Počet zhlédnutí, hodnocení nebo nákupů.
- **Variabilita Popularity:**
  - Popularita se může měnit mezi klidnými obdobími a návaly událostí.
- **Publikum:**
  - **Stabilní Publikum:** Odpovědné za klidná období.
  - **Zvědavé Publikum:** Odpovědné za návaly událostí.

---

#### **Maximum Likelihood Estimation (MLE) pro Poissonův Proces**
- **Cíl:**
  - Najít nejpravděpodobnější hodnotu parametru \( \lambda \) pro Poissonův proces.
- **Log-likelihood Funkce:**
  $$
  \ell(\lambda) = n \ln \lambda_P - \lambda_P T
  $$
- **Odhad:**
  - Derivace \( \ell'(\lambda) = \frac{n}{\lambda_P} - T = 0 \)
  - Řešení: \( \lambda_P = \frac{n}{T} \)

---

#### **Formální Definice Bodových Procesů**
- **Náhodné Události:**
  - Události mohou být diskrétní nebo kontinuální.
- **Intenzitní Funkce (\( \lambda(t) \)):**
  - Popisuje míru výskytu událostí v čase.

---

#### **SFP Intenzitní Funkce (Self-Feeding Process)**
- **Definice:**
  - Intenzitní funkce pro SFP je definována jako:
    $$
    \lambda_S(t|H) =
    \begin{cases}
    \mu & \text{pokud } t \leq t_1, \\
    \frac{1}{t_1} + \mu e & \text{pokud } t_1 < t \leq t_2, \\
    \frac{1}{\Delta t} + \mu e & \text{jinak},
    \end{cases}
    $$
  - Kde \( \Delta t \) je rozdíl mezi posledními dvěma událostmi před \( t \).

---

#### **EM Algoritmus pro Směs Procesů (PP + SFP)**
- **Kroky:**
  1. **Inicializace:**
     - Náhodně nastavit \( Z^{(0)} \), \( \lambda_P \) a \( \mu \).
  2. **Iterace:**
     - **E-Krok:**
       - Aktualizovat latentní proměnné \( Z \) na základě aktuálních odhadů.
     - **M-Krok:**
       - Odhadnout parametry \( \lambda_P \) a \( \mu \) na základě aktualizovaných latentních proměnných.
- **Odhad Parametrů:**
  - \( \lambda_P = \frac{\sum_j (1 - z^{(j)}_i)}{T N} \)
  - \( \mu = \text{Median}(\Delta T | Z^{(j)}) \)

---

#### **Poznámky**
- **Stabilní Publikum:** Modelováno pomocí Poissonova procesu.
- **Zvědavé Publikum:** Modelováno pomocí SFP.
- **Cíl:** Na základě pozorovaného smíšeného procesu odhadnout parametry obou procesů.
- **Latentní Proměnné:** \( Z = \{z_1, z_2, \ldots, z_n\} \) označují, ke kterému procesu událost patří.

---

#### **Shrnutí**
- **Bodové Procesy:** Používány k modelování časových událostí v recommender systémech.
- **Poissonův Proces:** Vhodný pro stabilní publikum s konstantní intenzitou.
- **SFP:** Vhodný pro zvědavé publikum s variabilní intenzitou událostí.
- **EM Algoritmus:** Efektivní metoda pro odhad parametrů směsi procesů s latentními proměnnými.
- **Popularita:** Klíčová pro doporučovací systémy, měří se různými metrikami jako počet zhlédnutí, hodnocení nebo nákupů.
- **Diverzita a Robustnost:** Zajišťují, že recommender systémy jsou efektivní, spolehlivé a odolné proti nepředvídatelným událostem.
