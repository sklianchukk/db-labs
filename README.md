# 🧭 Tour Agency Management System

## 📖 Project Overview

A Flask-based REST API for managing tourist routes, guides and tour departures for a travel agency.  
The project is part of database / cloud technologies labs and demonstrates:

- work with a relational MySQL database (designed in 3NF),
- implementation of layered architecture (controller → service → DAO → domain),
- CRUD operations for main entities,
- examples of `1:N` and `M:N` relations exposed via REST endpoints,
- testing with Postman and further deployment to cloud infrastructure.

---

## 🚀 Quick Links

*(locally, after running `python app.py`)*

- **💚 Health Check**: `http://localhost:5000/health`
- **🧾 Routes list**: `http://localhost:5000/routes/`
- **🧾 Route details**: `http://localhost:5000/routes/<id>`
- **🧾 Route departures (1:N)**: `http://localhost:5000/routes/<id>/departures`
- **🧾 Route guides (M:N)**: `http://localhost:5000/routes/<id>/guides`
- **🧾 Route full details**: `http://localhost:5000/routes/<id>/details`
- **(Optional)** Swagger / OpenAPI (if Flasgger is enabled): `http://localhost:5000/apidocs`

> In the current version Swagger may not yet be enabled.  
> If you add Flasgger, the interactive documentation will be available at `/apidocs`.

## ✈️ Features

- 🧭 **Route Management**
  - Store tourist routes (cruise, hiking, bus, hotel stay)
  - Route description, duration, price per person
  - Route type (`route_types`)
  - Linked hotel (if relevant)

- 🏨 **Hotel Integration**
  - Hotel information (name, location, rating)
  - Linking a hotel to a route (vacation in a specific hotel)

- 🧑‍🤝‍🧑 **Guide Management (M:N)**
  - Guides table (`guides`)
  - Many-to-many relation between routes and guides via `route_guides`
  - Work periods of a guide on a route (`start_date`, `end_date`)

- 🗓 **Tour Departures (1:N)**
  - Separate table `tour_departures`
  - Departure start date, status, price per person
  - One route → many departures (1:N)

- 🛣 **Stops**
  - Store stops (`stops`)
  - Relation between routes and stops via `route_stops` with an order index

---

## ⚙️ Tech Stack

- **Backend:** Python 3.x, Flask
- **Database:** MySQL (local or Azure Database for MySQL)
- **DB access:** `mysql-connector-python` (no ORM)
- **Configuration:** YAML (`app/config/app.yml`) + optional environment overrides
- **API testing:** Postman / curl
- **Architecture:** Controller → Service → DAO → Domain (layered architecture)

## ⚡ Quick Start


1. **Clone repository**
```bash
git clone https://github.com/sklianchukk/db-labs.git
cd db-labs/tour_agency_backend
```
If your structure is different — go to the folder that contains app.py, app/, requirements.txt.

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# або
.\venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install -r app/requirements.txt
```
Communication with MySQL is done via mysql-connector-python

4. **Configure database**
The project uses a YAML configuration file: `app/config/app.yml`

```Example content
database:
  host: 127.0.0.1        # or Azure MySQL host, e.g. tour-agency-mysql.mysql.database.azure.com
  port: 3306
  user: root             # your MySQL user
  password: your_password_here
  name: lab1             # database name from Lab 1

```
*Steps:*
- Make sure your MySQL server is running (locally or in the cloud).
- Create the `lab1` database if it does not exist yet: `CREATE DATABASE lab1 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
`
- Execute the SQL script with the DB schema (exported from MySQL Workbench for Lab 1).
- Optionally execute data.sql from this project to insert sample data.

In a cloud environment (e.g. Azure App Service) the parameters `host`, `user`, `password`, `name`
can also be passed via environment variables (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`)
and override the values from YAML.


5. **Run application (development)**
```bash
python app.py
```
By default Flask will listen on:
```text
http://127.0.0.1:5000
```

6. **Access the application**
- Home: http://localhost:5000/
- Health: http://localhost:5000/health
- Route by id: http://localhost:5000/routes/1
- Swagger UI: http://localhost:5000/api/docs

## 📚 API Documentation

### Interactive Documentation
Visit **Swagger UI** at `http://your-server:5000/api/docs` for:
- 📖 Full API documentation
- 🧪 Interactive endpoint testing
- 📝 Request/response schemas
- ✅ Try it out directly in the browser

## Database Schema
### Core Tables
- `routes` – routes (name, description, duration, price, type, hotel)
- `route_types` – types of routes (cruise, hiking, bus, hotel vacation, etc.)
- `hotels` – hotels (name, location, rating)
- `guides` – guides (first name, last name, contact info)
- `route_guides` – junction table (M:N) between routes and guides
- `tour_departures` – departures for each route (start date, status, price)
- `stops` – route stops
- `route_stops` – relation between routes and stops (order index, stop duration)

## 🚢 Manual Deployment (local)

### Manual Deployment
```bash
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
python app.py
```

### Cloud Deployment (example: Azure App Service)
Push to main branch triggers automatic deployment via GitHub Actions:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

## 📁 Project Structure

```bash
project/
├── app/
│   ├── controller/       # API endpoints
│   ├── service/          # Business logic
│   ├── dao/              # Data access
│   ├── domain/           # SQLAlchemy models
│   ├── config.yaml       # DB configuration
│   ├── database.py       # SQLAlchemy setup
│   └── __init__.py       # App factory
├── requirements.txt
├── .gitignore
└── README.md
```
## 📄 License

This project is part of the Database course at Lviv Polytechnic National University.

## 👨‍💻 Author

Bohdan Sklianchuk - [GitHub Profile](https://github.com/sklianchukk)

## 🙏 Acknowledgments

- Course: "Бази даних і знань" (Databases and Knowledge)
- Lviv Polytechnic National University
- AWS for cloud infrastructure
