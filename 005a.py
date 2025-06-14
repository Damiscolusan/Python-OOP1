
class Monster():
  
    def __init__(self, health, energy):
        # self.health sprecifies that health belongs to the Monster class
        #it serves as a connector/reference to the monster class
        self.health= health
        self.energy=energy
        print('The monster was created') #__init__ is called whe the object is created

    def __len__(self):
        return self.health
    
    def __abs__(self):
        return self.energy
    
    def __add__(self, other):
        return self.health+other
    
    def __str__(self):
        return(f'The monsters level of health at {self.health}% is still enough to finish the game')
    # def __str__(self):
    #     return f"Circle with radius {self.radius}"
    #methods 
    def attack(self,amount):
        print('The monster has attacked')
        print(f'About {amount}% level of damage was dealt')
        self.energy+=20
        print(self.energy)
        
    def move(self, speed):
        self.speed=speed
        print()
        print(f'The monster has moved')
        print(f"It has a speed of {speed}m/s")
    
    
monster1 =Monster(10,20) #__init__ is called whe the object is created
monster2 =Monster(health=50, energy=100) #__init__ is called whe the object is created

# print(monster1.health)
# print(monster2.health)
print()
# print(len(monster1)); print(abs(monster1))

# For any kind of method, you need a reference to the class as first parameter
# dir  # used to print the result of an object-- atributes and the normal method
# print(dir(monster1))
# __dict__ # gives all of the attributes of an object in form of a dictionary
# print(monster1.__dict__)
# print(vars(monster1))

#for the__add__ method
# print(monster1+55)
# print(monster1.__add__(78))

print(monster1.__str__())
print()
# with str you can just print mpnster 1 and instead of getting the object contianer info
# which is useless to you at the moment 
# you can generate useful info just like that
print(monster1)
print(str(monster1))

