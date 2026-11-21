# 🌿 GreenAura Plant Shop API

A RESTful backend for the GreenAura plant shopping application, built with FastAPI and SQLAlchemy.

The API provides plant and category management, user authentication, profile management, image uploads, and persistent user favorites.

## ✨ Features

- **Plant Management:** Retrieve, create, and delete plant records.
- **Plant Search:** Search the catalogue by plant name, description, or category.
- **Category Management:** Retrieve, create, and delete categories.
- **User Registration:** Create new user accounts.
- **Authentication:** JWT-based login and authenticated endpoints.
- **User Profiles:** Retrieve and update account information.
- **Profile Picture Upload:** Upload JPG, PNG, and WEBP images.
- **Plant Image Upload:** Store plant images on the server.
- **Favorites:** Manage persistent favorites for authenticated users.
- **Static File Serving:** Serve uploaded plant and profile images.

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic Settings
- JWT Authentication
- Uvicorn
- Multipart File Uploads

## 📂 Project Structure

```text
greenaura-plant-shop-api/
│
├── app/
│   ├── auth/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── uploads/
│   ├── plants/
│   └── profile_pictures/
│
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/ARK13-org/Greenaura-Plant-Shop-Api.git
```

### 2. Navigate to the project directory

```bash
cd Greenaura-Plant-Shop-Api
```

### 3. Create a virtual environment

```powershell
py -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Configure the secret key

Set a strong secret key before starting the application:

```powershell
$env:SECRET_KEY = "your-own-long-random-secret"
```

### 7. Start the API

```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

- Base URL: `http://127.0.0.1:8000`
- Swagger Documentation: `http://127.0.0.1:8000/docs`
- Health Check: `http://127.0.0.1:8000/health`

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| GET | `/plants/` | Retrieve plants |
| GET | `/plants/{plant_id}` | Retrieve a plant |
| POST | `/plants/` | Create a plant with an image |
| DELETE | `/plants/{plant_id}` | Delete a plant |
| PUT | `/plants/{plant_id}/favorite` | Update favorite status |
| GET | `/category` | Retrieve categories |
| POST | `/category` | Create a category |
| DELETE | `/category/{category_id}` | Delete a category |
| POST | `/user` | Register a user |
| GET | `/auth/me` | Retrieve authenticated user |
| POST | `/auth/login` | Authenticate a user |
| PATCH | `/user/me` | Update user profile |
| GET | `/user/me/favorites` | Retrieve user favorites |
| PUT | `/user/{user_id}/profile-picture` | Upload profile picture |

## 🗄️ Database

GreenAura uses SQLite with SQLAlchemy ORM.

The database connection is configured through application settings. A local database file is created when the application initializes if one does not already exist.

The repository excludes local database files, so a fresh clone does not automatically contain the catalogue data from another development environment.

## 🔐 Security Notes

- Authentication uses JWT access tokens.
- Protected endpoints require bearer-token authentication.
- Configure a strong `SECRET_KEY` before running the application.
- Keep environment files, database files, and private user uploads out of public commits.

## 🔗 Related Repository

[GreenAura Flutter Plant Shop](https://github.com/ARK13-org/Greenaura-Plant-Shop)

---

**GreenAura — Bring Nature Home 🌱**
