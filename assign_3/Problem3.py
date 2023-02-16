def passwordStrength(password):
    score = 0
    lenn = (len(password))
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    loww = "abcdefghijklmnopqrstuvwxyz"
    digg = "0123456789"
    for i in range(lenn):
        if password[i] in digg and i == 0:
            score = score + 40
        elif password[i] in digg and i != 0:
            score = score + 25
        elif password[i] in upp and i == 0:
            score = score + 25
        elif password[i] in loww and i == lenn - 1:
            score = score + 15
        elif password[i] in loww and i != lenn - 1:
            score = score + 5
        

    
    print(score)

passwordStrength('f^BAcG') 
passwordStrength('W63UtHTuN') 
passwordStrength('Msq08#2wGpMm') 
passwordStrength('qHjTt9YQ')  
passwordStrength('gw74X5I2')  
passwordStrength('9@%B9T(jZJ')  
passwordStrength('y*n(q%XxVp2') 
passwordStrength('!fxus') 
