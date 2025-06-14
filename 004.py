'''zip groups lists or  tuples together 
'''

pizza_names=['4 cheeses', 'calzone', 'hawai']
pizza_prices = [10.5, 11, 9]

names_and_prices = list(zip(pizza_names, pizza_prices))

for (name, price) in names_and_prices:
    print(f"{name} - {price}$")
    
unzipped = list(zip(*names_and_prices))   
unzipped

pn, pp = list(zip(*names_and_prices))  
pn,pp
    
print('AY')
