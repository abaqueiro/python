#!/usr/bin/python
print('=======================================================')
print('               BODY MASS INDEX CALCULATOR')
print('=======================================================')
name = input('What is your name? ')

msg = name + ', type your weight in kg: '
ans = input(msg)
try:
	weight = float(ans)
	msg = 'Type your height in centimeters: '
	ans = input(msg)
	height = float(ans)
except:
	print('ERROR: Not a number, BYE!')
	quit()

body_mass_index = weight / (height/100) ** 2
print()
print('Your body mass index is: ', body_mass_index)

if body_mass_index >= 30:
	categ = 'OBESITY'
elif body_mass_index >= 25:
	categ = 'OVERWEIGHT'
elif body_mass_index >= 18:
	categ = 'NORMAL weight'
else:
	categ = 'UNDERWEIGHT'
print('This is categorized as',categ)
print()

print('For more info visit:')
print('https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm')
