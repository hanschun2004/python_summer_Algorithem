# 팩토리얼
# 내가 원하는 값까지의 총 곱한 값을 구하기
# ex) fact(5)
# 5*4*3*2*1

def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n

print(fact(5))
print(fact(10))

































