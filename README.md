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

### 🧰 VS Code Integration

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

