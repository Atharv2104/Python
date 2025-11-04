fs=frozenset([1,2,3,4,5,6,7])
print(fs)

for i in fs:
    print(i)

#add & removeing not possible

#but still we can do operations like union,intersection,difference

fs1=frozenset([1,2,3,4,5,6,7])
fs2=frozenset([6,4,7,8,9,10,12,13])

result=fs1.union(fs2)
print("Union of frozenSet:",result)


result=fs1&fs2
print("intersection of frozenSet:",result)

result=fs1-fs2
print("difference of frozenSet:",result)
