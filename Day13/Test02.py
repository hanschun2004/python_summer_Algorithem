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


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_Queue()
q.dequeue()
q.dequeue()
q.print_Queue()
print(q.peek())
