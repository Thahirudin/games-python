bigtail = int(input("big tail? (1/0): "))
if bigtail == 1 :
    glasses = int(input("glasses? (1/0): "))
    if glasses == 1 :
        bluetrousers = int(input("blue trousers? (1/0): "))
        if bluetrousers == 1 :
            yellowhat = 1 ;
            if yellowhat == 1 :
                print("(Yellow Hat) Berang Berang Pakai Baju Yang Benar")
        elif bluetrousers == 0 :
            redhat = 1 
            if redhat == 1 :
                print("(Red Hat) Berang Berang Pakai Baju Yang Benar")
        else:
            print("Invalid input")
    elif glasses == 0 :
        greenshirt = int(input("green shirt? (1/0): "))
        if greenshirt == 1 :
            browntrousers = int(input("brown trousers? (1/0): "))
            if browntrousers == 1 :
                bluehat = 1 
                if bluehat == 1 :
                    print("(blue hat) Berang Berang Pakai Baju Yang Benar")
            elif browntrousers == 0 :
                yellowhat = 1
                if yellowhat == 1 :
                    print("(yellow hat) Berang Berang Pakai Baju Yang Benar")
            else:
                print("Invalid input")
        elif greenshirt == 0 :
            bluehat = 1
            if bluehat == 1 :
                print("(blue hat) Berang Berang Pakai Baju Yang Benar")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
elif bigtail == 0:
    bigtooth = int(input("big tooth? (1/0): "))
    if bigtooth == 1 :
        bluetrousers = int(input("blue trousers? (1/0): "))
        if bluetrousers == 1 :
            redhat  = 1
            if redhat == 1 :
                print("(red hat) Berang Berang Pakai Baju Yang Benar")
        elif bluetrousers == 0 :
            yellowhat = 1
            if yellowhat == 1 :
                print("(yellow hat) Berang Berang Pakai Baju Yang Benar")
        else:
            print("Invalid input")
    elif bigtooth == 0 :
        bluehat = 1
        if bluehat == 1 :
            print("(blue hat) Berang Berang Pakai Baju Yang Benar")
    else:
        print("Invalid input")
else:
    print("Invalid input")
