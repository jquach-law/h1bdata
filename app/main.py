from dotenv import load_dotenv
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)
load_dotenv()


@app.route("/")
def data():
    conn = psycopg2.connect(os.environ["CRDB_CONN_STR"])
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM exam_score")
        rows = cur.fetchall()
        conn.commit()
    return jsonify(rows)
