from smart import *
print("1- addition \n 2- substitution \n 3- multiplication \n 4- division \n 5-square \n 6-power \n 7- to quit")
x=int(input())
while(x!=7):
    if(0<x<7):
        match x:
            case 1:
                try:
                    
                    a=float(input("type the first number:"))
                    b=float(input("type the second:"))
                    print(add(a,b))
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
            case 2:
                try:

                    a=int(input("type the first number:"))
                    b=int(input("type the second:"))
                    print(subs(a,b))
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
            case 3:
                try:

                    a=int(input("type the first number:"))
                    b=int(input("type the second:"))
                    print(mul(a,b))
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
            case 4:
                try:

                    a=int(input("type the first number:"))
                    b=int(input("type the second:"))
                    print(basic.div(a,b))
                except ZeroDivisionError:
                    print("you can't divide by zero")
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
            case 5:
                try:
                    a=int(input("type your number"))
                    if a<0:
                        print("your number shouldn't be negative")
                    else:
                        print(square(a))
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
            case _:
                try:
                    a=int(input("type the number:"))
                    b=int(input("type the power:"))
                    print(power(a,b))
                except limitexception:
                    print(f"you can't put a number bigger than {config.MAX_VALUE}")
                break
    else:
                print("choose a valid number ")
                print("1- addition \n 2- substitution \n 3- multiplication \n 4- division \n 5-square \n 6-power \n 7- to quit")
                x=int(input())
