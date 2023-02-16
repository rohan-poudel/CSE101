def calculate(x,n):
    summ = 0
    for i in range(1,n+1):
        
        summ = summ + ((2 * (x ** i)) +((n ** 2) / i))

    print(summ)

#testing values
calculate(3, 6)
calculate(-2, 4)
calculate(7, 2)