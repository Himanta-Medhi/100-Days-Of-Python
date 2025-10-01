import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))

normal_password = []

for num in range(0,no_of_letters):
    normal_password.append(random.choice(letters))

for num in range(0,no_of_symbols):
    normal_password.append(random.choice(symbols))

for num in range(0,no_of_numbers):
    normal_password.append(random.choice(numbers))

# print(normal_password)


random.shuffle(normal_password)
# print(normal_password)

hard_password = ""
for character in normal_password:
    hard_password += character

print(f"Your password is: {hard_password}")