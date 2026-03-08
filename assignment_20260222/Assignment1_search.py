class Node:
    left = None
    right = None
    def __init__(self, val):
        self.val = val
    def printa(self):
        if self.left:
            self.left.printa()
        print(self.val)
        if self.right:
            self.right.printa()
    def search(self, value) -> bool:
        if value < self.val:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value == self.val:
            return True
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

def main():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right = Node(16)
    root.right.left = Node(12)
    root.right.right = Node(20)
    root.printa()
    print(f"Search for 4: {root.search(4)}")
    print(f"Search for 10: {root.search(10)}")
    print(f"Search for 20: {root.search(20)}")

if __name__ == "__main__":
    main()
