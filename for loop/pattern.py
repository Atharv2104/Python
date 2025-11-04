def print_design(n):
    for i in range(n):
        for j in range(0,i+1):
            print(j,end=' ')
        print()
n=int(input("enter N"))
print_design(n)            