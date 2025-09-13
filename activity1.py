try:
    x = int(input("enter a number"))
    print("you entered", x)
except ValueError as ex:
    print("exception:" , ex)