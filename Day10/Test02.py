# 퀵 정렬 (파이썬 장점을 살린 코드)

# 시간 복잡도 평균 O(N log N)
# 데이터가 무작위로 입력된 경우에는 효율적 .. (이미 정렬되어 있는 경우 느림)


def quick_sort(ls):
    if len(ls) <= 1 :
        return ls

    pivot = ls[0]
    tail = ls[1:]
        
    left = [i for i in tail if i <=pivot]
    right = [ i for i in tail if i >= pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort([5,22,6,1,2,4,66]))
