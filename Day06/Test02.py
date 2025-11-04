class Info:
    __private_a = 5 # __로 시작하면 비공개 속성이된다. (클래스 내부에서만 사용가능)
    __b = 10
    def setA(self,a):
        self.__private_a = a
    def getA(self):
        return self.__private_a
    
info = Info()
info.setA(10)
print(info.getA(self)) # 매세드로 만들어서 불러와야함
