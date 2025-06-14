

class Pizza():
    def __init__(self, name, price, ingredients, vegetarians=False):
        self.name = name
        self.price= price
        self.ingredients= ingredients
        self.vegetarians = vegetarians



    '''def display(self):
                veg_str=""
                if self.vegetarians: # if vegetarians is True
                    veg_str= "- VEGETARIAN "
                    print(f"PIZZA {self.name}: {self.price}$ "+ veg_str)                    
                print(", ".join(self.ingredients))
                print()
                return '''

    def display(self):
                if self.vegetarians==True:
                    print(f"PIZZA {self.name}: {self.price}$- VEGETARIAN")                    
                else:
                    print(f"PIZZA {self.name}: {self.price}$")
                print(", ".join(self.ingredients))
                return ''  # use return to print an empty line  
    
                
                
                
   
pizzas=[ Pizza('4cheese',8.98,('blue cheese','brie','emmental','mozarella'),True),
    Pizza('Dominos',7.93,('Flour', 'cheese','meat','emmental','mozarella')),
        Pizza('Hawai',10.93,('Flour', 'Tomato','meat','onions','Pineapple Sauce')),
        Pizza('Vegetarian',5.93,('Flour', 'blue cheese','Tofu','Mushrooms','Iru'), True)
        ]

# 
    
# Let's sort the Pizza

def pizza_sort(e):
    # return e.name  # try e.price  len(e.ingredients)
    return e.price                           # for sorting in this format this is just how it works

pizzas.sort(key=pizza_sort, reverse=True)

for i in pizzas:                       # Display sorted pizzas
    print (i.display())        

