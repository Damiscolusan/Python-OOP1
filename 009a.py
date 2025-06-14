
 
class Monster():
    
    def __init__(self, health, energy):
         self.health = health
         self.energy = energy  
    
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
# first call the Monster init with this old 
# Monster.__init__(self, health, energy) from the monster class, then you'll now add the attributes
# health, energy in the init method from the parent class into the child
# class as def __init__(self, speed, health, energy): 


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