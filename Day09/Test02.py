def hanoi(n,fm,by,to):
    if n == 1:
        print("1번째 원반이 {}에서 {}로 이동".format(fm,to)) #1acb
    else:
        hanoi(n-1,fm,to,by) # 3-1, 2-1 
        print("{}번째 원반이 {}에서 {}로 이동".format(n,fm,to)) # 2 # 3
        hanoi(n-1,by,fm,to) # 2-1 # 3-1 , 2-1
    

hanoi(3, 'A', 'B', 'C')

# 1번째 원반이 A에서 C로 이동
# 2번째 원반이 A에서 B로 이동
# 1번째 원반이 C에서 B로 이동
# 3번째 원반이 A에서 C로 이동
# 1번째 원반이 B에서 A로 이동
# 2번째 원반이 B에서 C로 이동
# 1번째 원반이 A에서 C로 이동

# 1 : 가장 작은 원반
# 2 : 중간 원반
# 3 : 가장 큰 원반

'''
hanoi(3, a, b, c)
    hanoi(2, a, c,b)
        hanoi(1, a, b ,c)
        -> print(1번 원반 a -> c)

hanoi()
'''









































    
