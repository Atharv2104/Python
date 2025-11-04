try:
    x=int(input("enter a no:"))
    y=int(input("enter a no"))
    z=x/y
except ValueError:
    print("invlid no")
except ZeroDivisionError:
    print("can not divide by zero")
else:
    print("result is:",z)
finally:
    print("execution completed")                
    