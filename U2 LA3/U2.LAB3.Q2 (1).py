# errors:

"""
1	Some_number = 0
2	i = 1
3	While i < 11
4		Some_number += 1
5	Print some_number
__________________________________________

1. Line 3, 'while' is a python keyword, and 
hence, must be written the way it is meant
to be written, as python is case sensitive.

2. Again, in line 3, after declaring the 
while statement, the colon (:) is missing,
so the IDE is confused where the scope of
the loop starts and ends.

3. Line 5, the variable name is typed wrong,
instead of 'some_number' it's 'Some_number'.
Python is case senstitive, meaning, when the
variables are called, they must match the 
declaration name. 

4. Line 5, the parentheses around the variable
name are missing. 
__________________________________________

When the program is fixed of all its errors, 
this is what it looks like:


Some_number = 0
i = 1
while i < 11:
    Some_number += 1
print(Some_number)

__________________________________________
"""

number = int(input("Amount of numbers: "))
sum = 0

while (True):
	for n in range(number):
		numbers = float(input("Enter number: "))
		sum += numbers
		
	print("Sum of numbers is",sum)