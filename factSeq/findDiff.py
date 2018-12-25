#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:36:07 2018

@author: descentis
"""

import difflib

def find_diff(s1,s2):
    d = difflib.Differ()
    difference_string = list(d.compare(s1,s2))
    
    new_list = []
    ind_minus = 1
    minus_list = []
    ind_plus = 1
    plus_list = []
    ind=0
    for w in difference_string:
        if(w[0]=='-'):
            minus_list.append(ind_minus)
            ind_minus+=1
        if(w[0]=='+'):
            plus_list.append(ind_plus)
            ind_plus+=1
        if(w[0]==' '):
            ind_minus+=1
            ind_plus+=1
        ind+=1
    
    #print(difference_string)
    #print("*************************")
    #print(plus_list)
    #print("*************************")
    #print(minus_list)
    new_list.append(plus_list)
    new_list.append(minus_list)
    return new_list
    
    

'''
s1 = ['Use' , 'Yugoslav' , 'Infobox' , 'Infobox' , 'Infobox' , 'Ship' , 'Career' , 'Enns' , 'River' , 'Stabilimento' , 'Tecnico' , 'Triestino' , 'Linz' , 'October' , 'Kingdom' , 'Serbs' , 'Croats' , 'Slovenes' , 'Sister' , 'Kingdom' , 'Infobox' , 'Ship' , 'Career' , 'Serbs' , 'Croats' , 'Yugoslavia' , 'Drava' , 'River' , 'Luftwaffe' , 'April' , 'Infobox' , 'Yarrow' , 'Armor' , 'Bulkhead' , 'Deck' , 'Conning' , 'Yugoslav' , 'Navy' , 'Navy' , 'Stabilimento' , 'Tecnico' , 'Triestino' , 'Linz' , 'Naval' , 'Program' , 'Information' , 'September' , 'October' , 'Length' , 'Beam' , 'Yarrow' , 'Information' , 'Armor' , 'Bulkhead' , 'Deck' , 'Information' , 'September' , 'Danube' , 'Flotilla' , 'October' , 'Belgrade' , 'October' , 'Serbs' , 'Belgrade' , 'Grosser' , 'Krieg' , 'Island' , 'October' , 'Budapest' , 'Flotilla' , 'Rjahovo' , 'Danube' , 'Mackensen' , 'Army' , 'Greger' , 'René' , 'Warships' , 'World' , 'War' , 'Allan' , 'London' , 'England' , 'Halpern' , 'Paul' , 'History' , 'World' , 'War' , 'Naval' , 'Institute' , 'Press' , 'Annapolis' , 'Maryland' , 'Jane' , 'Information' , 'Group' , 'Jane' , 'Fighting' , 'Ships' , 'World' , 'War' , 'II' , 'Studio' , 'Editions' , 'London' , 'England' , 'Drava']
s2 = ['Use' , 'Yugoslav' , 'Infobox' , 'Infobox' , 'Infobox' , 'Ship' , 'Career' , 'Enns' , 'River' , 'Stabilimento' , 'Tecnico' , 'Triestino' , 'Linz' , 'October' , 'Kingdom' , 'Serbs' , 'Croats' , 'Slovenes' , 'Sister' , 'Kingdom' , 'Infobox' , 'Ship' , 'Career' , 'Serbs' , 'Croats' , 'Yugoslavia' , 'Drava' , 'River' , 'Luftwaffe' , 'April' , 'Infobox' , 'Yarrow' , 'Armor' , 'Bulkhead' , 'Deck' , 'Conning' , 'Yugoslav' , 'Navy' , 'World' , 'War' , 'Danube' , 'Flotilla' , 'Army' , 'World' , 'War' , 'Kingdom' , 'Serbs' , 'Croats' , 'Slovenes' , 'Yugoslavia' , 'Nazi' , 'Axis' , 'Yugoslavia' , 'April' , 'Kingdom' , 'Hungary' , 'Hungary' , 'Navy' , 'Stabilimento' , 'Tecnico' , 'Triestino' , 'Linz' , 'Naval' , 'Program' , 'Information' , 'September' , 'October' , 'Length' , 'Beam' , 'Yarrow' , 'Information' , 'Armor' , 'Bulkhead' , 'Deck' , 'Information' , 'September' , 'Danube' , 'Flotilla' , 'October' , 'Belgrade' , 'October' , 'Serbs' , 'Belgrade' , 'Grosser' , 'Krieg' , 'Island' , 'October' , 'Budapest' , 'Flotilla' , 'Rjahovo' , 'Danube' , 'Mackensen' , 'Army' , 'Greger' , 'René' , 'Warships' , 'World' , 'War' , 'Allan' , 'London' , 'England' , 'Halpern' , 'Paul' , 'History' , 'World' , 'War' , 'Naval' , 'Institute' , 'Press' , 'Annapolis' , 'Maryland' , 'Jane' , 'Information' , 'Group' , 'Jane' , 'Fighting' , 'Ships' , 'World' , 'War' , 'II' , 'Studio' , 'Editions' , 'London' , 'England' , 'Drava']


find_diff(s1,s2)
'''