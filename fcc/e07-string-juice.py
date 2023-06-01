#!/usr/bin/python
print('=' * 80)
print('STRING JUICE'.center(80))
print('=' * 80)

print('\\n can be used as a new line character inside strings:')
print('line 1\nline 2\nline 3')
print()

print("msg = 'orange'")
print()
msg = 'orange'

print( 'Iterate string', msg , 'an array of characters:' )
i = 0
nc = len(msg) # we use len built-in function to get string length
while (i < nc):
	print( 'msg[',i,'] is', msg[i] )
	i = i + 1
print()

print( 'Iterate string', msg, 'as a list using for c in:' )
for c in msg :
	print(c)
print()

print('in operator:')
print( '   ', "'g' in 'orange' is", 'g' in 'orange' )
print( '   ', "'so' in 'Alfonso' is", 'so' in 'Alfonso' )
print()

print('in operator is used to iterate on list members:')
planetList = ['Mercury','Venus','Earth','Mars']
for planet in planetList :
	print('   ', planet)
print()

print('* operator on strings allows string repetition:')
print( "'.' * 80' to build a 80 dots string" )
print( '.' * 80 )
print()

print('we can use the dir(method) to list the methods available in an instance of a class:')
print('type(msg)')
print(type(msg))
print('dir(msg)')
print(dir(msg))


