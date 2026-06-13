a = 8
b = 7
if a > b :
    print("a is greater than b")
c = "Hamza"
d = "Hamza"
if c == d :
    print("Both are equal")
e = 9
d = 8
if e > d :
    print("e is lesser than d")
f = 18
if f >= 18 :
    print("You are able to vote")
marks = 80
if marks <= 50 :
    print("Youhave passed")
else:
    print("You have failed")
g = 9
h = 78
if g < h :
    print("h is greater than g")
else:
    print("g is greater h ")
text_variable = ""
if text_variable == "":
    print("The variable contains an empty string!")
else:
    print("The variable is not empty.")
name = "Muhammed Rafiq"
if name == "Muhammed Rafiq":
    print("The name is there")
null = 0
if null == 0 :
    print("Truth")
else:
    print("false")
numb = 7
if numb == 0 :
    print("Truth")
else:
    print("Falsy")
mar = 98
if mar >= 80 :
    print("YOU passed")
else:
    print("You need improvemnet")

correct_username = "admin"
correct_password = "SecretPassword123"

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

