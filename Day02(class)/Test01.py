# <출력 결과>

# 요금 투입 : 1000
# ================= 커피 자판기 ===================
# 1. 커피(200원) 2. 코코아(250원) 3. 반환 4. 종료
# 메뉴 선택 : 1
# 커피가 나왔습니다.
# 현재 금액은 800원 입니다.

# ================= 커피 자판기 ====================
# 1. 커피(200원) 2. 코코아(250원) 3. 반환 4. 종료
# 메뉴선택 : 2
# 코코아가 나왔습니다.
# 현재 금액은 550원입니다.


# ================= 커피 자판기 ====================
# 1. 커피(200원) 2. 코코아(250원) 3. 반환 4. 종료
# 메뉴선택 : 3
# 550원을 반환합니다.

# exit(0) - 강제 종료

# 금액이 부족하면 다시 요금을 투입할 수 있도록..(심화)
# 금액을 다시 투입하시겠습니까 ? (y/n)
# y  --> 요금 다시 투입
# n  --> break함수 실행
'''
def coffee(money): 
    change = money - 200
    return change

def cocoa(money):
    change = money - 250
    return change

def returns(change):
    change = 0
    returns = change
    return returns
      
def esc():
    print(exit(0))


money = 0
money = int(input("요금 투입 : "))
change = money
while True:
    print("="*13, "커피 자판기","="*13)
    print("1. 커피(200원) 2. 코코아(250원) 3. 반환 4. 종료")
    menu = int(input("메뉴 선택 : "))

    if menu == 1:
        change = coffee(money)
        if change >= 0:
            print("커피가 나왔습니다.")
            print("현재 금액은 {}원 입니다.".format(change))
            money = change
            
        else:
            yn = input("금액을 다시 투입하시겠습니까? (y/n): ")
            if yn == 'y':
                add = int(input("요금 다시 투입 : "))
                money += add
            elif yn =="n":
                esc()
        
    if menu == 2:
        change = cocoa(money)

        if change >= 0:
            print("코코아가 나왔습니다.")
            print("현재 금액은 {}원 입니다.".format(change))
            money = change
        else:
            yn = input("금액을 다시 투입하시겠습니까? (y/n): ")
            if yn == 'y':
                add = int(input("요금 다시 투입 : "))
                money += add
            elif yn =="n":
                esc()
                
    if menu == 3:
        returns = returns(change)
        money = 0
        print("{}원을 반환합니다.".format(returns))
        esc()

    if menu == 4:
        esc()        
'''
def addInputCheck():
    global check # 전역변수 - 같은 변수명에 해당하는 친구를 함수가 끝나도
                 # 그변수가 사라지지 않고 값이 없어지지 않게 해주는 역할
                 # 외부변수를 가져다 쓰겠다...
    while True:
        an = input("모자란 금액을 투입하시겠습니까?")
        if an =="y" or an =="Y":
            check = False
            break
        elif an.lower() == "n":
            break
        else:
            print("잘못된 입력 !")

def coffee(money): 
    if money < 200:
        addInputCheck()
    else:
        money -= 200
        print("커피가 나왔습니다")
        print("현재 금액은 {}원입니다.".format(money))  
    return money

def cocoa(money):
    if money < 250:
        addInputCheck()
    else:
        money -= 250
        print("커피가 나왔습니다")
        print("현재 금액은 {}원입니다.".format(money))  
    return money

def returns(change):
    print("{}원을 반환합니다.".format(money))
      
def esc():
    print(exit(0))


money = 0

while True:
    money += int(input("요금 투입 : "))
    check = True # global
    while check:
        print("===================== 커피 자판기 =======================")
        print("1. 커피(200원) 2. 코코아(250원) 3. 반환 4. 종료")
        n = int(input("메뉴 선택 : "))
        if n == 1:
            money = coffee(money)
        elif n == 2:
            money = cocoa(money)
                
        elif n == 3:
            money = returns(money)

        elif n == 4:
            esc()
        else:
            print("잘못된 번호 입력 !")

























    
