class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price= price

pizzas =[
    Pizza('Calzone', 8), 
    Pizza('4 cheese', 9.5),
    Pizza('Hawai', 10)
]                

pizzas_names =[i.name for i in pizzas if len(i.name)>5] 

# any : Return True if one item is True
#Concepts
# print(any([False,False,False]))

# print(any([False,False,True]))
# We want to check if pizza is expensive, so its check if any pizza > 10   # for loop shd be written first
expensive_pizza_exists = any([i.price > 10 for i in pizzas])
print(expensive_pizza_exists)