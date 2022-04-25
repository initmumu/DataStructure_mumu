class NodeType:
    def __init__(self, item):
        self.info = item
        self.next = None


class queue:
    def __init__(self):
        self.length = 0
        self.rear = None
        self.front = None

    def isFull(self):
        try:
            newItem = NodeType("Full test")
            del newItem
            return False

        except Exception as e:
            return True

    def isEmpty(self):
        return self.length == 0

    def isLength(self):
        return self.length

    def enqueue(self, item):
        newItem = NodeType(item)
        if self.isEmpty():
            self.rear = newItem
            self.length += 1
            self.front = newItem
            return
        
        self.rear.next = newItem
        self.rear = newItem

        self.length += 1
    
    def dequeue(self):
        tempItem = self.front.info
        tempNode = self.front
        self.front = self.front.next

        del tempNode
        self.length -= 1
        return tempItem

    def __str__(self):
        msg = '['
        location = self.front

        for i in range(self.length):
            if i != self.length - 1:
                msg += str(location.info) + ", "
                location = location.next
                continue
            msg += "%s" % location.info

        msg += "]"

        return msg
