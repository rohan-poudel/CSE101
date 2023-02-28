
def scrabble_sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if len(a[i]) > len(a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            elif len(a[i]) == len(a[j]):
                if a[i] > a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp


    print(a)
#testcases
liss1 = ["hello","my","this","that","something","sandom"]
liss2 = ["poudel","rohan","is","name","my"]
scrabble_sort(liss1)
scrabble_sort(liss2)