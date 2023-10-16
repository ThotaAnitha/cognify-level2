import random
def main():
    lower_range= int(input("enter the lower range value:"))
    upper_range= int(input("enter the higher range vale:"))
    random_number=random.randint(lower_range,upper_range)
    check=0
    while True:
        guess=int(input("eter your guess value:"))
        check +=1
        if guess < random_number:
            print("your guess is low!")
        elif guess > random_number:
            print("your guess is high!")
        else:
            print(f,"Congratulations the guess number {random_number} is correct") 
            break
main()
               
    