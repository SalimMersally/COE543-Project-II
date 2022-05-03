from flask import Flask, render_template, request
from functions.Vectors import *

app = Flask(__name__)

XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
]

vectors = getAllVectors(XMLpaths)
queryResult = []


@app.route("/", methods=("GET", "POST"))
def hello_world():
    if request.method == "POST":
        pprint(getTextQueryVector(request.form["query"]))
        return request.form["query"]
    print(request)
    return render_template("index.html")
