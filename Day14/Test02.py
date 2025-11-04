#DFS(깊이 우선 탐색)
# - 루트 노드나 임의의 노드에서 시작하여 최대로 진입할 수 있는
# 깊이까지 탐색한 후 돌아와 다른 노드를 탐색하는 방식
# - stack을 사용하여 데이터를 탐색
# - 경로상의 노드들만 기억하면 되므로 저장공간의 수요가 비교적 작다.

graph = {#인접리스트
    1 : [2,3,4],
    2 : [1,5],
    3 : [1,6,7],
    4 : [1,8],
    5 : [2,9],
    6 : [3,10],
    7 : [3],
    8 : [4],
    9 : [5],
    10 : [6]
    }
'''
visited = []
def defs_recursion(graph,cur,visited_arr):
    visited_arr.append(cur)
    for i in graph[cur]:
        if i not in visited_arr:
            defs_recursion(graph,i,visited_arr)

    return

defs_recursion(graph,1,visited)
print(visited)
'''
def def_stack(graph,start):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        for node in graph[current]:
            if node not in visited:
                stack.append(node)
    return visited
print(def_stack(graph,1))
