from glob import escape
import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request, Response
from functions.Vectors import *
from functions.SimilarityVSM import *
from functions.TreeEditDistance import *
from functions.indexing import *
from functions.normalizeText import *

app = Flask(__name__)

XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
    "XMLdocuments/food1.xml",
    "XMLdocuments/food2.xml",
    "XMLdocuments/food3.xml",
    "XMLdocuments/food4.xml",
    "XMLdocuments/food5.xml",
    "XMLdocuments/food6.xml",
    "XMLdocuments/food7.xml",
    "XMLdocuments/food8.xml",
    "XMLdocuments/food9.xml",
    "XMLdocuments/food10.xml",
    "XMLdocuments/food11.xml",
    "XMLdocuments/food12.xml",
    "XMLdocuments/food13.xml",
    "XMLdocuments/food14.xml",
    "XMLdocuments/food15.xml",
    "XMLdocuments/food16.xml",
    "XMLdocuments/food17.xml",
    "XMLdocuments/food18.xml",
    "XMLdocuments/food19.xml",
    "XMLdocuments/food20.xml",
    "XMLdocuments/food21.xml",
    "XMLdocuments/food22.xml",
    "XMLdocuments/food23.xml",
    "XMLdocuments/food24.xml",
    "XMLdocuments/food25.xml",
    "XMLdocuments/food26.xml",
    "XMLdocuments/food27.xml",
    "XMLdocuments/food28.xml",
    "XMLdocuments/food29.xml",
    "XMLdocuments/food30.xml",
    "XMLdocuments/food31.xml",
    "XMLdocuments/food32.xml",
    "XMLdocuments/food33.xml",
    "XMLdocuments/food34.xml",
    "XMLdocuments/food35.xml",
    "XMLdocuments/food36.xml",
    "XMLdocuments/city1.xml",
    "XMLdocuments/city2.xml",
    "XMLdocuments/city3.xml",
]

vectors = getAllVectors(XMLpaths)
indexTable = getIndexingTable(vectors)


roots = []
for path in XMLpaths:
    tree = ET.parse(path)
    root = tree.getroot()
    roots.append(root)

queryResult = []


@app.route("/", methods=("GET", "POST"))
def main():
    if request.method == "POST":
        timeBefore = time.time()
        queryVector = {}
        queryResult = []

        if request.form["queryType"] == "text":
            queryVector = getTextQueryVector(request.form["query"])
        else:
            tree = ET.ElementTree(ET.fromstring(request.form["query"]))
            root = tree.getroot()
            getVectorWithTF(root, "", queryVector)

        if request.form["simType"] == "VSM":
            newVectorList = getDocumentFromIndex(indexTable, queryVector, vectors)
            queryResult = getAllSimVSM(queryVector, newVectorList)
        else:
            tree = ET.ElementTree(ET.fromstring(request.form["query"]))
            root = tree.getroot()
            queryResult = getAllSimTED(root, roots, XMLpaths)

        timeAfter = time.time()

        print("Query Vector")
        pprint(queryVector)
        print("Query result")
        pprint(queryResult)

        timeTaken = round(timeAfter - timeBefore, 4)

        return render_template("result.html", queryResult=queryResult, time=timeTaken)

    print(request)
    return render_template("index.html")


@app.route("/<folder>/<doc>")
def getDoc1(folder, doc):
    tree = ET.parse(folder + "/" + doc)
    root = tree.getroot()
    xmlstr = ET.tostring(root, encoding="utf8", method="xml")
    return Response(xmlstr, mimetype="text/xml")
