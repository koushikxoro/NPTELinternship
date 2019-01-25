# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:36:00 2019

@author: Amit
"""

import gensim
import xml.etree.cElementTree as ec
import mwparserfromhell
import matplotlib.pyplot as plt
from dateutil.parser import parse
from datetime import datetime

model = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')

print('Model Loaded')
def getDistance(articleName,model):
    tree = ec.parse(articleName)
    
    root = tree.getroot()
    root = root[1]
    Text = ''
    
    result = 0
    #returnResult = []
    #flag=0
    uniqueFacts = {}
    #lenUniqueFacts = 0
    #uniqueFrev = []
    #proDist = 0
    wordPairs = {}
    #aceDict = {}
    #aceNum = 1
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
                    
                    
                    for i in range(len(wikilinks)):
                        if(len(wikilinks)>1):
                                
                            if(i==0):
                                
                                
                                dummyWord = wikilinks[i]+'#$#'+wikilinks[i+1]
                                
                                '''
                                #tracking a factoid
                                if(wikilinks[i]=='Ace Hardware' or wikilinks[i+1]=='Ace Hardware'):
                                    aceDict[aceNum] = dummyWord
                                    aceNum+=1
                                '''
                                    
                                    
                                if(wordPairs.get(dummyWord)==None):
                                    distance = model.wmdistance(wikilinks[i],wikilinks[i+1])
                                    wordPairs[dummyWord] = distance
                                else:
                                    distance = wordPairs[dummyWord]
                                if(uniqueFacts.get(wikilinks[i])==None):                                
                                    uniqueFacts[wikilinks[i]] = [distance+distance]
                                else:
                                    uniqueFacts[wikilinks[i]].append(distance+distance)
                            if(i!=len(wikilinks)-1):
                                
                                dummyWord = wikilinks[i-1]+'#$#'+wikilinks[i]
                                
                                '''
                                #tracking a factoid
                                if(wikilinks[i-1]=='Ace Hardware' or wikilinks[i]=='Ace Hardware'):
                                    aceDict[aceNum] = dummyWord
                                    aceNum+=1   
                                '''
                                
                                if(wordPairs.get(dummyWord)==None):
                                    d1 = model.wmdistance(wikilinks[i-1],wikilinks[i])
                                    wordPairs[dummyWord] = d1
                                else:
                                    d1 = wordPairs[dummyWord]
                                
                                dummyWord = wikilinks[i]+'#$#'+wikilinks[i+1]
                                
                                '''
                                #tracking a factoid
                                if(wikilinks[i]=='Ace Hardware' or wikilinks[i+1]=='Ace Hardware'):
                                    aceDict[aceNum] = dummyWord
                                    aceNum+=1
                                '''
                                
                                if(wordPairs.get(dummyWord)==None):
                                    d2 = model.wmdistance(wikilinks[i],wikilinks[i+1])
                                    wordPairs[dummyWord] = d2
                                else:
                                    d2 = wordPairs[dummyWord]
                                if(uniqueFacts.get(wikilinks[i])==None):
                                    uniqueFacts[wikilinks[i]] = [d1+d2]
                                else:
                                    uniqueFacts[wikilinks[i]].append(d1+d2)
                            else:
                                dummyWord = wikilinks[i-1]+'#$#'+wikilinks[i]
                                
                                '''
                                #tracking a factoid
                                if(wikilinks[i-1]=='Ace Hardware' or wikilinks[i]=='Ace Hardware'):
                                    aceDict[aceNum] = dummyWord
                                    aceNum+=1      
                                '''                                                          
                                
                                if(wordPairs.get(dummyWord)==None):
                                    distance = model.wmdistance(wikilinks[i-1],wikilinks[i])
                                    wordPairs[dummyWord] = distance
                                else:
                                    distance = wordPairs[dummyWord]
                                if(uniqueFacts.get(wikilinks[i])==None):                                
                                    uniqueFacts[wikilinks[i]] = [distance+distance]
                                else:
                                    uniqueFacts[wikilinks[i]].append(distance+distance)
                            
    
    countDecrease = 0
    for k,v in uniqueFacts.items():
        dis = 0
        for i in range(len(v)-1):
            dis+=v[i]-v[i+1]
        if(dis>=0):
            countDecrease+=1
    
    
    
    '''
    print(uniqueFacts)
    
    print('===========')
    
    print(aceDict)
    '''
    result = countDecrease/len(uniqueFacts)
                                

        
    return result

def findDistance(model,article_name,point):
    distance = getDistance('wiki_data/FA/'+article_name+'.xml',model)

    with open('testFile.txt','a',errors='ignore') as myFile:
        myFile.write(article_name[:-4]+' '+str(distance)+'\n')
    
    
    '''
    xAxis = [i for i in range(1,len(distance[0])+1)]
    sc = [point for i in range(1,len(distance[0])+1)]
    
    plt.xlabel('Revisions', fontsize=12)
    
    plt.ylabel('sum of distance', fontsize=12)
    
    plt.scatter(xAxis,distance[0],c = 'r', s=sc, marker='o')
    for i in distance[3]:
        plt.axvline(x=i,lw=0.5,ls='--')
    #plt.axvline(x=distance[1])
    #plt.axvline(x=distance[2])
    #print(distance[3])
    plt.show()
    '''