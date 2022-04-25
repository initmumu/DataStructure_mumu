MAX_ITEMS = 100

class stack:
    def __init__(self):
        self.info = [None for i in range(MAX_ITEMS)]
        self.length = 0

    def isFull(self):
        return (self.length == MAX_ITEMS)

    def isEmpty(self):
        return (self.length == 0)

    def isLength(self):
        return self.length

    def push(self, item):
        if self.isFull():
            return "Stack is Full!"

        self.info[self.length] = item
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!!"

        popedItem = self.info[self.length-1]
        self.info[self.length-1] = None
        self.length -= 1

        return popedItem

    def retrieveItem(self, item):
        for i in range(self.length):
            if self.info[i] == item:
                return i

        return "item is not in stack!"

    def deleteItem(self, item):
        index = self.retrieveItem(item)

        if not index == "item is not in stack!":
            for i in range(index, self.length):
                self.info[i] = self.info[i+1]
            self.length -= 1

    def __str__(self):
        msg = "["
        for i in range(self.length):
            if self.length-1 != i:
                msg += str(self.info[i]) + ", "
                continue
            msg += str(self.info[i])
        msg += "]"
        return msg
    