# [ 상속 ] - 부모를 선택하여 코드를 흡수하는 것
# [ 규칙 ]
# - 자식이 부모를 선택
# - 1개만 선택 가능
# - 선택시 부모클래스의 모든 코드가 자식 클래스에도 적용 **

# [ 주의 사항 ]
# - 부모 클래스는 별다른 언급이 없어도 자동 초기화
#   super() 자동생성 , 적으면 적은 내용이 적용된다
# - 부모클래스는 위에 말했던 것 처럼 자동초기화가 되므로
#   생성자의 형태를 반드시 맞추어야한다.
# - 부모와 자식클래스에서 같은 이름이 존재할 경우 자식이 우선 **





# 부모 클래스

class Country():
    name = "국가명"
    population = '인구'
    captial = "수도"
    def __init__(self,name):
        self.name = name
    def show(self):
        print("국가 클래스의 매소드입니다.")

# 자식 클래스

class Korea(Country):
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("국가 이름은 : ", self.name)

c = Country("대한 민국") # 부모 클래스 객체
print(c.name) 
k= Korea("한국") # 자식 클래스 객체
print(c.name)
print()
k.show_name() # 자식 매서드
k.show() # 부모 메서드 - 부모의 모든 내용이 자식에게도 적용이 된다는 것을 알 수 있다. 
c.show()
print(k.captial)
#print(c.show_name)# - 부모에서는 자식 메서드 접근 불가










































