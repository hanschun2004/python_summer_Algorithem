# 퀵정렬 -> 분할 정복 기법
'''
ls = [3, 7, 6, 5, 2, 4, 9]

def quick_sort(ls):
    left = []
    right = []

    # 피벗 선택
    pr_idx = len(ls) // 2
    x = ls[pr_idx]

    pl = 0
    pr = len(ls) - 1

    while pl <= pr:
        while ls[pl] < x:
            pl += 1
        while ls[pr] > x:
            pr -= 1
        if pl <= pr:
            ls[pl], ls[pr] = ls[pr], ls[pl]
            pl += 1
            pr -= 1
    print(ls)


sorted_ls = quick_sort(ls)
print(sorted_ls)

'''



def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    left = []
    middle = [] # 중간 (데이터 한개)
    right = []

    pivot = ls[len(ls) //2]
    for i in range(len(ls)):
        if ls[i] < pivot:
            left.append(ls[i])
        elif ls[i] > pivot:
            right.append(ls[i])
        else:
            middle.append(ls[i])
    print(left)
    print(right)
    
    return quick_sort(left) + middle + quick_sort(right) # ??

        
print(quick_sort([3,4,1,5,6,2,6,7]))
middle = [5]

























