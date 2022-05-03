from pprint import pp, pprint


# the following method will compare two array of words following the
# Wagnar and Fisher algorithm (assuming the element to comapre are words and not
# character). the cost model is as follow:
#   - costDelWord = 1
#   - costInsWord = 1
#   - costUpdWord = 0 if same, 1 if different
# note that we assumed the comparision is case sensitive


def WF(A, B):

    M = len(A)
    N = len(B)

    Distance = [[None for i in range(N + 1)] for i in range(M + 1)]
    Distance[0][0] = 0

    for i in range(1, M + 1):
        Distance[i][0] = Distance[i - 1][0] + costDelWord()
    for j in range(1, N + 1):
        Distance[0][j] = Distance[0][j - 1] + costInsWord()

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            Distance[i][j] = min(
                Distance[i - 1][j - 1] + costUpdWord(A[i - 1], B[j - 1]),
                Distance[i - 1][j] + costDelWord(),
                Distance[i][j - 1] + costInsWord(),
            )

    return Distance[M][N]


def costUpdWord(A, B):
    if A == B:
        return 0
    return 1


def costInsWord():
    return 1


def costDelWord():
    return 1


# this method will be used to get the similarity between
# two pathes based on wagner and fisher
def getSimPath(path1, path2):
    array1 = path1.split("/")
    array2 = path2.split("/")
    distance = WF(array1, array2)

    sim = 1 - (distance / (len(array1) + len(array2)))
    return sim
