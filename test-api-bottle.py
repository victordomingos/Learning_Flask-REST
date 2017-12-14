from bottle import default_app, post, get, put, delete, request, response

app = application = default_app()

@get('/')
def index():
    return 3000*"This is NPK!\nThere is no such thing as NPK... is it?"

if __name__ == "__main__":
    app.run(port=1200, threaded=True)


