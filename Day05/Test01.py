# 저희 학원은 자바,C언어만 강의하고 있었습니다.
# 장사가 너무 잘돼서 파이썬 과목을 추가하기로 결정하였고
# 관리 프로그램 클래스도 개량하여 사용하기로 하였습니다.
# (StudentEx 클래스)
# (추가된 항목)
# 파이썬
# 합계, 평균 등이 제대로 나오도록 아래의 객체를 생성후 정보 출력

#     name    java    c       python    
# [1] 엑스맨   80      85      90
# [2] 배트맨   90      85      80
# [3] 슈퍼맨   100     20      25


class Student():
    name = ""
    java = 0
    c = 0
    tot = 0
    avg = 0

    def __init__(self,name,java,c):
        self.name = name
        self.java = java
        self.c = c
        self.tot1()
        self.avg1()


    def tot1(self):
        self.tot = self.java + self.c

    def avg1(self):
        self.avg = self.tot / 2 
        
    def disp(self):
        print("{}\t{}\t{}\t".format(self.name,self.java,self.c),end ="")
        print(self.tot,"\t", self.avg)


class StudentEx(Student):
    python = 0
    
    def __init__(self,name,java,c,python):
        super().__init__(name,java,c)
        self.python = python
        self.tot1() # 여기 도저히 이해 안가서 넘어감
        self.avg1() # 여기 도저히 이해 안가서 넘어감

    def tot1(self):
        self.tot = self.java + self.c + self.python
    
    def avg1(self):
        self.avg = self.tot/3 

    def disp(self):
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(self.name,
                                                  self.java,
                                                  self.c,
                                                  self.python,
                                                  self.tot,
                                                  self.avg))
        
        
parent = Student("홍길동", 88, 44)       
parent.disp()

s1 = StudentEx("엑스맨", 80, 85, 90)
s2 = StudentEx("배트맨", 90, 85, 80)
s3 = StudentEx("슈퍼맨", 100, 20, 25)

s1.disp()
s2.disp()
s3.disp()


      
'''

class Student:
    name = ""
    java = 0
    c = 0
    tot = 0
    avg = 0
    
    def __init__(self, name, java , c):
        self.name = name
        self.java = java
        self.c = c
        self.tot1()
        self.avg1()

    def tot1(self):
        self.tot = self.java + self.c 

    def avg1(self):
        self.avg = self.tot/2

    def disp(self):
        print("{}\t{}\t{}\t{}\t{:.2f}".format(
            self.name,
            self.java,
            self.c,
            self.tot,
            self.avg))


class StudentEx(Student):
    python = 0
    
    def __init__(self, name, java , c, python):
        super().__init__(name, java , c)
        self.python = python
        self.tot1() # 자식 메소드 
        self.avg1() # 자식 메소드 

    def tot1(self):
        self.tot = self.java + self.c + self.python

    def getTot(self):
        return self.tot

    def avg1(self):
        self.avg = self.tot/3 
    
    def disp(self):
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(
            self.name,
            self.java,
            self.c,
            self.python,
            self.tot,
            self.avg))

부모 = Student("홍길동",88,44)
부모.disp()

s1 = StudentEx("엑스맨", 80, 85, 90)
s2 = StudentEx("배트맨", 90, 85, 80)
s3 = StudentEx("슈퍼맨", 100, 20, 25)

s1.disp()
s2.disp()
s3.disp()            

'''











































    
   
