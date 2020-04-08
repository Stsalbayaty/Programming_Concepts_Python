
pocketNum = int(input("Enter a number between 0 and 36: "))

if pocketNum < 0 or pocketNum > 36:
    print("You entered an invalid pocket number, please run the program again to enter a valid number.")
  
else:
    if pocketNum == 0:
        print("Pocket is green.")
    elif pocketNum >= 1 and pocketNum <= 10:
        if pocketNum % 2 == 0:
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif pocketNum >= 11 and pocketNum <= 18:
        if pocketNum % 2 == 0:  
            print("Pocket is red")
        else:
            print("Pocket is black")
    elif pocketNum >= 19 and pocketNum <= 28:
        if pocketNum % 2 == 0: 
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif pocketNum >= 29 and pocketNum <= 36:
        if pocketNum % 2 == 0:  
            print("Pocket is red")
        else:
            print("Pocket is black")