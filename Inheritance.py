from msilib.sequence import InstallExecuteSequence


class User:
    def sig_in(self):
         print("logged in")

class Wizard:
    def __init__(self, name,power):
        self.name= name
        self.power =power
    def attack(self):
        print(f'{self.name} attaking with power of {self.power}')
class Archer:
   def __init__(self, name,num_arrows):
        self.name= name
        self.num_arrows =num_arrows
   def attack(self):
        print(f'{self.name} attacking with arrows of {self.num_arrows}')

wizard1 = Wizard("Mahesh", 200)
archer1 = Archer("Thalapaty", 300)
wizard1.attack()
archer1.attack()
print(isinstance(wizard1, Wizard))
