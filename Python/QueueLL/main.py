from QueueLL import *

a = queue()

print(a)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)

print(a)
print(a.isLength())
a.dequeue()
a.dequeue()
a.dequeue()


print(a)
print(a.isLength())
