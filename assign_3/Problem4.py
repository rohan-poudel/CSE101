def chooseHighestGPA(a):
    lis1 = a.split(" ")
    # print(lis1)
    x = str(lis1[1])
    y = str(lis1[2])
    z = str(lis1[3])
    x = float(x[0:4])
    y = float(y[0:4])
    z = float(z[0:4])
    maxx = max(x,y,z)
    print(maxx)
    



chooseHighestGPA('Cumulative: 3.84,Department: 3.91,Major: 3.87')
chooseHighestGPA('Coomoolative: 3.90,Depertmant: 3.75,Mayejohr: 3.85')
chooseHighestGPA('Cumulateeve: 4.00,Deperatmaerafsndfat: 4.00,MAYERasdf: 4.00') 