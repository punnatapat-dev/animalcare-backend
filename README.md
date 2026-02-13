# 🐾 AnimalCare Backend

AnimalCare ist ein RESTful Backend-System für eine Tierarzt- und Tiervermittlungsplattform, entwickelt mit Django und Django REST Framework.

Dieses Projekt entstand im Rahmen meiner IT-Umschulung und dient dazu, meine Backend-Entwicklungsfähigkeiten zu vertiefen sowie eine strukturierte, realitätsnahe Adoptionsverwaltung zu simulieren.

---

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

| Methode | Endpoint | Beschreibung |
|----------|----------|--------------|
| GET | /api/animals/ | Liste aller Tiere |
| POST | /api/animals/ | Neues Tier erstellen (Login erforderlich) |
| GET | /api/animals/{id}/ | Einzelnes Tier abrufen |
| PUT | /api/animals/{id}/ | Tier aktualisieren |
| DELETE | /api/animals/{id}/ | Tier löschen |

---

## 🔐 Berechtigungen

- Anonyme Benutzer → Nur Lesezugriff  
- Authentifizierte Benutzer → Voller CRUD-Zugriff  

Implementierte Permission:  
IsAuthenticatedOrReadOnly

---

## ❤️ Motivation

Dieses Projekt ist persönlich inspiriert von meinen vier geliebten Hunden — Almond, Joghurt, Taohoo und Kiekie.

Es verbindet persönliche Motivation mit strukturierter Backend-Entwicklungspraxis.

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
