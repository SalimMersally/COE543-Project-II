import xml.etree.ElementTree as ET
import string
from pprint import pprint


def getPaths(root, path, list):

    path = path + "/" + root.tag
    attributeDict = root.attrib

    if root.text:
        wordlist = root.text.translate(
            str.maketrans(" ", " ", string.punctuation)
        ).split()

        for word in wordlist:
            tuple = (word, path)
            list.append(tuple)

    for att in attributeDict:
        attributePath = path + "/" + att + "/@"
        wordlist = (
            attributeDict[att]
            .translate(str.maketrans(" ", " ", string.punctuation))
            .split()
        )
        for word in wordlist:
            tuple = (word, attributePath)
            list.append(tuple)

    for child in root:
        getPaths(child, path, list)


def getAllTerms(XMLpaths):
    list = []
    for xmlfile in XMLpaths:
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        pathlist = []
        getPaths(root, "", pathlist)
        list.append(pathlist)
    return list


XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
]
list = getAllTerms(XMLpaths)

pprint(list)
