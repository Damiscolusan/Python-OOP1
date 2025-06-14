class Monster():
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        
        print(f"A monster that has health at {self.health}% and energy at {self.energy}%")
        
    def update_energy(self,amount):
        print()
        self.energy= self.energy + amount
        
    def get_damage(self,amount):
        # self.amount=amount #1
        self.health= self.health-amount  #2
        return amount  #3
             
"""
Create a Hero class with 2 parameters: damage, monster
Pass monster object into another class as an argument
The monster  class should be have a method that 
lowers the health --> get_damage(amount)
The hero class should have an attack method that calls 
the get_damage method from the monster
"""

class Hero():
    def __init__(self, damage, monster):
        self.damage=damage
        self.monster=monster
        
    
    def attack(self):
        # self.damage=self.monster.get_damage(self.damage)
        self.monster.get_damage(self.damage)
        # return self.damage
    
        
        
monster =Monster(health=100, energy=100)
hero =Hero(20,monster=monster)

print(monster.health)
hero.attack()
print(monster.health)
