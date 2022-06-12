from dotenv import load_dotenv
from flask import Flask, jsonify, request
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


@app.route("/search")
def search():
    employer = request.args.get("employer")
    job_title = request.args.get("job_title")
    city = request.args.get("city")

    conn = psycopg2.connect(os.path.expandvars(os.environ["CRDB_CONN_STR"]))
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        # TODO: Look up ways to sanitize query / prevent SQL injection attacks.
        query = f"""
            SELECT *
            FROM h1bdata_table
        """
        # TODO: Refactor to make it cleaner.
        if employer or job_title or city:
            is_first_where_condition = True
            query += """
            WHERE
            """
            if employer:
                query += f"""
            {"AND " if not is_first_where_condition else ""}"EMPLOYER_NAME" LIKE '%{employer if employer else ""}%'
                """
                is_first_where_condition = False
            if job_title:
                query += f"""
            {"AND " if not is_first_where_condition else ""}"JOB_TITLE" LIKE '%{job_title if job_title else ""}%'
                """
                is_first_where_condition = False
            if city:
                query += f"""
            {"AND " if not is_first_where_condition else ""}"EMPLOYER_CITY" LIKE '%{city if city else ""}%'
                """
                is_first_where_condition = False

        cur.execute(query)
        rows = cur.fetchall()
        conn.commit()
    return jsonify(rows)
