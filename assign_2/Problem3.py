def waterBill(gall):
    price = 50
    if gall <= 110:
        print(price)
    elif gall > 110:
        extra = gall - 110
        price = price + (extra * 0.75)
        print(price)

#Test cases
print("Testing waterBill(60): ", end="")
waterBill(60)
print()

print("Testing waterBill(110): ", end="")
waterBill(110)
print()

print("Testing waterBill(115): ", end="")
waterBill(115)
print()

print("Testing waterBill(145): ", end="")
waterBill(145)

