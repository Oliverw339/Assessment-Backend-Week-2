"""An API for handling marine experiments."""

from datetime import datetime

from flask import Flask, jsonify, request
from psycopg2 import sql

from database_functions import get_db_connection


app = Flask(__name__)

"""
For testing reasons; please ALWAYS use this connection. 

- Do not make another connection in your code
- Do not close this connection

If you do not understand this instructions; as a coach to explain
"""
conn = get_db_connection("marine_experiments")


@app.get("/")
def home():
    """Returns an informational message."""
    return jsonify({
        "designation": "Project Armada",
        "resource": "JSON-based API",
        "status": "Classified"
    })


def get_exp_by_type(exp_type):
    cursor = conn.cursor()
    query = """ SELECT * 
    FROM experiment 
    JOIN experiment_type USING(experiment_type_id) 
    WHERE experiment.type_name = %(exp_type)s;
    """
    cursor.execute(query, {'experiment_type': exp_type})
    rows = cursor.fetchall()
    cursor.close()
    return rows


def get_above_score(score):
    cursor = conn.cursor()
    query = """ SELECT * 
    FROM experiment  
    WHERE experiment.score > %(score)s;
    """
    cursor.execute(query, {'score': score})
    rows = cursor.fetchall()
    cursor.close()
    return rows


@app.route("/experiment", methods=['GET'])
def experiments_search():
    exp_type = request.args.get('type')
    exp_score_over = request.args.get('score_over')

    exp_types = ["intelligence", "obedience", "aggression"]
    scores = [i for i in range(0, 101)]

    if exp_type not in exp_types:
        return {"error": "Invalid value for type parameter"}, 400

    if exp_score_over not in scores:
        return {"error": "Invalid value for score parameter"}, 400

    if exp_types != None:
        return list(get_exp_by_type(exp_type)), 200

    if exp_score_over != None:
        return list(get_above_score(exp_score_over)), 200


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.config["TESTING"] = True

    app.run(port=8000, debug=True)

    conn.close()
