file=open("demo.txt","w")

file.write("hello,this is demo file \n")
file.write("we learn file handing")
file.close()

file=open("demo.txt","r")

print(file.read())
file.close()

file = open("demo.txt", "a")
file.write("in python")
file.close()

file=open("demo.txt","r")

print(file.read())
file.close()

