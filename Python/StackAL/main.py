from StackAL import *

a = stack()

print(a)
print(a.isLength())


for i in range(1000000000000000000000000):
    a.push(i)

print(a)
print(a.isLength())

a.pop()
a.pop()

print(a)
print(a.isLength())
