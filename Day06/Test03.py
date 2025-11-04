# 정적 메소드 ( @classmethod , @staticmethod)
# - 클래스 에서 직접 접근 할 수있는 메소드
# - 파이썬에서는 다른 언어와 다르게 정적 메소드임에도 불구하고
# 인스턴스 객체에서도 접근이 가능하다.

class Test:
	def instance_method(self,a,b):
		return a+b 
	
	@classmethod
	def class_method(cls,a,b): # cls 인자를 활용하여 현재 클래스의 클래스 속성을 가져온다. 
		return a+b
	
	@staticmethod # 부모 클래스의 속성값을 가져온다. 
	def static_method(a,b):
		return a+b
	
a = Test()
print(a.instance_method(1,2))
print(a.class_method(3,4))
print(a.static_method(5,6))

print(Test.class_method(10,11))
print(Test.static_method(20,21))
# print(Test.instance_method(20,21)) 객체가 만들어져야지만 사용 가능 


