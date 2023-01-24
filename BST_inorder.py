class Node:
    slots= 'element', 'left', 'right'
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0
    def __len__(self):
        return self.count
    
    def createTree(self, node):
        position = input(f"Add node on the Left of {node.element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = Node(nodeData)
            node.left = curr
            self.createTree(curr)
            self.count += 1
        position = input(f"Add node on the Right of {node.element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = Node(nodeData)
            node.right = curr
            self.createTree(curr)
            self.count += 1

    def createRoot(self):
        rootData = input("Enter data for Root: ")
        self.root = Node(rootData)
        self.createTree(self.root)
        self.count += 1

    def inorder(self, troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element, end=" ")
            self.inorder(troot.right)

    def height(self, troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)

            if x > y:
                return x + 1
            else:
                return y + 1
            
        return 0

def options():
    options_list = ['Create Tree', 'Inorder', 'Count','Height']

    print("\nMENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    if choice == 1:
        bt.createRoot()
    elif choice == 2:
        print("Inorder Traversal:")
        bt.inorder(bt.root)
    elif choice == 3:
        print("Number of Nodes: ",len(bt))
    elif choice == 4:
         print("Height: ", bt.height(bt.root) - 1)

if __name__ == '__main__':
    bt = BinaryTree()
    while True:
        choice = options()
        switch_case(choice)
