import random

def boston(num_sides):
    sides = []
    sum = 0
    
    for i in range(3):
        sides.append(random.randrange(1,num_sides+1))
    sides.sort()
    sum += sides[-1]
    sides = []
    

    for j in range(2):
        sides.append(random.randrange(1,num_sides+1))
    sides.sort()
    sum += sides[-1]
    sides = []

    
    sides.append(random.randrange(1,num_sides+1))
    sum += sides[0]
    sides = []
       
        
    
    return sum
    

# The code below will call your function many times to check the result.
# If your simulation is correct, the average score when num_sides = 6
# should be approximately 12.9.
trials = 100000
num_sides = 6
avg = sum([boston(num_sides) for i in range(trials)])/trials
print(f'Average score per game for num_sides = {num_sides}: {avg}  (should be approximately 12.9)')

num_sides = 8
avg = sum([boston(num_sides) for i in range(trials)])/trials
print(f'Average score per game for num_sides = {num_sides}: {avg}  (should be approximately 16.8)')

num_sides = 20
avg = sum([boston(num_sides) for i in range(trials)])/trials
print(f'Average score per game for num_sides = {num_sides}: {avg}  (should be approximately 39.8)')
