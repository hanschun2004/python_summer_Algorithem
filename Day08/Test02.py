# 삽입 정렬
# 대표적 정렬 알고리즘 O(n^2)
# 정렬범위를 1칸씩 확장
# 정렬 범위를 2개를 시작해서 전체로 확장 O(n)
# 새롭게 추가된 값과 기존값이랑 비교 O(n)

ls = [6,4,8,23,5,3,1,12,2,7,9,32,54,26,29]
#ls.sort()
count1 = 0
count2 = 0
def insert_sort(ls):
    print(ls)
    for i in range(1, len(ls)): # i는 두번째 수부터 끝까지 시작
        for j in range(i,0,-1):
            if ls[j-1] > ls[j]:
                ls[j-1] , ls[j] = ls[j] , ls[j-1] # 5 6 1 4 8
                print(ls)
            global count2
            count2 += 1
    global count1
    count1 +=1
    return ls
print(insert_sort(ls))
print("첫 번째 반복문 실행 횟수 : {}".format(count1))
print("두 번째 반복문 실행 횟수 : {}".format(count2))          

print()
# 최적화 삽입 정렬
# 뒤에 있는 데이터가 앞에 있는 데이터보다 작을때만 실행
# 앞에있는 데이터가 뒤에 있는 데이터보다 클때만 실행

ls = [6,4,5,8,3,1,12,2,7,9,32,54,26,29]
# ls.sort()
count1 = 0
count2 = 0
def insert_sort(ls):
    print(ls)
    for i in range(1, len(ls)):
        j = i 
        while j > 0 and ls[j-1] > ls[j]:
            ls[j-1] , ls[j] = ls[j] , ls[j-1]
            print(ls)
            j -= 1
            global count2
            count2 += 1
        global count1
        count1 += 1
    return ls      
print(insert_sort(ls))
print("첫번째 반복문 실행 횟수 : {}".format(count1))
print("두번째 반복문 실행 횟수 : {}".format(count2))     

























































    
    
