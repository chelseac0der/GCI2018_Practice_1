# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string

for i in range(10):
    print("GCI is great")

name = input("Enter your name: ")
print("Hello",name,",please to meet you!","Did you know that your name backwards is", reverse(name),"?" )
