import imp
from itertools import count
from pprint import *
import xml.etree.ElementTree as ET
from weighting import TF
#from preprocess import *

xmldoc = "Helper/doc1.xml"
tree = ET.parse(xmldoc)


arr = [[('LAU', '/university'),
  ('ECE', '/university/faculty/department'),
  ('Joe', '/university/faculty/department/professor'),
  ('Tekli', '/university/faculty/department/professor'),
  ('Wissam', '/university/faculty/department/professor'),
  ('Fawaz', '/university/faculty/department/professor'),
  ('Salim', '/university/faculty/department/student'),
  ('Al', '/university/faculty/department/student'),
  ('Mersally', '/university/faculty/department/student'),
  ('Ahmad', '/university/faculty/department/student'),
  ('Al', '/university/faculty/department/student'),
  ('Sayed', '/university/faculty/department/student'),
  ('Al', '/university/faculty/department/student'),
  ('Sabsabi', '/university/faculty/department/student'),
  ('Lamis', '/university/faculty/laboratory/student'),
  ('Armoush', '/university/faculty/laboratory/student')],
 [('LAU', '/university'),('Lebanese', '/university/name'),      # wa2et nkarer echya bi 2 doc ma 3am te5da 
  ('American', '/university/name'),
  ('University', '/university/name'),
  ('LAU', '/university/shortName'),
  ('LAU', '/university/description'),
  ('is', '/university/description'),
  ('an', '/university/description'),
  ('American', '/university/description'),
  ('university', '/university/description'),
  ('located', '/university/description'),
  ('in', '/university/description'),
  ('Lebanon', '/university/description'),
  ('It', '/university/description'),
  ('is', '/university/description'),
  ('one', '/university/description'),
  ('of', '/university/description'),
  ('the', '/university/description'),
  ('leading', '/university/description'),
  ('American', '/university/description'),
  ('universities', '/university/description'),
  ('in', '/university/description'),
  ('Lebanon', '/university/description'),
  ('A', '/university/description/info/@'),
  ('small', '/university/description/info/@'),
  ('description', '/university/description/info/@'),
  ('Salim', '/university/students/student'),
  ('Al', '/university/students/student'),
  ('Mersally', '/university/students/student'),
  ('Ahmad', '/university/students/student'),
  ('Al', '/university/students/student'),
  ('Sayed', '/university/students/student'),
  ('Al', '/university/students/student'),
  ('Sabsabi', '/university/students/student'),
  ('Lamis', '/university/students/student'),
  ('Armoush', '/university/students/student')],
 [('American', '/university/name'),
  ('Univeristy', '/university/name'),
  ('of', '/university/name'),
  ('Beirut', '/university/name'),
  ('AUB', '/university/shortName'),
  ('AUB', '/university/description'),
  ('is', '/university/description'),
  ('an', '/university/description'),
  ('American', '/university/description'),
  ('university', '/university/description'),
  ('located', '/university/description'),
  ('in', '/university/description'),
  ('Beirut', '/university/description'),
  ('Lebanon', '/university/description'),
  ('It', '/university/description'),
  ('is', '/university/description'),
  ('one', '/university/description'),
  ('of', '/university/description'),
  ('the', '/university/description'),
  ('leading', '/university/description'),
  ('American', '/university/description'),
  ('universities', '/university/description'),
  ('in', '/university/description'),
  ('Lebanon', '/university/description'),
  ('Aman', '/university/students/student'),
  ('Al', '/university/students/student'),
  ('Masri', '/university/students/student'),
  ('Jacob', '/university/students/student'),
  ('Maximus', '/university/students/student'),
  ('Joe', '/university/students/student'),
  ('Malik', '/university/students/student')],
 [('LAU', '/universities/university'),
  ('ECE', '/universities/university/faculty/department'),
  ('Joe', '/universities/university/faculty/department/professor'),
  ('Tekli', '/universities/university/faculty/department/professor'),
  ('Wissam', '/universities/university/faculty/department/professor'),
  ('Fawaz', '/universities/university/faculty/department/professor'),
  ('Salim', '/universities/university/faculty/department/student'),
  ('Al', '/universities/university/faculty/department/student'),
  ('Mersally', '/universities/university/faculty/department/student'),
  ('2222', '/universities/university/faculty/department/student/id/@'),
  ('Ahmad', '/universities/university/faculty/department/student'),
  ('Al', '/universities/university/faculty/department/student'),
  ('Sayed', '/universities/university/faculty/department/student'),
  ('Al', '/universities/university/faculty/department/student'),
  ('Sabsabi', '/universities/university/faculty/department/student'),
  ('4444', '/universities/university/faculty/department/student/id/@'),
  ('Lamis', '/universities/university/faculty/laboratory/student'),
  ('Armoush', '/universities/university/faculty/laboratory/student'),
  ('5959', '/universities/university/faculty/laboratory/student/id/@'),
  ('AUB', '/universities/university'),
  ('ECE', '/universities/university/faculty/department'),
  ('Joe', '/universities/university/faculty/department/professor'),
  ('Tekli', '/universities/university/faculty/department/professor'),
  ('Wissam', '/universities/university/faculty/department/professor'),
  ('Fawaz', '/universities/university/faculty/department/professor'),
  ('Aman', '/universities/university/faculty/department/student'),
  ('Masri', '/universities/university/faculty/department/student'),
  ('1234', '/universities/university/faculty/department/student/id/@'),
  ('Lea', '/universities/university/faculty/department/student'),
  ('Trobat', '/universities/university/faculty/department/student'),
  ('4567', '/universities/university/faculty/department/student/id/@'),
  ('Caylob', '/universities/university/faculty/laboratory/student'),
  ('Maximus', '/universities/university/faculty/laboratory/student'),
  ('1345', '/universities/university/faculty/laboratory/student/id/@')]]

dic = TF(arr)
pprint(dic)
print(dic.get( ('Fawaz', '/universities/university/faculty/department/professor')))
if ('Fawaz', '/universities/university/faculty/department/professor') in dic :
    print("true")
# # print("s")
# # root = tree.getroot()
# # childr = root[0]
# # for child in childr : 
# #     if child.tag == "laboratory" :
# #         childr = child
# #         exit
# # print(child[0].text)
# arr = ["university", "faculty", "department", "student"]
# # print(arr[1])
# root = tree.getroot()
# # root = root[0]
# # root = root [0]
# # root = root [0]
# # print(root)
# # if "Tekli" in root.text :
# #     print("yes")
# c1 = Tf('Ahmad',arr, root,0,0)
# print("My final count of Ahmad : " + str(c1))