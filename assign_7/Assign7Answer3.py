# CSE 101
# Name:
# Email:

# Part 1
def arabic2wolfie(num):
    dictt = {"I":1,"IF":3,"F":4,"IE":7,"E":8,"ET":24,"T":32,"ES":56,"S":64}
    numbers = list(dictt.values())
    symbols = list(dictt.keys())
    wolfie = ''
    i = 0

    while num != 0:
                
        if num in numbers:
            wolfie += symbols[numbers.index(num)]
            num = num - numbers[numbers.index(num)]
            
            
        elif  num > numbers[i] and num < numbers[i+1]:
            wolfie += symbols[i]
            num = num - numbers[i]
            i = -1

        # print(i)
        # print(num)
        i += 1
        

    return wolfie


    
        

    
    

# # Part 2
def wolfie2arabic(symbol):
    dictt = {"I":1,"IF":3,"F":4,"IE":7,"E":8,"ET":24,"T":32,"ES":56,"S":64}
    numbers = list(dictt.values())
    symbols = list(dictt.keys())
    arabic = 0
    lissym = list(symbol)
    
    i = 0
    while lissym != []:
        if len(lissym) == 1:
            arabic += dictt.get(lissym[0])
            return arabic

        
        elif dictt.get(lissym[i]) >= dictt.get(lissym[i+1]):
            arabic += dictt.get(lissym[i])
            del lissym[i]
            i = -1

        elif dictt.get(lissym[i]) < dictt.get(lissym[i+1]):
            arabic -= dictt.get(lissym[i])
            del lissym[i]
            i = -1


        # print(i)
        # print(lissym)

        i += 1


    return arabic



def main():

    # Part 1
    # print("Testing Part 1")
    # print('Testing arabic2wolfie() with num = 10: ' + str(arabic2wolfie(10)))
    # print('Testing arabic2wolfie() with num = 14: ' + str(arabic2wolfie(14)))
    # print('Testing arabic2wolfie() with num = 22: ' + str(arabic2wolfie(22)))
    # print('Testing arabic2wolfie() with num = 28: ' + str(arabic2wolfie(28)))
    # print('Testing arabic2wolfie() with num = 30: ' + str(arabic2wolfie(30)))
    # print('Testing arabic2wolfie() with num = 54: ' + str(arabic2wolfie(54)))
    # print()

    # # Part 2
    # print("Testing Part 2")
    print("Testing wolfie2arabic() with wolfie = 'EII': " + str(wolfie2arabic('EII')))
    print("Testing wolfie2arabic() with wolfie = 'EFII': " + str(wolfie2arabic('EFII')))
    print("Testing wolfie2arabic() with wolfie = 'EEFII': " + str(wolfie2arabic('EEFII')))
    print("Testing wolfie2arabic() with wolfie = 'ETF': " + str(wolfie2arabic('ETF')))
    print("Testing wolfie2arabic() with wolfie = 'ETFII': " + str(wolfie2arabic('ETFII')))
    print("Testing wolfie2arabic() with wolfie = 'TEEFII': " + str(wolfie2arabic('TEEFII')))
    # print()


if __name__ == '__main__':
    main()
