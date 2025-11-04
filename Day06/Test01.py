class Pen():
	amount = 0 
	def getAmount(self):
		return self.amount
	def setAmount(self, amount):
		self.amount = amount 

class SharpPencil(Pen):
    width = 0 #펜의 굵기
    def setWidth(self, width):
    	self.width = width
    def getWidth(self):
    	return self.width
    	
class BallPen(Pen):
    color = "" #볼펜의 색
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color

class FountainPen(BallPen):
       def refill(self,n):
       	self.setAmount(n)

p = FountainPen()
p.refill(3)
print(p.amount)
p.setColor("주황색")
print(p.getColor())




'''
class Pen():
    amount = 0
    def getAmount(self):
        return self.amount
    def setAmount(self,amount):
        self.amount = amount

class SharpPencil(Pen):
    width = 0 #펜의 굵기
    def setWidth(self,width):
        self.width = width
    def getWidth(self):
        return self.width

class BallPen(Pen):
    color = ""
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color    

class FountainPen(BallPen):
    def refill(self,n):
        self.setAmount(n)

p = FountainPen()
p.refill(3)
print(p.amount) # pen 클래스 안에 있는 amount (할아버지 할머니 맴버필드)
p.setColor("주황색")
print(p.getColor())

'''












































