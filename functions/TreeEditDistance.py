# the following method will calculate the Edit Distance Matrices
# to transform treeA into treeB following Nermin and Jagadish algorithm
# this method take into considiration all tags, text and attributes


def NJ(A, B, nameA, nameB, matricesDic):

    subTreeA = findSubTree(A, nameA)
    subTreeB = findSubTree(B, nameB)

    M = len(subTreeA)  # number of first Level children in A
    N = len(subTreeB)  # number of first Level children in B

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = costUpd(subTreeA, subTreeB, nameA, nameB, matricesDic)

    i = 1
    j = 1
    for childA in subTreeA:
        Distance[i][0] = Distance[i - 1][0] + costDelete(childA, B)
        i += 1

    for childB in subTreeB:
        Distance[0][j] = Distance[0][j - 1] + costInsert(childB, A)
        j += 1

    i = 1
    for childA in subTreeA:

        j = 1
        for childB in subTreeB:
            childAName = nameA + "-" + str(i - 1)
            childBName = nameB + "-" + str(j - 1)

            Distance[i][j] = min(
                (
                    Distance[i - 1][j - 1]
                    + NJ(A, B, childAName, childBName, matricesDic)
                ),
                (Distance[i - 1][j] + costDelete(childA, B)),
                (Distance[i][j - 1] + costInsert(childB, A)),
            )
            j += 1
        i += 1

    matricesDic[nameA + "/" + nameB] = Distance
    return Distance[M][N]


def getAllSimTED(queryRoot, documentsRoot, XMLPaths):
    simList = []
    i = 0
    for root in documentsRoot:
        distance = NJ(queryRoot, root, "Q", "D", {})
        sim = 1 - distance / (nodeCounter(queryRoot) + nodeCounter(root))
        sim = round(sim, 3)
        simList.append((XMLPaths[i], sim))
        i = i + 1

    return sorted(simList, key=lambda tuple: tuple[1], reverse=True)


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration all Tags, attributes, and text
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes + words + att
#   - InsTree = 1 if subtree available in A, else sum of nodes + words + att
#   - UpdTag = 1 if tags are diffent, 0 if same + cost of upd text + cost of upd att


def findSubTree(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


def isTreeIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.tag != root2.tag:
        return False
    if root1.text != root2.text:
        return False
    if root1.attrib != root2.attrib:
        return False
    if len(root1) != len(root2):
        return False
    for i in range(0, len(root1)):
        if not isTreeIdentical(root1[i], root2[i]):
            return False
    return True


def isSubTree(root1, root2):
    if root1 is None:
        return True

    if root2 is None:
        return False

    if isTreeIdentical(root1, root2):
        return True

    for i in range(0, len(root2)):
        if isSubTree(root1, root2[i]):
            return True

    return False


def nodeCounter(root):
    counter = 0

    if root is None:
        return counter

    counter += 1

    if root.text is not None:
        counter += len(root.text.split())

    if root.attrib != {}:
        counter += len(root.attrib.keys()) + len(root.attrib.values())

    for child in root:
        counter += nodeCounter(child)

    return counter


def costInsert(subTreeB, A):
    if isSubTree(subTreeB, A):
        return 1
    else:
        return nodeCounter(subTreeB)


def costDelete(subTreeA, B):
    if isSubTree(subTreeA, B):
        return 1
    else:
        return nodeCounter(subTreeA)


def costUpd(rootA, rootB, nameA, nameB, matricesDic):
    cost = 0

    if rootA.tag != rootB.tag:
        cost += 1

    if (rootA.text is not None) or (rootB.text is not None):
        textA = rootA.text
        textB = rootB.text
        if textA is None:
            textA = ""
        if textB is None:
            textB = ""
        distanceOfText = WF_Array(textA, textB)
        matricesDic[nameA + "/" + nameB + "/text"] = distanceOfText
        cost += distanceOfText[len(textA.split())][len(textB.split())]

    if (rootA.attrib != {}) or (rootB.attrib != {}):
        distanceOfAtt = WF_Dict(rootA.attrib, rootB.attrib)
        matricesDic[nameA + "/" + nameB + "/attribute"] = distanceOfAtt
        cost += distanceOfAtt[len(distanceOfAtt) - 1][len(distanceOfAtt[0]) - 1]

    return cost


# the following method are used to get the edit distance, edit script, and
# patch a dictionary (to be used for attribute and value of trees)
# the algorithm follow wagnar and fisher approach but with tuples of 2 words
# instead of one. the cost model is as follow:
#   - InsAtt = 2
#   - DelAtt = 2
#   - UpdAtt = 0 if same, 1 if same but diff value, 2 if att and val diff


def WF_Dict(dictA, dictB):

    listA = list(dictA.items())
    listB = list(dictB.items())

    M = len(listA)
    N = len(listB)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelAtt()
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsAtt()

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1] + costUpdAtt(listA[i - 1], listB[j - 1]),
                Distance[i - 1][j] + costDelAtt(),
                Distance[i][j - 1] + costInsAtt(),
            )

    return Distance


def costUpdAtt(A, B):
    if A[0] == B[0] and A[1] == B[1]:
        return 0
    elif A[0] == B[0]:
        return 1
    else:
        return 2


def costInsAtt():
    return 2


def costDelAtt():
    return 2


# the following method will compare two array of words following the
# Wagnar and Fisher algorithm (assuming the element to comapre are words and not
# character). the cost model is as follow:
#   - costDelWord = 1
#   - costInsWord = 1
#   - costUpdWord = 0 if same, 1 if different
# note that we assumed the comparision is case sensitive


def WF_Array(A, B):

    tokenA = A.split()
    tokenB = B.split()

    M = len(tokenA)
    N = len(tokenB)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelWord()
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsWord()

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1] + costUpdWord(tokenA[i - 1], tokenB[j - 1]),
                Distance[i - 1][j] + costDelWord(),
                Distance[i][j - 1] + costInsWord(),
            )

    return Distance


def costUpdWord(A, B):
    if A == B:
        return 0
    return 1


def costInsWord():
    return 1


def costDelWord():
    return 1
