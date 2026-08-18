# Student Management System

A containerized, database-driven **Student Management System** built with **Python, Streamlit, MySQL, and Docker**.

The application implements an end-to-end data management workflow for capturing, persisting, querying, modifying, and deleting student records through an interactive Streamlit interface backed by a MySQL relational database.

## Architecture

```text
                ┌─────────────────────┐
                │     Streamlit UI    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Python Backend    │
                │ Application Logic   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    MySQL Database   │
                │ Persistent Storage  │
                └─────────────────────┘

              Docker Compose
        ┌─────────────────────────────┐
        │  Application + Database     │
        └─────────────────────────────┘
```

## Core Capabilities

The system provides a complete student-record lifecycle:

* **Insert** — create new student records
* **View** — retrieve stored records
* **Search** — query records using student attributes
* **Update** — modify existing records
* **Delete** — remove records using the Roll Number as the primary key

Student information includes fields such as:

* Roll Number
* Name
* Email
* Phone Number
* Marks

## Data Flow

```text
User Input
    ↓
Streamlit Interface
    ↓
Python Application Layer
    ↓
SQL Query Execution
    ↓
MySQL
    ↓
Persistent Student Records
```

This architecture separates **user interaction, application logic, and data persistence**, providing a practical foundation for database-backed applications.

## Technology Stack

| Component        | Technology     |
| ---------------- | -------------- |
| Application      | Python         |
| Interface        | Streamlit      |
| Database         | MySQL          |
| Query Language   | SQL            |
| Containerization | Docker         |
| Orchestration    | Docker Compose |

## Database Operations

The application is structured around standard relational database operations:

```text
INSERT  → Create student records
SELECT  → Retrieve and search records
UPDATE  → Modify existing records
DELETE  → Remove records
```

The **Roll Number** serves as the primary key, providing a unique identifier for each student record.

## Containerization

The complete application is containerized to provide a reproducible runtime environment.

### Dockerfile

Defines the application image, Python runtime, dependencies, and execution configuration.

### requirements.txt

Defines the Python packages required by the application.

### docker-compose.yml

Orchestrates the application and MySQL services, allowing the system to be launched as a multi-container application.

## Running with Docker

Clone the repository:

```bash
git clone https://github.com/abdullahzulfiqar2550-gif/Student-Management-System.git
cd Student-Management-System
```

Build and start the services:

```bash
docker compose up --build
```

Once the containers are running, access the Streamlit application:

```text
http://localhost:8501
```

To stop the services:

```bash
docker compose down
```

## Engineering Focus

The project demonstrates the integration of four fundamental application layers:

**Presentation Layer**
Streamlit provides the interface for collecting and displaying student data.

**Application Layer**
Python manages application logic, input handling, and database interactions.

**Data Layer**
MySQL provides structured relational storage and SQL-based data management.

**Infrastructure Layer**
Docker and Docker Compose provide reproducible application and database environments.

## Objective

The objective of this project is to demonstrate an end-to-end **data-driven application architecture** in which user-generated information moves reliably from an interactive interface into a relational database and can subsequently be queried and managed through application logic.

This pattern is directly applicable to systems involving **customer records, employee management, inventory, admissions, healthcare records, and other transactional data applications**.

## Future Extensions

The architecture can be extended with:

* Authentication and role-based access control
* Data validation and schema constraints
* Analytics and performance dashboards
* REST API integration
* Automated testing
* CI/CD pipelines
* Cloud deployment
* Production database configuration
* Logging and monitoring

## Author

**Muhammad Abdullah**

AI Engineer | Python | Machine Learning | Deep Learning | SQL | Data Engineering
