# 문제 1) 1~n 까지의 합을 출력하는 메서드
# 문제 2) 정수 여러개를 입력받아 최대값을 출력하는 메서드

class Test:
    total = 0 # 총합
    max_num = 0 # 최대값
    def mx(self, *data):
        max_num = data[0]
        for i in data:
            if i > self.max_num:
                self.max_num = i

    def tot(self , num):
        for i in range(num+1):
            self.total += i 

    def disp(self):
        print(self.total)
        print(self.max_num)

t = Test()
t.mx(1,2,3,16)
print(t.max_num)

t.tot(100)
print(t.total)

t.disp()

