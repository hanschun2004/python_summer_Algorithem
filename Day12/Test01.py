class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.max = 9999

    def push(self, data): # data 추가
        # 데이터를 추가할때마다 head가 추가한 Node가 되어야 한다.***
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def pop(self): # data 내보내기
        if self.isEmpty():
            print("stack unflower")
            return None
        else:
            data = self.head.val
            self.head = self.head.next
            return data

    def peek(self): # head 데이터값(맨위에 있는 데이터)
        if self.isEmpty():
            print("stack unflower")
            return
        data = self.head.val
        return data

    def isEmpty(self): # head가 비었는지 안비었는지
        return self.head == None
    

    def printStack(self): # 전체 출력
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.printStack()
print()

st.pop()
st.printStack()
print()

print(st.peek())
