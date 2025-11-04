# 가변 매개변수
# - 매개변수의 개수를 상황에 따라서 여러개 만들 수 있도록 하는 문법
# - 매개변수 앞에 *을 붙여서 선언하면 된다.
# - 가변 매개변수는 튜플로 처리된다.

def tot(*data):
    print(data)
    print(type(data))
    print(data.__len__())
    to = 0
    for i in data:
        to += i
    print(to)

tot(1,2,3,4,5,6,7,8,9,10)
print(max(1,2,3,4,5))
print(max(1,2,3))#가변매개변수로 만들어진 함수 def max(*data):
#print(abs(1,2,3,4,5))#1,2,3,4,5 -> 5given error   def abs(a):


#가변 매개변수를 응용하여 max함수와 min함수가 내장함수처럼 실행될 수 있도록..

def max(*data):
    maxNum = data[0]
    for i in data: # i = 값 한개씩..
        if i > maxNum:
            maxNum = i
    return maxNum
    

print(max(-1,-2,-3)) # -1
print(max(1,2,3,4,5)) # 5
def min(*data):
    minNum = data[0]
    for i in range(len(data)):#range() - i = 정수값..
        if data[i] < minNum:
            minNum = data[i]
    return minNum
    

print(min(3,4,5,6)) # 3
print(min(-1,-3,1,2)) # -3


def abs(a):
    if a < 0:
        return -a
    return a

print(abs(10))
print(abs(-10))

