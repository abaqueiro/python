#!/usr/bin/python
print('=======================================================')
print('               BOOLEAN OPERATIONS')
print('=======================================================')
print()

values = [ True, False ]

print('negation:')
for v1 in values :
	print( '   ', 'not', v1, 'is', not v1 )
print()

print('or operation:')
for v1 in values :
	for v2 in values :
		print( '   ', v1, 'or', v2, 'is', v1 or v2 )
print()

print('and operation:')
for v1 in values :
	for v2 in values :
		print( '   ', v1, 'and', v2, 'is', v1 and v2 )
print()

