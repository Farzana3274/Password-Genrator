import random
import random 
letter = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']
entered_letter = int(input("How many letter would you like tto enter? "))
entered_number = int(input("How many number would you like tto enter? "))
entered_symbols = int(input("How many symbol would you like tto enter? "))

password_list = []
for char in range(1, entered_letter+1):
    password_list += random.choice(letter)

for num in range(1, entered_number+1):
   password_list += random.choice(numbers)

for symbol in range(1, entered_symbols + 1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
passord_str = ""
for char in password_list:
    passord_str += char
print(passord_str)






