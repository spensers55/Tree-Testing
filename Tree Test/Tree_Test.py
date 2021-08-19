# This program is to test trees in python. For now, I'm only using a binary tree

class TreeNode: # normal child node. For the root, None will be passed
    value = 0
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

def insertVal(val, root): # TODO: Complete insertion
    val = int(val)
    root.value = int(root.value)
    if val <= root.value: # sort down
        if root.leftChild != None: # if not at end of branch, recur
            insertVal(val, root.leftChild)
        else: # if at end of branch, add new node
            newNode = TreeNode
            newNode.parent = root
            newNode.value = val
            root.leftChild = newNode
            newNode.leftChild = None
            newNode.rightChild = None
    else: # sort up
        if root.rightChild != None: # if not at end of branch, recur
            insertVal(val, root.rightChild)
        else: # if at end of branch, add new node
            newNode = TreeNode(val, root)
            root.rightChild = newNode
            newNode.leftChild = None
            newNode.rightChild = None


def removeNode(root, value): # recursive algorithm to remove a value
    node = treeSearch(value, root) # value does not exist
    if node == None:
        print("No such value in tree")
        return
    parent = node.parent
    left = False
    if parent.leftChild == node:
        left = True

    if node.leftChild == None: # node has 1 or 0 children, simple replacement.
        if left:
            parent.leftChlid = node.rightChild # replace child
            parent.leftChild.parent = parent # replace parent
        else:
            parent.rightChild = node.rightChild # replace child
            parent.rightChild.parent = parent # replace parent
        return
    elif node.rightChild == None:
        if left:
            parent.leftChild = node.leftChild # replace child
            parent.leftChild.parent = parent # replace parent
        else:
            parent.rightChild = node.leftChild # replace child
            parent.rightChild.parent = parent # replace parent
        return
    # how to do this sourced from here: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    # executes if node has 2 children
    replacement = findMaxVal(node.leftChild) # find replacment value
    node.value = replacement.value # replace value only
    removeNode(replacement, replacement.value) # recur in order to get rid of replacement 



def findMaxVal(root):
    if root.rightChild == None:
        return root
    else:
        return findMaxVal(root.rightChild)



def treeSearch(value, node):
    current = node
    if current == None: # if we reach end of tree
        return None
    if value != current.value: # when we are not in the correct node
        if value <= current.value:
            current = current.leftChild # get closer
            treeSearch(value, current) # recur
        elif value > current.value:
            current = current.rightChild # get closer
            treeSearch(value, current)
    else: # if we are in the correct node
        return current

root = None
current = None
previous = None
while True:
    print("1: add value\n"+ # menu stolen from my previous projects
        "2: remove value\n"+
        "3: print tree\n"+
        "4: create new tree\n"+
        "5: quit\n")
    choice = input("enter choice: ")
    if choice == "4":
        val = input("Enter the root value: ")
        root = TreeNode(val, None)
    elif choice == "3":
        if root == None:
            print("No tree to print")
        else:
            printTraverse(root)
    elif choice == "2":
        if root == None:
            print("No tree to remove from")
        else:
            val = int(input("Enter value to be removed: "))
            removeNode(root, val)
    elif choice == "1":
        if root != None:
            val = int(input("Enter new value: "))
            insertVal(val, root)
        else:
            print("No tree to add to")
    elif choice == "5":
        break


            