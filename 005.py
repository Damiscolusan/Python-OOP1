# __Dunder __ methods
# [double underscore methods]

# A dunder method is amethod that is notcalled by the user
# Instead it is called by python when something happens
# __init__ is called whe the object is created
# __len __ is called when the object is passed into len()
# __abs __ is called when the object is passed into abs()


class Monster():
  
    def __init__(self, health, energy):
        # self.health sprecifies that health belongs to the Monster class
        #it serves as a connector to the monster class
        self.health= health
        self.energy=energy
        print('The monster was created') #__init__ is called whe the object is created

    #methods 
    def attack(self,amount):
        print('The monster has attacked')
        print(f'About {amount}% level of damage was dealt')
        self.energy+=20
        print(self.energy)
        
    def move(self, speed):
        print()
        print(f'The monster has moved')
        print(f"It has a speed of {speed}m/s")
    
    
monster1 =Monster(10,20) #__init__ is called whe the object is created
monster2 =Monster(health=50, energy=100) #__init__ is called whe the object is created

print(monster1.health)
print(monster2.health)



# For any kind of method, you need a reference to the class as first parameter
