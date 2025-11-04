# 학생 정보
# 이름 , 나이 , 국어 ,영어 , 수학, 총점, 평균
# 값들은 모두 생성자를 통해 값이 저장될 수 있도록 ..
# 출력 메소드
# 총점 구하는 메소드
# 평균 구하는 메소드
'''
class student:
    name = ""
    age = 0
    korea = 0
    english = 0
    math = 0
    tot = 0
    avg = 0
    def __init__(self, name, age, korea , english , math):
        print("생성자 만듬 확인")
        self.name = name
        self.age = age
        self.korea = korea
        self.english = english
        self.math = math

    def add(self):
        self.added = self.korea + self.english + self.math
        return self.added

    def avg(self):
        avg = self.added/3
        return avg
    
    def showInfo(self,):
        print("이름 : {}".format(self.name))
        print("나이 : {}살".format(self.age))
        print("국어 : {}".format(self.korea))
        print("영어 : {}".format(self.english))
        print("수학 : {}".format(self.math))
        print()
        print("총점 : {}".format(s.add()))
        print("평균 : {:.2f}".format(s.avg()))
        
s = student("홍길동",19,80,60,90)
s.showInfo()
'''

class student:
    name = ""
    age,kor,eng ,math,tot,avg =0,0,0, 0,0,0.0

    def __init__(self,name,age,kor,eng,math):
        self.name = name
        self.age = age
        self.kor = kor
        self.eng = eng
        self.math = math
        self.setTot()
        self.setAvg()

    def setTot(self):
        self.tot = self.kor + self.eng + self.math

    def setAvg(self):
        self.avg = self.tot/3
    
    def disp(self):
        print("이름 : {}".format(self.name))
        print("나이 : {}".format(self.age))
        print("국어 : {}".format(self.kor))
        print("영어 : {}".format(self.eng))
        print("수학 : {}".format(self.math))
        print("총점 : {}".format(self.tot))
        print("평균 : {:.2f}".format(self.avg))
        
st = student("홍길동",20,100,60,90)
st.disp()

st1 = student("이몽룡",30,100,30,90)
st1.disp()
# 기초값을 생성시에 생성자를 사용할 때도 있습니당







    
