import random

def simple_method():
    ran_num = random.randint(1, 5)
    # print(ran_num)
    number = int(input("Enter a number under 5: "))

    if number == ran_num:
        print("you guessed it right")
    else:
        print("You are wrong")

def by_while_loop_method():
    
    run = True
    ran_num = random.randint(1, 5)
    
    while run == True:

        number = int(input("Enter a number under 5: "))

        if number == ran_num:
            print("you guessed it right")
            break
        else:
            print("You are wrong")
            continue

def limited_attempts_method():
    attempts = 3
    ran_num = random.randint(1, 5)
    
    for i in range(3):
        number = int(input("Enter a number under 5: "))

        if number == ran_num:
            print("you guessed it right")
            break
        else:
            print("You are wrong")
            attempts -= 1
            print("total moves left " + str(attempts))
            continue


