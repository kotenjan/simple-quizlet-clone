### Personalizované Strojové Učení: Invariantní Modely

---

#### **Bias v Doporučovacích Systémech**
- **Zranitelnost:**
  - Doporučovací systémy jsou náchylné k různým typům zkreslení, které ovlivňují spravedlnost a přesnost.
- **Typy Zkreslení:**
  - **Uživatelské Zkreslení:** Preferování určitých uživatelů nad jinými.
  - **Položkové Zkreslení:** Preferování určitých položek nad ostatními.
  - **Demografické Zkreslení:** Nepřiměřené zastoupení demografických skupin.
- **Výzvy:**
  - **Nespravedlivé Zacházení:** Některým uživatelům nebo položkám může být systémově nedostatečně doporučováno.
  - **Omezená Diverzita:** Doporučení mohou být příliš podobná, což snižuje rozmanitost.
  - **Posilování Stereotypů:** Systémy mohou nepovědomě posilovat existující stereotypy.
- **Position Bias:**
  - Tendence upřednostňovat položky v prominentních pozicích, čímž se zvyšuje viditelnost populárních položek.
  - **Poznámky:**
    - Recommender systémy mohou být naprogramovány tak, aby některé položky zobrazovaly na prvních pozicích.
    - Modely se často snaží „zkreslit“ doporučení tím, že relevantnější položky umístí na přední místa.
    - Některé algoritmy Personalizovaného Strojového Učení (PML) se zaměřují právě na tento aspekt.

---

#### **Invariantní Modely**
- **Definice:**
  - Modely, které vykazují invarianci vůči určitým transformacím vstupu, což znamená, že jejich výstup se nemění, když jsou vstupy transformovány specifickým způsobem.
- **Typy Invariance:**
  - **Domain Invariance:**
    - Například Graph Neural Networks (GNNs) používané v kolaborativní filtraci modelují interakce uživatel-položka jako graf.
    - GNNs zachytávají interakce nezávisle na jejich doméně.
  - **Time Invariance:**
    - Předpoklad, že model není ovlivněn časem.
    - Například pořadí, ve kterém uživatelé hodnotí položky, není zohledňováno při hodnocení jejich preferencí.
  - **Permutation-Equivariant Models:**
    - Modely, které jsou ekvivariantní vůči permutacím vstupních prvků.
    - Zpracovávají vstupy bez ohledu na jejich původní pořadí, což zlepšuje pochopení vztahů mezi prvky.
    - Užitečné pro úlohy, kde pořadí prvků by nemělo ovlivňovat predikce, například při klasifikaci množin nebo grafů.

---

#### **Odd-One-Out Problem**
- **Definice:**
  - Problém identifikace položky, která nepatří k danému souboru, často použitý v doporučovacích systémech.
- **Tradicionalní Přístup:**
  - Předvídání uživatelských volb pro určení, která položka je nejpravděpodobněji kliknutelná z daného seznamu.
- **Triplet Problem:**
  - **Definice:**
    - Prezentace tří obrázků \( I_a, I_b, I_c \) jednotlivci.
    - Úkolem je předpovědět, která dvojice obrázků vykazuje nejbližší konceptuální podobnost na základě daných možností.
  - **Cíle:**
    - Vyvinout modely schopné předpovídat podobnost v nových tripletech.
    - Vytvářet embeddingy, které zachycují, jak lidé vnímají a rozumějí konceptuálním vztahům.

---

#### **Maximální Pravděpodobnostní Odhad (Maximum Likelihood Estimation - MLE)**
- **Formální Definice:**
  - **Proměnné:**
    - \( Y_i \): Náhodná proměnná reprezentující \( i \)-tý hod mince.
      - \( Y_i = 1 \): Hlava.
      - \( Y_i = 0 \): Orel.
    - \( P(Y_i = 1) = p \), \( P(Y_i = 0) = 1 - p \).
  - **Pozorování:**
    - Sekvence hodů: \( Y_1, Y_2, \ldots, Y_{100} \) s 70 hlavy a 30 orlů.
  - **Pravděpodobnostní Funkce:**
    $$
    L(p) = p^{70} (1 - p)^{30}
    $$
  - **Log-likelihood:**
    $$
    \ln L(p) = 70 \ln p + 30 \ln (1 - p)
    $$
  - **Derivace a Řešení:**
    - Derivace log-likelihood:
      $$
      \ell'(p) = \frac{70}{p} - \frac{30}{1 - p}
      $$
    - Nastavení derivace na nulu:
      $$
      0 = \frac{70}{p} - \frac{30}{1 - p} \Rightarrow 100p = 70 \Rightarrow p = 0.70
      $$
    - **Nejpravděpodobnější hodnota \( p \) je 0.70.**

---

#### **Popularita v Doporučovacích Systémech**
- **Definice:**
  - Relativní frekvence položek mezi uživateli.
- **Měření Popularity:**
  - Počet zhlédnutí, hodnocení nebo nákupů položek.
- **Význam:**
  - Porozumění popularitě je klíčové pro vytváření efektivních doporučovacích algoritmů.
- **Variabilita Popularity:**
  - Popularita online položek se liší mezi:
    - **Klidnými (normálními) obdobími.**
    - **Velkými sekvencemi událostí (návaly událostí).**
- **Modelování Publikum:**
  - **Stabilní Publikum:**
    - Odpovědné za klidná období.
    - Modelováno pomocí Poissonova procesu (PP).
  - **Zvědavé Publikum:**
    - Odpovědné za návaly událostí.
    - Modelováno pomocí Self-Feeding Process (SFP).

---

#### **Bodové Procesy (Point Processes)**
- **Definice:**
  - Matematický model pro náhodné události v čase nebo prostoru.
- **Komponenty:**
  - **Intenzitní Funkce (\( \lambda(t) \)):**
    - Popisuje míru výskytu událostí v čase.
  - **Vlastnosti Událostí:**
    - Může být diskrétní nebo kontinuální.
    - Události mohou být závislé nebo nezávislé.

---

#### **Intenzitní Funkce**
- **Formální Definice:**
  - Pro bodový proces s časy událostí \( T = \{t_1, t_2, \ldots, t_n\} \).
  - \( N(t) \): Počet událostí do času \( t \).
  - Intenzitní funkce:
    $$
    \lambda(t) = \lim_{\Delta t \to 0} \frac{E[N(t + \Delta t) - N(t)]}{\Delta t}
    $$

---

#### **Poissonův Proces**
- **Charakteristiky:**
  - **Homogenita:** Míra událostí je konstantní \( \lambda(t) = \lambda_P \).
  - **Paměťovost:** Čas do další události následuje exponenciální rozdělení, což znamená, že nemá paměť minulosti.
- **Aplikace:**
  - Modelování náhodných událostí, jako jsou příjezdy do služby, radioaktivní rozpad apod.
- **Vlastnosti:**
  - \( E[N(t + 1) - N(t)] = \lambda \) pro každou pevnou jednotku času.
  - **Poznámka:**
    - Konstantní \( \lambda \) neimplikuje pravidelnost v časových intervalech.
    - Například při \( \lambda = 1 \) můžeme mít 10 událostí v 10 jednotkách času, ale jejich skutečné časy se mohou lišit.

---

#### **Odhad Poissonova Procesu**
- **Cíl:**
  - Najít nejpravděpodobnější hodnotu parametru \( \lambda \).
- **Log-likelihood Funkce:**
  $$
  \ell(\lambda) = n \ln \lambda_P - \lambda_P T
  $$
- **Odhad:**
  - Derivace log-likelihood:
    $$
    \ell'(\lambda) = \frac{n}{\lambda_P} - T = 0 \Rightarrow \lambda_P = \frac{n}{T}
    $$

---

#### **Zvědavé Publikum a Self-Feeding Process (SFP)**
- **Problém:**
  - Poissonův proces není vhodný pro modelování zvědavého publika kvůli nepředvídatelnosti a variabilitě událostí.
- **Řešení:**
  - Modelování zvědavého publika pomocí Self-Feeding Process (SFP).
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
  - Expectation-Maximization (EM) algoritmus je iterativní metoda pro odhad parametrů modelů s latentními nebo chybějícími daty.
- **Kroky:**
  1. **Inicializace:**
     - Náhodně nastavit počáteční hodnoty \( Z^{(0)} \), \( \lambda_P \) a \( \mu \).
     - Nastavit počet iterací \( N > 0 \).
  2. **Iterace do Konvergence:**
     - **E-Krok (Expectation Step):**
       - Aktualizovat všechny \( Z^{(j)} \) na základě předchozích hodnot.
       - Pro každého \( j \) vzorkovat \( Z^{(j)}_i \) z Bernoulli rozdělení:
         $$
         Z^{(j)}_i \sim \text{Bernoulli}\left(\frac{L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=1)}{L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=0) + L(\lambda_P, \mu, Z^{(j)}_{-i}, z_i=1)}\right)
         $$
     - **M-Krok (Maximization Step):**
       - Odhadnout parametry \( \lambda_P \) a \( \mu \):
         $$
         \lambda_P = \frac{\sum_j (1 - z^{(j)}_i)}{T N}
         $$
         $$
         \mu = \text{Median}(\Delta T | Z^{(j)})
         $$
- **Poznámky:**
  - \( Z_{-i} \) představuje všechny \( z \) kromě \( z_i \).
  - Likelihood funkce pro směs:
    $$
    L(\lambda_P, \mu, Z) = \prod_{i=1}^n \lambda_S(t_i|H)^{z_i} \lambda_P^{1 - z_i} e^{-\int_0^T (\lambda_S(t|H) + \lambda_P) dt}
    $$

---

#### **SPoSE (Sparse Positive Similarity Embedding)**
- **Definice:**
  - Model vyvinutý k učení individuálních reprezentací z tripletů.
  - Akronym pro Sparse Positive Similarity Embedding.
- **Cíle:**
  - Predikce latentní podobnostní struktury mezi objekty.
  - Zachycení většiny vysvětlitelné variance v lidských behaviorálních hodnoceních.
- **Funkce Podobnosti:**
  - \( S(a, b) \): Funkce reprezentující podobnost mezi položkami \( a \) a \( b \).
  - Pravděpodobnost dvojic:
    $$
    P(x_1, x_2) = \frac{e^{S(x_1, x_2)}}{e^{S(x_1, x_2)} + e^{S(x_1, x_3)} + e^{S(x_2, x_3)}}
    $$
- **Metriky:**
  - **Metody Výpočtu Podobnosti:**
    - **Euclidean Distance:** Tradiční metoda měření vzdálenosti mezi vektory.
    - **Cosine Similarity:** Měřítko podobnosti založené na úhlu mezi vektory.
    - **Výsledky:** Cosine similarity je experimentálně efektivnější.
- **Optimalizační Cíl:**
  - Minimalizovat následující funkci:
    $$
    \text{argmin}_{x_j} \sum_{i=1}^n \log \frac{e^{x_{a_i,1}^\top x_{a_i,2}}}{e^{x_{a_i,1}^\top x_{a_i,2}} + e^{x_{a_i,1}^\top x_{a_i,3}} + e^{x_{a_i,2}^\top x_{a_i,3}}}} + \lambda \sum_{j} \|x_j\|_1
    $$

---

#### **Permutational Layer**
- **Definice:**
  - Komponenta neuronových sítí pro zpracování vstupních sekvencí proměnné délky.
- **Funkce:**
  - Zpracovává permutace vstupních prvků, což umožňuje modelu zvládnout různé pořadí sekvencí.
  - Extrahuje rysy nezávisle na původních pozicích, čímž zlepšuje pochopení vztahů mezi prvky.
- **Užití:**
  - Užitečné v úlohách, kde pořadí prvků by nemělo ovlivňovat predikce, například při klasifikaci množin nebo grafů.
  - Často aplikováno v úlohách klasifikace množin, kde jsou predikce založeny na vlastnostech množiny spíše než na pořadí prvků.

---

#### **Shrnutí**
- **Bias v Doporučovacích Systémech:**
  - Doporučovací systémy mohou být ovlivněny různými typy zkreslení, což ovlivňuje jejich spravedlnost a přesnost.
  - Je důležité identifikovat a minimalizovat tyto zkreslení pro zajištění spravedlivých a přesných doporučení.
- **Invariantní Modely:**
  - Modely, které jsou nezávislé na určitých transformacích vstupu, což zvyšuje jejich robustnost a flexibilitu.
  - Zahrnují domain invariance, time invariance a permutation-equivariant models.
- **Odd-One-Out Problem a Triplet Problem:**
  - Úloha identifikace položky, která nepatří k danému souboru.
  - Triplet problem zahrnuje predikci podobnosti mezi dvojicemi položek na základě tripletů.
- **SPoSE:**
  - Model pro učení reprezentací z tripletů, který zachycuje latentní podobnostní struktury mezi objekty.
  - Využívá cosine similarity pro efektivnější měření podobnosti.
- **EM Algoritmus:**
  - Iterativní metoda pro odhad parametrů modelů s latentními proměnnými.
  - Použitý pro směs procesů (PP + SFP) k odhadu parametrů stabilního a zvědavého publika.
- **Permutational Layer:**
  - Umožňuje neuronovým sítím zpracovávat vstupy nezávisle na jejich pořadí.
  - Zlepšuje pochopení vztahů mezi prvky ve vstupních datech.
- **Popularita a Časová Dynamika:**
  - Popularita položek se může lišit v čase, což ovlivňuje doporučovací algoritmy.
  - Modelování stabilního a zvědavého publika pomáhá lépe porozumět variabilitě popularity.
