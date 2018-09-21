class math():
    def add(self, a, b):
        print("add:", a + b)
 
class mean(math):
    def add(self, a, b):
        print("add:", a + b + b)
    
ab = mean()
ab.add(1, 3)
