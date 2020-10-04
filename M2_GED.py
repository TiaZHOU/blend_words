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

import time

#import thread
'''

matching method 

    1.apart candidate word into 2 part by first vowel.

    2.match first part with dict words' same length front part. setting a distance to limited

    3.match second part with dic words',similar to the length, end part.setting a distance to limited
'''
'''
method 2  Global Edit Distance
    
    1. Specified parameters [m,i,d,r]:
            m ---> Match
            i ---> Insertion
            d ---> Deletion
            r ---> Replace
            
        1.1. Example of general parameters:
    
            1.1.1. "Normal" Distance:
            para1 = [ 1,-1,-1,-1 ]
        
    2. Read data from data set:
        candi: represents the list of candidates
        dic: represents the list of dictionary
        
    3. Find global edit distance from part from candidate and part from dictionary under limitation
    
    4. Write the results to the specific file.
       

dic= open("test_dic.txt",'r')
candi = open("test_candi.txt",'r')
match = open("test_match_ged_v2.txt",'w+') 
'''
dic= open("dict.txt",'r')
candi = open("candidates.txt",'r')
match = open("match_ged_v3.txt",'w+') 

candis = candi.readlines()
dics = dic.readlines()

def ged(part,token,dis):#rate_here= 2(right_rate-0.5)
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
                          
               
    if  distanceG[ lenP-1 ][ lenT-1 ]  >= dis:
       # print(part+" matching "+ token)
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
    return dic_word[pos2:len(dic_word)]
    
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
match.write("GED version 2.0 11/9-21:45,distance:F1S3 match,first vowel ignore \n")
print (to)
process = 0
for candi in candis:
    process += 1
    if process%17 == 0:
        print(process/170,"%")
        print (time.time()-to)
    candi = candi.strip()
    front_match = 0
    end_match = 0  
    pos=find_vowel(candi)
    #print (pos)

    if pos == len(candi) or pos == 0:
        pass
    else:
        #print(candi)
        
        fpc = first_part(candi,pos)
        for dic in dics:
            dic = dic.strip()
            if fpc[0] != dic[0]:
                pass
            else:
                fpd = front_part(dic,pos)
                if ged(fpc,fpd,1)==1:
                   # print(candi)
                   # print(dic)
                    front_match = 1
                    break  
        spc = second_part(candi,pos)
        for dic in dics:
            dic = dic.strip()
            if spc[len(spc)-1]!=dic[len(dic)-1] or len(candi)-len(dic) > 2:
                pass
            else: 
                epd = end_part(dic,len(dic)-len(candi)+pos)
                if ged(spc,epd,3) == 1:
                    #print(spc)
                    end_match = 1
                    break           
        if front_match + end_match == 2:
            match.write(candi+"\n")
            count += 1
            print(count,candi)
            print (time.time()-to)
            
match.close()

