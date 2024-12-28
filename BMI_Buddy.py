height= float(input('enter height: '))
weight= float(input('enter weight: '))

if height < 3:
    raise ValueError('heigh is wrong!')
if weight < 30:
    raise TypeError

bmi= weight / height ** 2
print(bmi)
