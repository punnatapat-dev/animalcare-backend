# 🐾 AnimalCare Backend (Django)

AnimalCare ist ein RESTful Backend-System für eine Tierarzt- und Tiervermittlungsplattform, entwickelt mit Django und Django REST Framework.

Dieses Projekt dient dazu, meine Backend-Entwicklungsfähigkeiten zu vertiefen sowie eine strukturierte Adoptionsverwaltung zu simulieren.

## 📸 Project Preview

### 🖥️ Frontend (Angular)

![Frontend Dashboard](./screenshots/frontend-dashboard.jpg)

### ⚙️ Backend API (Django REST Framework)

![Backend API](./screenshots/backend-api.png)

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

### ✅ **24.02.2026 - Media URLs + API Konsistenz & Permissions Final Check (Milestone 7.2)**

- **[Improvement] Absolute Image URLs**: API liefert Bild-URLs stabil (z.B. `http://127.0.0.1:8000/media/...`) für direkte Frontend-Nutzung.
- **[Fix] Konsistente Response-Struktur**: Pagination / `results`-Format wurde geprüft (Frontend arbeitet zuverlässig mit `data.results`).
- **[Security] Permissions Re-Check**: Object-Level Permissions (`IsOwnerOrReadOnly`) + JWT Zugriff final gegengeprüft (PUT/DELETE nur Owner).
- **[Stability] End-to-End Stabilisierung**: Upload, Anzeigen, Bearbeiten und Löschen inklusive Bilder erfolgreich getestet.

### ✅ **23.02.2026 - Owner Data Fix & Image Handling Stabilization (Milestone 6.1)**

- **[Fix] Owner-Data Migration:** Bestehende Tierdatensätze ohne `owner` wurden nachträglich per Django-Shell korrigiert, um Object-Level Permissions vollständig funktionsfähig zu machen.
- **[Fix] 403 Forbidden Issue:** Behebung von Update-Fehlern durch fehlende Owner-Zuweisung.
- **[Improvement] Image Upload Stabilization:** Sicherstellung der korrekten Verarbeitung von `multipart/form-data` für Bild-Uploads.
- **[Refactoring] Permission Cleanup:** Entfernung temporärer `AllowAny`-Konfiguration zur Wiederherstellung sicherer Zugriffskontrolle.
- **[Validation] End-to-End Test:** Erfolgreiche Verifizierung von:
  - JWT Authentication
  - Owner Auto-Binding
  - Update & Delete mit Object-Level Security
  - Image Upload & Media Serving

### ✅ **21.02.2026 - JWT & Object-Level Security (Milestone 5)**

- **[New] JWT Authentication**: Integration von `SimpleJWT` für sichere Login-Prozesse.
- **[New] Object-Level Permissions**: Implementierung von `IsOwnerOrReadOnly`. Nur der Ersteller kann seine eigenen Einträge bearbeiten oder löschen.
- **[New] Owner Auto-Binding**: Beim Erstellen eines Tieres wird der eingeloggte Benutzer automatisch als `owner` zugewiesen.
- **[Security] Serializer Protection**: Das `owner`-Feld ist nun schreibgeschützt (ReadOnlyField), um Manipulationen zu verhindern.

### ✅ **20.02.2026 - API Full CRUD Completion**

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

- [x] **Meilenstein 5: JWT Authentifizierung & Access Control** ✅ _(Backend bereit, Frontend-Anbindung in Arbeit)_
- [x] **Meilenstein 6: Bearbeitungsmodus (Edit Animal)** ✅
- [x] Meilenstein 7: Media Root & Image Upload 📸 (Local Development abgeschlossen - Git-ignored)

- [ ] Meilenstein 8: Production Storage Integration (Switching from Local Media to Cloudinary or AWS S3)

---

## 📡 API-Endpunkte

| Methode    | Endpoint             | Beschreibung                          |
| :--------- | :------------------- | :------------------------------------ |
| **GET**    | `/api/animals/`      | Liste aller Tiere (mit Search/Filter) |
| **POST**   | `/api/animals/`      | Neues Tier erstellen                  |
| **GET**    | `/api/animals/{id}/` | Einzelnes Tier abrufen                |
| **DELETE** | `/api/animals/{id}/` | Tier löschen                          |
| **PUT**    | `/api/animals/{id}/` | Tier aktualisieren                    |

---

### 🔑 Authentifizierung & Security

| Methode  | Endpoint              | Beschreibung                                |
| :------- | :-------------------- | :------------------------------------------ |
| **POST** | `/api/login/`         | User Login - liefert Access & Refresh Token |
| **POST** | `/api/token/refresh/` | Erneuert einen abgelaufenen Access Token    |

**Sicherheitsregel:** - `GET`: Öffentlich zugänglich (Read-Only).

- `POST/PUT/DELETE`: Erfordert gültigen JWT-Token.
- `PUT/DELETE`: Nur für den Benutzer erlaubt, der den Eintrag erstellt hat (Owner).

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

---

## 🖼️ Media & Database Management

Um das Repository leicht zu halten und die Privatsphäre der Entwicklungsdaten zu schützen, werden folgende Dateien **nicht** auf GitHub übertragen (siehe `.gitignore`):

- **`media/`**: Dieser Ordner enthält alle hochgeladenen Tierbilder im lokalen Development.
- **`db.sqlite3`**: Die lokale Datenbank mit Test-Usern und Einträgen.

### 🛠️ Setup für lokale Entwicklung:

1. Nach dem Klonen des Projekts ist der Ordner `media/` leer.
2. Wenn du ein Tier über die API/Admin-Panel erstellst und ein Bild hochlädst, wird der Ordner automatisch erstellt.
3. **Produktion:** In einer Produktionsumgebung (z.B. Heroku/DigitalOcean) sollten diese Dateien auf einem Cloud-Speicher wie **AWS S3** oder **Cloudinary** gespeichert werden.
