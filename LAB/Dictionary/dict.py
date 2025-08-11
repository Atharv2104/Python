Student={"Name":"Atharv","Age":20,"class":"TY"}
print(Student)
print(type(Student))

print(Student["Name"])
print(Student["Age"])
print(Student["class"])


Student.update({"Age":21})
print("updated:",Student)

print("key in student dict:",Student.keys())

print("value in student dict:",Student.values())

print("item in student dict:",Student.items())

print("popitem  in student dict:",Student.popitem())

print("get in student dict:",Student.get("Name"))

Student.clear()
print(Student)

