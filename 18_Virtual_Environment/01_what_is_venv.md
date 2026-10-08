# ============================================================
# VIRTUAL ENVIRONMENT
# ============================================================

## What is a Virtual Environment?

A virtual environment is an isolated Python environment
created for a particular project.

It allows each project to have its own Python packages
and package versions.

---

## Why Do We Need a Virtual Environment?

Suppose we have two projects:

Project A:
    Django 4.2

Project B:
    Django 5.2

If both projects use the same global Python environment,
different package versions can cause conflicts.

A virtual environment solves this problem.

Each project can have its own environment:

Project A
    ↓
Virtual Environment A
    ↓
Django 4.2


Project B
    ↓
Virtual Environment B
    ↓
Django 5.2

---

## Main Advantages

1. Package isolation
2. Different package versions
3. Avoids dependency conflicts
4. Keeps projects clean
5. Useful for deployment
6. Makes projects easier to reproduce

---

## Important Terms

### Global Environment

The Python environment installed on your computer.

Packages installed globally can be available
to multiple projects.

---

### Virtual Environment

An isolated environment created for one project.

Packages installed inside it are normally available
only inside that environment.

---

## Python venv Module

Python provides the built-in `venv` module
for creating virtual environments.

No separate installation is normally required.

---

## Basic Flow

Project
    ↓
Create Virtual Environment
    ↓
Activate Environment
    ↓
Install Packages
    ↓
Work on Project
    ↓
Freeze Packages
    ↓
requirements.txt
    ↓
Share / Deploy Project

---

## Example Project Structure

my_project/
│
├── venv/
├── app.py
├── requirements.txt
└── README.md

---

## Important Note

The virtual environment folder is usually NOT uploaded
to GitHub.

Instead, we share:

requirements.txt

Other developers can create their own environment
and install the required packages.

# ============================================================
# QUICK REVISION
# ============================================================

Virtual Environment
    ↓
Isolated Python environment.

venv
    ↓
Python module used to create virtual environments.

Main purpose
    ↓
Avoid package and dependency conflicts.