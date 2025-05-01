# Sindhu’s BMI Calculator

A tiny Flask-powered web app that takes your weight (in kilograms) and height (in centimeters), crunches the numbers, and tells you your BMI—fast and simple.

## Quick start

```bash
git clone https://github.com/YOUR‑USERNAME/bmi‑calculator.git
cd bmi‑calculator
python -m venv .venv
source .venv/bin/activate           # Windows → .venv\Scripts\activate
pip install -r requirements.txt
export FLASK_APP=bmi_app.py         # Windows → set FLASK_APP=bmi_app.py
flask run                           # http://127.0.0.1:5000
