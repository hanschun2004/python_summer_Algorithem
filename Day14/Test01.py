# Direct Graph
# - vertex(노드)와 edge(이동경로)가 있는 그래프
# - edge가 방향성이 있는 그래프(One way)

# Undirect Graph
# - vertex 와 edge 가 존재
# - edge가 방향성이 없는 그래프(Both way)

# weighted graph
# -edge가 value 포함

# vertexList
# 리스트안에 vertex의 값을 다넣으면 vertexlist
# ex) vertexlist = ['0', '1' ..]

# EdgeList
# -리스트 안에 엣지들을 모두 넣으면 엣지 리스트
# ex) edgelist = [(0,1) , (1,0) , (2,1) .. ]

# Adjacency list
# - 리스트 of 리스트
# - edgelist 랑 vertexlist를 합쳐서 생성
# - ex) Adjacency = [[1] , [0] , [0,3] ..]

# BFS 알고리즘(너비 우선탐색)
# - 그래프에서 가까운 노드부터 탐색하는 알고리즘
# - 모든 간선의 비용이 동일한 조건에서 최단거리를 구하는 문제
# - 미로를 빠져나가는 최단 거리 (경로)
# - 그래프에서 가장 가까운 노드부터 우선적으로 탐색하기 때문에
# - 선입선출의 Queue를 사용

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            print("No data!!")
        else:
            value = self.head.val
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return value

    def peek(self):#가장 먼저 삭제 될 데이터를 return
        if self.isEmpty():
            return None
        else:
            return self.head.val

    def isEmpty(self):
        return self.head == None


    def print_Queue(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


# vertexList = ['0','1','2','3','4','5','6']
# edgeList = [(0,1),(1,2),(2,3),(3,4),(4,5),(1,6)]
# graphs = (vertexList , edgeList)

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

visited = [False] * 8
def dfs1(v):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs1(i)
dfs1(1)

'''
def bfs(graph, start):
    vertexList, edgeList = graph
    a = Queue()
    visitedList = []
    a.enqueue = [start]
    adjacencyList = [[] for vertex in vertexList]
    # print(adjacencyList)
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    # print(adjacencyList)
    while a.head:
        current = a.dequeue()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                a.enqueue(neighbor)
        visitedList.append(current)
    return visitedList
'''
def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)
        visited.appen(current)
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
    return visitedList

print(bfs(graphs,0))





#vertexList = ['0','1','2','3','4','5','6']
#edgeList = [(0,1),(1,2),(2,3),(3,4),(4,5),(1,6)]
#graphs = (vertexList , edgeList)
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

def bfs(graph,start):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)
        visited.append(current)
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
    return visited
    
    
print(bfs(graph,1))



graph = [
    [],
    [2,3],
    [4,5],
    [6],
    [2,5],
    [2,4],
    [3,7],
    [6]
]
visited = [False] * 8
def dfs1(v):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs1(i)
dfs1(1)




