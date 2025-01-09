### Personalizované Strojové Učení: Matice Faktorizace

---

#### **Matice Faktorizace (Matrix Factorization)**
- **Definice:**
  - Matice faktorizace je jeden z hlavních algoritmů Personalizovaného Strojového Učení (PML).
  - Cíle mohou být uloženy v cílové matici \( R \) s rozměry \( m \times n \) a prvky z \( \mathbb{R} \).
- **Příklad:**
  - Pro doporučovací systémy může cílová matice \( R \) (hodnotící matice) s \( m = 4 \) uživateli a \( n = 6 \) položkami vypadat takto:
    $$
    R =
    \begin{pmatrix}
    1 & 4 & 3 & 2 & 2 & 1 \\
    3 & 2 & 3 & 4 & 2 & 1 \\
    1 & 5 & 5 & 5 & 3 & 5 \\
    2 & 1 & 2 & 3 & 3 & 3 \\
    \end{pmatrix}
    $$
  - **Interpretace:**
    - Např. uživatel \( u_3 \) ohodnotil položku \( i_1 \) s 1 hvězdičkou, položky \( i_2 \), \( i_3 \), \( i_4 \) a \( i_6 \) s 5 hvězdičkami, a položku \( i_5 \) s 3 hvězdičkami.
- **Poznámka:**
  - V reálných aplikacích nejsou všechny prvky matice \( R \) plně známé.

---

#### **Myšlenka Matice Faktorizace**
- **Definice:**
  - Matice faktorizace znamená vyjádření dané matice \( R \) jako součin dvou matic. Např.:
    $$
    R = UV^\top
    $$
- **Využití:**
  - Metody matice faktorizace jsou základním kamenem mnoha algoritmů a používají se k dosažení numericky stabilnějších výpočtů.

---

#### **Intuice Matice Faktorizace**
- **Základní Idea:**
  - Nízkodimenzionální aproximace vstupní matice \( R \) s rozměry \( m \times n \) vychází z faktu z lineární algebry:
    - Násobením matic \( U \in \mathbb{R}^{m \times d} \) a \( V \in \mathbb{R}^{d \times n} \) vznikne matice nízkého řádu s rozměry \( m \times n \).
    - Tento součin je možný pro jakékoliv kladné celé číslo \( d \) a matice \( R \) bude mít nízký řád pro \( d < \min(m, n) \).
- **Optimalizace:**
  - Cílem je najít nižší dimenzionální matice \( U \) a \( V \) tak, aby známé prvky matice \( R \) byly dobře aproximovány součinem \( UV^\top \).

---

#### **Řád Matice (Rank of a Matrix)**
- **Definice:**
  - Řád matice je počet lineárně nezávislých sloupců, které obsahuje.
  - Alternativně lze řád definovat jako počet nenulových singulárních hodnot matice.
- **Vlastnosti:**
  - \( \text{rank}(A) = \text{rank}(A^\top) \).
  - Pokud \( m \geq n \), matice \( A \) je plného řádu, pokud \( \text{rank}(A) = n \). V tomto případě je \( n \) také maximální možný řád.
  - Pro matice, kde \( m = n \), existuje inverzní matice \( A^{-1} \) pouze pokud je \( A \) plného řádu.
  - Matice je nazývána nízkého řádu (low rank) nebo řádu deficitu (rank deficient), pokud nemá plný řád.

---

#### **Singulární Hodnotová Decompozice (SVD)**
- **Definice:**
  - SVD je metoda rozkladu matice na součin tří matic, což umožňuje získat nejlepší nízkorozměrnou aproximaci původní matice.
- **Formule:**
  - Pokud \( A \in \mathbb{R}^{m \times n} \) má řád \( r \), pak nejlepší aproximace řádu \( k \) je:
    $$
    A_k = \sum_{i=1}^{k} d_i u_i v_i^\top
    $$
    - Kde \( d_1 \geq d_2 \geq \dots \geq d_k > 0 \) jsou singulární hodnoty matice \( A \).
    - \( u_i \) a \( v_i \) jsou odpovídající levé a pravé singulární vektory.

---

#### **Predikce pomocí Matice Faktorizace**
- **Reprezentace doporučovacího systému:**
  - Hodnocení jsou uložena v matici \( R \) s rozměry \( m \times n \), kde \( m \) je počet uživatelů a \( n \) počet položek.
  - Prvky \( R \) mohou být z \( \mathbb{R} \cup \{?\} \), kde \( ? \) značí neznámé hodnocení.
- **Cíl:**
  - Předpovědět neznámá hodnocení \( r_{u,i} = ? \) pomocí známých hodnocení \( r_{u,i} \neq ? \).

---

#### **Matice Faktorizace pro Doporučovací Systémy**
- **Notace:**
  - \( U \): Matice uživatelů, kde \( U \in \mathbb{R}^{m \times d} \).
  - \( V \): Matice položek, kde \( V \in \mathbb{R}^{n \times d} \).
  - \( \Omega \): Množina uživatelsky-položkových párů \( (i, j) \), kde \( r_{i,j} \) je známé.
- **Aproximace:**
  - Přiblížení \( r_{i,j} \) je dáno skalárním součinem řádku \( u_i \) z \( U \) a řádku \( v_j \) z \( V \):
    $$
    \hat{r}_{i,j} = u_i^\top v_j
    $$
  - \( d \) je horní hranice pro řád matice.

---

#### **Optimalizační Problém**
- **Metrika chyby:**
  - Chyba aproximace se měří pomocí čtvercových reziduí:
    $$
    (r_{i,j} - u_i^\top v_j)^2
    $$
- **Cíl:**
  - Najít matice \( U \) a \( V \) minimalizující:
    $$
    \min_{U,V} \sum_{(i,j) \in \Omega} (r_{i,j} - u_i^\top v_j)^2 + \lambda \left( \sum_x \|u_x\|^2 + \sum_y \|v_y\|^2 \right)
    $$
  - Kde \( \lambda \) je regulační konstanta.

---

#### **Řešení Optimalizačního Problému**
- **Metoda Alternujícího Nejmenších Čtverců (ALS):**
  - Postupně fixujeme matici \( U \) nebo \( V \) a optimalizujeme druhou matici.
  - Při fixaci jedné matice se optimalizační problém stává konvexním a podobným lineární regresi.
- **Kroky ALS:**
  1. Náhodně inicializujte \( U \) a \( V \).
  2. Opakujte dokud nedojde ke konvergenci:
     - Pro každý uživatel \( i \):
       $$
       u_i = (V^\top C_i V + \lambda I)^{-1} V^\top C_i P_i
       $$
     - Pro každou položku \( j \):
       $$
       v_j = (U^\top C_j U + \lambda I)^{-1} U^\top C_j P_j
       $$

---

#### **Sparsita a Predikce**
- **Problém:**
  - Matice \( U \) a \( V \) jsou optimalizovány pouze na základě známých prvků matice \( R \), které jsou obvykle jen malou částí všech prvků.
- **Příklad:**
  - V soutěži Netflix Prize z roku 2006 bylo \( n = 17 \) tisíc filmů a \( m = 500 \) tisíc uživatelů, což dává matici \( R \) s 8,5 miliardami prvků. Netflix poskytl pouze 100 milionů známých hodnocení.
- **Výsledek:**
  - Součin \( UV^\top \) vytváří matici stejného rozměru jako \( R \) se všemi známými i neznámými prvky.
  - Neznámé hodnocení \( r_{i,j} = ? \) je odhadnuto jako:
    $$
    \hat{r}_{i,j} = u_i^\top v_j
    $$

---

#### **Příklad Matice Faktorizace**
- **Hodnotící matice:**
  $$
  R =
  \begin{pmatrix}
  1 & ? & ? & 2 & ? & 1 \\
  ? & 2 & 3 & ? & 2 & 1 \\
  1 & 5 & 5 & ? & ? & 5 \\
  ? & ? & 2 & ? & ? & 3 \\
  \end{pmatrix}
  $$
- **Hyperparametr:**
  - \( d = 2 \) (dimenzionalita faktorů)
- **Optimalizované matice:**
  $$
  U =
  \begin{pmatrix}
  0.3 & 0.7 \\
  0.3 & 0.5 \\
  0.2 & 0.4 \\
  0.2 & 0.1 \\
  \end{pmatrix}, \quad
  V^\top =
  \begin{pmatrix}
  1 & 10 & 11 & 10 & 4 & 20 \\
  1 & -1 & -2 & -1 & 1 & -4 \\
  \end{pmatrix}
  $$
- **Aproximace:**
  $$
  UV^\top =
  \begin{pmatrix}
  1 & 2.3 & 1.9 & 2.3 & 1.9 & 3.2 \\
  0.8 & 2.5 & 2.3 & 2.5 & 1.7 & 4 \\
  0.6 & 1.6 & 1.4 & 1.6 & 1.2 & 2.4 \\
  0.3 & 1.9 & 2 & 1.9 & 0.9 & 3.6 \\
  \end{pmatrix}
  $$
  - **Poznámka:** Červené čísla jsou požadované predikce.
  - Např. predikované hodnocení uživatele 3 pro položku 4 je \( \hat{r}_{3,4} = 1.6 \).

---

#### **Supervised Learning Úloha**
- **Parametry učení:**
  - \( U \in \mathbb{R}^{m \times d} \) a \( V \in \mathbb{R}^{n \times d} \)
- **Hyperparametry:**
  - Regulační konstanta \( \lambda > 0 \)
  - Dimenzionalita matice \( d \) (kladné celé číslo, výrazně menší než \( \min(m, n) \))
- **Tuning Hyperparametrů:**
  - Provádí se obvyklým způsobem pomocí křížové validace.
- **Cíl:**
  - Naučit matice \( U \) a \( V \) dané \( d \) a \( \lambda \):
    $$
    \min_{U,V} \sum_{(i,j) \in \Omega} (r_{i,j} - u_i^\top v_j)^2 + \lambda \left( \sum_x \|u_x\|^2 + \sum_y \|v_y\|^2 \right)
    $$

---

#### **Alternující Nejmenší Čtverce (ALS)**
- **Idea:**
  - Střídavě fixujeme matici \( U \) a \( V \). Nepřiřazená matice je považována za proměnnou a podléhá minimalizaci.
  - S jednou fixovanou maticí se optimalizační problém stává konvexním a podobným lineární regresi.
- **Optimalizační Krok:**
  - Při fixaci \( V \), nalezneme optimální \( U \), a naopak.

---

#### **Matice Faktorizace pro Implicitní Zpětnou Vazbu**
- **Realita:**
  - V reálných aplikacích často pozorujeme více implicitní než explicitní zpětné vazby.
  - Explicitní zpětná vazba je někdy považována za implicitní.
- **Příklad:**
  - Uživatel \( i \) sledoval 35 % filmu A a 85 % filmu B.
    - Znamená to, že uživatel má film B více rád než film A?
    - Znamená to, že uživatel má film B více než dvakrát tak rád jako film A?
- **Poznámka:**
  - Metoda naučená výše je vhodnější pro explicitní zpětnou vazbu. Pro implicitní zpětnou vazbu potřebujeme jiný přístup.

---

#### **Modelování Implicitní Zpětné Vazby**
- **Příklad Binární Interakční Matice \( P \):**
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
- **Hlavní Rozdíly oproti předchozí metodě MF:**
  - Zohlednění různých úrovní důvěry (\( C_{ij} \)).
  - Optimalizace musí zahrnovat všechny možné páry \( (i, j) \), nejen ty s pozorovanými daty.
- **Metody Řešení:**
  - Použití gradientního sestupu.
  - Použití ALS: Při fixaci \( V \), najdeme \( u_i \).

---

#### **Uzavřená Forma Řešení**
- **Optimalizační Cíl:**
  - Minimalizovat ztrátu:
    $$
    L_i = \min_{u_i} \sum_j C_{ij} (P_{ij} - u_i^\top v_j)^2 + \lambda \|u_i\|^2
    $$
- **Transformace Ztráty:**
  $$
  L_i = \| \sqrt{C_i} P_i - \sqrt{C_i} V u_i \|^2 + \lambda \|u_i\|^2
  $$
- **Derivace:**
  $$
  \nabla_{u_i} = -2 (\sqrt{C_i} V)^\top (\sqrt{C_i} P_i - \sqrt{C_i} V u_i) + 2 \lambda u_i
  $$
- **Výsledek Uzavřené Formy:**
  $$
  u_i = (V^\top C_i V + \lambda I)^{-1} V^\top C_i P_i
  $$

---

#### **Závěr**
- **Matice Faktorizace** je klíčovou metodou v personalizovaném strojovém učení pro doporučovací systémy.
- **ALS** je efektivní metoda pro optimalizaci matic \( U \) a \( V \).
- **Implicitní zpětná vazba** vyžaduje specifické metody modelování a optimalizace.
- **Řád matice** a **SVD** jsou základními koncepty pro pochopení matice faktorizace.
