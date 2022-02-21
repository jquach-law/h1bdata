from dotenv import load_dotenv
from flask import Flask, jsonify
import psycopg2
import psycopg2.extras
import os

app = Flask(__name__)
load_dotenv()


@app.route("/")
def data():
    conn = psycopg2.connect(os.path.expandvars(os.environ["CRDB_CONN_STR"]))
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT * FROM h1bdata_table")
        rows = cur.fetchall()
        conn.commit()
    return jsonify(rows)