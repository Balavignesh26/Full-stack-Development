from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import re
from pathlib import Path

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-this"   # change in production
DB_PATH = Path(__file__).parent / "data.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    # Server-side validation
    if not name or not email or not message:
        flash("Please fill required fields (Name, Email, Message).")
        return redirect(url_for("home"))

    if not valid_email(email):
        flash("Please use a valid email address.")
        return redirect(url_for("home"))

    conn = get_db()
    conn.execute(
        "INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
        (name, email, subject, message)
    )
    conn.commit()
    conn.close()

    # Redirect to success page (pass name in query string)
    return redirect(url_for("success", name=name))

@app.route("/success")
def success():
    name = request.args.get("name", "")
    return render_template("success.html", name=name)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)