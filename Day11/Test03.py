
#Linked List(연결 리스트)
#Node : 관리할 데이터를 보관하는곳을 노드라고 함
#    -> 자료구조에서 관리하고 있는 정보들 중 하나를 저장하고 있는 단위

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        cur = self.head  # 10의 객체
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        
    def remove(self,data):
        # 데이터 삭제..그 값 찾아서 삭제
        # - head의 값만 있을때랑 head뒤에 데이터가 더 있을때..
        if data == self.head.val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.next.val == data:
                    cur.next = cur.next.next
                    break
                cur = cur.next

    def reverse(self): # 머리부터 꼬리까지 뒤집기 *****
        prev = None
        cur = self.head
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        self.head = prev

        
    def addData(self,data, adddata): # 내가 원하는 위치에 데이터 넣기
        cur = self.head
        
        while cur is not None: 
            if self.val == data:
                add = Node(adddata)
                add.next = cur.next
                cur.next = add
            cur = cur.next
       
    
    def print(self): # 전체 데이터(val)출력
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

linkedList = LinkedList(10)
linkedList.add(20)
linkedList.add(30)
linkedList.print()
linkedList.remove(20)
linkedList.print()
linkedList.remove(30)
linkedList.print()
linkedList.add(20)
linkedList.add(30)
linkedList.print()
#linkedList.remove(10)
#linkedList.print()
linkedList.addData(15,25)
linkedList.print()































