import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request, Response
from functions.Vectors import *
from functions.SimilarityVSM import *
from functions.TreeEditDistance import *
from functions.indexing import *

app = Flask(__name__)

XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
    "XMLdocuments/SampleDoc1.xml",
    "XMLdocuments/SampleDoc2.xml",
    "XMLdocuments/SampleLarge.xml",
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
