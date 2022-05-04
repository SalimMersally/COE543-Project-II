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

XMLpaths1 = [
    "XMLdocuments1/city1.xml",
    "XMLdocuments1/city2.xml",
    "XMLdocuments1/city3.xml",
    "XMLdocuments1/city4.xml",
    "XMLdocuments1/city5.xml",
    "XMLdocuments1/university1.xml",
    "XMLdocuments1/university2.xml",
    "XMLdocuments1/university3.xml",
    "XMLdocuments1/university4.xml",
    "XMLdocuments1/food1.xml",
    "XMLdocuments1/food2.xml",
    "XMLdocuments1/food3.xml",
    "XMLdocuments1/food4.xml",
    "XMLdocuments1/food5.xml",
    "XMLdocuments1/food6.xml",
    "XMLdocuments1/food7.xml",
    "XMLdocuments1/food8.xml",
    "XMLdocuments1/food9.xml",
    "XMLdocuments1/food10.xml",
    "XMLdocuments1/food11.xml",
    "XMLdocuments1/food12.xml",
    "XMLdocuments1/food13.xml",
    "XMLdocuments1/food14.xml",
    "XMLdocuments1/food15.xml",
    "XMLdocuments1/food16.xml",
    "XMLdocuments1/food17.xml",
    "XMLdocuments1/food18.xml",
    "XMLdocuments1/food19.xml",
    "XMLdocuments1/food20.xml",
    "XMLdocuments1/food21.xml",
    "XMLdocuments1/food22.xml",
    "XMLdocuments1/food23.xml",
    "XMLdocuments1/food24.xml",
    "XMLdocuments1/food25.xml",
    "XMLdocuments1/food26.xml",
    "XMLdocuments1/food27.xml",
    "XMLdocuments1/food28.xml",
    "XMLdocuments1/food29.xml",
    "XMLdocuments1/food30.xml",
    "XMLdocuments1/food31.xml",
    "XMLdocuments1/food32.xml",
    "XMLdocuments1/food33.xml",
    "XMLdocuments1/food34.xml",
    "XMLdocuments1/food35.xml",
    "XMLdocuments1/food36.xml",
]

XMLpaths2 = [
    "XMLdocuments2/university1.xml",
    "XMLdocuments2/university2.xml",
    "XMLdocuments2/university3.xml",
    "XMLdocuments2/university4.xml",
    "XMLdocuments2/food1.xml",
    "XMLdocuments2/food2.xml",
    "XMLdocuments2/food3.xml",
    "XMLdocuments2/food4.xml",
    "XMLdocuments2/food5.xml",
    "XMLdocuments2/food6.xml",
    "XMLdocuments2/food7.xml",
    "XMLdocuments2/food8.xml",
    "XMLdocuments2/food9.xml",
    "XMLdocuments2/food10.xml",
    "XMLdocuments2/food11.xml",
    "XMLdocuments2/food12.xml",
    "XMLdocuments2/food13.xml",
    "XMLdocuments2/food14.xml",
    "XMLdocuments2/food15.xml",
    "XMLdocuments2/food16.xml",
    "XMLdocuments2/food17.xml",
    "XMLdocuments2/food18.xml",
    "XMLdocuments2/food19.xml",
    "XMLdocuments2/food20.xml",
    "XMLdocuments2/food21.xml",
    "XMLdocuments2/food22.xml",
    "XMLdocuments2/food23.xml",
    "XMLdocuments2/food24.xml",
    "XMLdocuments2/food25.xml",
    "XMLdocuments2/food26.xml",
    "XMLdocuments2/food27.xml",
    "XMLdocuments2/food28.xml",
    "XMLdocuments2/food29.xml",
    "XMLdocuments2/food30.xml",
    "XMLdocuments2/food31.xml",
    "XMLdocuments2/food32.xml",
    "XMLdocuments2/food33.xml",
    "XMLdocuments2/food34.xml",
    "XMLdocuments2/food35.xml",
    "XMLdocuments2/food36.xml",
]


vectors = getAllVectors(XMLpaths1)
indexTable = getIndexingTable(vectors)


roots = []
for path in XMLpaths1:
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
            queryResult = getAllSimTED(root, roots, XMLpaths1)

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
