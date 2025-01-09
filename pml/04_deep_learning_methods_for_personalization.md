### Personalizované Strojové Učení: Metody Hlubokého 

---

#### **Dimenzionální Redukce (Dimensionality Reduction)**
- **Definice:**
  - Technika používaná ke snížení počtu atributů (features) v datasetu při zachování nejrelevantnějších informací.
- **Specifika datových vstupů:**
  - Různé typy dat (hudba, fotografie, text) mají jedinečné charakteristiky vyžadující specifické přístupy strojového učení.
- **Tradiční metody:**
  - **PCA (Principal Component Analysis):**
    - Může selhat při práci s daty obsahujícími nelineární vztahy.
- **Autoenkodéry:**
  - **Definice:**
    - Neřízené neuronové sítě používané pro komprimované reprezentace dat.
  - **Využití:**
    - Efektivní pro dimenzionální redukci a zpracování složitých vstupů.

---

#### **Autoenkodér (Autoencoder)**
- **Definice:**
  - Typ neuronové sítě s dopředným průchodem (feed-forward), navržený k rekonstrukci svého vstupu \( x_i \) jako výstup \( \hat{x}_i \).
- **Struktura:**
  - **Encoder (Kódovač):** Převádí vstup do latentního prostoru (bottleneck layer).
  - **Decoder (Dekodovač):** Rekonstruuje vstup z latentního prostoru.
- **Bottleneck Layer:**
  - Zahrnuje vrstvy s výrazně nižším počtem dimenzí než vstup, čímž zabraňuje triviálním řešením (např. kopírování vstupu na výstup).
- **Optimalizační Cíl:**
  - Minimalizovat rozdíl mezi vstupem a rekonstruovaným výstupem:
    $$
    \min_{E,D} \sum_{i} \|x_i - D(E(x_i))\|^2
    $$

---

#### **Struktura a Optimalizace Autoenkodérů**
- **Jednoduchý Autoenkodér:**
  - **Vrstvy:** Jedna skrytá vrstva.
  - **Ztrátová Funkce:** Čtvercová chyba (squared error loss).
  - **Optimalizační Funkce:**
    $$
    \min_{U,V} \sum_{i} \|x_i - x_i UV\|^2
    $$
  - **Pozorování:**
    - Pokud je \( k \geq m \), \( UV \neq I \), kde \( I \) je identita.
    - Pokud je \( k < m \), \( UV \neq I \), což umožňuje redukci dimenzí.
    - Pro \( k \geq m \) nedochází k redukci dimenzí, což vede k triviálnímu řešení.

---

#### **PCA × Autoenkodér**
- **Kombinace tradičních metod PCA s autoenkodéry:**
  - Zlepšuje efektivitu dimenzionální redukce.
  - Využívá výhod PCA pro lineární vztahy a autoenkodéry pro nelineární vztahy.

---

#### **Autoenkodéry pro Kolaborativní Filtraci (CF)**
- **Cíle:**
  - Kódovat interakce uživatel-položka do nižší dimenzionálního prostoru pro objevení smysluplných vzorů.
  - Aplikovatelné na explicitní i implicitní zpětnou vazbu.
  - Efektivní při práci se vzácnými daty interakcí uživatelů.
  - Vyvažování složitosti modelu a škálovatelnosti, zejména v rozsáhlých doporučovacích systémech.
  - Možnost využití transfer learningu pro zlepšení obsahově založených metod.

---

#### **Autoenkodéry pro Implicitní Zpětnou Vazbu**
- **Problém:**
  - V reálných aplikacích je více implicitní zpětné vazby než explicitní.
  - **Příklad:**
    - Uživatel sledoval 35 % filmu A a 85 % filmu B.
      - Znamená to, že uživatel má film B více rád než A?
      - Znamená to, že uživatel má film B více než dvakrát tak rád jako film A?
- **Poznámka:**
  - Tradiční metody jako výše popsané jsou vhodnější pro explicitní zpětnou vazbu, vyžadujeme tedy jiný přístup pro implicitní zpětnou vazbu.

---

#### **Modelování Implicitní Zpětné Vazby**
- **Binární Interakční Matice \( P \):**
  $$
  P =
  \begin{pmatrix}
  1 & 0 & 0 & 1 & 0 & 1 \\
  0 & 1 & 1 & 0 & 1 & 1 \\
  1 & 1 & 1 & 0 & 0 & 1 \\
  0 & 0 & 1 & 0 & 0 & 1 \\
  \end{pmatrix}
  $$
  - \( P_{ij} = 1 \) pokud uživatel \( i \) interagoval s položkou \( j \), jinak \( P_{ij} = 0 \).
- **Matice Důvěry \( C \):**
  $$
  C =
  \begin{pmatrix}
  0.85 & 0 & 0 & 0.34 & 0 & 0.98 \\
  0 & 0.37 & 0.10 & 0 & 0.63 & 0.01 \\
  0.45 & 0.42 & 0.43 & 0 & 0 & 0.23 \\
  0 & 0 & 0.26 & 0 & 0 & 0.88 \\
  \end{pmatrix}
  $$
  - \( C_{ij} \) představuje důvěryhodnost interakce mezi uživatelem \( i \) a položkou \( j \).

---

#### **Kolaborativní Filtrace pro Implicitní Zpětnou Vazbu**
- **Optimalizační Úloha:**
  $$
  \min_{U,V} \sum_{i,j} C_{ij} (P_{ij} - u_i^\top v_j)^2 + \lambda \|u_i\|^2 + \lambda \|v_j\|^2
  $$
- **Hlavní Rozdíly oproti tradiční metodě MF:**
  - Zohlednění různých úrovní důvěry (\( C_{ij} \)).
  - Optimalizace zahrnuje všechny možné páry \( (i, j) \), nikoli pouze pozorované datové body.
- **Metody Řešení:**
  - **Gradientní Sestup (Gradient Descent):** Použití gradientního sestupu k minimalizaci ztrátové funkce.
  - **Alternující Nejmenší Čtverce (ALS):** Při fixaci jedné matice optimalizovat druhou.

---

#### **Uzavřená Forma Řešení pro EASE**
- **Optimalizační Cíl:**
  $$
  L_i = \min_{u_i} \sum_{j} C_{ij} (P_{ij} - u_i^\top v_j)^2 + \lambda \|u_i\|^2
  $$
- **Transformace Ztráty:**
  $$
  L_i = \| \sqrt{C_i} P_i - \sqrt{C_i} V u_i \|^2 + \lambda \|u_i\|^2
  $$
- **Derivace Ztráty:**
  $$
  \nabla_{u_i} = -2 (\sqrt{C_i} V)^\top (\sqrt{C_i} P_i - \sqrt{C_i} V u_i) + 2 \lambda u_i
  $$
- **Řešení Uzavřené Formy:**
  $$
  u_i = (V^\top C_i V + \lambda I)^{-1} V^\top C_i P_i
  $$
- **Finalizace:**
  - **Matice \( B \):**
    $$
    B = (X^\top X + \lambda I)^{-1} (X^\top X - \text{diag}(P))
    $$
  - **Důvod Constraint \( \text{diag}(B) = 0 \):**
    - Zabraňuje triviálnímu rekonstrukci vstupu bez redukce dimenzí.

---

#### **EASE (Embarrassingly Shallow Autoencoders)**
- **Definice:**
  - Nejjednodušší autoenkodér, který řeší problém minimalizace:
    $$
    \min_B \|X - XB\|^2 + \lambda \|B\|^2 \quad \text{při} \quad \text{diag}(B) = 0
    $$
- **Důvod Constraint:**
  - Zajišťuje, že diagonální prvky matice \( B \) jsou nulové, což zabraňuje triviálnímu rekonstrukci vstupu bez redukce dimenzí.
- **Uzavřená Forma Řešení:**
  - Použití Lagrangian metody pro minimalizaci s omezením:
    $$
    B = (X^\top X + \lambda I)^{-1} (X^\top X - \text{diag}(P))
    $$
- **Výhody:**
  - Má uzavřenou formu řešení, což zvyšuje efektivitu výpočtu.
- **Otázka:**
  - Je metoda EASE dobrá?  
    *(Diskuse o efektivitě a vhodnosti metody pro různé typy dat a aplikací)*

---

#### **Mixing Implicit and Explicit Feedback**
- **Některé metody kombinují implicitní a explicitní zpětnou vazbu:**
  - **Explicitní zpětná vazba:** Hodnocení od 1 do 5 hvězdiček.
  - **Implicitní zpětná vazba:** Zda uživatel interagoval (1) nebo ne (0) se stejnou položkou.
- **Příklad:**
  - Zavedení 1x1 konvolučního autoenkodéru pro kombinaci implicitní a explicitní zpětné vazby.

---

#### **Sekvenčně založené Doporučování (Sequential-based Recommendation)**
- **Problém:**
  - V tradičních doporučovacích systémech jsou interakce uživatel-položka považovány za nezávislé.
- **Řešení:**
  - Modely sekvenčního doporučování zohledňují pořadí a časování uživatelských interakcí.
- **Aplikace:**
  - Doporučování produktů v e-commerce sezení.
  - Navrhování následujícího filmu nebo videa v uživatelově historii sledování.
  - Personalizace obsahu v doporučovacích systémech novinek a článků.
- **Výhody:**
  - Využívá sekvenční vzory, časové dynamiky a uživatelské chování pro přesnější a kontextově uvědomělé doporučení.

---

#### **Shrnutí**
- **Autoenkodéry** jsou efektivní nástroje pro dimenzionální redukci, zvláště při práci s nelineárními daty.
- **EASE** představuje zjednodušenou verzi autoenkodérů s uzavřenou formou řešení, která je efektivní pro kolaborativní filtraci.
- **Implicitní Zpětná Vazba:** Vyžaduje specifické metody modelování, které zohledňují důvěryhodnost interakcí a práci s vzácnými daty.
- **Optimalizační Metody:** ALS a gradientní sestup jsou klíčové pro nalezení optimálních matic \( U \) a \( V \).
- **Sekvenčně založené Doporučování:** Zlepšuje přesnost a relevanci doporučení tím, že bere v úvahu pořadí a časování uživatelských akcí.
