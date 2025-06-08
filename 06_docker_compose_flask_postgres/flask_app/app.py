from flask import Flask, request, render_template_string
import time
import psycopg2
import os

time.sleep(5)

app = Flask(__name__)
conn = psycopg2.connect(os.environ["DATABASE_URL"])
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS submissions (id SERIAL PRIMARY KEY, name TEXT);")
conn.commit()

HTML = """
<form method="post">
  Name: <input name="name">
  <input type="submit">
</form>
{% if name %}
  <p>Hello, {{ name }}! Thanks for submitting.</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        name = request.form["name"]
        cur.execute("INSERT INTO submissions (name) VALUES (%s);", (name,))
        conn.commit()
    return render_template_string(HTML, name=name)
