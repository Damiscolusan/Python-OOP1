class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price= price

pizzas =[
    Pizza('Calzone', 8), 
    Pizza('4 cheese', 9.5),
    Pizza('Hawai', 10)
]                
#Let'sa say I want to create a list for pizza names
# pizza_names =[]
# for i in pizzas:
#     pizza_names.append(i.name)

# How to do above in one line
# pizzas_names =[i.name for i in pizzas] 

#means I take all the items in pizzas which is repd by 'i'  and I am going to add i.name in 'i'
# which is the names of all the pizzas

pizzas_names =[i.name for i in pizzas if len(i.name)>5] 
# only add the item if len(i.name)>5
print(pizzas_names)
