correct_pass = "some_pass"
not_found = True
while not_found:
    string=input("enter string: ")
    if string == correct_pass:
        not_found = False
    else: 
        print("wrong password")

print("pasword matched")

'''
correct_pass = "some_pass"
while True:
    string=input("enter string: ")
    if string == correct_pass:
        break
    else: 
        print("wrong password")

print("pasword matched")
'''
