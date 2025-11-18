# 🏫 School Management System

A modular, schema-first system built with PostgreSQL, FastAPI, and Angular. Designed for clarity, extensibility, and collaborative development.

---

## 🚀 Local Setup Guide

### 🧱 PostgreSQL Installation

1. **Install PostgreSQL for Windows**  
   [EnterpriseDB Installer](https://www.enterprisedb.com/docs/supported-open-source/postgresql/installing/windows/)

2. **Confirm PostgreSQL Server is Running**  
   - Open **Windows Services**
   - Look for `postgresql-x64-<version>` and ensure it’s running

3. **Add PostgreSQL to User PATH**  
   - Add `C:\Program Files\PostgreSQL\<version>\bin` to your user environment PATH

---

### 🧪 Initialize the Database

```bash
psql -U postgres -f "sql/init.sql"
psql -U dev_user -d school_management -f "sql/data-model.sql"
```

> Optional reset:
```bash
psql -U postgres -f "sql/reset.sql"
```

---

### Setup JWT Secret

Run this locally to generate your local secret; copy the results and update .env

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Starting the API (manual)

This is a POC — no secret management is used. Use the local dev DB credentials from the SQL files when initializing the database.

1. Create & activate a virtual environment

PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

CMD:
```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies
```powershell
pip install -r requirements.txt
```

3. (Optional) Initialize or reset the database
```powershell
psql -U postgres -f "sql/init.sql"
psql -U dev_user -d school_management -f "sql/data-model.sql"
# or reset:
psql -U postgres -f "sql/reset.sql"
```

4. Start the server (development)
```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open in your browser:
- http://127.0.0.1:8000/docs (Swagger UI)
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json


> Note: VS Code Debug configuration will also activate the venv and run uvicorn if you prefer the debugger workflow.

![VS Code Debugger](./documentation/Debugger_Screenshot.png)

### Generating the Code

#### SQL Alchemy Models

OPTIONAL: this can be run to refresh the SQL Alchemy ORM models if there are changes in the database (run from project root): 
* sqlacodegen postgresql://dev_user:cs491@localhost:5432/school_management --schema school --outfile app/models/sqlalchemy_models.py

#### Pydantic Models

OPTIONAL: this can be run to refresh the Pydantic API models if there are any changes in the database (run from project root):
* datamodel-codegen --input .\app\models\sqlalchemy_models.py --input-file-type python --output .\app\schemas\schemas.py
* datamodel-codegen --input .\app\schemas\model_schema.json --input-file-type json --output .\app\schemas\generated_models.py

---

### 🧰 VS Code Integration

#### PostgreSQL
1. Install the **PostgreSQL extension** (by Microsoft)
2. Press `Ctrl + Shift + P` → PostgreSQL: Add Connection
3. Use these settings:

```json
{
  "host": "localhost",
  "user": "dev_user",
  "port": 5432,
  "ssl": false,
  "database": "school_management",
  "password": "cs491"
}
```

#### Python Linting Errors
If you are getting pylance warnings with your imports resolving, make sure your interpreter is changed to the venv:

Ctrl + shift + p > Python: Select Interpreter

<img src="documentation/Interpreter_Screenshot.png" width="50%" height="200px" alt="VS Code Command Palette">

## Diagrams

> Diagrams Requires [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview) in VS Code  
> Press `Ctrl + Shift + V` to render

---

## 📊 [Entity Relationship Diagram](documentation/entity-relationship-diagram.md)

This diagram illustrates the relational data model that underpins the School Management System. It defines the core entities, their attributes, and the relationships necessary to support key application features such as user management, course scheduling, attendance tracking, and performance reporting.

The schema is implemented in PostgreSQL and serves as the single source of truth across the stack. SQLAlchemy leverages this model to generate the Object-Relational Mapping (ORM) layer, enabling seamless integration with the FastAPI backend and ensuring consistency between the database and application logic.

---

## 🧱 [System Architecture Diagram](documentation/system-diagram.md)

## 🧩 Overview

This diagram presents a high-level view of the School Management System architecture, illustrating the core components and their interactions across layers. It serves as a blueprint for understanding how data flows through the system—from user interfaces to backend services and persistent storage.

### 🔧 Key Layers and Components

- **Frontend (Angular)**  
  Provides a responsive user interface for students, teachers, and administrators. Communicates with the backend via RESTful APIs.

- **Backend (FastAPI + SQLAlchemy)**  
  Acts as the application’s control center, handling business logic, authentication, and data orchestration. SQLAlchemy bridges the gap between Python objects and the PostgreSQL database.

- **Database (PostgreSQL)**  
  Stores normalized relational data supporting core modules like user management, course scheduling, attendance, and grading. Designed for extensibility and future-proofing.

- **Authentication Layer**  
  The School Management System implements a secure, scalable authentication and authorization (A&A) layer to manage user access across roles such as students, teachers, and administrators.

### 📡 Communication Flow

- Frontend sends HTTP requests to FastAPI endpoints.
- FastAPI processes requests, applies business logic, and interacts with the database via SQLAlchemy ORM.
- Responses are returned to the frontend for rendering.
- Authentication and authorization are enforced at the API layer using JWT tokens and role-based access control.

---

## 🔄 [Development Workflow](documentation/development-workflow-diagram.md)

This diagram provides a high-level overview of the team’s end-to-end development process—from task intake and branching strategy to code review, testing, and deployment. It captures the key stages, tools, and handoffs that ensure consistent delivery, traceability, and collaboration across the stack. For detailed swim lanes, validation gates, and role-specific responsibilities, refer to the annotations within the diagram itself.

---

