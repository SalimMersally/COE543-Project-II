import xml.etree.ElementTree as ET
import math
from pprint import pprint
from functions.normalizeText import *

# Wd(ti) = TF(ti, D) * IDF(ti, C)
# TF = frequency
# IDF(ti,D) = log (N/DF)      N: nb of indexing nodes in D
# DF(ti,D) is the number of indexing node elements in D containing ti
# t term and D document
# C document collection

# the following method will return a dictionary of an XML tree
# the dictionary will represent the vector of the XML document following the
# term context model
# the key is a tuple (term, path) and the value is the TF
# another method will be used if IDF is needed
def getVectorWithTF(root, path, vector):
    path = path + "/" + root.tag
    attributeDict = root.attrib

    # handling the tags
    tagPath = path
    wordlist = normalizeText(root.tag)
    for word in wordlist:
        dimension = (word, tagPath)
        if dimension in vector:
            vector[dimension] = vector[dimension] + 1
        else:
            vector[dimension] = 1

    # handling the text
    if root.text:
        wordPath = path + "/#"
        wordlist = normalizeText(root.text)
        for word in wordlist:
            dimension = (word, wordPath)
            if dimension in vector:
                vector[dimension] = vector[dimension] + 1
            else:
                vector[dimension] = 1

    # handling the attribute
    for att in attributeDict:
        attributePath = path + "/" + att + "/@"
        wordlist = normalizeText(attributeDict[att])
        for word in wordlist:
            dimension = (word, attributePath)
            if dimension in vector:
                vector[dimension] = vector[dimension] + 1
            else:
                vector[dimension] = 1

    for child in root:
        getVectorWithTF(child, path, vector)


# the following method will return the vector with only TF for only text
# it will be used to get the vector of text query
# we will assume the path is an empty string in this case
def getTextQueryVector(text):
    vector = {}
    wordlist = normalizeText(text)

    for word in wordlist:
        dimension = (word, "")
        if dimension in vector:
            vector[dimension] = vector[dimension] + 1
        else:
            vector[dimension] = 1
    return vector


# the following method will compute the DF of a specific dimension (term, path)
# the list of vectors contains only TF at this stage
def DF(dimension, listOfVectors):
    DF = 0
    for path in listOfVectors:
        vector = listOfVectors[path]
        if dimension in vector:
            DF = DF + 1
    return DF


# in this method we will take the array of vector with TF
# and will add IDF to the weight
# this method will use the DF method
def IDF(listOfVectors):
    for path in listOfVectors:
        vector = listOfVectors[path]
        for dimension in vector:
            vector[dimension] = vector[dimension] * math.log(
                len(listOfVectors) / DF(dimension, listOfVectors)
            )


# the following method will go over all the XML documents, transform them into tree,
# and then get the vector of TF of all of them
def getAllVectors(XMLpaths):
    listOfVectors = {}
    for xmlfile in XMLpaths:
        print(xmlfile)
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        vector = {}
        getVectorWithTF(root, "", vector)
        listOfVectors[xmlfile] = vector

    print("Vectors with only TF")
    pprint(listOfVectors)
    IDF(listOfVectors)
    print("Vectors with TF and IDF")
    pprint(listOfVectors)
    return listOfVectors
