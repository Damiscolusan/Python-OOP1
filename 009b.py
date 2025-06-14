
 
class Monster():
    
    def __init__(self, health, energy):
         self.health = health
         self.energy = energy  
    
    #methods     
    def attack(self, amount):
        print('The monster was attacked')
        print(f'{amount}% damage was dealt')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print (f' It has a speed of {speed}m/s')
        
        
# You can overwrite a speed from the parent class in and to the child class e.g move method in parent class
class Shark(Monster):
    def __init__(self, speed, health, energy):
        #Monster.__init__(self,health, energy)
        #super just calls the parent class
        super().__init__(health, energy)
        super(). move(10)  # it displays in the instance of shark Class
        self.speed = speed
        
    # You can call a method of the parent class with super


    def bite(self):
        return('The shark has bitten')  
    
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}m/s')
        
class  Scorpion(Monster):
    def __init__(self,poison_damage, scorpion_health, scorpion_energy):
        super().__init__(health= scorpion_health, energy=scorpion_energy)
        self.poison_damage = poison_damage
        print('The Scorpion is a small but Dangerous Animal')
        
    def attack(self):
        print('The Scorpion attacked')
        print(f'{self.poison_damage}% damage was dealt')
        self.health = self.health-self.poison_damage
        
        # Imaginary sickness damage in a Human class
        #Let's imagine we wantted to get the remaining health from the scorpions attack on a human with an attribute of damage
        # self.scorpion.attack(self.damage)
        
#CReate a ScorpioN class that inherits the Monster and it shd get health and energy from the
# parent, there shd be a poison_damage attribute
#  Overwrite the damage_method to show poison damage



""" shark = Shark( speed = 120, health = 100, energy = 50)
print(shark.speed)
print(shark.health)
print(shark.energy)
print()
shark.move()
shark.attack(78)
print(shark.energy) """
scorpion=Scorpion(poison_damage=15, scorpion_health = 100, scorpion_energy = 50)
scorpion.attack()
print(f'Only {scorpion.health}% of health is remaining for the Scorpion')