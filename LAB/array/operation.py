import array as arr
a=arr.array('i',[1,2,3,4])

print("create array is:")
for i in range(0,3):
    print(a[i],end=" ")

a.append(5)
print("\nappended arry :")
for i in range(len(a)):
    print(a[i],end=" ")


a.insert(4,10)
print("\n after inserted array :")
for i in range(len(a)):
    print(a[i],end=" ")

a.reverse()
print("\n reverse array :")
for i in range(len(a)):
    print(a[i],end=" ")

a.remove(2)
print("\narray:")
for i in range(len(a)):
    print(a[i],end=" ")

a.extend([6,7,8,9,2,1,5,3,10])
print("\narray :")
for i in range(len(a)):
    print(a[i],end=" ")



a.clear()
print("\narray :")
for i in range(len(a)):
    print(a[i],end=" ")







    





