#!/usr/bin/python
print('=======================================================')
print('               COMPARISON OPERATORS')
print('=======================================================')

try:
	msg = "Type a number (a): "
	ans = input(msg)
	a = float(ans)
	msg = "Type a number (b): "
	ans = input(msg)
	b = float(ans)
except:
	print('ERROR: Not a number, BYE!')
	quit()

print()

# string concatenation
msg = str(a) + ' < ' + str(b) + ' is ' + str(a < b)
print(msg)
msg = str(a) + ' <= ' + str(b) + ' is ' + str(a <= b)
print(msg)
msg = str(a) + ' == ' + str(b) + ' is ' + str(a == b)
print(msg)
msg = str(a) + ' != ' + str(b) + ' is ' + str(a != b)
print(msg)
msg = str(a) + ' > ' + str(b) + ' is ' + str(a > b)
print(msg)
msg = str(a) + ' >= ' + str(b) + ' is ' + str(a >= b)
print(msg)

