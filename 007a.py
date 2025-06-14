class Monster():
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self.set_energy(energy)
        print(f"A monster that has health at {self.health}% and energy at {self.energy}%")
        
    def update_energy(self,amount):
        print()
        self.energy= self.energy+amount
        #NO need to worry about,return statements or local/global scope, all you do is target the attribute self.energy and 
        # set it to a new value or update whatever you want
        # you can also use a return statement if you want
        
    def set_energy(self, energy):  #1
        new_energy= energy *2   #2
        self.energy = new_energy  #3  #it's 120 because it ran set energy in the init section before update_energy
 
monster =Monster(health=100, energy=50)
# print(monster.health)
monster.update_energy(20)
print(monster.energy)   #it's 120 because it ran set energy in the init section before update_energy
