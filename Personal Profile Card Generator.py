username = input("Enter your name: ")
userage = int(input("Enter your age: "))
userhobbies = input("Enter your hobbies: ")
x = {}
x.update({"Name": username, "Age": userage, "Hobbies": userhobbies})
print("Profile Card ;",x)