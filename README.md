# 🐍 Python Project Template

A lightweight starter boilerplate for new Python projects, featuring a cross-platform environment setup script.

---

## 📦 Features

- ✅ Cross-platform setup (`Windows`, `Linux`, `macOS`)
- 🧹 Auto-cleans existing virtual environment
- 🛠️ Installs all dependencies from `requirements.txt`
- 💯 No external dependencies — uses only built-in Python modules

---

## 📥 Clone This Template

```bash
git clone https://github.com/AbdullahSaif-code/Python-Project-Templet.git my-new-project
cd my-new-project
```
---

## ⚙️ Run Setup Script
🧰 One command to build or rebuild your virtual environment from scratch:

```bash
# On Linux/macOS
python3 setup.py

# On Windows
python setup.py
```
---

## 💻 Activate Virtual Environment
```bash
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```
---
## 📁 Folder Structure

```bash
.
├── venv/                  # Auto-created Python virtual environment
├── setup.py               # Cross-platform setup script (delete/create venv, install deps)
├── requirements.txt       # List of required Python packages
├── .gitignore             # Ignore venv, __pycache__, etc.
└── README.md              # This file
```
---

## 💡 Use Case
- 🎯 Ideal for quick Python prototyping or bootstrapping new apps.
- 🧑‍💻 Ensures consistent, isolated environments across devices.
- 👨‍🏫 Great for team projects or solo experimentation.
  
---

## 📝 Notes
- ❌ Don’t commit the venv/ folder — it’s ignored by .gitignore.
- 📦 Update dependencies using:
  
```bash
pip freeze > requirements.txt
```
- 🛠️ Re-run setup.py anytime you want a clean, fresh environment.
