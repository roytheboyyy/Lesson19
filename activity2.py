try:
    a , b = eval(input("enter two numbers separated by a comma"))
    result = a / b
    print("result is", result)
except ZeroDivisionError as e1:
    print("Divived by Zero !!",e1)
except SyntaxError as e2:
    print("Numbers entered wrong",e2)

else:

    print("No Exceptions")

finally:

    print("This will execute no matter what")