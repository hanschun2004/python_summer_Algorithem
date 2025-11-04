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

# 괄호의 짝 확인하기
# 괄호의 균형이 맞는지 확인 by True, False
# ((()))  -> True
# ((((())) -> False
# ()() -> True

def balance(st):
    stack = Stack()
    check = True

    for i in st:
        if i == "(":
            stack.push(i)
        else:
            # pop하기 전에 stack객체 안에 리스트가 비었는지..
            if stack.isEmpty():
                check = False
            else:
                stack.pop()
            # 리스트가 비었으면 check = False..
            # 리스트가 안비었으면 계속 stack.pop()
    if check and stack.isEmpty():
        return True
    else:
        return False

print(balance("()()"))
print(balance("(()))"))
print(balance("((((()))))"))
print(balance("()()(())()()"))












