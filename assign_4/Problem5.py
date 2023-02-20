def calculateHighAverageLow(data):
    a = []
    result = []
    avg = 0.0
    for i in range(len(data)):
        b = []
        a = data[i]
        b.append(max(a))
        avg = sum(a)/len(a)
        b.append(avg)
        b.append(min(a))
        result.append(b)
                 
    return result
# Test cases 
print(calculateHighAverageLow([[10, 15], [5]]))   
print(calculateHighAverageLow([[20,30,10,5,5], [36,25,20], [17,2,12,14]]))  
print(calculateHighAverageLow([[20,-25,-30,35,-15], [15,10,-5,25,20,17.5]]))