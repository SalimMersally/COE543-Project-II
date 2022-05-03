from Vectors import getAllVectors
from pprint import pprint


def getIndexingTable(arrDics,XMLpaths):
    out={}
    i = 0
    for dic in arrDics:
        for key in dic:
            term = key [0] 
            if (term in out.keys()):
                if(XMLpaths[i] not in out[term]):
                    out[term]= out[term] + (XMLpaths[i],)    
            else:
                out[term] = (XMLpaths[i],)
        i +=1;
        
    return out


XMLpaths = [
    "XMLdocuments/doc1.xml",
    "XMLdocuments/doc2.xml",
    "XMLdocuments/doc3.xml",
    "XMLdocuments/doc4.xml",
]

list = getAllVectors(XMLpaths)
dic =  getIndexingTable(list,XMLpaths)

pprint(dic)
