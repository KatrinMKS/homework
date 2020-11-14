class x:
  def _init_(self, x):
    self.x = x
                
  def check(self, a, b, c):
    return a + b + c == self.x
                
if _name_ == "_main_":
  a = int(input())
  b = int(input())
  c = int(input())
      
  checker = X(180)
  if checker.check(a, b, c):
    print("Triangle")
  else:
    print("It's not triangle")
