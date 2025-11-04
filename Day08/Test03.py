# 재귀 함수()
# - 함수가 자기 자신을호출하는게 재귀함수

def disp(a):
    if a == 1:
        print(a)
        return # 재귀함수의 종료 지점 ** 만들어주지 않으면 무한 재귀
    print(a)
    disp(a-1)
disp(3)

a=3
for i in range(a,0,-1):
    print(i)
    






























