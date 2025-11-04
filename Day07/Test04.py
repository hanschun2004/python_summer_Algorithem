# 버블 정렬
# - 대표적 정렬 알고리즘 O(n^2)
# - 앞에서부터 정렬해나가는 구조
# - 선택정렬 vs 버블정렬
# - -> 정렬된 배열이 들어올 경우, 복잡도가 O(n)까지만 가능

# 이웃한 두 값을 비교하여 정렬한다.
# 큰값이 오른쪽으로 이동하는 과정이 반복되면서 비교했던 모든 값들의 최대값이
# 맨 오른쪽으로 옮겨지게 된다.


ls = [ 8,4,1,2,3 ]
def bubble_sort(ls):
    print(ls)
    for i in range(len(ls)-1,0,-1):
        for j in range(0,i):
            temp = ls[i]
            if ls[i] < ls[j]:
                ls[i] , ls[j] = ls[j] , ls[i]
                print(ls)
bubble_sort(ls)



ls = [8,4,1,2,3]
def bubble_sort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[i]:
                ls[j],ls[i] = ls[i],ls[j]
    print(ls)

    
