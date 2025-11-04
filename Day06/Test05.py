# 추상 클래스
# abc모듈 import 해야 사용가능
# - 미구현 추상 메소드를 한개 이상 가지면 자식 클래스에 해당 추상 메소드를
# - 반드시 구현하도록 만들어집니다.

from abc import *

class Test(metaclass = ABCMeta):
	name = "이름"
	age = 0
	
	@abstractmethod # 추상메소드 (빈껍데기 메소드)
	def disp(self):  # - 자식에서 무조건 같은 이름으로 오버라이드
		pass
	
class Test1(Test):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def showName(self):
		print("이름은 {}입니다.".format(self.name))
		
	def disp(self):
		print("hello")

a= Test1("홍길동", 20)
a.showName()
# a.disp()
# b = Test() # - 추상 클래스의 객체는 만들 수 없다. 
# 부모 객체를 만들 필요가 없을떄 추상 클래스로 못 만들게 한다. 






