file = open("hello.txt","r")
def totalwords(file):
    nlines = nwords = nchars  = diffword = onceword = 0
    
    for line in file:
        dicword = {}
        lenn = line.split()
        
        for word in lenn:
            if word not in dicword:
                dicword[word] = 1
                diffword += 1
            else:
                dicword[word] += 1
                
            
        nlines += 1
        nwords += len(line.split())
        nchars += len(line)
        for keys in dicword:
            if dicword[keys] == 1:
                onceword += 1
        lisval = []
    for items in dicword:
        lisval.append((dicword[items],items))
    lisval.sort(reverse=True)
    
    
    
    print(f"Total Words : {nwords}")
    print(f"Average Word Length : {nchars / nwords:.2f}") 
    print(f"Number of Different Words : {diffword}")
    print(f"Number of Words Used Once : {onceword}")
    print(f"Type-Token Ratio : {diffword/nwords:.2f}")
    print(f"Hapax Legomena Ratio : {onceword/nwords:.2f}")

    # print(lisval)
    for i in range(4):
        print(str(lisval[i][1]) + str(":") +str(lisval[i][0]), end= " ")
    print("\n")
    


totalwords(file)

