class opration:
    a=0
    b=0
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def add(self):
        print(self.a + self.b)   
    
 

ob=opration(5,5)
ob.add() 
del ob.a
ob.add()
del ob
 #ob.add()
