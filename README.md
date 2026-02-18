# 🐾 AnimalCare Backend

AnimalCare ist ein RESTful Backend-System für eine Tierarzt- und Tiervermittlungsplattform, entwickelt mit Django und Django REST Framework.

Dieses Projekt entstand im Rahmen meiner IT-Umschulung und dient dazu, meine Backend-Entwicklungsfähigkeiten zu vertiefen sowie eine strukturierte, realitätsnahe Adoptionsverwaltung zu simulieren.

## ❤️ Motivation

Dieses Projekt ist persönlich inspiriert von meinen vier geliebten Hunden — Almond, Joghurt, Taohoo und Kiekie.

## Es verbindet persönliche Motivation mit strukturierter Backend-Entwicklungspraxis.

## 🚀 Funktionen

- CRUD-API für Tiere
- Statussystem (Available, Reserved, Adopted)
- RESTful API-Architektur
- Authentifizierung & Berechtigungsverwaltung
- Django Admin Panel
- Strukturierter und skalierbarer Backend-Aufbau

---

## 🛠 Tech Stack

- Python 3.13
- Django
- Django REST Framework
- SQLite (Entwicklung)
- Git & GitHub

---

## 📦 Installation

git clone https://github.com/YOUR-USERNAME/animalcare-backend.git  
cd animalcare  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver

Im Browser öffnen:  
http://127.0.0.1:8000/api/animals/

---

## 📡 API-Endpunkte

| Methode | Endpoint           | Beschreibung                              |
| ------- | ------------------ | ----------------------------------------- |
| GET     | /api/animals/      | Liste aller Tiere                         |
| POST    | /api/animals/      | Neues Tier erstellen (Login erforderlich) |
| GET     | /api/animals/{id}/ | Einzelnes Tier abrufen                    |
| PUT     | /api/animals/{id}/ | Tier aktualisieren                        |
| DELETE  | /api/animals/{id}/ | Tier löschen                              |

---

## 🔐 Berechtigungen

- Anonyme Benutzer → Nur Lesezugriff
- Authentifizierte Benutzer → Voller CRUD-Zugriff

Implementierte Permission:  
IsAuthenticatedOrReadOnly

---

## 📌 Projektstatus

Backend v0.1 abgeschlossen

Geplante nächste Schritte:

- Adoptions-Workflow
- Filter- und Suchfunktion
- Pagination
- Angular-Frontend-Integration
- JWT-Authentifizierung
- Deployment

### 🔍 Filter- und Suchfunktion (Neu!) (15.02.2026)

Die API wurde am 15.02.2026 um leistungsstarke Funktionen erweitert:

- **Nach Status filtern:** `GET /api/animals/?status=Available` (Verfügbare Werte: Available, Reserved, Adopted)
- **Nach Namen suchen:** `GET /api/animals/?search=Almond` (Findet alle Tiere, deren Name die Zeichenfolge enthält)
- **Pagination:** Die Ergebnisse werden nun in Seiten unterteilt (6 Tiere pro Seite), um die Ladezeiten zu optimieren.
  - Beispiel: `GET /api/animals/?page=2`

🔐 JWT-Authentifizierung (Neu!) (15.02.2026)

Das System nutzt nun JSON Web Tokens (JWT) für eine sichere Authentifizierung:

- **Token abrufen:** `POST /api/token/` (Benutzername & Passwort senden)
- **Token erneuern:** `GET /api/token/refresh/`
- Diese Funktion ermöglicht es dem Angular-Frontend, Benutzer sicher anzumelden.

---

👥 User-Animal Relationship (Neu!) (16.02.2026)

- **Owner-Verknüpfung:** Jedes Tier ist nun fest mit einem Benutzer (Owner) verknüpft.
- **Datenintegrität:** Durch `on_delete=models.CASCADE` werden Tierdaten automatisch bereinigt, wenn ein Benutzer gelöscht wird.
- **Vorbereitung für Angular:** Diese Struktur ermöglicht es, im Frontend Funktionen wie "Meine Tiere" anzuzeigen.

---

📌 Projektstatus

- [x] Backend v0.1 abgeschlossen
- [x] Filter- und Suchfunktion
- [x] Pagination
- [x] JWT-Authentifizierung
- [x] User-Animal Relationship
- [ ] Adoptions-Workflow
- [ ] Angular-Frontend-Integration
- [ ] Deployment

---

# 🐾 AnimalCare Backend (Django)

Update: 18.02.2026

### ✅ Erledigt:

- **CORS-Config**: Zugriff für localhost:4200 erlaubt.
- **API Endpoints**: `/api/animals/` liefert jetzt Daten im JSON-Format (inkl. results-Array).
- **Database**: Modell für "Animals" erfolgreich erstellt (Name, Species, Status).
- **POST-Methode Implementiert**: Das Hinzufügen neuer Tiere über die API ist jetzt voll funktionsfähig.
- **Berechtigungen (Permissions)**: `permission_classes` auf `AllowAny` gesetzt, um POST-Anfragen vom Frontend zu ermöglichen.
- **Erweitertes Datenmodell**: `RABBIT` und `OTHER` zur Auswahl der Tierarten hinzugefügt.
- **Datenbank-Migration**: `makemigrations` und `migrate` erfolgreich durchgeführt, um neue Tierarten zu unterstützen.

### 🚀 Nächste Schritte:

- POST-Methode für das Hinzufügen neuer Tiere vorbereiten.
- DELETE-Methode implementieren, um Tiere aus der Liste zu entfernen.
