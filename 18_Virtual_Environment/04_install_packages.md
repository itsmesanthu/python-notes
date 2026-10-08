# ============================================================
# INSTALL PACKAGES
# ============================================================

Once the virtual environment is activated,
we can install Python packages using pip.

---

# ============================================================
# 1. ACTIVATE ENVIRONMENT
# ============================================================

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

---

# ============================================================
# 2. INSTALL A PACKAGE
# ============================================================

Install requests:

pip install requests

---

# ============================================================
# 3. INSTALL DJANGO
# ============================================================

pip install django

---

# ============================================================
# 4. INSTALL MULTIPLE PACKAGES
# ============================================================

pip install django requests pandas

---

# ============================================================
# 5. CHECK INSTALLED PACKAGES
# ============================================================

pip list

This displays installed packages and their versions.

---

# ============================================================
# 6. SHOW PACKAGE INFORMATION
# ============================================================

pip show django

This displays information such as:

Name
Version
Location
Dependencies

---

# ============================================================
# 7. INSTALL SPECIFIC VERSION
# ============================================================

pip install django==5.2.17

This installs the specified version.

---

# ============================================================
# 8. UPGRADE PACKAGE
# ============================================================

pip install --upgrade django

This upgrades the package to a newer available version.

---

# ============================================================
# 9. UNINSTALL PACKAGE
# ============================================================

pip uninstall django

---

# ============================================================
# 10. INSTALL FROM requirements.txt
# ============================================================

pip install -r requirements.txt

This installs the packages listed
inside requirements.txt.

---

# ============================================================
# EXAMPLE
# ============================================================

Suppose requirements.txt contains:

Django==5.2.17
requests==2.32.5
pandas==2.3.3

Run:

pip install -r requirements.txt

The listed packages will be installed.

---

# ============================================================
# QUICK REVISION
# ============================================================

Install:
pip install package_name

Specific version:
pip install package_name==version

Multiple packages:
pip install package1 package2

List packages:
pip list

Package information:
pip show package_name

Upgrade:
pip install --upgrade package_name

Uninstall:
pip uninstall package_name

Install requirements:
pip install -r requirements.txt