# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:36:28 2019

@author: Amit
"""

import gensim
#from gensim.models import Word2Vec
import xml.etree.cElementTree as ec
import mwparserfromhell
import matplotlib.pyplot as plt
import os

#model = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

print('Model Loaded')
FAList = os.listdir('wiki_data/test')
allDistanceDict = {}
vocabularyDict = {}
def getDistance(articleName,model):
    tree = ec.parse(articleName)
    
    root = tree.getroot()
    root = root[1]
    Text = ''
    
    result = []
    for child in root:
        if 'revision' in child.tag:
            for each in child:
                if 'text' in each.tag:
                    Text = each.text
                    
                    wikicode = mwparserfromhell.parse(Text)
                    wikiLinks = wikicode.filter_wikilinks()
                    wikilinks = []
                    for links in wikiLinks:
                        if(('File:' not in links) and ('Category:' not in links)):
                            if('|' in links):
                                wikilinks.append(links[2:-2].split('|')[1])
                            else:
                                wikilinks.append(links[2:-2])
                    
                    #distance_list = []
                    for i in range(len(wikilinks)):
                        if(i!=len(wikilinks)-1):                            
                            #distance = model.wmdistance(wikilinks[i],wikilinks[i+1])
                            #distance_list.append(distance)
                            dummyWordPair = wikilinks[i]+'#$#'+wikilinks[i+1]
                            if(allDistanceDict.get(dummyWordPair)==None):
                                distance = model.wmdistance(wikilinks[i],wikilinks[i+1])
                                allDistanceDict[dummyWordPair] = distance
                            if(vocabularyDict.get(wikilinks[i])==None):
                                l = []
                                l.append(wikilinks[i+1])
                                vocabularyDict[wikilinks[i]] = l
                            else:
                                if(wikilinks[i+1] not in vocabularyDict[wikilinks[i]]):
                                    vocabularyDict[wikilinks[i]].append(wikilinks[i+1])
                    
    countDistance = 0
 
    for i in range(len(wikilinks)-3):
        li = vocabularyDict[wikilinks[i]]
        distance_list = []
        localDict = {}
        for j in li:
            dummyWord = wikilinks[i]+'#$#'+j
            distance_list.append(allDistanceDict[dummyWord])
            localDict[j] = allDistanceDict[dummyWord]
        if((allDistanceDict[wikilinks[i]+'#$#'+wikilinks[i+1]] <= min(distance_list)) or (model.wmdistance(wikilinks[i],wikilinks[i+2]) <= min(distance_list)) or (model.wmdistance(wikilinks[i],wikilinks[i+3]) <= min(distance_list)) ):
                       countDistance+=1

    
    percentageDistance = countDistance/len(wikilinks)
    result.append(percentageDistance)
    return result


    
for articles in FAList:
    distance = getDistance('wiki_data/test/'+articles,model)
    with open('testFile.txt','a',errors='ignore') as myFile:
        myFile.write(articles[:-4]+' '+str(distance)+'\n')
