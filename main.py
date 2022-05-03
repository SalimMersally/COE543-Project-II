from copy import deepcopy
import math
from mimetypes import suffix_map
from pprint import pprint

from pathSimilarity import getSimPath


weight = [
    {
        ("LAU", "/university"): math.log(2),
        ("ECE", "/university/faculty/department"): math.log(2),
        ("Joe", "/university/faculty/department/professor"): math.log(2),
    },
    {
        ("LAU", "/university"): 1,
        ("ECE", "/university/faculty/department"): 1,
        ("Joe", "/university/faculty/department/professor"): 1,
    },
    {
        ("A", "/university"): 1,
        ("B", "/university/name"): 1,
        ("C", "/university/name/at/@"): 1,
    },
]


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


sim = getSimVSM(weight[0], weight[1])
print(sim)
