digits = [2, 3, 4, 5,0, 1, 9, 8, 10, 6]
print('Printing original list:')
print(digits)


digits.sort()
print('Sorting the list:')
print(digits)

digits.reverse()
print('Reversing the list:')
print(digits)

digits.sort(reverse=True)
print('Reversing the list:')
print(digits)

more_digits = [1, 0, 2, 3, 5, 4, -5, -3, -2, -1, -4]
print('Printing original list:')
print(more_digits)

more_digits.sort()
print('Sorting the list:')
print(more_digits)

more_digits.sort(reverse=True)
print('Reversing the list:')
print(more_digits)

def absvalue(more_digits):
    return abs(more_digits)
more_digits.sort(key = absvalue)
print('Sorting based on absolute value:')
print(more_digits)

more_digits.sort(key = lambda more_digits: abs(more_digits))
print('Using lambada:')
print(more_digits)

digit_sorted = [3, 6, 4, 7, 5, 2]
print('Printing original list:')
print(digit_sorted)

print('Sorting the list:')
new_list = sorted(digit_sorted)
print(new_list)

print('A tuple:')
tupleDigits = (3, 5, 7, 1, 2, 4, 6, 8, 9)
print(tupleDigits)

print('Reverse tuple:')
new_tuple = sorted(tupleDigits, reverse=True)
print(new_tuple)

print('A dictionary:')
dict_dig = {5, 5, 10, 1, 0}
print(dict_dig)
dict_dig_sorted = sorted(dict_dig)
print(dict_dig_sorted)