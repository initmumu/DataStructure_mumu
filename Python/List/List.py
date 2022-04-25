class NodeType:
    def __init__(self, item):
        self.info = item
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0
    
    def isLength(self):
        return self.length

    def isFull(self):
        try:
            newItem = NodeType("Full test")
            del newItem
            return False

        except:
            return True

    def isEmpty(self):
        return (self.length == 0)

    def append(self, item):
        newItem = NodeType(item)
        if self.length == 0:
            self.head = newItem
            self.last = newItem
            newItem.next = newItem
            newItem.prev = newItem
            self.length += 1
            return

        newItem.prev = self.last
        newItem.next = self.head
        self.last.next = newItem
        self.last = newItem
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "Empty List"

        tempNode = self.last
        value = tempNode.info

        self.last = self.last.prev
        self.last.next = self.head

        if self.length == 2:
            self.head = self.last

        elif self.length == 1:
            self.head = None
            self.last = None

        del tempNode

        self.length -= 1

        return value

    def insert(self, item, index):
        if self.length <= index:
            return "out of index"

        location = self.head
        newItem = NodeType(item)
        
        for i in range(index):
            location = location.next
            if i == index - 1:
                newItem.next = location.next
                newItem.prev = location
                newItem.next.prev = newItem
                location.next = newItem
            
        self.length += 1



    def __str__(self):  
        msg = "["
        
        location = self.head
        for i in range(self.length):
            if i != self.length - 1:
                msg += "%s, " % location.info
                location = location.next
                continue
            msg += "%s" %location.info

        msg += "]"
        return msg

        
