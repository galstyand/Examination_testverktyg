# Examination_Testverktyg

Detta projekt är ett automatiserat testverktyg byggt med [Behave](https://behave.readthedocs.io/en/stable/) (BDD) och [Playwright för Python](https://playwright.dev/python/). Projektet är strukturerat för att följa en tydlig separation mellan funktionella krav (stories), testscenarier (features), sidrepresentationer (pages) och stegsdefinitioner (steps).

## Projektstruktur

```plaintext
Examination_Testverktyg/
├── .venv/                    # Virtuell miljö
├── Stories.md                # Lista över användarberättelser (user stories)
├── src/                      # All testlogik ligger här
│   ├── features/             # .feature-filer som beskriver testscenarier i Gherkin
│   ├── pages/                # Sidobjekt enligt Page Object Model (POM)
│   ├── steps/                # Stegdefinitioner för Behave
│   └── environment.py        # Hooks och testmiljöinställningar
```
## Förutsättningar
Installera Playwright och dess webbläsare med följande kommandon:

```plaintext
pip install playwright
playwright install
```

## Köra tester
Navigera till src-mappen och kör följande kommando:

```plaintext
cd src
behave
```
Detta kör samtliga .feature-filer med tillhörande stegdefinitioner.

## Innehåll
```plaintext
Stories.md: Sammanställning av alla user stories som testfallen baseras på.

features/: Gherkin-baserade .feature-filer som beskriver användarinteraktioner.

pages/: Pythonklasser som representerar sidorna i applikationen.

steps/: Mapp med Behave-steg kopplade till scenarierna i feature-filerna.

environment.py: Setup/teardown för testmiljön, körs innan/efter varje scenario eller testkörning.
```