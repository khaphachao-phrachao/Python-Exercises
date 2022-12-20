# Create lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

# Instead of printing the elements one by one, make a new list 
# that has all the elements less than 5 from this list in it and 
# print out this new list.
for e in a:
    if e < 5:
        x.append(e)
print(x)

# Same, but in one line
print( [ x for x in a if x < 5 ] ) 

# Ask the user for a number and return a list that contains only 
# elements from the original list a that are smaller than that 
# number given by the user.
z = []
num = int(input("Type your number:"))
for e in a:
    if e < num:
        z.append(e)
print(z)