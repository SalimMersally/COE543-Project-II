from preprocess import getAllTerms
from pprint import pprint

def getIndexingTable(list,XMLpaths):
    dic={"":()}
    i =0
    for arr in list:
        for tuple in arr:
            term = tuple[0]
            if term in dic:
                if XMLpaths[i] not in dic[term] :
                    dic[term]=dic[term]+ (XMLpaths[i],)
            else:
                dic[term] = (XMLpaths[i],)
        i +=1;
        
    return dic

XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
]
list = getAllTerms(XMLpaths)
dic =  getIndexingTable(list,XMLpaths)
pprint(dic)

           
