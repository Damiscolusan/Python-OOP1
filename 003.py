class Monster():
    # attributes
    health = 90
    energy = 40

    #methods 
    def attack(self,amount):
        print('The monster has attacked')
        print(f'About {amount}% level of damage was dealt')
        monster.energy+=20
        print("The new monster's energy is now " + str(monster.energy)+ '%')   # You can also use self
        
    def move(self, speed):
        print()
        print(f'The monster has moved')
        print(f"It has a speed of {speed}m/s")
    
    
monster =Monster()
monster.attack(40) 
monster.move(20)



# For any kind of method, you need a reference to the class as first parameter
