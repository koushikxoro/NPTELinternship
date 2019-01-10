#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:12:01 2019

@author: computerlab
"""
import math
import xml.etree.cElementTree as ET
import mwparserfromhell
from googleapiclient.discovery import build
import time

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
    
c1=search('the')
count_main=0
count=0
def ngd(input1,input2):
    return (max(math.log10(search(input1)),math.log10(search(input2)))-math.log10(search(input1+" "+input2)))/(math.log10(c1)-min(math.log10(search(input1)),math.log10(search(input2))))
def magic(path):
     tree = ET.parse(path)
     root = tree.getroot()
     root = tree.getroot()
     
     count_rev=0
     mdic={}
     print("In function")
     for rev in root.find('{http://www.mediawiki.org/xml/export-0.10/}page').findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
         
         count_rev+=1
         #print(count_rev)
         
         
        
         text = rev.find('{http://www.mediawiki.org/xml/export-0.10/}text').text;
         if(not text):
             
             continue
         wikicode=mwparserfromhell.parse(text)
         templates=wikicode.filter_wikilinks()
         if(len(templates)==0):
             continue
         first=templates[0]
         for i in templates[1:]:
             str1=str(first)
             str2=str(i)
             #slicing for removing  square braces
             str3=str1[2:len(str1)-2]+"$#$$@*"+str2[2:len(str2)-2]
             if str3 not in mdic.keys():
                 mdic[str3]=1
             first=i
         
         #print(templates)
     #print(mdic)
     #print(len(mdic.keys()))  
     c=0
     t1=time.time()
     for key in mdic:
         c+=1
         if c==34:
             break
         l1=key.split('$#$$@*')
         print(ngd(l1[0],l1[0]))
     t2=time.time()
     print(t2-t1)       
               
                    

magic("Zhang_Heng.xml")

