# ============================================================
# ACTIVATE VIRTUAL ENVIRONMENT
# ============================================================

After creating a virtual environment,
we need to activate it.

The activation command depends on the operating system.

---

# WINDOWS

## Command Prompt

Run:

venv\Scripts\activate

After activation, you may see:

(venv)

at the beginning of the terminal.

Example:

(venv) C:\Users\Santhu\project>

---

## PowerShell

Run:

.\venv\Scripts\Activate.ps1

Example:

(venv) PS C:\Users\Santhu\project>

---

# macOS / LINUX

Run:

source venv/bin/activate

Example:

(venv) santhu@Mac project %

---

# ============================================================
# CHECK WHETHER ENVIRONMENT IS ACTIVE
# ============================================================

Look at the terminal.

If you see:

(venv)

the virtual environment is active.

---

# ============================================================
# CHECK PYTHON
# ============================================================

Windows:

where python

macOS/Linux:

which python

The path should point to the virtual environment.

---

# ============================================================
# CHECK PIP
# ============================================================

Windows:

where pip

macOS/Linux:

which pip

The path should point to the virtual environment.

---

# ============================================================
# DEACTIVATE
# ============================================================

To leave the virtual environment:

deactivate

The `(venv)` should disappear.

---

# ============================================================
# COMPLETE FLOW
# ============================================================

Create:

python -m venv venv

        ↓

Activate:

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

        ↓

Install packages

        ↓

Work on project

        ↓

Deactivate:

deactivate

# ============================================================
# QUICK REVISION
# ============================================================

Windows CMD:
venv\Scripts\activate

Windows PowerShell:
.\venv\Scripts\Activate.ps1

macOS/Linux:
source venv/bin/activate

Deactivate:
deactivate