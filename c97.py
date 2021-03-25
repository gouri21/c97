import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
print("guess a number between 1 and 9")
while chances<5:
    guess = int(input("enter your guess"))
    if guess == number:
        print("congratulations you won!")
        break
    elif guess<number:
        print("guess a number higher than that",guess)
    else:
        print("guess a number lower than that",guess)
    chances +=1
if not chances<5:
    print("you lose and the number is",number)



