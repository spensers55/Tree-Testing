# This program is to test trees in python. For now, I'm only using a binary tree

class TreeNode: # normal child node. For the root, None will be passed
    value = None
    leftChild = None
    rightChild = None
    parent = None
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def printTraverse(node): # recursive algorithm to traverse tree and print
    if node.leftChild != None: # check if we are all the way left
        printTraverse(node.leftChild) # move further left
    print(node.value) # print the value of the node
    if node.rightChild != None: # now check to make sure we are all the way right
        printTraverse(node.rightChild) # move further right
    return # go to parent

def insertVal(val): # TODO: Complete insertion 
    pass

def insertNode(node, root): # TODO: finish removal process
    if node.value < root.value:
        pass
    elif node.value > root.value:
        pass


def removeTraverse(node, value, root): # recursive algorithm to remove a value
    if node.value == value: # checking node value
        parent = node.parent
        if node.leftChild != None:
            if parent.leftChild == node:
                parent.leftChild = node.leftChild # incomplete: only takes care of one child, cannot do both
            else:
                parent.rightChild = node.leftChild
        elif node.rightChild != None:
            if parent.leftChild == node:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
        else:
            if parent.leftChild == node:
                parent.leftChild = None
            else:
               parent.rightChild = None

    if node.leftChild != None:
        printTraverse(node.leftChild)

    if node.rightChild != None:
        printTraverse(node.rightChild)
    return

root = None
current = None
previous = None
while True:
    print("1: add value\n"+ # menu stolen from my previous projects
        "2: remove value\n"+
        "3: print tree\n"+
        "4: create new tree"+
        "5: quit\n")
    choice = input("enter choice: ")
    if choice == "4":
        val = input("Enter the root value: ")
        root = TreeNode(val, None)
    if choice == "3":
        if root == None:
            print("No tree to print")
        else:
            printTraverse(root)
    if choice == "2":
        if root == None:
            print("No tree to remove from")
        else:
            val = input("Enter value to be removed: ")

            