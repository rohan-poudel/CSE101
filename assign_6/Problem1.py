def fourMostCommonCharacters(strr):
    newstr = strr.upper()
    dictt = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(strr)):
        if newstr[i] in dictt.keys():
            dictt[newstr[i]] += 1
        elif newstr[i] in alpha:
            dictt.update({newstr[i]:1})
    
    # print(dictt)
    lisval = []
    for items in dictt:
        lisval.append((dictt[items],items))
    lisval.sort(reverse=True)
    
    # print(lisval)
    for i in range(4):
        print(str(lisval[i][1]) + str(":") +str(lisval[i][0]), end= " ")
    print("\n")

    return 0

fourMostCommonCharacters("Hyundaimotorcompany") # prints O: 3 Y: 2 N: 2 A: 2
fourMostCommonCharacters("Mississipi")    # prints I: 4 S: 4 M: 1 P: 1 
fourMostCommonCharacters("Daimlerchrysler")     # prints R: 3 L: 2 E: 2 D: 1 
