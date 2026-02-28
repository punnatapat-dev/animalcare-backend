# 🐾 AnimalCare Backend (Django)

AnimalCare ist ein RESTful Backend-System für eine Tierarzt- und Tiervermittlungsplattform, entwickelt mit Django und Django REST Framework.

Dieses Projekt dient dazu, meine Backend-Entwicklungsfähigkeiten zu vertiefen sowie eine strukturierte Adoptionsverwaltung zu simulieren.

## 📸 Project Preview

### 🖥️ Frontend (Angular)

![Frontend Dashboard](./screenshots/frontend-dashboard.png)

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
- **Cloud Storage:** Cloudinary (Production Media Storage)

---

## 📜 Update-Historie & Projektfortschritt

### ✅ **28.02.2026 – Species Query Filtering Support (API Enhancement)**

- **[New] Species Query Parameter:** Unterstützung von `?species=DOG` in `get_queryset()`.
- **[Combined Filtering] Mehrere Query-Parameter möglich:** `species`, `search` und `status` können kombiniert werden.
- **[Server-Side Filtering] Performance-Optimierung:** Daten werden direkt serverseitig gefiltert.
- **[Validation] API-Test erfolgreich:** Beispiele wie  
  `/api/animals/?species=DOG&search=lu` liefern korrekte Ergebnisse.
- **[Frontend-Kompatibilität] Angular Dropdown vollständig unterstützt.**

### ✅ **27.02.2026 – Pagination Removal & API Response Stabilisierung (Milestone 9)**

- **[Backend] Pagination deaktiviert:** Entfernung von `DEFAULT_PAGINATION_CLASS` und `PAGE_SIZE`, damit `/api/animals/` nun alle Tiere in einer einzigen Response liefert.
- **[API Change] Response-Struktur vereinfacht:** Statt `{ results: [...] }` wird nun direkt ein Array zurückgegeben.
- **[Frontend-Kompatibilität] API-Format dokumentiert:** Anpassung und Validierung der API-Kommunikation nach Pagination-Entfernung.
- **[Stability] End-to-End Re-Test:** Login → Create → Image Upload (Cloudinary) → Update → Delete erfolgreich erneut getestet.
- **[Code Cleanup] REST_FRAMEWORK Settings bereinigt:** Entfernen nicht benötigter Pagination-Konfiguration für klarere Production-Settings.

### ✅ **26.02.2026 – Cloudinary Production Storage Integration (Milestone 8)**

- **[New] Cloudinary Integration:** Migration von lokalem `MEDIA_ROOT` Storage zu Cloudinary Cloud Storage.
- **[Upload] Multipart Image Handling:** Backend verarbeitet nun `multipart/form-data` und lädt Bilder automatisch zu Cloudinary hoch.
- **[Auto-Binding] Owner + Image Upload kombiniert:** Beim Erstellen eines Tieres wird:
  - Der eingeloggte User automatisch als Owner gesetzt
  - Das Bild zu Cloudinary hochgeladen
  - `image_url` und `image_public_id` in der Datenbank gespeichert
- **[Update Logic] Image Replacement:** Beim Bearbeiten eines Tieres wird:
  - Das alte Bild in Cloudinary automatisch gelöscht
  - Das neue Bild hochgeladen
  - Die Datenbank aktualisiert
- **[Security] Serializer Protection:** Das temporäre Upload-Feld `image` ist `write_only`, um Model-Fehler zu vermeiden.
- **[Validation] End-to-End getestet:** Angular → Django → Cloudinary → DB → Angular Rendering erfolgreich verifiziert.

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

- [x] Meilenstein 8: Cloudinary Production Storage Integration ☁️ ✅
- [ ] Meilenstein 9: API Performance & Deployment Preparation 🚀

---

## 📡 API-Endpunkte

| Methode    | Endpoint             | Beschreibung                                                     |
| :--------- | :------------------- | :--------------------------------------------------------------- |
| **GET**    | `/api/animals/`      | Liste aller Tiere (mit Search/Filter)                            |
| **POST**   | `/api/animals/`      | Neues Tier erstellen                                             |
| **GET**    | `/api/animals/{id}/` | Einzelnes Tier abrufen                                           |
| **DELETE** | `/api/animals/{id}/` | Tier löschen                                                     |
| **PUT**    | `/api/animals/{id}/` | Tier aktualisieren                                               |
| **GET**    | `/api/animals/`      | Liste aller Tiere (Search, Status- & Species-Filter unterstützt) |

---

### 🔑 Authentifizierung & Security

| Methode  | Endpoint              | Beschreibung                                            |
| :------- | :-------------------- | :------------------------------------------------------ |
| **POST** | `/api/login/`         | User Login - liefert Access & Refresh Token             |
| **POST** | `/api/token/refresh/` | Erneuert einen abgelaufenen Access Token                |
| **POST** | `/api/animals/`       | Neues Tier erstellen (inkl. Bild-Upload via Cloudinary) |
| **PUT**  | `/api/animals/{id}/`  | Tier aktualisieren (inkl. Bildersatz)                   |

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

## 🖼️ Media & Storage

### ☁️ Cloudinary Production Storage

Dieses Projekt verwendet nun **Cloudinary** als Cloud Storage Lösung für Bilder.

### 🔄 Storage-Strategie

- Bilder werden nicht mehr lokal im `media/`-Ordner gespeichert.
- Keine Bilddateien werden im Repository versioniert.
- Upload erfolgt direkt von Django → Cloudinary.
- `image_url` speichert die öffentliche Cloudinary-URL.
- `image_public_id` ermöglicht das Ersetzen oder Löschen bestehender Bilder.

### 🔁 Image Replacement Logic

Beim Aktualisieren eines Tieres:

- Das alte Bild wird automatisch in Cloudinary gelöscht.
- Das neue Bild wird hochgeladen.
- Die Datenbank wird entsprechend aktualisiert.

### 🔐 Sicherheit

- Bild-Uploads erfolgen ausschließlich über authentifizierte Requests.
- Das temporäre Upload-Feld (`image`) ist `write_only` im Serializer.
