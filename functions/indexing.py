from functions.Vectors import getAllVectors
from pprint import pprint


def getIndexingTable(listOfVectors):
    out = {}
    for path in listOfVectors:
        vector = listOfVectors[path]
        for dimension in vector:
            term = dimension[0]
            if term in out.keys():
                if path not in out[term]:
                    out[term].append(path)
            else:
                out[term] = [path]
    print("Indexing Table")
    pprint(out)
    return out


def getDocumentFromIndex(indexTable, queryVector, oldVectorList):
    newVectorList = {}

    for dimenion in queryVector:
        term = dimenion[0]
        if term in indexTable:
            docPaths = indexTable[term]
            for path in docPaths:
                if path not in newVectorList:
                    newVectorList[path] = oldVectorList[path]

    print("Document to query from indexing table")
    pprint(newVectorList)
    return newVectorList
