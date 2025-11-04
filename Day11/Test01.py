class Stack():
    def __init__(self):
        self.stack = []
        self.max = 9999

    # push
    def push(self,data):
        if self.max == len(self.stack):
            print("stack overflow")
            return
        self.stack.append(data)
        

    # pop
    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
            return
        return self.stack.pop() # 리스트 pop함수 이용

    # top
    def top(self):
        if self.isEmpty():
            print("stack underflow")
            return
        return self.stack[-1]

    # isEmpty - return True or False
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)

#문자열을 입력받아 문자열을 거꾸로 출력

def reverse(st):
    stack = Stack()
    result = ""
    for i in st:
        stack.push(i)
    # stack.printStack()
    '''
    while not stack.isEmpty(): # stack에서 pop을 사용하면 list안에 있는 값들이 삭제..
        result += stack.pop() # result = result + stack.pop()
    '''      
    while True:
        result += stack.pop()

        if stack.isEmpty(): #리스트가 비어있는지 안비었는지..
            break
        
    return result
print(reverse("Hello")) # olleH

        












