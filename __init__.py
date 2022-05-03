#!/usr/bin/python3.6

from flask import Flask


app = Flask(__name__)


@app.route('/down')
def down():
        return {"status": "DOWN", "response": False }

