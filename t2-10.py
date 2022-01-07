# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,such as
#counter=1
# While counter <= 5:
#      print(“Type in the”, counter, “number”
#      counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
counter=1
while counter<=5:
    x=int(input("Guess the lucky number betwwen 1 to 100: "))
    if x==50:
        print("Good guess!")
    

    else:
        if counter<5:
            print("Try again!")
    counter+=1

print("Game over!")


