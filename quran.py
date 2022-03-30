import json
import base64
from typing import Dict
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from quran import Quran
import quran as listsurah
from urllib import parse
import instagram
import pinterest

app = Flask(__name__)
CORS(app)


app.secret_key = "Iniadalahserverinstatools"


@app.route("/")
def index():
    return "HALAMAN INDEX"


@cross_origin()
@app.route("/api/quran", methods=["POST"])
def quran_api():
    if request.method == "POST":
        quran = Quran()
        data = request.get_json()
        if data:
            if data.get("type") == "quran":
                return jsonify(
                    success=True,
                    message="Berhasil",
                    data=[
                        {"surah": surah, "nomor": index}
                        for index, surah in enumerate(listsurah.api_quran.list_quran, 1)
                    ],
                )
            if data.get("type") == "select":
                data = data.get("data")
                if data:
                    surah = data.get("surah")
                    ayat = data.get("ayat")
                    return jsonify(quran.select(surah, ayat))
                else:
                    return jsonify(
                        dict(success=False, message="gagal, param data tidak ada")
                    )
            elif data.get("type") == "surah":
                data = data.get("data")
                if data:
                    surah = data.get("surah")
                    return jsonify(quran.surah(surah))
                else:
                    return jsonify(
                        dict(success=False, message="gagal, param data tidak ada")
                    )
            elif data.get("type") == "specify":
                data = data.get("data")
                if data:
                    surah = data.get("surah")
                    start = data.get("start")
                    end = data.get("end")
                    return jsonify(quran.specify(surah, start=start, end=end))
                else:
                    return jsonify(
                        dict(success=False, message="gagal, param data tidak ada")
                    )
            elif data.get("type") == "search":
                data = data.get("data")
                if data:
                    data = data.get("query")
                    return jsonify(quran.search(data))
            else:
                return jsonify(status=False, message=None)
        else:
            return jsonify(status=False, message=None)
    return jsonify(None)


@app.route("/api/pinterest")
def pin():
    arg = request.args
    query = arg.get("q")
    if query:
        result = pinterest.get_image(query)
    else:
        result = pinterest.get_image("random")
    return jsonify(result)
