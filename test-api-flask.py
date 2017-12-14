#! /usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 100*"This is NPK!\nThere is no such thing as NPK... is it?"

#if __name__ == "__main__":
app.run(port=5000, threaded=True)



