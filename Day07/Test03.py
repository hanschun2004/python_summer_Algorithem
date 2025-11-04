# 선택 정렬
# - 작은 값을 찾아내서 첫 인덱스랑 교체
# - 모든 값 중에서 가장 작은값으로 시작
# - 첫번째 값(index=0)을 제외하고 남은 값 중에서 가장 작은 값
# ...
# i번째부터 n-1번째까지 값중에 가장 작은 값
# ...
# 모두 비교하여 비교할 대상이 없을때 정렬

# --> O(1) & O(n) & O(n)
# --> 비효율적 알고리즘, But 구현 쉬움.

ls = [8,4,1,2,3]
def selectsort(ls):
        print(ls)
        print()
        for i in range(0,len(ls)-1):
                for j in range(i+1,len(ls)):
                        selectNum = ls[i]
                        compareNum = ls[j]
                        if selectNum > compareNum: 
                                ls[j] = selectNum
                                ls[i] = compareNum
                                print(ls)
                                print()
selectsort(ls)



ls = [ 8,4,1,2,3 ]
def selectsort(ls):
    for i in range(len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
                # temp= ls[i]
                # ls[i] = ls[j]
                # ls[j] = temp
    print(ls)
selectsort(ls)
