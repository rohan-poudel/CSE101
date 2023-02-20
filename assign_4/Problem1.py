def bestStudent(names, records):
    lenn = len(records)
    marks = []
    result = []
    agee = []
    for i in range(0,lenn,2):
        
        agee.append(records[i])
        marks.append(records[i+1])
        # records.pop(i)

    # print(agee)
    # print(marks)
    maxx = max(marks)
    
    place = marks.index(maxx)
    result.append(names[place])
    result.append(agee[place])
    return  result


# Test cases 
print(bestStudent(['Qi', 'Jack', 'Connor', 'Romin'], [21, 92, 25, 95, 24, 90, 26, 98])) 
print(bestStudent(['Albert', 'Cris', 'Danny'], [22, 100, 24, 90, 23, 91])) 
print(bestStudent(['Albert', 'Erin', 'Yang', 'Cris', 'Danny'], [25, 80, 24, 94, 27, 88, 23, 91, 24, 98])) 
print(bestStudent(['Toni', 'Kim'], [25, 95, 27, 88]))