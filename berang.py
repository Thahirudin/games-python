bigtail = input("Big Tail? (yes/no): ").lower()
if bigtail == "yes":
    glasses = input("glasses? (yes/no): ").lower()
    if glasses == "yes":
        bluetrousers = input("blue trousers? (yes/no): ").lower()
        if bluetrousers == "yes":
            print("Yellow Hat")
        elif bluetrousers == "no":
            print("Red Hat")
        else:
            print("Invalid input")
    elif glasses == "no":
        greenshirt = input("green shirt? (yes/no): ").lower()
        if greenshirt == "yes":
            browntrousers = input("brown trousers? (yes/no): ").lower()
            if browntrousers == "yes":
                print("Blue Hat")
            elif browntrousers == "no":
                print("Yellow Hat")
            else:
                print("Invalid input")
        elif greenshirt == "no":
            print("Blue Hat")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
elif bigtail == "no":
    bigtooth = input("big tooth? (yes/no): ").lower()
    if bigtooth == "yes":
        bluetrousers = input("blue trousers? (yes/no): ").lower()
        if bluetrousers == "yes":
            print("Red Hat")
        elif bluetrousers == "no":
            print("Yellow Hat")
        else:
            print("Invalid input")
    elif bigtooth == "no":
        print("Blue Hat")
    else:
        print("Invalid input")
else:
    print("Invalid input")
