class node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = node('Electronics')

    laptop = node('Laptop')

    root.child(laptop)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    pass