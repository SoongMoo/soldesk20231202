val = 10
PI = 3.141592
def randint(x):
	return 3 * x + 5
class Calc:
     	def __init__(self, first, second): # 멤버필드를 초기화하기 위한 메서드 : 생성자
         		self.first = first
         		self.second = second
     	def add(self):
         		self.result = self.first + self.second
         		return self.result
     	def div(self):
         		self.result = self.first / self.second
         		return self.result
calc = Calc(10, 20)