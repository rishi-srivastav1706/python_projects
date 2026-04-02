# a = input("Enter a string: ")
# if a == a[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


a = input("Enter a string: ")
for i in range(len(a) // 2):
    if a[i] != a[-i - 1]:
        print("The string is not a palindrome.")
        break
    else:
        print("The string is a palindrome.")