str = input("Enter a string: ")
count = 0
for i in str:
    if i == " ":
        count += 1
print("The number of spaces in the string is:", count)
