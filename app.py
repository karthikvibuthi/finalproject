from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extract_email(text):
    """Extracts email from resume text."""
    email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    return email[0].split()[0].strip(';') if email else None

@app.route("/", methods=["GET", "POST"])
def index():
    email = None
    if request.method == "POST":
        resume_text = request.form.get("resume_text")
        if resume_text:
            email = extract_email(resume_text)
    return render_template("index.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)
