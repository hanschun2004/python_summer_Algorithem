# 키워드 가변 인자
# - 키워드를 지정하여 인자값을 넣는데.. 인자값의 변수명을 지정하여 넣는 방식
# - 딕셔너리타입으로 인자값이 저장되는 형태
# - 매개변수 앞에 **을 붙여서 선언하면된다.

def disp(**data):
    print(type(data))
    print(data)

    #딕셔너리 key : value
    #value값은 key값을 통해서 호출 가능 ( 딕셔너리명[키값] )

    for key in data: #key = 'a' 'b' 'c'
        print(key , " : ",data[key])
        
disp(a=1,b=2,c=3)
disp(id="hello",pw=1234)

