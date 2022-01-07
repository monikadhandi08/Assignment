while True:
    x=int(input("Guess the lucky number from 1 to 100: "))
    if x==10:
        print("Congratulation you are winner")
        break
    
    else:
        print("Sorry its wrong number")
        y=input("Do you want to guess again 'Yes' or 'no'")
        if y=="no":
            break



