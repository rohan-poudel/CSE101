def moveUp(students): 
    liss = []
    for i in range(len(students)):
        a = int(students[i][-1])
        b = students[i][0:-1]
        if  a >=1 and a < 4:
            a += 1
        else:
            a = 0
        # print (a)
        c = b + str(a)
        # print(c)
        if a != 0:
            liss.append(c)
    # print(liss)    
    return liss
    

# Test cases 
print('Expected list:', "['Moe, U3', 'Homer, U4']") 
print('  Actual list:', moveUp(['Moe, U2', 'Homer, U3'])) 
print('Expected list:', "['Sydney, U4', 'Qi, U2', 'Cassey, U3']") 
print('  Actual list:', moveUp(['Dan, U4', 'Sydney, U3', 'Qi, U1', 'Jason, U4', 'Cassey, U2'])) 
print('Expected list:', ['Kate, U2', 'Susan, U3', 'Becky, U4', 'Bob, U2']) 
print('  Actual list:', moveUp(['Kate, U1', 'Dan, U4', 'Sydney, U4', 'Susan, U2', 'Becky, U3', 'Qi, U4', 'Bob, U1'])) 
print('Expected list:', '[]') 
print('  Actual list:', moveUp(['Dan, U4', 'Sydney, U4', 'Qi, U4']))