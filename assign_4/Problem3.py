def pizza_cost(size,ext):
    price = 0.0
    if size == 'Small':
        price = 12
    if size == 'Medium':
        price = 14
    if size == 'Large':
        price = 16
    for i in range(len(ext)):
        a = ext.pop()
        b = a.split(" ")
        for j in range(len(b)):
            if b[j] == "Extra":
                price = price + 1.5
            else:
                price = price + 2
    print(price)



pizza_cost('Small', ['Sausage', 'Pineapple']) #16.0 or 16 
pizza_cost('Large', ['Onions', 'Peppers', 'Chocolate', 'Extra Extra Extra Extra Bacon', 'Mushrooms']) #32.0 or 32 
pizza_cost('Medium', ['Olives', 'Extra Extra Extra Sausage', 'Extra Extra Cheese', 'Mushrooms']) #29.5 
pizza_cost('Medium', ['Extra Bacon', 'Chicken', 'Pepperoni'])# 21.5 
 
