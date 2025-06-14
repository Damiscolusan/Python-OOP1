#Private Attributes and others


class Monster():
    '''A monster that has some attributes'''
    def __init__(self, health, energy):
         self.health = health
         self.energy = energy  
         
         # private attributes
         self._id =5  #not supposed to be changed and accessed
    
    #methods     
    def attack(self, amount):
        print('The monster was attacked')
        return(f'{amount}% damage was dealt')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print (f' It has a speed of {speed}m/s')
        
monster =Monster(20,10)

# print(monster.id)

# hassattr
"""  
It's format is
hasattr(object, 'attribute_name') , it checks if the attribute is in the object 
and returns a boolean

"""
# print(hasattr(monster, 'health'))
""" if hasattr(monster, 'health'):
    print(f'The monster has {monster.health}% health')    """
    
"""
Set Attribute
It's format is
setattr(object, 'attribute', set_a_new_value)
"""
# setattr(monster,'weapon', 'sword')
## same as doing/assigning a new parameter called monster.weapon = 'sword
# print(monster.weapon)

#Application
""" new_attributes = (['weapon', 'Axe'],['armor', 'Shield'],['potion', 'mana'])
for attr, value in new_attributes:
    setattr(monster,attr, value)
    
print(vars(monster))
"""

"""doc
doc is just there to explain what the monster does 
"""

#print(monster.__doc__)
help(Monster) # used to understand function, classes and pretty much anything and what they do