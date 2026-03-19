# 🚀 Python QA Automation Project

This project is a Python-based QA Automation framework using best practices such as virtual environments, modular structure, and scalable test architecture.

---

## 📦 Project Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Python_Project
```

---

## 🧱 Create Virtual Environment

We use a **local virtual environment** to isolate dependencies.

```bash
python3 -m venv .venv
```

This will create a `.venv/` folder inside the project.

---

## ⚡ Activate Virtual Environment

### Mac / Linux:

```bash
source .venv/bin/activate
```

### Windows:

```bash
.venv\Scripts\activate
```

After activation, your terminal should look like:

```bash
(.venv) your-machine-name:Python_Project
```

---

## 🧪 Verify Environment

Make sure Python is coming from the virtual environment:

```bash
which python
```

Expected output:

```
.../Python_Project/.venv/bin/python
```

---

## 📦 Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install pytest playwright
playwright install
pip freeze > requirements.txt
```

---

## ▶️ Run Tests

Run all tests:

```bash
pytest
```

Run specific test file:

```bash
pytest Tests/test_example.py
```

---

## 📁 Project Structure

```
Python_Project/
│
├── .venv/                 # Virtual environment (ignored by git)
├── Pages/                 # Page Object Models
├── Tests/                 # Test cases
├── Steps/                 # Step definitions (BDD)
├── Features/              # Feature files
├── Runners/               # Test runners
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚨 Important Notes

- `.venv/` is ignored in `.gitignore`
- Do NOT commit virtual environments
- Always install dependencies using `requirements.txt`

---

## 💡 Best Practices

- Use one virtual environment per project
- Keep dependencies updated in `requirements.txt`
- Write modular and reusable test code
- Follow Page Object Model (POM) structure

---

## 🧑‍💻 Author

Alex Dzhoharidze
Senior QA Automation Engineer

---
