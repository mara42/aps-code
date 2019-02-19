class linkedList:

    def __init__(self):
        self.nodes = []
        self.head = None
        self.tail = None

    def push(self, value):
        if not self.head:
            self.head = node(value, None)
            if not self.tail:
                self.tail = self.head
        else:
            self.tail.successor = node(value, None)
            self.tail = self.tail.successor

    def ireverse(self):
        current = self.head.successor
        prev = self.head
        while 1:
            nex = current.successor
            current.successor = prev
            prev = current
            current = nex
            if nex is None:
                break
        self.head, self.tail = self.tail, self.head




class node:

    def __init__(self, value, succ):
        self.value = value
        self.successor = succ

    def __str__(self):
        return str(self.value)


asdf = linkedList()

for i in range(10):
    asdf.push(i)

asdf.ireverse()

do = asdf.head
for j in range(10):
    print(do)
    do = do.successor