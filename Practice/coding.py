age = 33
name = 'alex'
flag  = True

print(age, name, flag)

############################

if age > 30:
    flag = True
elif age < 30:
    flag = False
else:
    print('age is 30')

############################

for i in range(0,10):
    print(i)

for i in name:
    print(i)

############################

k = 0
while k < 10:
    print(k)
    k += 1

############################

for index, value in enumerate(name):
    print(index, value)

############################

if "a" in name:
    flag = True
else:
    flag = False

############################

