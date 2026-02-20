# 🐾 AnimalCare Backend (Django)

AnimalCare ist ein RESTful Backend-System für eine Tierarzt- und Tiervermittlungsplattform, entwickelt mit Django und Django REST Framework.

Dieses Projekt dient dazu, meine Backend-Entwicklungsfähigkeiten zu vertiefen sowie eine strukturierte Adoptionsverwaltung zu simulieren.

---

## ❤️ Inspiration

Dieses Projekt ist von meinen vier geliebten Hunden **(Almond🐶, Joghurt🐶, Taohoo🐶 und Kiekie🐶)** inspiriert.
Auch wenn sie heute nicht mehr bei mir sind, wollte ich ihnen mit dieser kleinen Anwendung ein persönliches Andenken widmen und Lernen mit etwas Bedeutungsvollem verbinden.

---

---

## ✨ Funktionen & Features

- **CRUD-API:** Vollständige Verwaltung von Tierdaten (Create, Read, Update, Delete).
- **RESTful Architektur:** Strukturierte API-Endpunkte für Frontend-Integration.
- **Berechtigungssystem:** Schutz der Daten durch `IsAuthenticatedOrReadOnly`.
- **CORS-Konfiguration:** Sicherer Zugriff für das Angular-Frontend (localhost:4200).
- **Datenmodell:** Unterstützung verschiedener Tierarten (DOG, CAT, RABBIT, OTHER).

---

## 🛠 Tech Stack

- **Sprache:** Python 3.13
- **Framework:** Django & Django REST Framework
- **Datenbank:** SQLite (Entwicklung)
- **Authentifizierung:** JWT (JSON Web Tokens)

---

## 📜 Update-Historie & Projektfortschritt

###✅ **20.02.2026 - API Full CRUD Completion**

[New] PUT-Methode: Der Endpoint /api/animals/{id}/ unterstützt nun vollständige Updates.

[Refactoring] Optimierung der Serializer-Validierung für konsistente Daten beim Bearbeiten.

[Docs] API-Dokumentation um die Update-Logik erweitert.

### ✅ **19.02.2026 - API Finalisierung**

- **[New]** **DELETE-Methode**: Erfolgreich implementiert und mit dem Angular-Frontend getestet.
- **[Fixed]** API liefert nun konsistente Datenstrukturen (Results-Array) für die Frontend-Signals.

### ✅ **18.02.2026 - Integration & Erweitertes Modell**

- **CORS-Config**: Zugriff für das Frontend erlaubt.
- **Datenbank-Migration**: Neue Tierarten (RABBIT, OTHER) hinzugefügt.
- **Permissions**: Vorübergehende Anpassung auf `AllowAny` für reibungslose Frontend-Tests.

### ✅ **16.02.2026 - User-Animal Relationship**

- **Owner-Verknüpfung**: Tiere sind nun fest mit einem Benutzer (Owner) verknüpft.
- **Datenintegrität**: Implementierung von `on_delete=models.CASCADE`.

### ✅ **15.02.2026 - Filter, Suche & JWT**

- **Suche & Filter**: Endpunkte für `status` und `search` hinzugefügt.
- **Pagination**: Ergebnisse werden in Seiten (6 Tiere pro Seite) unterteilt.
- **JWT-Auth**: Authentifizierung via JSON Web Tokens vorbereitet.

---

## 📊 Nächste Schritte

- [ ] **Meilenstein 5: JWT Authentifizierung & Login-System** ⏳ _(Endpoints vorhanden, Frontend-Integration folgt)_
- [x] **Meilenstein 6: Bearbeitungsmodus (Edit Animal)** ✅
- [ ] **Meilenstein 7: Media Root & Image Upload** 📸

---

## 📡 API-Endpunkte

| Methode    | Endpoint             | Beschreibung                          |
| :--------- | :------------------- | :------------------------------------ |
| **GET**    | `/api/animals/`      | Liste aller Tiere (mit Search/Filter) |
| **POST**   | `/api/animals/`      | Neues Tier erstellen                  |
| **GET**    | `/api/animals/{id}/` | Einzelnes Tier abrufen                |
| **DELETE** | `/api/animals/{id}/` | Tier löschen                          |

---

## 📦 Installation

```bash
# Repository klonen
git clone [https://github.com/YOUR-USERNAME/animalcare-backend.git](https://github.com/YOUR-USERNAME/animalcare-backend.git)
cd animalcare-backend

# Virtual Environment & Abhängigkeiten
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate für Windows
pip install -r requirements.txt

# Migrationen & Server-Start
python manage.py migrate
python manage.py runserver
```
