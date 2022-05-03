# Wd(ti) = TF(ti, D) * IDF(ti, C)
# TF = frequency 
# IDF(ti,D) = log (N/DF)      N: nb of indexing nodes in D
# DF(ti,D) is the number of indexing node elements in D containing ti
# t term and D document 
# C document collection
from itertools import count
import xml.etree.ElementTree as ET
# NEED TO 
def TF(listOfDoc) :
    list = []
    
    for doc in listOfDoc:
        dic = {}
        for tuple in doc:
            if tuple in dic :
                dic[tuple] = dic.get(tuple) + 1
            else :
                dic[tuple] = 1

            #     if tuple == n:
            #         frq = frq + 1
            # dic[tuple] = frq
        list.append(dic)

    return list

def DF() :

    return


# def Tf(name , pathArr,root, c, counter) :
#     #print(root.tag)
#     #print(root.text)
#     #if name in root.text :
#     #    counter = counter + count(name)

#     wordlist = root.text.split()
#     #print(wordlist)
#     for w in wordlist:
#         if w ==  name :
#             counter = counter + 1
#     #print("counter now :" + str(counter))    
#     c = c + 1
#     if c == len(pathArr) :
#     #   print("to return " +  str(counter))
#         return counter 
#     f = []
#     for child in root :
#         if child.tag == pathArr[c] :
#             root = child
#             f.append(root)
#     print(f)
#     return Tf(name , pathArr,root,c, counter)
     