class Person:
    name ="홍길동"
    def __init__(self):
        self.data = self.name
        
    @classmethod
    def class_person(cls):
        return cls().name
    
    @staticmethod
    def static_person():
        return Person.name

class Student(Person):
    name = "학생"
person1 = Student.class_person() # cls 인자가 활용되면서 현재 클래스의 속성값을 가져옴
person2 = Student.static_person() # 부모 클래스의 클래스 속성 값만 가져옴
print(person1, person2)














