# 시간 복잡도
# - 알고리즘 문제를 해결하기 위한 시간(연산)의 횟수를 말한다.
# - 알고리즘을 평가하는데 있어 수행시간과 메모리 사용량을 평가 기준으로
# 두는데 수행시간에 해당하는것이 시간 복잡도 (Time Complexity)
# 메모리 사용량에 해당되는 것이 공간 복잡도 (Space Complexity)

# - 연산 횟수를 카운팅할때 3가지의 경우
# 1. 최선의 경우 Best Case
# 2. 최악의 경우 Worst Case
# 3. 평균적인 경우 Average Case

# Big - O 표기법
# 산술연산 -> O(1)
# 길이가 n인 리스트의 모든 요소 출력 -> O(n)
# 이중 for문 -> O(n^2)
# 삼중 for문 -> O(n^3)

# List자료형은 삽입,제거, 탐색, 포함여부 확인 모두 O(n)에 해당되는 시간 복잡도
# Dictionary, Set는 삽입, 제거, 탐색, 포함여부 확인 연산에 O(1)의 시간복잡도
# 탐색이나 확인이 주로 필요한 연산은 Set이나 Dictionary를 사용하는 것이 좋고
# 순서와 index에 따른 접근이 필요하면 List 자료형을 사용하는 것이 좋다.

# - 복잡도 -
# O(1) < O(log(n)) < O(nlog(n)) < O(n^2) ..

# 1부터 n까지의 합을 구하는 알고리즘
def sum(n): #O(n)
    total = 0
    for i in range(1,n+1):
        total += i
    return total

def sum1(n): #O(1)
    return int((n+1)* n/2)

print(sum(10))
print(sum1(10))

