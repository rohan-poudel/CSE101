def movieTicket(age,price):
    if age < 2:
        price = 0
        print(price)
    elif age >= 2 and age <= 11:
        price = price * 0.85
        print(price)
    elif age >= 65:
        price  = float(price) * 0.8
        print(price)
    else:
        print(price)

#Test cases
print("Testing movieTicket(60,12): ", end="")
movieTicket(60,12)
print()

print("Testing movieTicket(1,17): ", end="")
movieTicket(1,17)
print()

print("Testing movieTicket(72,15.5): ", end="")
movieTicket(72,15.5)
print()

print("Testing movieTicket(8,11): ", end="")
movieTicket(8,11)