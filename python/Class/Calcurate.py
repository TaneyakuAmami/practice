class Calcurate():
    def __init__(self, a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def print_tot(self):
        tot = self.num1 + self.num2 + self.num3
        print(tot)

myinstance = Calcurate(1,2,3)
myinstance.print_tot()
