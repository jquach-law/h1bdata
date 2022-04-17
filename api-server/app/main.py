from dotenv import load_dotenv
from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras
from psycopg2 import sql
import os

app = Flask(__name__)
load_dotenv()


@app.route("/")
def all_data():
    conn = psycopg2.connect(os.path.expandvars(os.environ["CRDB_CONN_STR"]))
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT * FROM h1bdata_table")
        rows = cur.fetchall()
        conn.commit()
    return jsonify(rows)


@app.route("/search")
def search():
    employer = request.args.get("employer")
    job_title = request.args.get("job_title")
    city = request.args.get("city")

    employer = employer if employer else ""
    job_title = job_title if job_title else ""
    city = city if city else ""

    conn = psycopg2.connect(os.path.expandvars(os.environ["CRDB_CONN_STR"]))
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        query = sql.SQL(
            """
                SELECT *
                FROM h1bdata_table
                WHERE "EMPLOYER_NAME" LIKE {}
                    AND "JOB_TITLE" LIKE {}
                    AND "EMPLOYER_CITY" LIKE {};
            """
        ).format(
            sql.Literal(f"%{employer}%"),
            sql.Literal(f"%{job_title}%"),
            sql.Literal(f"%{city}%"),
        )
        cur.execute(query)
        rows = cur.fetchall()
        conn.commit()
    return jsonify(rows)
