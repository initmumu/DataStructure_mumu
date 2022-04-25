from StackLL import *

a = stack()

print(a)
print(a.isLength())


for i in range(1,11):
    a.push(i)

print(a)
print(a.isLength())

a.pop()
a.pop()

print(a)
print(a.isLength())
