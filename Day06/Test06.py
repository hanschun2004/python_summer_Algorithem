# 동물
# 이름(변수), 색(변수) , 울음소리(메서드) , 먹는 음식(메서드)

# 고양이
# 나비 , 검정색 , 야옹 , 생선

# 강아지
# 초코, 갈색, 멍멍, 사료

# 햄스터
# 햄찌, 회색 , 찍찍 , 해바라기씨


from abc import *

class Animal(metaclass = ABCMeta):
    name = ""
    color = ""

    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food(self):
        pass
        
    def disp(self):
        print("이름 : {}".format(self.name))
        print("색깔 : {}".format(self.color))
        

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name,color)

    def sound(self):
        print("멍멍")
    def food(self):
        print("사료")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name,color)    
    def sound(self):
        print("야용")
    def food(self):
        print("생선")
        
class Hamster(Animal):
    def __init__(self, name, color):
        super().__init__(name,color)    
    def sound(self):
        print("찍찍")
    def food(self):
        print("해바라기씨")


        
d = Dog("초코", "갈색")
d.disp()
d.sound()
d.food()

c = Cat("나비", "검정색")
h = Hamster("햄찌", "회색")











    
