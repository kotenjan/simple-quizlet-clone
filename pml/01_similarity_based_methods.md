### Personalizované Strojové Učení: Paměťové Přístupy v 

---

#### **Doporučovací Systémy (Recommender Systems)**
- **Typy doporučení:**
  - **Předměty uživatelům:** Nejčastější typ (např. doporučení filmů na Netflixu).
  - **Uživatelé předmětu:** Doporučení uživatelů, kteří by mohli mít zájem o určitý produkt.
  - **Předměty předmětům:** Doporučení podobných produktů (např. doporučení knih podobných té, kterou uživatel právě čte).
  - **Uživatelé uživatelům:** Doporučení podobných uživatelů (např. „Lidé podobní vám také sledují…“).
- **Předměty mohou zahrnovat:**
  - Filmy, produkty, novinky, hudbu, knihy, recepty a další.

- **Praktická aktivita:**
  - Pracujte ve dvojicích: Otevřete aplikaci (např. Instagram) nebo navštivte webovou stránku (např. seznam.cz) a najděte jeden příklad každého ze čtyř výše uvedených scénářů doporučování, které již jsou aplikovány nebo by mohly být implementovány.

---

#### **Paměťové Přístupy (Memory-based Approaches)**
- **Doporučovatelé jako dva různé problémy učení:**
  - **Prediktivní modelování:** Předpovídání hodnocení položky \( j \) uživatelem \( i \).
  - **Retrieval modelování:** Učení rankingových systémů – uživatel \( i \) preferuje položku \( j_1 \) více než položku \( j_2 \).
- **Základ na minulých interakcích a/nebo atributech:**
  - **Interakce:**
    - **Explicitní:** Když uživatel ohodnotí píseň 4 hvězdičkami na stupnici od 0 do 5.
    - **Implicitní:** Když uživatel například sleduje 80 % obsahu.
  - **Atributy:**
    - **Uživatelé:** Pohlaví, věk, lokalita a další.
    - **Předměty:** Text, video, metadata a další.

---

#### **Modelování Interakcí**
- **Explicitní zpětná vazba:**
  - Uživatelé přímo hodnotí položky (např. hodnocení filmů).
- **Implicitní zpětná vazba:**
  - Závisí na chování uživatelů bez přímého hodnocení (např. sledování videí, kliknutí na produkty).

#### **Kombinace Implicitní a Explicitní Zpětné Vazby**
- Kombinace obou typů zpětné vazby pro přesnější doporučení.

---

#### **Personalizované Strojové Učení (Personalized Machine Learning)**
- **Charakteristiky:**
  - Není jednoduchý regresní nebo klasifikační problém.
  - Personalizovaný model zajišťuje, že různí uživatelé obdrží odlišná doporučení na základě jejich interakcí a atributů.
- **Příklad:**
  - Vektor \( \mathbf{a}_i \) je atributový vektor uživatele \( i \) a \( \mathbf{a}_j \) je atributový vektor položky \( j \).
  - Pomocí lineární regrese lze předpovědět, jak se uživateli \( i \) bude líbit položka \( j \):
    $$
    r_{i,j} = \boldsymbol{\omega}^\top \times [\mathbf{a}_i \; \mathbf{a}_j]
    $$
  - **Otázka:** Je lineární regrese personalizovaný model pro doporučovače? Proč?

---

#### **Algoritmy Doporučování**
- **Paměťové Přístupy:**
  - Jednoduché a často používané modely.
  - Doporučují položky podobné těm, se kterými uživatel již interagoval.
  - Klíčové je správné měření podobnosti.
- **Základní metody výpočtu podobnosti:**
  - Na základě atributů uživatelů/předmětů.
  - Na základě interakcí uživatel-předmět.

---

#### **Modelování Atributů**
- **Jak doporučovat na základě atributů:**
  - Analýza a využití atributových matic pro uživatele a předměty.

---

#### **k-NN Algoritmus pro Doporučování**
- **Popis:**
  - k-NN je instance-based metoda, která může být buď obsahově založená, nebo kolaborativní.
  - Používá se také pro regresi a klasifikaci.
- **Postup:**
  1. Definujte uživatelský vektor \( \mathbf{u}_i \) s neznámým hodnocením \( r_{i,j} \) pro položku \( j \).
  2. Vypočítejte vzdálenost \( d(x, i) \) mezi \( \mathbf{u}_i \) a všemi ostatními uživatelskými vektory \( \mathbf{u}_x \).
  3. Najděte \( k \) nejbližších sousedů, kteří mají hodnocení pro položku \( j \).
  4. Kombinujte jejich hodnoty \( r_{x,j} \) (např. průměr).
  5. Výsledek je predikované hodnocení.

- **Weighted k-NN:**
  - Přidělení vyšší váhy podobnějším uživatelům při kombinování hodnocení.
  - **Příklad vzorce pro predikci:**
    $$
    \hat{r}_{i,j} = \frac{\sum_{l \in K} \text{sim}(i, l) \times r_{l,j}}{\sum_{l \in K} \text{sim}(i, l)}
    $$
  - \( K \) je množina \( k \)-nejbližších sousedů.
---

#### **Definování Funkce Podobnosti**
- **Problém:**
  - Ve většině případů jsou vektory částečně známy, protože vidíme jen část interakcí uživatele.
- **Příklad:**
  - \( U_1 = \{1, 3, 4, 8, 12, 15, 17, 24, 35, 39, 41, 43\} \)
  - \( U_2 = \{2, 3, 4, 5, 9, 12, 13, 16, 19, 24, 17, 31\} \)
  - \( U_3 = \{4, 5, 9, 12\} \)
  - \( U_4 = \{4, 9\} \)
- **Jednoduchá definice podobnosti:**
  $$
  \text{sim}(i, l) = |U_i \cap U_l|
  $$

- **Diskuse:**
  - Je rozumné tvrdit, že \( \text{sim}(1, 2) > \text{sim}(3, 4) \)?
  - Poznámka: Uživatelé 1 a 2 jsou vysoce motivovaní a mají mnoho interakcí, což může zkreslit funkci podobnosti.

---

#### **Jaccardova Podobnost**
- **Náprava problému s jednoduchou podobností:**
  - Normalizace podobnosti podle popularity uživatelů.
- **Definice:**
  $$
  \text{Jaccard}(i, l) = \frac{|U_i \cap U_l|}{|U_i \cup U_l|}
  $$
- **Vlastnosti:**
  - Hodnota mezi 0 a 1.
  - 0 pokud nemají žádné společné interakce.
  - 1 pokud jsou všechny interakce uživatelů identické.

---

#### **Kosínová Podobnost (Cosine Similarity)**
- **Limita Jaccardovy podobnosti:**
  - Definována pouze pro množiny interakcí.
  - Nepoužitelná při přiřazené zpětné vazbě (např. +1, -1, 0).
- **Definice:**
  $$
  \cos(\theta) = \frac{\langle \mathbf{a}, \mathbf{b} \rangle}{\|\mathbf{a}\| \cdot \|\mathbf{b}\|}
  $$
- **Vlastnosti:**
  - Měří úhel mezi vektory interakcí.
  - Vhodná pro situace s pozitivní a negativní zpětnou vazbou.

---

#### **Eukleidovská Podobnost (Euclidean Similarity)**
- **Definice:**
  $$
  \text{ES}(\mathbf{a}, \mathbf{b}) = \frac{1}{1 + d(\mathbf{a}, \mathbf{b})}
  $$
  - Kde \( d(\mathbf{a}, \mathbf{b}) \) je eukleidovská vzdálenost mezi vektory \( \mathbf{a} \) a \( \mathbf{b} \).
- **Vlastnosti:**
  - \( \text{ES}(\mathbf{a}, \mathbf{b}) = 1 \), když \( \mathbf{a} = \mathbf{b} \).
  - Přibližuje se 0, když jsou vektory velmi vzdálené.
  - Může být definováno pro libovolnou definovanou vzdálenost.

---

#### **Explicitní Zpětná Vazba a Biasy**
- **Problém:**
  - Někteří uživatelé jsou přísní (haters) a jiní štědří (lovers) ve svých hodnoceních.
- **Řešení:**
  - Odečíst průměrné hodnocení každého uživatele před aplikací k-NN.
  - Při predikci přidat zpět průměrné hodnocení uživatele.

---

#### **Výhody a Nevýhody k-NN Algoritmu pro Doporučování**
- **Výhody:**
  - Nepotřebuje trénování (memory-based metoda).
  - Jednoduchá implementace a vysvětlení.
  - Relativně stabilní při přidávání nových interakcí.
- **Nevýhody:**
  - Omezené pokrytí kvůli řídnutí dat (sparsity).
  - Prakticky náročné pro velké datové sady.
    - Řešení: Použití clusteringu a redukce dimenzionality pro zlepšení škálovatelnosti.