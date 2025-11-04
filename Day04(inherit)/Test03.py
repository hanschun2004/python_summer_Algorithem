# 부모 클래스

class Country():
    # name = "국가명"
    population = '인구'
    captial = "수도"
    def __init__(self):
        print("부모 생성자")
    def show(self):
        print("국가 클래스의 매소드입니다.")

# 자식 클래스

class Korea(Country):
    def __init__(self, name, population, captial):
        print("자식 생성자")
        self.name = name
        self.population = population
        self.captial = captial
        super().show() # 부모 생성자 실행 super().메소드 - 부모 메소드 실행
        # super() - 부모 self - 자기자신 
    def show_name(self):
        print("국가 이름은 : ", self.name)
        
    def input_super(self):
        population = self.population
        

c = Country() # 부모 객체
k = Korea("대한민국", 80 , "서울" ) # 자식 객체

print()
k.show_name()
c.show()

print()
k.input_super()
c.show()

