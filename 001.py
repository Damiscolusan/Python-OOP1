

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
    
                
                
                
                
#pizza1 = Pizza('4cheese','8.98',('blue cheese','brie','emmental','mozarella'))
#pizza1.display()

#Create a Tuple pizzas which has 3/4 pizzas with different name, price and ingredients, you need to display all your pizzas
pizzas=( Pizza('4cheese',8.98,('blue cheese','brie','emmental','mozarella'),True),
    Pizza('Dominos',7.93,('Flour', 'cheese','meat','emmental','mozarella')),
        Pizza('Hawai',10.93,('Flour', 'Tomato','meat','onions','Pineapple Sauce')),
        Pizza('Vegetarian',5.93,('Flour', 'blue cheese','Tofu','Mushrooms','Iru'), True)
        )

#for i in pizzas:
 #   if i.vegetarians== True:
  #      print (i.display())
   #     print ()

'''for i in pizzas:
    if not i.vegetarians:
        #print ("This one is Non-vegetarian Pizzas ")
        print (i.display())   '''
        
#For pizzas that has Tomato

for i in pizzas:
    if 'Tomato' in i.ingredients:
        #print ("This one is Non-vegetarian Pizzas ")
        print (i.display())
        
        # Cost less than 10 dollars

for i in pizzas:
    if  i.price< 10:
      
        print (i.display())