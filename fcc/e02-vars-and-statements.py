#!/usr/bin/python
# no var declaration, just name the var and use it
x = 5

# look how indentation replaces the {} to mark where statements end
# conditional
print( 'x =', x )
if x < 10 :
	print( 'x is smaller than 10' ) # is printed
if x > 20 :
	print( 'x is bigger than 20') # is not printed
print('Finish')
print()

# Using while to count backwards
while x > 0 :
	print(x)
	x = x - 1
print('Cuchaaaa')
print()

# print an integer literal
print(123)
# prints 123
print()

# print a float
print(3.1415)
# prints 3.1415
print()

# print a string
print('hellow')
# prints hellow
print()

# python is case sensitive:
x = 3
X = 23
print(x,X)
# prints 3 23
