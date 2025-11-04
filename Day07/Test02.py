# 리스트 자료형 시간복잡도
# 1. index() -> ls[i] -> 인덱스로 값 찾기 -> O(1)
# 2. store() -> ls[i] -> 인덱스로 데이터 저장 -> O(1)
# 3. length() -> len(ls) -> 리스트 길이 -> O(1)
# 4. append() -> ls.append(i) -> 리스트 뒤에 값 저장 -> O(1)

# 5. slice() -> ls[a:b] -> O(n log) ->리스트 길이가 클수록 오래걸림

# 6. insert() -> ls.insert(i,value) -> 원하는 위치에 저장 -> O(n)
# 7. delete() -> ls.remove(value) -> 원하는 값 삭제 -> O(n)

# 8. sort() -> ls.sort() -> 정렬 알고리즘 -> O(N log N)

# 딕셔너리 자료형 시간복잡도
# 대부분의 함수 O(1)
# - for key in dic : O(n)

#O(1) : 상수 시간 -> 문제를 해결 하기 위한 단계 수가 1개
def hello():
    print("hello")

#O(n) : 선형 -> 문제를 해결하기 위한 단계수와 입력값이 1:1 대응
def print_n(n):
    for i in range(n):
        print(i)

#O(n^2) :  반복문 2번 -> 문제 해결하기 위한 단계수가 n^2
def print_n1(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#O(log n) , O(n log n) : 정렬 알고리즘에서 많이 사용
def search(ls,a,first = 0,last=None):
    if not last:
        last = len(ls)
    point = (last - first)
    if ls[point] == a:
        return point
    elif ls[point] > a:
        return search(ls,a,first,point)
    else:
        return search(ls,a,point,last)

# 내가 입력된 값을 찾아주는 알고리즘 
# 인덱스를 계속 찾는 것 
# 자기 함수를 계속 불러오면서 big O 표기법 확인함
#... yeah
