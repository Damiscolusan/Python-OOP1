class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price= price

pizzas =[
    Pizza('Calzone', 8), 
    Pizza('4 cheese', 9.5),
    Pizza('Hawai', 18)
]                

pizzas_names =[i.name for i in pizzas if len(i.name)>5] 

# sum  to count no of elements in a certain condition
expensive_pizzas_nb = sum([1 for i in pizzas if i.price> 10]) # if the condition is met, it starts counting from 1, you can using 2
print(expensive_pizzas_nb)