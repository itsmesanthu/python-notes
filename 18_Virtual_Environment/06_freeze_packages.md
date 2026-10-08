# ============================================================
# FREEZE PACKAGES
# ============================================================

## What is pip freeze?

`pip freeze` displays the packages installed
in the current Python environment.

It also displays their exact versions.

---

# ============================================================
# 1. BASIC pip freeze
# ============================================================

Run:

pip freeze

Example output:

Django==5.2.17
pandas==2.3.3
requests==2.32.5

---

# ============================================================
# 2. SAVE PACKAGES TO requirements.txt
# ============================================================

Run:

pip freeze > requirements.txt

This creates or replaces:

requirements.txt

with the packages installed in the
current environment.

---

# ============================================================
# 3. VIEW requirements.txt
# ============================================================

Example:

Django==5.2.17
pandas==2.3.3
requests==2.32.5

---

# ============================================================
# 4. INSTALL FROM THE FILE
# ============================================================

On another machine:

pip install -r requirements.txt

This installs the listed packages.

---

# ============================================================
# 5. WHY pip freeze IS USEFUL
# ============================================================

It helps to:

1. Record installed packages
2. Record package versions
3. Recreate an environment
4. Share project dependencies
5. Support deployment

---

# ============================================================
# COMPLETE WORKFLOW
# ============================================================

Create:

python -m venv venv

        ↓

Activate:

source venv/bin/activate

        ↓

Install:

pip install django pandas requests

        ↓

Work on project

        ↓

Freeze:

pip freeze > requirements.txt

        ↓

Share project

        ↓

Another developer:

python -m venv venv

        ↓

Activate environment

        ↓

pip install -r requirements.txt

---

# ============================================================
# QUICK REVISION
# ============================================================

pip freeze

    ↓

Shows installed packages.

pip freeze > requirements.txt

    ↓

Saves installed packages and versions.

pip install -r requirements.txt

    ↓

Installs packages from the file.