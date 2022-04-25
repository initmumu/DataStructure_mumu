from StackAL import *

a = stack()

print(a)
print(a.isLength())


a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)

print(a)
print(a.isLength())

a.pop()
a.pop()
a.deleteItem(3)
print(a)
print(a.isLength())
