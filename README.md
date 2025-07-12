# 🧾 AppKardex

AppKardex is a web application built with **Python** and the **Flask** framework, designed to manage and display academic Kardex (student records). The project follows a clean, organized architecture with controllers, models, and HTML templates.

---

## 🧱 Project Structure

```bash
APPKARDEX/
│
├── .venv/ # Python virtual environment
├── src/ # Source code
│ ├── app.py # Main Flask application
│ ├── controllers/ # Route logic / business logic
│ ├── database/ # Database configuration and connection
│ ├── Models/ # Data models
│ ├── Static/ # Static files (CSS, JS, images)
│ └── Templates/ # HTML templates (Jinja2)
│
├── .gitignore
├── LICENSE
└── README.md

```

---

## 🚀 Technologies Used

- **Python 3.10+**
- **Flask**
- **HTML5**
- **CSS3**
- **Jinja2** (template engine)
- **SQLite / MySQL** (depending on your database)

---

## ⚙️ How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/AngelDuarte08/KardexUppe.git
cd AppKardex


```

## Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # On Linux/macOS
.venv\Scripts\activate       # On Windows

```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
cd src
python app.py

```

## Open your browser and visit:

```bash
http://localhost:5000
```

## 📂 Folder Overview

```bash
| Folder         | Description                               |
| -------------- | ----------------------------------------- |
| `controllers/` | Application routes and control logic      |
| `Models/`      | Classes and database models               |
| `database/`    | DB configuration and connection logic     |
| `Templates/`   | HTML templates rendered by Flask          |
| `Static/`      | Static resources like CSS, JS, and images |
```

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributions

Contributions are welcome! If you find a bug or have a suggestion, feel free to fork the project and open a pull request.

## 👨‍💻 Developed by

Angel Duarte
Jocelyn Arroyo
Paulina Garcia
