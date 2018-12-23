#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:42:54 2018

@author: sujit_jaiwaliya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:08:14 2018

@author: descentis
"""

import xml.etree.cElementTree as ET
import matplotlib.pyplot as plt
#import mwparserfromhell 
from nltk.tag import pos_tag
import re,os

path="all_files/";
dirs = os.listdir( path );


for file in dirs:
    print(file);
file_no=0;
listi=[];
for file in dirs:
    print(file);
    file_no=file_no+1;
    if(file_no!=9 and file!=".DS_Store"):
        tree = ET.parse(file);
        revision_no =0;
        byte_data = [];
        r_no=[];
        unique_pronouns=set();
        no_unique_pronouns=[];
        root = tree.getroot()
        for elem in root:
            if(elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page"):
                for child in elem:
                    if(child.tag == "{http://www.mediawiki.org/xml/export-0.10/}revision"):
                        for revision in child:
                            #print("inside revision ",revision_no,": ",revision.tag);
                            if(revision.tag=="{http://www.mediawiki.org/xml/export-0.10/}text"):
                                attrib=revision.attrib;
                                if(attrib.get('bytes')!= None and int(attrib.get('bytes'))!=0 and file!=".DS_Store"):
                                    
                                    r_no.append(revision_no);
                                    byte_data.append(int(attrib.get('bytes')));
                                    print("file_no=",file_no,"Revision_number =",revision_no,"bytes=",byte_data[revision_no]);
                                    text = revision.text;
                                    revision_no=revision_no+1;
                                    p=re.sub('[^A-Za-z]+',' ',text);
                                    tagged_sent = pos_tag(p.split());
                                    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
                                    u_p_length = len(unique_pronouns);
                                    for i in range(len(propernouns)):
                                        propernouns[i]=propernouns[i].lower();
                                        if(len(propernouns[i])!=1 and len(propernouns[i])!=2):
                                            unique_pronouns.add(propernouns[i]);
            
                                    no_unique_pronouns.append(len(unique_pronouns));
                                        #print("u_p_length =",u_p_length,"len(unique_pronouns) =",len(unique_pronouns))
                                #print("no of unique elemnt is ",len(unique_pronouns)-u_p_length);
                                #print("------------------",unique_pronouns);
                                                    
        #plt.plot(r_no,byte_data);
        plt.plot(r_no,no_unique_pronouns);
        plt.savefig("graph.PNG");
        print("------------------",unique_pronouns);
        print("Total number of unique proper nouns are ",len(unique_pronouns),"");
    
    
    #print("Text-------------------------------------------------------------------------------------------->\n\n\n",revision.text);
                
