from flask import Flask, render_template, request, Response
from functions.Vectors import *
from functions.SimilarityVSM import *

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
def main():
    if request.method == "POST":
        queryVector = getTextQueryVector(request.form["query"])
        queryResult = getAllSimVSM(queryVector, vectors, XMLpaths)

        print("Query Vector")
        pprint(queryVector)
        print("Query result")
        pprint(queryResult)

        return render_template("result.html", queryResult=queryResult)
    print(request)
    return render_template("index.html")


@app.route("/XMLdocuments/doc1.xml")
def getDoc1():
    tree = ET.parse(XMLpaths[0])
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")


@app.route("/XMLdocuments/doc2.xml")
def getDoc2():
    tree = ET.parse(XMLpaths[1])
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")


@app.route("/XMLdocuments/doc3.xml")
def getDoc3():
    tree = ET.parse(XMLpaths[2])
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")


@app.route("/XMLdocuments/doc4.xml")
def getDoc4():
    tree = ET.parse(XMLpaths[3])
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")
