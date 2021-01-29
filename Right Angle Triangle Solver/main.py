import math
print('---Welcome to Right Angle Triangle Solver---')
a = float(input('\n Enter the Length of First leg of a Triangle?'))
b = float(input('\n Enter the Length of Second leg of a Triangle?'))
h = round(math.sqrt(a*a + b*b),2)

print(f'\nHypotenuse of the Triangle will be {h}')

area = round(a*b/2,2)

print(f'Area of the Triangle with side {a},{b},{h} will be {area}')