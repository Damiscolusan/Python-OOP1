#"

#"Classes and scope

#"Since every method has a reference to the class it is easy to get and change class
#"class attributes
 #"
#"Because of that, methods rely much less on parameters, global and return
#"(although you can use it)
 
#"Objects can even be influence from the outside and from a local scope of a function
 
#"Scope Problem

def update_health(amount):
    health+= amount

health = 10
update_health(20)

print(health)


#it won't work