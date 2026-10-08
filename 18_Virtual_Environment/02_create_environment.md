# ============================================================
# CREATE VIRTUAL ENVIRONMENT
# ============================================================

## 1. Open Terminal

Open Terminal, Command Prompt, PowerShell,
or the VS Code terminal.

Go to your project folder.

Example:

cd my_project

---

## 2. Create Virtual Environment

Run:

python -m venv venv

This creates a virtual environment named:

venv

---

## 3. Understanding the Command

python
    ↓
Runs Python.

-m
    ↓
Runs a Python module.

venv
    ↓
Python's virtual environment module.

venv
    ↓
Name of the environment.

---

## Alternative Environment Name

You can choose another name:

python -m venv myenv

This creates:

myenv/

---

## Example

mkdir python_project

cd python_project

python -m venv venv

---

## Project Structure

python_project/
│
└── venv/

---

## Create Environment Using python3

On some systems:

python3 -m venv venv

This is commonly used on macOS/Linux
when `python` points to another version.

---

## Check Python Version

Windows:

python --version

macOS/Linux:

python3 --version

Example:

Python 3.14.3

---

## Check pip

Windows:

python -m pip --version

macOS/Linux:

python3 -m pip --version

---

## Important

Creating the environment does NOT mean
it is currently active.

After creating it, you normally need to activate it.

---

# ============================================================
# QUICK REVISION
# ============================================================

Create environment:

python -m venv venv

or:

python3 -m venv venv

Flow:

Project folder
    ↓
python -m venv venv
    ↓
venv folder created
    ↓
Activate it