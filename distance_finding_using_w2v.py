#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:59:02 2019

@author: computerlab
"""

import xml.etree.cElementTree as ET
from nltk import word_tokenize
from nltk.tag import pos_tag
import string

from gensim.models import Word2Vec
model=Word2Vec.load('en.model')
file2=open("distance_v2.txt","w")
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
     
     
     
     c=0
     print("In function")
     for rev in root.find('{http://www.mediawiki.org/xml/export-0.10/}page').findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
         
         
         c+=1
         x.append(c)
         
         
         
        
         text = rev.find('{http://www.mediawiki.org/xml/export-0.10/}text').text;
         if(not text):
             
             continue
         tags=["NNP","NNPS"]

         tagged_sent =  pos_tag(word_tokenize(text))
         
         m=0
         sum=0
         while m<len(tagged_sent):
		             
             if hasNumbers(tagged_sent[m][0]) == False and hasPunctuations(tagged_sent[m][0]) == False and len(tagged_sent[m][0]) > 2 and tagged_sent[m][1] in tags:
                 first=tagged_sent[m][0]
                 
                 break
             m+=1    
         #print("FOund!!")
         count=0
         for tagged_word in tagged_sent[m+1:]:
             
             
             if hasNumbers(tagged_word[0]) == False and hasPunctuations(tagged_word[0]) == False and len(tagged_word[0]) > 2 and (tagged_word[1] in tags):
                 print("yes")
                 try:
                     sum+=model.wv.similarity(first,tagged_word[0])
		             
                 except:
                     pass
                 else:
                     count+=1
         
                 
                    
                 first=tagged_word[0]
         y.append(sum/count)  
         
print(y)
str1=''                     
for i in range(0,len(y)):
	str1+=str(y[i])+" "
file2.write(str1)
'''                    
plt.plot(x,y)
plt.xlabel("revisions")
plt.ylabel("magic")
plt.savefig('see.png',dpi=800)
'''
distme("2.xml")

file2.close()
