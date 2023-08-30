class LoveDive:
    def setdata(self, first, second):
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

a = LoveDive()
a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())  

b = LoveDive()
b.setdata(10,2)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
