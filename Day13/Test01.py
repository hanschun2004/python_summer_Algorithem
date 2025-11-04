# Queue
# FIFO (First In First Out)
# 가장 먼저 쌓인 데이터가 가장 먼저 처리
# 파이썬에서는 queue 라이브러리를 제공하지만 큐와 관련된 자료주로 list를
# 이용하여 구현 가능
# 사용 예) 예약 시스템 , 스케줄링
# 값 입력 -> enque
# 값 삭제 -> dequeue
# 출력 -> print_que
# 비었는지 확인 -> isEmpty

class Queue:
    def __init__(self):
        self.data = []
        
    def enqueue(self,data):
        self.data.insert(0,data)

    def dequeue(self):
        if self.isEmpty():
            print("데이터가 존재하지 않습니다.")
            return None
        return self.data.pop()

    def print_queue(self):
        print(self.data)

    def isEmpty(self):
        return self.data == []

que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.print_queue()
print()

print(que.dequeue())
que.print_queue()




    
















'''
#Queue
#FIFO (First In First Out)
# 가장먼저 쌓인 데이터가 가장 먼저 처리
# 파이썬에서는 queue 라이브러리를 제공하지만 큐와 관련된 자료구조 list를
# 이용하여 구현 가능
# 사용예) 예약시스템, 스케줄링
# 값 입력 -> enqueue
# 값 삭제 -> dequeue
# 출력 -> print_que
# 비었는지 확인 -> isEmpty

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self,data):
        self.data.insert(0,data)

    def dequeue(self):
        if self.isEmpty():
            print("데이터가 존재하지않습니다")
            return None
        return self.data.pop()

    def print_queue(self):
        print(self.data)

    def isEmpty(self):
        return self.data == []

que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.print_queue()
print(que.dequeue())
que.print_queue()
'''
