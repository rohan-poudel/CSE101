def ladder(r,cmd):
    rung = 1
    cmd = cmd.upper()
    lenn = len(cmd)
    for i in range(lenn):
        if cmd[i] == 'C':
            rung = rung + 1
            if rung > r:
                rung = 1
        elif cmd[i] == 'D':
            rung = rung - 1
            if rung <= 1:
                rung = 1
        elif cmd[i] == 'J':
            rung =  1
    print(rung)

ladder(4, 'CDDCCCCCJC')
ladder(5, 'CDDCCCCCJC')
ladder(5, 'CDDCCDCCDCCC')
ladder(10, 'CDDCCDCCDCCC')
ladder(10, 'CDDJCCDCCDCCJCCCDCCCCC')
ladder(7, 'CDDJCCDCCDCCJCCCDCC') 
ladder(7, 'DDCDCCCDCJCCDCDCC')