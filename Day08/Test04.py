# 총합을 구하는 재귀 함수

def tot(a):
    result = 0
    if a == 1:
        return 1
    else:
        result = a + tot(a-1)
        return result

print(tot(10))
print(tot(5))


