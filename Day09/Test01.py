# 최대 공약수 ( 유클리드 호제법 )
'''
check = True
def gcd(a,b):
    global check
    
    if a % b == 0:
        return b
    else:
        while check:
            print("{} / {} = {}".format(a,b,a%b))
            check = False
        print("{} / {} = {}".format(b,a%b, b%(a%b)))
        return gcd(b,a%b)

print(gcd(106,16))
'''


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(106,16))





















