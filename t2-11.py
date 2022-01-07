# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that 
# users do not have to continue guessing after they found the number. If the user does not guess the number at all, print 
# “Sorry but that was not very successful”.

counter=1
while counter<=5:
    x=int(input("Guess the lucky number betwwen 1 to 100: "))
    if x==50:
        print("Good guess!")
        break

    else:
        if counter<5:
            print("Try again!")
    counter+=1

if counter==6:
    print("Sorry but that was not very successful")
