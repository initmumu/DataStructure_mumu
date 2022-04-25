MAX_ITEMS = 100

class queue:
    def __init__(self):
        self.info = [None for i in range(MAX_ITEMS)]
        self.length = 0
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.length == MAX_ITEMS)

    def isEmpty(self):
        return (self.length == 0)

    def isLength(self):
        return self.length

    def enqueue(self, item):
        if self.isFull():
            return "Queue is Full!"

        self.rear = (self.rear + 1) % MAX_ITEMS

        self.info[self.rear] = item
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty!"

        dequeueValue = self.info[self.front]
        self.front = (self.front + 1) % MAX_ITEMS

        self.length -= 1

        return dequeueValue

    def makeEmpty(self):
        self.info = [None for i in range(MAX_ITEMS)]
        self.length = 0
        self.front = -1
        self.rear = -1

    def __str__(self):
        msg = "["
        tempFront = self.front + 1
        for i in range(self.length):
            if i != self.length - 1:
                msg += str(self.info[tempFront]) + ", "
                tempFront = (tempFront + 1) % MAX_ITEMS
                continue
            msg += str(self.info[tempFront])
        msg += "]"

        return msg
             

        
        