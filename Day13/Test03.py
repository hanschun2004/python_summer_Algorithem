# Tree(트리)
# 계층적인 구조를 표현하기 위한 자료구조
# 여러노드가 한노드를 가르킬 수 없는 구조
# 조직도, 디렉터리 구조
# Stack이나 Queue 같은 선형 구조 X
# 나무 모양의 계층 구조
# 탐색이나 계층적 구조를 가져야하는 데이터를 다루는 곳에 많이 사용

# 이진트리(Binary Tree)
# - 최대 2개의 자식 노드를 가질 수 있는 노드
# - 한개의 노드가 2개의 자식 노드를 가지거나
#   한개를 가지거나, 아예 안가질 수 있다. 
        
class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)

    
    def add(self,data):
        if self.head.val == None:
            self.head.val = data
        else:
            self.add_node(self.head,data)


    def add_node(self,cur,data):
        if data < cur.val:
            if cur.left == None:
                cur.left = Node(data)
            else:
                self.add_node(cur.left,data)

        else:
            if cur.right == None:
                cur.right = Node(data)
            else:
                self.add_node(cur.right,data)

    def search(self,data):
        if self.head.val == None:
            return False
        else:
            return self.search_node(self.head,data)
        
    def search_node(self,cur,data):
        if data == cur.val:
            return True
        else:
            #왼쪽 오른쪽.. data라는 해당값이 있는지..
            if data < cur.val:
                if cur.left == None:
                    return False
                else:
                    return self.search_node(cur.left,data)
            else:
                if cur.right == None:
                    return False
                else:
                    return self.search_node(cur.right,data)

    def __most_left_val(self,cur):#중심노드 가장 왼쪽 객체 리턴..
        if cur.left == None:
            return cur
        else:
            return self.__most_left_val(cur.left)

    def removeData(self,parent,cur,data):
        # - cur 안에 있는 val와 data가 동일하면
        # - parent 왼쪽이 cur와 동일하다면
        # - parent 왼쪽을 None
        # - else
        # - parent 오른쪽 None
        # - cur 를 None

        # else
        # 내가 삭제할 데이터가 cur.val보다 큰지 작은지
        # - 재귀함수
        if cur.val == data:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
            cur = None
        else:
            if cur.val > data:
                self.removeData(cur,cur.left,data)
            else:
                self.removeData(cur,cur.right,data)

    def remove(self,data):
        if self.head == None:
            print("No data!")
        if self.head.val == data:
            if self.head.left == None and self.head.right == None:
                self.head = None
            elif self.head.left != None and self.head.right == None:
                self.head = self.head.left
            elif self.head.left == None and self.head.right != None:
                self.head = self.head.right
            else:
                self.head.val = self.__most_left_val(self.head.right).val
                self.removeData(self.head,self.head.right,self.head.val)
        else:
            if self.head.val > data:
                self.__remove(self.head,self.head.left,data)
            else:
                self.__remove(self.head,self.head.right,data)
                
    def __remove(self,parent,cur,data):#헤드가 아닐때 삭제..
        if cur == None:
            print("No data !")
        if cur.val == data:
            if cur.left == None and cur.right == None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            elif cur.left != None and cur.right == None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            elif cur.left == None and cur.right != None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right

            else:
                c = self.__most_left_val(cur.right)
                cur.val , c.val = c.val , cur.val
                cur.val = self.__most_left_val(cur.right).val
                self.removeData(cur,cur.right,cur.val)

        
        
tr = BinaryTree()
tr.add(20)
tr.add(33)
tr.add(17)
tr.add(15)
tr.add(12)
tr.add(19)
tr.add(22)

print(tr.search(22))
print(tr.search(11))
print(tr.search(33))
tr.remove(20)
tr.remove(22)
print(tr.search(33))
print(tr.search(20))
print(tr.search(22))


