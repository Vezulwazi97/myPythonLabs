hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

user_number = int(input('Enter a number that will replace the middle number in the list: '))
hat_list[2] = user_number
del hat_list[-1]
print('List length: ',len(hat_list))
print(hat_list)
