import xml.etree.cElementTree as ET
from nltk import word_tokenize
from nltk.tag import pos_tag
import string
import networkx as nx



prime_dict={}
file1=open("dict.txt","r")
file2=open("distance.txt","w")
file3=open("graph_modified.txt","r")

g=nx.Graph()

for line in file3:
    words=line.split()
    l1=[]
    for ele in words:
        int_ele=int(ele)
        l1.append(int_ele)
    t1=tuple(l1)
    l2=[t1]
    g.add_weighted_edges_from(l2)
print("Graph making complete")



count_main=0
count=0
for line in file1:
    count_main+=1
    words=line.split()
    prime_dict[words[0]]=int(words[1])
    

print("dictionary complete")
print(prime_dict.keys())


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasPunctuations(inputString):
    invalidChars = set(string.punctuation)
    if any(char in invalidChars for char in inputString):
        return True
    else:
        return False

def distme(path):
     tree = ET.parse(path)
     root = tree.getroot()
     root = tree.getroot()
     
     count_rev=0
    
     print("In function")
     for rev in root.find('{http://www.mediawiki.org/xml/export-0.10/}page').findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
         
         count_rev+=1
         print(count_rev)
         file2.write("\n-----Revision----- "+str(count_rev)+"\n")
        
         text = rev.find('{http://www.mediawiki.org/xml/export-0.10/}text').text;
         if(not text):
             
             continue
         tags=["NNP","NNPS"]

         tagged_sent =  pos_tag(word_tokenize(text))
         
         m=0

         while True:
             print("we")
             if hasNumbers(tagged_sent[m][0]) == False and hasPunctuations(tagged_sent[m][0]) == False and len(tagged_sent[m][0]) > 1 and tagged_sent[m][1] in tags:
                 first=tagged_sent[m][0]
                 
                 break
             m+=1    
         
         for tagged_word in tagged_sent[m+1:]:
             
             
             if hasNumbers(tagged_word[0]) == False and hasPunctuations(tagged_word[0]) == False and len(tagged_word[0]) > 1:  #to remove words like ",","132" etc.
                 if(tagged_word[1] in tags):
                    
                     print("Hello")
                     if tagged_word[0] in prime_dict.keys() and first in prime_dict.keys():
                         print(".")
                         a1=prime_dict[first]
                         a2=prime_dict[tagged_word[0]]
                         a1=int(a1)
                         a2=int(a2)
                         if a1 in g and a2 in g:
                             if nx.has_path(g,a1,a2):
                                 
                                 l1=nx.shortest_path_length(g,source=a1,target=a2)
                                 
                                 file2.write(str(l1))
                     first=tagged_word[0]
                     
                    

distme("Brockway_Mountain_Drive.xml")
file1.close()
file2.close()
file3.close()