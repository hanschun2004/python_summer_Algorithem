# stack
# - 데이터의 삽입과 삭제가 데이터의 가장 한쪽 끝에서만 일어나는 자료 구조
# - 가장 마지막에 삽입된 데이터가 가장 먼저 사용되거나 삭제됩니다.
# - LIFO ( 후입 선출 ) Last In First Out

# 예) 편의점 ( 음료 진열대)
#     프링글스 (과장)

# 데이터 삽입 - push
# 삭제 될 데이터를 return - top
# 데이터 삭제 - pop
# isEmpty - 비어 있는지 안비어있는지..


class Stack():
    def __init__(self):
        self.stack = []
        self.max = 9999

    # 푸시
    def push(self, data):
        if self.max == len(self.stack):
            print("stack overflow")
            return
        self.stack.append(data)

    # 팝
    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
            return
        return self.stack.pop() # 리스트 pop함수 이용
        
    # 탑
    def top(self):
        if len(self.stack) == 0:
            print("stack underflow")
            return
        return self.stack[-1]        
    # isEmpty - return True or False
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)
    

stack = Stack()
stack.push(10)# self.stack = [10]
stack.push(20)# self.stack = [10,20]
stack.printStack()

stack.pop() # self.stack = [10]
stack.push(20) # self.stack = [10,20]
stack.printStack()
print(stack.top()) # 20 
        


    
