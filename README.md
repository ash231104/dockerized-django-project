# Dockerized Django Project – RailSathiBE

This repository is a **Dockerized version** of the existing Django project [RailSathiBE](https://github.com/s2pl/RailSathiBE), completed as part of the **NullClass Internship – Docker Assignment (Option B)**.

---

## 🔧 What I Did

- Cloned the original Django project from GitHub.
- Configured it with **Docker** and **Docker Compose**.
- Connected it to a **PostgreSQL** database using environment variables.
- Created `.env.example` for secure configuration.
- Verified that the application runs on [http://localhost:8000/items/](http://localhost:8000/items/).
- Ensured hot-reloading with volume mounts.
- Confirmed it works end-to-end via `/items/` API response.

---

## 🐳 How to Run the Project (Dockerized)

### 1. Clone This Repository

```bash
git clone https://github.com/<your-username>/<your-dockerized-repo>.git
cd RailSathiBE
```

### 2. Set Up Environment Variables
```bash
Copy code
cp .env.example .env
```
Update the .env file if needed.

### 3. Build and Run Containers
```bash
Copy code
docker-compose up --build
```

### 4. Access the Project
Visit: http://localhost:8000/items/

Expected response:

```json
Copy code
{ "message": "Hello from /items/" }
```
## 📁 Folder Structure
Copy code
```
RailSathiBE/
├── backend/
│   └── items/
│       ├── views.py
│       └── urls.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```
## 📦 Tech Stack
Django

PostgreSQL

Docker & Docker Compose

Python 3.10+

## ✅ Assignment Deliverables
✅ Dockerized Django project

✅ .env.example included

✅ Application running at /items/

✅ Output verified

✅ README provided (you are reading it!)