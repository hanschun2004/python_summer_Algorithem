# 생성자
# -> 객체가 생성될 때 t = Test() 처음으로 실행되면 무조건 한번은 실행되는 메서드

class Info:
    name = ""
    age = 0
    def __init__(self): # 디폴트 생성자 (생성자를 안만들었을때 사용된다.)
        print("기본 생성자")
        
    def __init__(self, name , age):
        print("생성자입니다.")
        self.name = name
        self.age = age

    def __init__(self,a):
        print("매개변수 하나 받아오는 생성자",a)
    
    def disp(self):
        print("이름 : {}".format(self.name))
        print("나이 : {}살".format(self.age))

'''
in2 = Info()
in2.disp()
'''

in1 = Info("홍길동",20) # 객체를 만들때 무조건 실행 
in1.disp()


























