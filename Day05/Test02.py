# 구성 항목 : 아이디(id), 공격력(atk), 체력(hp), 공격 대상(target)
# atk,hp 는 양수만 설정 되도록 구현
# [1]   뽀로로   10      100     타요
# [2]   타요     15      80      뽀로로

# [1] 과 [2]를 생성하시고 정보를 출력한뒤 서로 2번 공격하면 어떻게 되는지
# 구현.. attack() 메소드를 player에 추가한 다음
# 공격하면 상대방의 체력이 내 공격력만큼 감소되도록 구현
'''
class Player:
    Id = 0
    atk = 0
    hp = 0
    target = None # 객체
    i = 0
    
    def __init__(self, Id, atk, hp):
        self.Id = Id
        self.atk = atk
        self.hp = hp
        self.check()
     
    def check(self):
        if self.atk > 0:
            print(self.Id," : atk 사용 가능")
        else:
            print(self.Id," : atk 사용 불가능 -> 1로 설정")
            self.atk = 1

        if self.hp > 0:
            print(self.Id," : hp 사용 가능")
        else:
            print(self.Id, " : hp 사용 불가능 -> 50으로 설정")
            self.hp = 50
        
    def disp(self,i):
        self.i = i
        print("[{}]".format(self.i),"{}\t{}\t{}".format(self.Id,
                                      self.atk,
                                      self.hp
                                      ))

    def setTarget(self,target):
        self.target = target
        print("타켓 설정 : ",self.target.Id,"공격 당함")
        

    def attack(self):
        if self.target.hp > 0:
            self.target.hp = self.target.hp - self.atk
            print("{}\t{}\t{}".format(self.target.Id, self.target.atk, self.target.hp))
        else:
            print(self.target.Id," : 사망")
        

p1 = Player("루피",10,100)
p2 = Player("타요",60,80)
print()

print("    {}\t{}\t{}".format("Id","atk","hp"))
p1.disp(1)
p2.disp(2)
print()

p1.setTarget(p2)
p1.attack() # p2의 체력이 p1의 공격력 만큼 줄어들면 된다.
p1.attack() # 타요의 체력은 60
print()

p2.setTarget(p1)
p2.attack()
p2.attack()
p2.attack()

'''


class Player:
    id = ""
    atk = 0
    hp = 0
    target = None # 객체

    
    def __init__(self, id, atk, hp):
        self.id = id
        self.setAtk(atk)
        self.setHp(hp)

    def setAtk(self,atk):
        if atk < 0:
            print("공격력 설정 오류입니다!")
            self.atk = 1
            return
        self.atk = atk

    def setHp(self, hp):
        if hp <= 0:
            print("체력 설정 오류입니다!")
            self.hp = 1
            return
        self.hp = hp 

    def setTarget(self,target):
        self.target = target

    def disp(self):
        print(self.id, self.atk, self.hp , self.target.id, sep ="\t")

    def attack(self):
        self.target.hp -= self.atk
        
     
p1 = Player("뽀로로",10,100)
p2 = Player("타요", 15,80)
p1.setTarget(p2)
p2.setTarget(p1)
p1.disp()
p2.disp()
p1.attack() # p2의 체력이 p1의 공격력 만큼 줄어들면 된다.
p1.attack() # 타요의 체력은 60
p2.disp()



