#Complex Inheritance

class Monster():
    
    # Class variables
    num_of_emps = 0
    raise_amt   =  1.04
    
    def __init__(self, health, energy, **kwargs):
        print(kwargs)# gives you dictionary of the remaining stored parameters
        self.health = health
        self.energy = energy  
        # super().__init__(speed=75, has_scales=False)
        super().__init__(**kwargs)  
         
    #methods     
    def attack(self, amount):
        print('The monster was attacked')
        print(f'{amount}% damage was dealt')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print (f' It has a speed of {speed}m/s')
        
class Fish():
   
    # def __init__(self, speed, has_scales, **kwargs): # For more more classes in the complex inheritances 
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales
        # super().__init__(**kwargs) for more classes
        
    
    def swim(self):
        print("The fish is swimming at a speed of " + {self.speed} +' m/s')
 

        
class Shark(Monster, Fish): 
    def __init__(self, bite_strength, health, energy, speed, has_scales): #add fish attributes later
        self.bite_strength = bite_strength
        #The argument needs to be keyword argument so health =health, speed = spped or the value, something should equals something
        super().__init__(health= health, energy = energy, speed= speed, has_scales=has_scales)


shark= Shark(bite_strength= 50, 
             health =200, energy =55, 
              speed = 120, has_scales =False) # inorder for this to work we need 
                                        # keyword unpacking using **kwargs in the 


print(shark.speed) 
# print(shark.has_scales)