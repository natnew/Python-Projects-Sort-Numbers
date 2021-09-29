# Python Projects: Sort Numbers 🐍
This repo contains python code that sorts some numbers.<br>
Run the code.


Python
```python
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
```

Output
```python
Printing original list:
[2, 3, 4, 5, 0, 1, 9, 8, 10, 6]
Sorting the list:
[0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
Reversing the list:
[10, 9, 8, 6, 5, 4, 3, 2, 1, 0]
Reversing the list:
[10, 9, 8, 6, 5, 4, 3, 2, 1, 0]
Printing original list:
[1, 0, 2, 3, 5, 4, -5, -3, -2, -1, -4]
Sorting the list:
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Reversing the list:
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
Sorting based on absolute value:
[0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
Using lambada:
[0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
Printing original list:
[3, 6, 4, 7, 5, 2]
Sorting the list:
[2, 3, 4, 5, 6, 7]
A tuple:
(3, 5, 7, 1, 2, 4, 6, 8, 9)
Reverse tuple:
[9, 8, 7, 6, 5, 4, 3, 2, 1]
A dictionary:
{0, 1, 10, 5}
[0, 1, 5, 10]
```
