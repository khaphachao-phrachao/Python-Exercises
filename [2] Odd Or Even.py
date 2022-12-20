number = int(input("Type your number:"))
if number % 2 == 0 and number % 4 == 0:
    print("Your number's even and is a multiple of 4!")
elif number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")

num = int(input("Type first number:"))
check = int(input("Type second number:"))
if check % num == 0:
    print(f'{num} is a multiple of {check}!')
else:
    print(f'{num} is NOT a multiple of {check}!')