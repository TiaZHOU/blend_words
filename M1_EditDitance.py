# -*- coding: utf-8 -*-

'''
Date: 11/9/2019
Author: Tianqi ZHOU
Work: Comp90049 Knowledge Technologies Assignmen 1
Goal: Implement for detecting occurrences of blend words
'''

'''
    Some libraries used in implement:
        1. editdistance : System library for find edit distance
        2. nltk: System library for creating N-gram for given string
'''

import editdistance
import time
#import thread
'''
matching method 

    1.apart candidate word into 2 part by first vowel.

    2.match first part with dict words' same length front part. setting a distance to limited

    3.match second part with dic words',similar to the length, end part.setting a distance to limited
'''
'''
method 1  Edit Distance
    
    1. Read data from data set:
        candi: represents the list of candidates
        dic: represents the list of dictionary
        
    3. Find edit distance from part from candidate and part from dictionary under limitation
    
    4. Write the results to the specific file.
       


dic= open("test_dic.txt",r)
#blend = open("test_blends.txt",r)
candi = open("test_candi.txt")
match = open("match2.txt",'w+')
'''
dic= open("dict.txt",'r')
candi = open("candidates.txt",'r')
match = open("ED_match_v2.txt",'w+') 

candis = candi.readlines()
dics = dic.readlines()

def edit(part,token,dis):
    #print(part+" matching "+ token)
    this_score = editdistance.eval(part,token)
    if this_score <dis:
        return 1
    else:
        return 0

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

count = 0   
to = time.time() 
match.write("ED version 2.0 11/9-21:11,distance:0,first vowel ignore\n")
print (to)
for candi in candis:
    candi = candi.strip()
    front_match = 0
    end_match = 0  
    pos=find_vowel(candi)
    #print (pos)
    #print (time.time()-to)
    if pos == len(candi) or pos == 0:
        pass
    else:
        #print(candi)
        
        fpc = first_part(candi,pos)
        for dic in dics:
            dic = dic.strip()
            if fpc[0]!= dic[0]:
                pass
            else:
                fpd = front_part(dic,pos)
                if edit(fpc,fpd,1)==1:
                    #print(fpc)
                    front_match = 1
                    break
        spc = second_part(candi,pos)
        for dic in dics:
            dic = dic.strip()
            if spc[len(spc)-1]!=dic[len(dic)-1] or len(candi)-len(dic) > 2:
                pass
            else:
                epd = end_part(dic,len(dic)-len(candi)+pos)
                if edit(spc,epd,1) == 1:
                    #print(spc)
                    end_match = 1
                    break
        if front_match + end_match == 2:
            match.write(candi+"\n")
            count += 1
            print(count,candi)
            print (time.time()-to)
match.close()    

