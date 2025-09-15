try:
    x = int(input("enter a number"))
    print("you are" , x , "years old")
    if x > 80:
        print("you are too old")
    elif x < 10:
        print("you are too young")
    else: print("Welcome in!")
except ValueError as ex:
    print("exception:" , ex)
finally:
    print("Action completed.")