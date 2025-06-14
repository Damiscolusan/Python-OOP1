class Monster():
    def __init__(self, health, energy):
        self.health = health
        self.set_energy(energy)   
        print(f'The Monster has a health of {self.health}% and energy of {self.energy} kJoules')
        
    def update_energy(self,amount):
        self.energy += amount
        
    def set_energy(self, energy):
        new_energy =energy*2
        self.energy = new_energy
        
    def get_damage(self, amount):
        self.health = self.health-amount
        
""" create a hero class with 2 parameters: damage, monster pass the object 
monster into another class as an argument
THe monster class should have a method that lowers the health-- get_damage(amount) 
which should reduce the health of the monster
Finally, the HEro class should have an attack method that calls the get_damage(amount)
method from the monster and the amount of damage is (hero.damage) 

   """
   
class Hero() :
    def __init__(self,damage, monster):
        self.damage = damage
        self.monster = monster
    
    def attack(self):
        print("Your life will reduce, you monster")
        self.monster.get_damage(self.damage)

   
monster = Monster(health =100, energy=50)
print (monster.energy)
print()

hero= Hero(20, monster=monster)
hero.attack()
print(monster.health)
