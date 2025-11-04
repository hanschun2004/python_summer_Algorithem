# 버블 정렬 최적화
# 스왑이 한번도 안일어날땐, 패스
def dubble_sort(ls):
    for i in range(len(ls)-1, 0, -1):
        swap = False
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[i] , ls[j] = ls[j] , ls[i]
                swap = True
        if not swap:
            break
ls = [1,2,3,4,8]
dubble_sort(ls)
print(ls)
ls.reverse()
dubble_sort(ls)
print(ls)
            
