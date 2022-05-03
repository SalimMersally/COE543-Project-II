# Wd(ti) = TF(ti, D) * IDF(ti, C)
# TF = frequency 
# IDF(ti,D) = log (N/DF)      N: nb of indexing nodes in D
# DF(ti,D) is the number of indexing node elements in D containing ti
# t term and D document 
# C document collection
from math import *
import math
from pprint import pprint
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

def DF(list) :
    newList = []
    for doc in list:
        newDic = {}
        for tuple in doc:
            frq = 0
            for doc2 in list:
                if tuple in doc2 :
                    frq = frq + 1
                    newDic[tuple] = frq
        newList.append(newDic)
    return newList 

def IDF(listFreq, listInvFreq) :
    finalList = []
    i = 0
    for doc in listFreq:
        
        dic = {}
        for tuple in doc:
            
            dic[tuple] = doc.get(tuple) * math.log((len(listFreq)) / (listInvFreq[i].get(tuple)))
        i = i+1
        pprint(dic)
        finalList.append(dic)

    return finalList


# No need for them now
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
     