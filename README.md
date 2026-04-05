# 💰 Finance Tracker API (Django REST)

## 📌 Project Overview

The **Finance Tracker API** is a backend system built using Django and Django REST Framework that allows users to manage their financial data, including income and expenses, with role-based access control and analytics features.

---

## 🚀 Features

* 🔐 User Authentication & Role-Based Access (Admin, Analyst)
* 💵 Add, Update, Delete Finance Entries
* 📊 Financial Summary (Total Income, Expense, Balance)
* 📂 Category-wise Expense Breakdown
* 🛠 Admin Dashboard for Management
* 🔗 RESTful API Architecture

---

## 🛠 Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework
* **Database:** SQLite (default)
* **Tools:** VS Code / PyCharm, Postman (for API testing)

---

## 📁 Project Structure

```
finance_tracker/
│
├── config/                # Main project settings & URLs
├── users/                 # Custom user & roles
├── finance/               # Finance entries (income/expense)
├── analytics/             # Summary & category analysis
├── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Project

```
git clone <your-repo-link>
cd finance_tracker
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```
python manage.py migrate
```

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

### 6️⃣ Run Server

```
python manage.py runserver
```

---

## 🌐 API Endpoints

### 🔑 Authentication (Admin Panel)

```
/admin/
```

---

### 💰 Finance APIs

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | /api/entries/      | Get all entries  |
| POST   | /api/entries/      | Create entry     |
| GET    | /api/entries/<id>/ | Get single entry |
| PUT    | /api/entries/<id>/ | Update entry     |
| DELETE | /api/entries/<id>/ | Delete entry     |

---

### 📊 Analytics APIs

| Method | Endpoint                   | Description        |
| ------ | -------------------------- | ------------------ |
| GET    | /api/analytics/summary/    | Financial summary  |
| GET    | /api/analytics/categories/ | Category breakdown |

---

## 📌 Example Request

### Add Income

```json
{
  "type": "income",
  "amount": 50000,
  "category": "salary"
}
```

### Add Expense

```json
{
  "type": "expense",
  "amount": 2000,
  "category": "food"
}
```

---

## 📈 Sample Output

### Summary API Response

```json
{
  "total_income": 50000,
  "total_expense": 2000,
  "balance": 48000
}
```

---

## 🔐 Role-Based Access

| Role    | Permissions                 |
| ------- | --------------------------- |
| Admin   | Full access (CRUD + delete) |
| Analyst | View analytics              |
| User    | Basic access                |

---

## 📷 Screenshots (Add Here)

* Admin Dashboard
* Finance Entries
* API Responses

---

## 🎯 Key Learning Outcomes

* Built REST APIs using Django REST Framework
* Implemented role-based permissions
* Designed modular backend architecture
* Worked with database models and queries

---

## 📌 Conclusion

This project demonstrates a complete backend solution for financial tracking with secure access control and analytics. It is suitable for real-world applications and showcases strong backend development skills.

---

## 👤 Author

**Nikita Yadav**


---
