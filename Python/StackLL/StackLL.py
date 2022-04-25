class NodeType:
    def __init__(self, item):
        self.info = item
        self.next = None

class stack:
    def __init__(self):
        self.listData = None
        self.length = 0
    
    def isFull(self):
        try:
            newItem = NodeType("FullCheck")
            del newItem
            return False
        except Exception as e:
            return True

    def isEmpty(self):
        return (self.length == 0)

    def isLength(self):
        return self.length

    def push(self, item):
        if self.isFull():
            return "Stack is Full"

        newItem = NodeType(item)
        newItem.next = self.listData

        self.listData = newItem

        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"

        tempNode = self.listData
        popedValue = tempNode.info
        del tempNode

        self.listData = self.listData.next
        self.length -= 1

        return popedValue

    def __str__(self):
        tempList = list()
        msg = "["

        location = self.listData
        
        for i in range(self.length):
            tempList.append(location.info)
            location = location.next

        tempList.sort()

        for i in range(len(tempList)):
            if not i == self.length - 1:
                msg += str(tempList[i]) + ", "
                continue
            msg += str(tempList[i])
        msg += "]"

        return msg