# CSE 101, Assignment 1, Problem 1
m = 180
h = 90
a = 18

#Converting variables
m = float(m) * 0.453592
h = float(h) * 2.54
s = 5
#Formula to Calculate BMR
bmrMan = (10 * m) + (6.25 * h) - (5 * a) + s

print('BMR for man:   ' + str(bmrMan))








'''# Problem 1
# Calculate BMR
print("Hello World!")
m = input('Enter your weight in pounds.')
h = input('Enter your height in total inches.')
a = int(input('Enter your age.'))

#Converting variables
m = float(m) * 0.453592
h = float(h) * 2.54
varr = input('Are you a man?(y/n)')
if varr == 'Y' or varr == 'y':
	s = int(5)
	g = 'Man'
else:
	s = int(-161)
	g = 'Woman'
#Formula to Calculate BMR
bmrMan = (10 * m) + (6.25 * h) - (5 * a) + s
print(f'BMR for man {bmrMan}')
'''