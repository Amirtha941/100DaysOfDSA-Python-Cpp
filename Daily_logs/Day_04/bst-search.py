class bst:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(data)

    def search(self, data):
        if self.key == data:
            print(f"{data} found (at node {self.key})")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f"{data} not found in left subtree of {self.key}")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f"{data} not found in right subtree of {self.key}")


root = bst(None)
values = [1, 3, 43, 19, 56]
for i in values:
    root.insert(i)

root.search(1)
root.search(43)
root.search(19)
root.search(100)
