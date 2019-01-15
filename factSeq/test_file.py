# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:28:52 2019

@author: Amit
"""

import gensim
import xml.etree.cElementTree as ec
import mwparserfromhell
import matplotlib.pyplot as plt

model = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')


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
                    
                    distance_list = []
                    for i in range(len(wikilinks)):
                        if(i!=len(wikilinks)-1):
                            distance = model.wmdistance(wikilinks[i],wikilinks[i+1])
                            distance_list.append(distance)
                    
                    distance_sum = sum(distance_list)
                    if(len(distance_list)!=0):
                        result.append(distance_sum/len(distance_list))
    
    return result

def findDistance(model,article_name,point):
    distance = getDistance('wiki_data/FA/'+article_name+'.xml',model)
    
    xAxis = [i for i in range(1,len(distance)+1)]
    sc = [point for i in range(1,len(distance)+1)]
    
    plt.xlabel('Revisions', fontsize=12)
    
    plt.ylabel('sum of distance', fontsize=12)
    
    plt.scatter(xAxis,distance,c = 'r', s=sc, marker='o')
    plt.show()