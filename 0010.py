#Complex Inheritance

class Monster():
    
    def __init__(self, health, energy):
         self.health = health
         self.energy = energy  
         super().__init__(speed=75, has_scales=False)   #ater writing initial things this came later 
    
    #methods     
    def attack(self, amount):
        print('The monster was attacked')
        print(f'{amount}% damage was dealt')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print (f' It has a speed of {speed}m/s')
        
class Fish():
    
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales
        # super().__init__() # for another list of inheritance or in the mro for maybe 
                             # to inherit from class Snake for example
    
    def swim(self):
        print("The fish is swimming at a speed of " + {self.speed} +' m/s')

# WHen we initially did print(shark.speed), the Normal inheritance of the monster still works because of the mro but 
# The init method of the fish was never called  and so as a consequence. speed and has scales 
# doesn't exist inside of the shark, we have to figure out is how to call this
# def __init__(self, speed, has_scales): method  and since we have to worry about the mro
# we have to fgure out how to call this init method[def __init__(self, speed, has_scales)] method
# with the argument ( speed, has_scales) from inside of the init method of the MOnster
 
# For that purpose we are gonna have the super().__init() method under the Monster class
# super is very intelligent function, the super init nneds to set the fish and has_scales
# of the other class which is the Fish again
 

             
        
class Shark(Monster, Fish): # add all the inheritances in the brackets
    def __init__(self, bite_strength, health, energy):
        self.bite_strength = bite_strength
        super().__init__(health, energy)
        
# In summary and according to the MRO, shark will inherit from the monster class and monster will inherit from the fish class etc.

#print(Shark.mro())

shark= Shark(bite_strength= 50, health = 200, energy = 55)
#shark.attack(10)

# print(shark.health)
# print(shark.energy) ; print(shark.energy) 


print(shark.speed) # error; no attribute speed initially but when we wrote the super thingyy in the monster class
                    # it gave us something
print(shark.has_scales)