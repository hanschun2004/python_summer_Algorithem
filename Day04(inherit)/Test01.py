# 숫자 이동

# class Game:

    # move = [ 0,0,0,0,8,0,0,0,0,0 ] # 맵
    # player = 0 # 캐릭터의 위치

    # 리스트를 이용해서 리스트 안에 값인 8이 사람
    # 숫자 1 ---> 왼쪽으로 이동 ( 1 )
    # 숫자 2 ---> 오른쪽으로 이동 ( 2 )
    # 리스트 출력 (3)

    # 단, 좌 우 끝에 도달했을때 예외적인 처리
    # 더이상 옆으로 이동 불가능

    # 0은 빈공간
    # 8은 사람  

import random
class Game:

    move = [ '[]','[]','[]','[]','[]','[]','[]','[]','[]','[]' ] # 맵
    player = 0 # 캐릭터의 위치
    left = 0
    right = 0
    
    def __init__(self, player, left , right):
        self.player = player
        self.left = left
        self.right = right

        ran = int(random.random()*len(self.move))
        self.move[ran] = '옷'
        self.player = ran


    def checkIdx(self):
        self.checkPlayerIdx()
        if self.player == 0 or self.player == len(self.move)-1:
           return False

        return True

    def checkPlayerIdx(self):
        for i in range(len(self.move)):
            if self.move[i] =='옷':
                self.player = i
            else:
                continue
        
        return True
        
    def move_left(self):
        self.checkPlayerIdx()
        if self.player > 0:
            self.move[self.player-1] = '옷'
            self.move[self.player] = '[]'
        else:
            print("이동 금지")


    def move_right(self):
        if self.checkIdx() and self.player != '[]':  # ????????
            self.move[self.player + 1] = '옷'
            self.move[self.player] = '[]'
        else:
            print("이동 금지")
       
     
    def start(self):
        while True:
            self.disp()
            n = int(input("1) 왼쪽 이동 2) 오른쪽 이동 3) 종료 : "))
            if n == 1:
                self.move_left()
            elif n == 2:
                self.move_right()
            elif n == 3:
                exit(0)
            else:
                print("잘못 입력 !")
            
    def disp(self):
        for i in range(len(self.move)):
            if self.move[i] =='[]':
                print("[]", end =' ')
            else:
                print("옷",end =' ')
        print()   

game = Game(0,0,0)
game.start()
