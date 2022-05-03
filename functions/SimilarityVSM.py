import math
from pprint import pprint

from functions.pathSimilarity import getSimPath


def getSimVSM(queryVector, DocumentVector):
    num = 0

    for dimension1 in queryVector:
        term1 = dimension1[0]

        for dimension2 in DocumentVector:
            term2 = dimension2[0]
            if term1 == term2:
                simPath = getSimPath(dimension1[1], dimension2[1])
                num = num + (
                    queryVector[dimension1] * DocumentVector[dimension2] * simPath
                )

    sumVector1 = 0
    sumVector2 = 0
    for dimension in queryVector:
        sumVector1 = sumVector1 + queryVector[dimension] ** 2

    for dimension in DocumentVector:
        sumVector2 = sumVector2 + DocumentVector[dimension] ** 2

    return num / math.sqrt(sumVector1 * sumVector2)


# the following method will get the similarity of the query vector with each document in the
# list of document provided
# it will sort them by decreasing order after that
def getAllSimVSM(queryVector, listOfDocumentVector, XMLPaths):
    simList = []
    i = 0
    for documentVector in listOfDocumentVector:
        sim = getSimVSM(queryVector, documentVector)
        simList.append((XMLPaths[i], sim))
        i = i + 1

    return sorted(simList, key=lambda tuple: tuple[1], reverse=True)
