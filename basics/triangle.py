# making right trinagle
'''
like this:
*
**
***
****
*****
******
'''

x = int(input('inter the hight of triangle: '))
star = "*"
for i in range(x):
    print('{}'.format(star * i))



# making isosceles triangle

for i in range(x):
    print("{}".format((star*i).center(x+1)))


# making right 90^ triangle

for i in range(x):
    print('{}'.format((star*i).rjust(x+1)))
