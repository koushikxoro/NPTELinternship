#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:17:12 2019

@author: computerlab
"""
import xml.etree.cElementTree as ET
import mwparserfromhell
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
     print(len(mdic.keys()))      
                     
                    

magic("Zhang_Heng.xml")