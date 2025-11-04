# 클래스 구성요소
# 1) 맴버 필드 (변수)
# 2) 함수 ( 매서드)

# 기존 함수와 차이점 (매서드 특징)
# 1) 매개변수 자리에 항상 self를 추가해야한다.
# 2) 매서드 밖에서 선언한 변수 사용시, 변수명 앞에 self.을 붙인다.

def func():
    print("함수 호출")
func()

class Test:
    num=0 # 맴버 필드.. -> 클래스 영역
    def func(self,num): # 클래스 메서드
        self.num = num # self. -> 클래스 안에 있는 변수 (맴버필드)
        print("매서드 호출!")
t = Test()
print(t.num)
t.func(10)
print(t.num)
