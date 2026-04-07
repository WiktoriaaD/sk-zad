
## 1. Tabela

Sieć bazowa: **192.168.150.0/24** (łączna pula 256 adresów).

| Dział | Obecnie hostów | +50% +1 (Router)| Wymagane hosty | Rozmiar | Maska |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1.** | 60 | 31 | **91** | 128 | **/25** |
| **2.**| 30 | 16 | **46** | 64 | **/26** |
| **3.** | 14 | 8 | **22** | 32 | **/27** |
| **4.** | 6 | 4 | **10** | 16 | **/28** |
| **5.** | 5 | 4 | **9** | 16 | **/28** |

---

## 2. Drzewko Podziału Podsieci

192.168.150.0/24:
* 192.168.150.0/25 (podsiec 1, 126)
* 192.168.150.128/25:
    * 192.168.150.128/26 (podsiec 2, 62)
    * 192.168.150.192/26:
        * 192.168.150.192/27 (podsiec 3, 30)
        * 192.168.150.224/27:
            * 192.168.150.224/28 (podsiec 4, 14)
            * 192.168.150.240/28 (podsiec 5, 14)

---

## 3. Szczegółowa Lista Podsieci

### *Podsieć 1:*
* **Adres podsieci:** `192.168.150.0/25`
* **Pierwszy adres hosta:** `192.168.150.1`
* **Ostatni adres hosta:** `192.168.150.126`
* **Adres broadcast:** `192.168.150.127`
* **Ilość dostępnych hostów:** 126
* **Nadwyżka względem minimalnej ilości (60+1):** 65 hostów zapasu
* **Nadwyżka względem over-provisioningu (91):** 35 hostów zapasu

### *Podsieć 2:*
* **Adres podsieci:** `192.168.150.128/26`
* **Pierwszy adres hosta:** `192.168.150.129`
* **Ostatni adres hosta:** `192.168.150.190`
* **Adres broadcast:** `192.168.150.191`
* **Ilość dostępnych hostów:** 62
* **Nadwyżka względem minimalnej ilości (30+1):** 31 hostów zapasu
* **Nadwyżka względem over-provisioningu (46):** 16 hostów zapasu

### *Podsieć 3:*
* **Adres podsieci:** `192.168.150.192/27`
* **Pierwszy adres hosta:** `192.168.150.193`
* **Ostatni adres hosta:** `192.168.150.222`
* **Adres broadcast:** `192.168.150.223`
* **Ilość dostępnych hostów:** 30
* **Nadwyżka względem minimalnej ilości (14+1):** 15 hostów zapasu
* **Nadwyżka względem over-provisioningu (22):** 8 hostów zapasu

### *Podsieć 4:*
* **Adres podsieci:** `192.168.150.224/28`
* **Pierwszy adres hosta:** `192.168.150.225`
* **Ostatni adres hosta:** `192.168.150.238`
* **Adres broadcast:** `192.168.150.239`
* **Ilość dostępnych hostów:** 14
* **Nadwyżka względem minimalnej ilości (6+1):** 7 hostów zapasu
* **Nadwyżka względem over-provisioningu (10):** 4 hosty zapasu

### *Podsieć 5:*
* **Adres podsieci:** `192.168.150.240/28`
* **Pierwszy adres hosta:** `192.168.150.241`
* **Ostatni adres hosta:** `192.168.150.254`
* **Adres broadcast:** `192.168.150.255`
* **Ilość dostępnych hostów:** 14
* **Nadwyżka względem minimalnej ilości (5+1):** 8 hostów zapasu
* **Nadwyżka względem over-provisioningu (9):** 5 hostów zapasu

---
