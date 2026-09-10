role=input("enter role: ")
age=int(input("enter age: "))
criteria = role=="student" or role=="Student" and age<21
print("Eligible : ", criteria)