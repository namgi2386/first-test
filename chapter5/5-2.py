class LoveDive:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = LoveDive(4,2)
print(a.add())

class MoreLoveDive(LoveDive): #매서드 상속
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreLoveDive(5,2)
print(b.add())
print(b.pow())
print(b.div())

class SafeLoveDive(LoveDive): #매서드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        else :
            return self.first / self.second
        
c = SafeLoveDive(5,0)
print(c.div())

class Family:
    lastname = "김"

x = Family()
y = Family()

print(x.lastname)
print(y.lastname)