def menu():
    print("Press [1] to Enter the number")
    print("Press [0] to Exit the program.")

menu()
option=int(input("Enter your option:"))

while option !=0:
    if option ==1:
        import math

        def isperfectsquare (x):
            s=int(math.sqrt(x))
            return s*s==x

        def isfabonacci (n):
            return isperfectsquare (5*n*n + 4) or isperfectsquare (5*n*n - 4)

        y=(input("Enter no. you want to check: "))

        import math
        s=str(y)

        for x in s:
            i=int(x)
            if (isfabonacci (i) == True):
                 print (i, "is valid")
            else:
                   print (i, "is invalid")
           
   
    else:
        print("Please enter a valid option")

    print()
    menu()
    option=int(input("Enter your option:"))

print("Thank you     ")
