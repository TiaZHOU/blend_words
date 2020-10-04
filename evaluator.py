# -*- coding: utf-8 -*-
'''
Date: 11/9/2019
Author: Tianqi ZHOU
Work: Comp90049 Knowledge Technologies Assignmen 1
Goal: Implement for evaluateing the results of detecting occurrences of blend words
'''

ed = open("ED_match_v1.txt",'r')
ged = open("match_ged_v2.txt",'r')
ngram = open("NG_match_v1.txt",'r')
dic = open("dict.txt",'r')
candi = open("candidates.txt",'r')
blend = open("blends.txt",'r')


eds = ed.readlines()
geds = ged.readlines()
ngrams = ngram.readlines()
candis = candi.readlines()
dics = dic.readlines()
blends = blend.readlines()


recall_list = [0 for i in range(0,183) ]
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

print ("total ", i , " blend words in candidates.")  

'''
evaluating the edit distance method

'''
ed_correct=0
for ed in eds:
    ed = ed.strip()
    for j in range(0,i):
        #print(recall_list[j])
        if recall_list[j] == ed:
            ed_correct += 1
            break
print ("edit distance recall ",ed_correct," out of ",i,"Precision:",ed_correct/(len(eds)-1)*100,"%")        

        
'''
evaluating the global edit distance method

'''

ged_correct=0
for ged in geds:
    ged = ged.strip()
    for j in range(0,i):
        if recall_list[j] == ged:
            ged_correct += 1
            break

print ("GED total recall ",ged_correct," out of ",i,"Precision:",ged_correct/(len(geds)-1)*100,"%")              
            
'''
evaluating the N-Gram edit distance method

'''  

ngram_correct=0  
for ngram in ngrams:
    ngram = ngram.strip()
    for j in range(0,i):
        if recall_list[j] == ngram:
            ngram_correct += 1
            break
print ("NGram recall ",ngram_correct," out of ",i,"Precision:",ngram_correct/(len(ngrams)-1)*100,"%")              
    




'''
total  151  blend words in candidates.
edit distance recall  40  out of  151 Precision: 1.7528483786152498 %
GED total recall  34  out of  151 Precision: 1.1303191489361704 %
NGram recall  43  out of  151 Precision: 1.5739385065885798 %

'''        
