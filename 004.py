# __Dunder __ methods
# [double underscore methods]

# A dunder method is a method that is not called by the user
# Instead it is called by python when something happens
# __init__ is called when the object is created
# __len __ is called when the object is passed into len()
# __abs __ is called when the object is passed into abs()    #absolute value i.e. positivise the number


class Monster():
    # attributes
    health = 90
    energy = 40
    
    def __init__(self):
        print('The monster was created') #__init__ is called when the object is created

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
    
    
monster1 =Monster() #__init__ is called when the object is created
monster2 =Monster() #__init__ is called when the object is created

# print(monster1.health)
# print(monster2.health)

#Observe below
print (monster1.energy)
monster1.attack(40)
print(monster1.energy)


# For any kind of method, you need a reference to the class as first parameter
