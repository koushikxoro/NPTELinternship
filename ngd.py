#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:23:35 2019

@author: computerlab
"""

import xml.etree.cElementTree as ET
from nltk import word_tokenize
from nltk.tag import pos_tag
import string
#import networkx as nx
import math

from googleapiclient.discovery import build


prime_dict={}
file1=open("dict.txt","r")
file2=open("distance_v2.txt","w")
file3=open("graph_modified.txt","r")

my_api_key = "AIzaSyA2dgLNT20li13vuoQPOZXS0zkm6x5Qjxk"
my_cse_id = "016040684614790340026:6z11qljew-y"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['queries']['request']
def search(input1):
    
    results = google_search('koushik', my_api_key, my_cse_id, num=10)
    for result in results:
        return(int((result['totalResults'])))
    
c1=25270000000000
count_main=0
count=0
def ngd(input1,input2):
    return (max(math.log10(search(input1)),math.log10(search(input2)))-math.log10(search(input1+" "+input2)))/(math.log10(c1)-min(math.log10(search(input1)),math.log10(search(input2))))

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
                     
                     print(".")
                     
                     di1=ngd(first,tagged_word[0])
                     file2.write(str(di1))
                     first=tagged_word[0]
                     
                    

distme("Brockway_Mountain_Drive.xml")
file1.close()
file2.close()
file3.close()