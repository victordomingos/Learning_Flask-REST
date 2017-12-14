#! /usr/bin/env python3

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    return 100*'Hello! This is KPK.'

app.run()
