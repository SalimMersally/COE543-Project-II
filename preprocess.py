import xml.etree.ElementTree as ET
import string

def preprocess(root,path,dic):
    
    attdic = root.attrib        
    wordlist = root.text.translate(str.maketrans(' ', ' ', string.punctuation)).split()
    path = path+ "/" + root.tag  
    
    for word in wordlist:
        tuple = (word, path)
        available = False
        for key in dic:
            if (tuple == key):
                available = True
        if(available):
            dic[tuple] = dic[tuple]+1
        else:
            dic[tuple]=1

    for att in attdic:
        attpath = path + "/" + att+ "/@"
        value = attdic [att]
        tuple = (value, attpath)
        available=False
        
        for key in dic:
            if (tuple == key):
                available = True
        if(available):
            dic[tuple] = dic[tuple]+1
        else:
            dic[tuple]=1
                
    for child in root: 
        preprocess(child, path, dic)

def getPaths(root,path,list):
    
    attdic = root.attrib        
    wordlist = root.text.translate(str.maketrans(' ', ' ', string.punctuation)).split()
    path = path+ "/" + root.tag  
    
    for word in wordlist:
        tuple = (word, path)
        list.append(tuple)

    for att in attdic:
        attpath = path + "/" + att+ "/@"
        value = attdic [att]
        tuple = (value, attpath)
        list.append(tuple)
        
               
    for child in root: 
       getPaths(child, path, list)

def getAllTerms(docarr,list):
    for xmlfile in docarr:
        tree = ET.parse(xmlfile)
        root = tree.getroot() 
        path= ""
        pathlist = []
        getPaths(root,path,pathlist)
        list.append(pathlist)
    
        
docarr =[ "XMLdocuments/doc2.xml", "XMLdocuments/doc1.xml" ]
list=[]
getAllTerms(docarr,list)
    
print(list)