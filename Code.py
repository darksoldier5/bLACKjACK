class player(object):
    def __init__(self,amount):
        self.amount = amount
        self.l = 0;
    def add(self,addition):
        self.amount += addition
class dstrb(object):
	def __init__(self):
		self.l = 0
		self.t = 0
		self.f = 0
	def distribution(self):
		from random import randint
		self.x1 = randint(1,11)
		self.x2 = randint(1,11)
		self.d1 = randint(1,11)
		self.d2 = randint(1,11)
	def reveal(self):
		print('Denomination of your cards are %4.0f and %4.0f' %(self.x1,self.x2))
		print("Denomination of dealer's card is %4.0f" %(self.d1))
	def play(self):
		self.l = input('you want to stand or hit')
	def stand(self):
		print("You have decided to stand and it's dealer's turn now" )
		self.t = self.x1 + self.x2
	def hit(self):
		from random import randint
		self.x3 = randint(1,11)
		self.t = self.x1 + self.x2 + self.x3
		if self.x3 == 11:
			self.t = self.x1 + self.x2 + self.x3 - 10
	def check(self):
		from random import randint
		if self.t == 21:
			print("It's a blackjack and you've won the game")
			self.f = 1
		if self.t > 21:
			print("You're busted and you've lost the game")
			self.f = 0
		else:
			if self.t > (self.d1+self.d2) :
				self.d3 = randint(1,11)
				if(self.d1 + self.d2 + self.d3) > 21:
					print('The dealer is busted and you have won the game')
					self.f = 1
				elif self.t < (self.d1+self.d2+self.d3):
					print("You've lost the bet")
					self.f = 0
				elif self.t > (self.d1 + self.d2 + self.d3):
					print("You've won the bet")
					self.f = 1
				elif self.t == (self.d1 + self.d2 + self.d3):
					print("it's a tie")
					self.f = 2
			if self.t < (self.d1+ self.d2):
				print("you've lost the bet")
				self.f = 0
	def winner(self):
		amnt = int(input("Enter your initial amount"))
		player1 = player(amnt)
		print("How much do you want to bid?")
		bid = int(input("Please enter your bid amount"))
		s = dstrb()
		s.distribution()
		s.reveal()
		s.play()
		if str(self.l).upper().startswith('H'):
			s.hit()
		if str(self.l).upper().startswith('S'):
			s.stand()
		s.check()
		if self.f == 1:
			player1.amount += bid
		elif self.f == 0:
			player1.amount -= bid
		print(player1.amount)
o = dstrb()
print(o.l);
o.winner()
