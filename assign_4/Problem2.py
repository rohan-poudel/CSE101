def tomorrowsDate(today):
    mon = int(today[0:2])
    day = int(today[3:5])
    year = int(today[6:10])
    
    if mon == 12 and day == 30:
        print(f"01/01/"+ str(year+1))
    elif day == 30:
        print(str(mon+1), end = '') 
        print(f'/01/'+ str(year))     
    else:
        print(mon,end="")
        print("/",end="")
        print(day+1,end="")
        print("/",end="")
        print(year)




tomorrowsDate('12/30/1999') #'1/1/2000' or '01/01/2000' 
tomorrowsDate('01/30/1996') #'2/1/1996' or '02/01/1996' 
tomorrowsDate('11/20/2021') #'11/21/2021' 