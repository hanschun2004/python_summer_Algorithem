# 계산기 프로그램
# 메소드 - 더하기 , 뺴기, 곱하기, 나누기
# 모든 내용을 다 출력하는 메소드 (showInfo)
'''
class Calc:
    add = 0
    sub = 0
    multi = 0
    div = 0
    
    def add(self, a, b):
        self.add = a + b

    def sub(self, a, b):
        self.sub = a - b

    def multi(self, a, b):
        self.multi = a * b    

    def div(self, a, b):
        self.div = a / b

    def showInfo(self):
        print("{} + {} = {}".format(a,b, self.add))
        print("{} - {} = {}".format(a,b, self.sub))
        print("{} * {} = {}".format(a,b, self.multi))
        print("{} / {} = {}".format(a,b, self.div))
        
c = Calc()
a = int(input("첫 번째 수 입력 : "))
b = int(input("두 번째 수 입력 : "))

c.add(a,b)
#print(c.add)
c.sub(a,b)
#print(c.sub)  
c.multi(a,b)
#print(c.multi)
c.div(a,b)
#print(c.div)
c.showInfo()
'''

class Calc:
    add = 0
    sub = 0
    multi = 0
    div = 0
    
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b    

    def div(self, a, b):
        return a / b

    def showInfo(self,a,b):
        print("더하기 : {}".format(self.add(a,b))) # 클래스 안의 함수도 호출 가
        print("빼기 : {}".format(self.sub(a,b)))
        print("곱하기: {}".format(self.multi(a,b)))
        print("나누기: {:f}".format(self.div(a,b)))
        
cal = Calc()
cal.showInfo(10,20)



