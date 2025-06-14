"""
    Inheritance means that 1 class gets attributes and methods from another 
    class (or classes), we have a parent class and single or multiple child classes
 A class can ingerit from an unlimited number of classes
 """ 
 
class Monster():
    health = 50
    energy = 100
    """def __init__(self, health, energy):
         self.health = health
         self.energy = energy  """
    
    #methods     
    def attack(self, amount):
        print('The monster was attacked')
        return(f'{amount}% damage was dealt')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print (f' It has a speed of {speed}m/s')
        
        
# You can overwrite a speed from the parent class in and to the child class e.g move method in parent class
class Shark(Monster):
    def __init__(self, speed):
        self.speed = speed

    def bite(self):
        return('The shark has bitten')  
    
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}m/s')
        

shark = Shark( speed = 120)
#print(shark.speed)
#print(shark.health)
#print(shark.attack(34))
shark.move()