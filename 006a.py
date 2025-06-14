"""
Create a Monster class with a parameter called func, store this func as a parameter
Create another class called Attacks, that has 4 methods:
#bite, strike, slash, kick(each method returns some text)

create a Monster object and give it one of the attack methods from the attack class
"""

class Monster():
    def __init__(self, func):
        self.func=func
        
        
class Attacks():
    
    def bite(self):
        return('bite')
        
    def strike(self):
        return('strike')
        
    def slash(self):
        return('slash')
        
    def kick(self):
        return('kick')
    
attack=Attacks().bite  
    
monster=Monster(func=attack)  #func is already equal to a  method, so it has to be later called
print(monster.func())