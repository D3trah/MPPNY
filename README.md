# 💪 Edzésnapló és Fitness Statisztika Mikroszerviz

**Készítette:** Dongó Petra
**Intézmény:** Eszterházy Károly Katolikus Egyetem  
**Kurzus:** Multi paradigmás programozási nyelvek gyakorlat  
**Neptun kód:** A3U8XV

---

## 📝 Projekt leírása
Ez az alkalmazás egy modern, mikroszerviz-architektúrájú projekt, amely Python nyelven készült. A célja egy személyes edzésnapló vezetése, ahol a felhasználó rögzítheti az elvégzett gyakorlatokat, az ismétlésszámokat, és automatikus statisztikai kimutatást kaphat a fejlődéséről.

## 🛠️ Alkalmazott technológiák és paradigmák
A projekt megfelel a kurzus minden technikai előírásának:
* **Backend:** FastAPI keretrendszer REST API végpontokkal.
* **Frontend:** Streamlit alapú webes felület interaktív adatvizualizációval.
* **Adatbázis:** SQLite tartós tárolás SQLAlchemy ORM használatával.
* **Paradigmák:** * **Objektumorientált (OOP):** Adatbázis modellek (WorkoutDB osztály) használata.
    * **Funkcionális:** List comprehension és deklaratív adatszerkezetek.
    * **Procedurális:** Logikai folyamatok strukturált függvényekben.
* **Automatizáció:** BeautifulSoup alapú web scraping modul (fitness hírek és tippek gyűjtése).
* **Tesztelés:** Pytest egységtesztek `@pytest.mark.parametrize` dekorátorral.

## 🚀 Telepítés és futtatás
1.  **Virtuális környezet létrehozása és aktiválása:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
2.  **Függőségek telepítése:**
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Backend indítása:**
    ```powershell
    uvicorn backend.main:app --reload
    ```
4.  **Frontend indítása:**
    ```powershell
    streamlit run frontend/app.py
    ```

## 🧪 Tesztelés futtatása
Az automatizált tesztek lefuttatásához használd a következő parancsot az aktív virtuális környezetben:
```powershell
pytest

Online elérhetőségek
GitHub Repository: https://github.com/D3trah/MPPNY

Backend (Render): https://dashboard.render.com/web/srv-d52pr96r433s738me3qg/deploys/dep-d52pr9er433s738me43g

Frontend (Streamlit Cloud): https://kwr2rssqhsrsmxwuwm4zug.streamlit.app