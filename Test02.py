#import random
from random import random
score = []
# 문제 1) score 리스트에 1 ~ 100 사이의 랜덤 값 5개를 저장하는 함수
def lsRandom(score):
    for i in range(5):#0 ~ 4
        a = int(random() * 100) + 1
        score.append(a)
    return score

score = lsRandom(score)
print(score)
    
# 문제 2) 성적이 60점 이상이면 합격, 합격생들의 idx와 성적을 리턴해주는 함수
# [ [ 인덱스, 성적 ] , [인덱스,성적]..]
def lsScore(score):
    ls = []
    '''
    for i in score: #score = [ 27, 66, 2, 89, 26 ]
        if i >= 60:
            ls.append([ score.index(i) , i])
    '''
    for i in range(len(score)):# 0 ~ 4
        if score[i] >= 60:
            ls.append([ i , score[i]])
        
    return ls 
ls = lsScore(score)
print(ls)

# 문제 3) 1등 학생의 방번호(idx)를 리턴해주는 함수
def maxScore(score):
    #return score.index(max(score))
    maxNum = -1
    maxIdx = -1
    for i in range(len(score)):
        if score[i] > maxNum:
            maxNum = score[i]
            maxIdx = i  
    return maxIdx
maxIdx = maxScore(score)
print(maxIdx)


