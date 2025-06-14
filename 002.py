class Monster():
    # attributes
    health = 90
    energy = 40

    #methods 
    def attack():
                      #Error , takes 0 positional arguments but one was given
                      # Python passes a reference to the class 
                      # as the first argument into the method, 
                      # so you need to type or add the reference to the monster class e.g. monster, self anything
        print('The monster has attacked')
    
    
monster =Monster()
monster.attack()


# For any kind of method, you need a reference to the class as first parameter
