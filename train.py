# -*- coding: utf-8 -*-
"""
Date: 11/9/2019
Author: Tianqi ZHOU
Work: Comp90049 Knowledge Technologies Assignmen 1
Goal: Implement for train the distance limitation of blend words

"""

import editdistance
import nltk

blend = open("blends.txt",'r')
blends = blend.readlines()

def first_part(candi_word,pos):#pos is the index of first vowel
    return candi_word[0:pos+1]
        
def second_part(candi_word,pos):#pos is the index of first vowel
    if pos == len(candi_word)-1:
        return candi_word[len(candi_word)-1]
    else:
        return candi_word[pos:len(candi_word)-1]

def front_part(dic_word,pos):#pos is the index of candi_word's first vowel 
    return dic_word[0:pos+1]

def end_part(dic_word,pos2):#pos2 is len(dic_word)-len(candi_word)+pos
    return dic_word[pos2:len(dic_word)-1]
    
def find_vowel(candi_word):#find the pos
    for i in range(len(candi_word)):
        if candi_word[i] in ('a', 'e', 'i', 'o', 'u'):
            n = i
            break
        else:
           n = len(candi_word)         
    return n



def ged(part,token):
    para1 = [ 1,-1,-1,-1 ]
    #para2 = [ 0, 1, 1, 1 ]
    lenP = len( part )
    lenT = len( token )
    #print(part+" matching "+ token)
    distanceG = [[0 for i in range(lenT) ] for i in range(lenP)]
    for i in range(0,lenT):
        distanceG[ 0 ][ i ] = i * para1[ 2 ]
            
    for i in range(0,lenP):
        distanceG[ i ][ 0 ] = i * para1[ 1 ]
               
    for i in range(1,lenP):
        for j in range(1,lenT):
            if part[ i ] == token[ j ]:
                distanceG[ i ][ j ] = max(
                distanceG[ i-1 ][ j-1 ] + para1[0],
                distanceG[ i-1 ][ j ] + para1[1],
                distanceG[ i ][ j-1 ] + para1[2]
                )
            else:
                distanceG[ i ][ j ] = max(
                distanceG[ i-1 ][ j-1 ] + para1[3],
                distanceG[ i-1 ][ j ] + para1[1],
                distanceG[ i ][ j-1 ] + para1[2]
                )
                          
               
    return distanceG[ lenP-1 ][ lenT-1 ]

def NGram(part,token):
    gram_distance = 0
    part_gram = list(nltk.bigrams(part))
    part_len = len(part_gram)
    token_gram = list(nltk.bigrams(token))
    token_len = len(token_gram)
    visit = [0 for i in range (token_len)]
    temp = 0
    for i in range (part_len):
        for j in range (token_len):
            if part_gram[i] == token_gram[j] and visit[j] != 1:
                temp += 1
                visit[j] = 1
    return part_len+token_len-2*temp


def analyze(d_list):
    len_d_list = len(d_list)
    highest=0
    total = 0
    for order in range (0,len_d_list):
        total += d_list[order]
        if d_list[order] > highest:
            highest = d_list[order]
    print("highest:",highest,"\n average:",total/len_d_list)   
    for n in range (0,highest+1):
        print ("total",d_list.count(n),"for ",n)

recall_list = [0 for i in range(0,183) ]
ed_list1 = [0 for i in range(0,183) ]
ged_list1 = [0 for i in range(0,183) ]
ngarm_list1 = [0 for i in range(0,183) ]
ed_list2 = [0 for i in range(0,183) ]
ged_list2 = [0 for i in range(0,183) ]
ngarm_list2 = [0 for i in range(0,183) ]
order = 0
i=0
for blend in blends:
    #print(blend)
    index = blend.find('\t')
    blend1 = blend[0:index]
    blend2 = blend[index+1:len(blend)]
    index2 = blend2.find('\t')
    blend3 = blend2[index2+1:len(blend2)]
    blend2 = blend2[0:index2]
    #print(blend1,blend2,blend3)
    for candi in candis:
        candi = candi.strip()
        #print (candi)
        if blend1 == candi:
            recall_list[ i ]= blend1
            i += 1
    pos=find_vowel(blend1)        
    fpc = first_part(blend1,pos)
    fpd = front_part(blend2,pos)
    spc = second_part(blend1,pos)
    epd = end_part(blend2,len(blend2)-len(blend1)+pos)
    ed_list1[order] = editdistance.eval(fpc,fpd)
    ged_list1[order] =  ged(fpc,fpd)
    ngarm_list1[order] =  NGram(fpc,fpd) 
    ed_list2[order] = editdistance.eval(spc,epd)
    #ged_list2[order] =  ged(spc,epd)
    ngarm_list2[order] =  NGram(spc,epd)               
    order += 1
    
    

print("for ed_list1")  
analyze(ed_list1)
print("for ed_list2")  
analyze(ed_list2)
print("for ged_list1")  
analyze(ged_list1)
print("for ged_list2")  
#analyze(ged_list2)
print("for ngram_list1")  
analyze(ngarm_list1)
print("for ngram_list2")  
analyze(ngarm_list2
        
print ("total "+ i +" blend words in candidates.")  

'''
for ed_list1
highest: 2 
 average: 0.28415300546448086
total 135 for  0
total 44 for  1
total 4 for  2
for ed_list2
highest: 11 
 average: 3.6448087431693987
total 5 for  0
total 21 for  1
total 39 for  2
total 27 for  3
total 32 for  4
total 23 for  5
total 20 for  6
total 10 for  7
total 3 for  8
total 1 for  9
total 1 for  10
total 1 for  11
for ged_list1
highest: 3 
 average: 0.7704918032786885
total 32 for  0
total 91 for  1
total 36 for  2
total 1 for  3
for ged_list2
for ngram_list1
highest: 4 
 average: 0.5737704918032787
total 135 for  0
total 0 for  1
total 43 for  2
total 1 for  3
total 4 for  4
for ngram_list2
highest: 12 
 average: 4.278688524590164
total 15 for  0
total 2 for  1
total 40 for  2
total 6 for  3
total 42 for  4
total 17 for  5
total 38 for  6
total 5 for  7
total 11 for  8
total 0 for  9
total 2 for  10
total 1 for  11
total 4 for  12

'''