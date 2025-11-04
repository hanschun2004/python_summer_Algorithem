class School:
    score = [87,100,11,72,92]

mega = School()

# 문제 1) 전체 합 출력
# 정답 1) 362
# 전부 함수..

def sum1(score):
    sum1 = 0
    for i in score:
        sum1 += i
    return sum1

print(sum1(mega.score))


# mega객체는 class 모양대로 만들어진거고 class모양에 리스트가 있었기 때문에
# 메가 객체 안에도 리스트가 생각이 돼서 메가 객체 안에있는 리스트를 불러와서
# sum1함수에 리스트 값을 넘겨줘서 값을 구하는거에요 !



# 문제 2) 4의 배수 합 출력
# 정답 2) 264   

def sum4(score):
    sum4 = 0
    for i in score:
        if i % 4 ==0:
            sum4 += i
    return sum4

print(sum4(mega.score))

# 문제 3) 4의 배수 개수를 출력 
# 정답 3) 3

def cnt(score):
    cnt = 0
    for i in score:
        if i % 4 ==0:
            cnt += 1
    return cnt

print(cnt(mega.score))

# 문제 4) 짝수의 개수 출력
# 정답 4) 3

def cnt2(score):
    cnt2 = 0
    for i in score:
        if i % 2 ==0:
            cnt2 += 1
    return cnt2

print(cnt2(mega.score))


