import datetime

name = input("Give me your name: ")
age = int(input("Your age, please: "))
year = datetime.datetime.today().year
year_100 = year + (100 - age)
print(f"{name}, you'll be 100 years old in {year_100}!")

times_to_print = int(input("How many times do you want this message printed?"))
print(f"{name}, you'll be 100 years old in {year_100}! \n" * times_to_print)