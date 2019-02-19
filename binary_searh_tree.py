class binarySearchTree:

    def __init__(self, root_val):
        self.root = binarySearchTree.Node(root_val)

    def insert(self, val):
        node = binarySearchTree.Node(val)
        check = self.root
        while 1:
            if check.value < val:
                if check.rchild is None:
                    check.rchild = node
                    return
                check = check.rchild
            else:
                if check.lchild is None:
                    check.lchild = node
                    return
                check = check.lchild

    def __iter__(self):
        return self

    def __next__(self):
        nod = self.root



    class Node:

        def __init__(self, value):
            self.value = value
            self.lchild = None
            self.rchild = None


asdf = binarySearchTree(5)

for i in range(10):
    asdf.insert(i)
