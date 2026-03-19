import string
import random
import os

data_system = os.getenv("LENGTH_PASSWORD")
if data_system is not None:
    length_password = int(data_system)
else:
    length_password = int(input("How many characters do you want in your password? : "))

all_characters = string.ascii_letters + string.digits + string.punctuation
my_password = ""
for i in range(length_password):
    random_character = random.choice(all_characters)
    my_password = my_password + random_character
print(f"Your new password is: {my_password}")