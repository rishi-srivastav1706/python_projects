a = input("Enter the first list of elements separated by spaces: ").split()
b = input("Enter the second list of elements separated by spaces: ").split()
set_a = set(a)
set_b = set(b)
if set_a.isdisjoint(set_b):
    print("There are no common elements in the two lists.")
else:
    print("There are common elements in the two lists.")

