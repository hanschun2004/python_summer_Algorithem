def test1(): # 안받고 안주고 (함수)
    print("test1함수")

def test2(): # 안받고 주고
    print("test2함수")
    return 1 #return을 만나면 무조건 함수 종료 *****
             #return만 쓰면 그냥 함수 종료
             #값을 줄게 있으면 return 뒤에 적어준다.

def test3(a):# 받고 안주고
    print("test3함수",a)

def test4(a):# 받고 주고
    print("test4함수")
    return a

test1() # 안주고 안받고 (호출)
print(test2()) # 안주고 받고
test3(5) # 주고 안받고
print(test4(10)) # 주고 받고   # test4(10) == return값

