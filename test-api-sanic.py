#! /usr/bin/env python3
from sanic import Sanic
from sanic.response import json, text

app = Sanic()

@app.route("/")
async def test(request):
    return text(300*"Hello! This is NPK through a Sanic app!")
    # return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, workers=4)
