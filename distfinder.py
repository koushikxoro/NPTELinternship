import xml.etree.cElementTree as ET
from nltk import word_tokenize
from nltk.tag import pos_tag
import string
import networkx as nx


filename="dict.txt"
filename1="distance.txt"
prime_dict={}
file1=open(filename,"r")
file2=open(filename1,"w")
for line in file1:
    words=line.split()
    prime_dict[words[0]]=words[1]
g=nx.read_gml('graph_main')
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasPunctuations(inputString):
    invalidChars = set(string.punctuation)
    if any(char in invalidChars for char in inputString):
        return True
    else:
        return False
x=[]
y=[]
def distme(path):
     tree = ET.parse(path)
     root = tree.getroot()
     root = tree.getroot()
     
     count_rev=0
    
     for rev in root.find('{http://www.mediawiki.org/xml/export-0.10/}page').findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
         
         count_rev+=1
         file2.write("\n-----Revision----- "+str(count_rev)+"\n")
        
         text = rev.find('{http://www.mediawiki.org/xml/export-0.10/}text').text;
         if(not text):
             
             continue
         tags=["NNP","NNPS"]

         tagged_sent =  pos_tag(word_tokenize(text))
         
         m=0
         all_count=0
         real_count=0
         while True:

             if hasNumbers(tagged_sent[m][0]) == False and hasPunctuations(tagged_sent[m][0]) == False and len(tagged_sent[m][0]) > 1 and tagged_sent[m][1] in tags:
                 first=tagged_sent[m][0]
                 break
             m+=1    
         
         for tagged_word in tagged_sent[m+1:]:
             
             
             if hasNumbers(tagged_word[0]) == False and hasPunctuations(tagged_word[0]) == False and len(tagged_word[0]) > 1:  #to remove words like ",","132" etc.
                 if(tagged_word[1] in tags):
                    
                     if tagged_word[0] in prime_dict.keys():
                         a1=prime_dict[first]   
                         a2=prime_dict[tagged_word[0]]
                         l1=nx.shortest_path_length(g,source=int(a1),target=int(a2))
                         first=tagged_word[0]
                         file2.write(str(l1))

distme("Brockway_Mountain_Drive.xml")
                         
                    
         
         
