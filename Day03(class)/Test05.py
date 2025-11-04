class Number:
    # n = 0 - 연산자 메서드 멤버 필드를 안 만들어도 된다. 
    def __init__(self,n):
        self.n = n
    # 연산자 메서드 ( 특수 메서드 )
    # - 객체와 객체끼리의 연산을 해주는 메서드
    # - 보통 클래스에서 재정의 해서 사용하는데 이걸 연산자 오버로딩
    
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    
a = Number(10) # 객체 변수 
b = Number(20)

print(a.__add__(b))
print(a+b)
print(a-b)

# __mul__(self,other) : (A*B)
# __trudediv__(self,other) : (A/B)
# __floordiv__(self,other) : (A//B)
# __mod__(self,other) : (A%B)

























