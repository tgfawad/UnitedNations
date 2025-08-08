UnitedNations: Flask API + React+d3 Frontend (Dockerized)

Overview

This repository contains a simple, production-ready example of a dockerized Python Flask API and a React + d3.js frontend application. The frontend is fully data-driven by the backend’s getMenu response and supports dynamic menu additions without code changes. Internationalization/localization is considered in the design (locale parameter), with English implemented by default.

What’s included

- Backend: Flask + SQLAlchemy + CORS
  - SQLite by default; easily switchable to Postgres/MariaDB/SQL Server via DATABASE_URL
  - Endpoints
    - GET /api/getMenu?locale=en
    - GET /api/rules/us_population_data (alias: /api/rules/us_population)
    - GET /api/rules/about
  - Unit tests with pytest
- Frontend: React (Vite) + d3.js
  - Fixed header, left menu (30%), content area (70%)
  - Renders Text/Table/Chart views based on backend menu
  - Runtime-configurable API base URL without rebuilding images (via /config.js)
- Dockerized
  - Two Dockerfiles (backend + frontend)
  - docker-compose for local dev/run

Quick start (Docker)

Prerequisites: Docker Desktop

1. Build and start the stack

```pwsh
docker compose up --build -d
```

2. Open the apps

- Backend API: http://localhost:5000/api/getMenu
- Frontend UI: http://localhost:8080

To stop:

```pwsh
docker compose down
```

Runtime configuration (frontend API base URL)

The frontend reads window.APP_CONFIG from /config.js served by Nginx. Change API_BASE_URL without rebuilding the image:

- With docker-compose, set FRONTEND_API_BASE_URL env var to point to the backend (defaults in this compose to http://localhost:5000 which is reachable by your browser).
- You can also volume-mount your own config.js if needed.

Local development (optional)

Backend (Python):

```pwsh
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r backend/requirements.txt
setx DATABASE_URL "sqlite:///instance/app.db"
python backend/wsgi.py
```

Frontend (Node):

```pwsh
cd frontend
npm ci
npm run dev
```

Note: For local dev, the frontend dev server uses Vite and expects API to be at http://localhost:5000 by default (see public/config.js or set VITE_FALLBACK_API_BASE_URL in .env.local).

API details

- GET /api/getMenu?locale=en
  - Returns static menu JSON for now (English only), including items for table, chart, and text views.
- GET /api/rules/us_population_data (alias /api/rules/us_population)
  - Fetches from https://raw.githubusercontent.com/molipet/full-stack-test/main/data.json
  - Transforms to array of { year, population }
- GET /api/rules/about
  - Returns the stored text plus “Last update: <current date and time>”.

Unit tests (backend)

Run tests locally:

```pwsh
./.venv/Scripts/Activate.ps1
pytest -q
```

Or inside Docker:

```pwsh
docker compose run --rm backend pytest -q
```

Switching databases

Set DATABASE_URL to a SQLAlchemy-compatible URI, for example:

- Postgres: postgresql+psycopg://user:pass@host:5432/dbname
- MariaDB/MySQL: mysql+pymysql://user:pass@host:3306/dbname
- SQL Server: mssql+pyodbc://user:pass@host:1433/dbname?driver=ODBC+Driver+17+for+SQL+Server

Internationalization

The API accepts a locale query parameter on /api/getMenu; only en is implemented today, but the structure is ready to add more locales.

Folder structure

backend/
app/ (Flask app)
tests/ (pytest unit tests)
frontend/
src/ (React source)
public/config.js (runtime API base URL)

Extras and next steps

- Add another language to getMenu
- Add zoom/tooltip to the chart
- Add sorting to the table view
- Add UI tests with Selenium
