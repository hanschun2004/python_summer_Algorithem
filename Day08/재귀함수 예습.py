'''
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i

    return output

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))
'''

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))

'''
'''
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(1) : ", fibonacci(1))
print("fibonacci(2) : ", fibonacci(2))
print("fibonacci(3) : ", fibonacci(3))
print("fibonacci(4) : ", fibonacci(4))
print("fibonacci(5) : ", fibonacci(5))
'''
'''
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}입니다.".format(counter))
'''

'''
dictionary = {
    1:1,
    2:1
}

def fibonacci(n):
    if n in dictionary:
        for key, value in dictionary.items():
            print(key, value)
        return dictionary[n]

    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        print("fibonacci({}) + fibonacci({})".format(n-1,n-2))
        dictionary[n] = output

        return output

print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(20) : ", fibonacci(20))
print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))
print("fibonacci(50) : ", fibonacci(50))
'''

'''
def Counter(n):
    if n == 0 :
        return 0
    else:
        Counter(n-1)

print("n = 0 : ", Counter(0))
print(Counter(5))
'''

def Adder(n):
    if n == 1:
        return 1
    else:
        result = n + Adder(n-1)

        print(n, end =" ")
        return result
print("n=1 : ", Adder(1))
print("\nn = 5 : ", Adder(5))
    













































