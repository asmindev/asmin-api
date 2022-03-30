from flask import Flask, request, jsonify
from flask_cors import CORS
import instagram
from pinterest import get_image

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    text = {"message": "Hello from my server"}
    return jsonify(text)


@app.route("/api/v1/instagram/stories")
def stories():
    if request.method == "GET":
        arg = request.args
        if arg:
            if "q" in arg:
                target = arg["q"]
                if target:
                    result = instagram.stories(target)
                    return jsonify(result)
        return jsonify({"error": "query is required"})
    else:
        return jsonify({"message": "Hello from my server"})


@app.route("/api/v1/instagram/reels")
def reels():
    if request.method == "GET":
        arg = request.args
        if arg:
            if "url" in arg:
                url = arg["url"]
                result = instagram.reels(url)
                return jsonify(result)
        return jsonify({"error": "url is required"})
    else:
        text = {"message": "Hello from my server"}
        return jsonify(text)


@app.route("/api/v1/pinterest")
def pinterest():
    if request.method == "GET":
        arg = request.args
        if arg:
            if "query" in arg:
                query = arg["query"]
                result = get_image(query)
                return jsonify(result)
        return jsonify({"error": "query is required"})
    else:
        text = {"message": "Hello from my server"}
        return jsonify(text)


app.run(debug=True)
