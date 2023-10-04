secret_number = 777

user_number = int(input('Enter your number here: '))

while user_number != secret_number:
    print("Ha ha! You're stuck in my loop")
    user_number = int(input('Enter your number here: '))
print(secret_number,'Well done, muggle! You are free now')
