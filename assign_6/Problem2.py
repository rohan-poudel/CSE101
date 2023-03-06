file = open("irisdata.txt","r")
def flower(file):
    i = 0
    sepallen = sepalwid = petallen = petalwid  = []
    for line in file:
        
        features = []
        features =  line.split(",")
        classs = features[-1]
        sepallen =  sepallen + [float(features[0])]
        sepalwid =   sepalwid + [float(features[1])]
        petallen =   petallen + [float(features[2])]
        petalwid =   petalwid + [float(features[3])]
        i += 1
        # print(features)

        
        if i == 50:
            # print(sepallen)
            print(f"Class {classs} ")
            print("Average sepallength: " + str(sum(sepallen)/50))
            print("Average sepalwidth: " + str(sum(sepalwid)/50))
            print("Average petallength: " + str(sum(petallen)/50))
            print("Average petalwidth: "+ str(sum(petalwid)/50) + "\n")
            i = 0
            sepallen = sepalwid = petallen = petalwid  = []
        

flower(file)


