# python implementation of binary search tree

'''
creation of a BST through Node class.

insert, update, delete through functions

in/pre/post-order traversal through functions
'''

# define a basic node. With left right parameters and value
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

# root: the root node of the BST
# val: the new node value to be inserted.
def insert(root, val):
    # check if end is reached. If yes all the node
    if root is None:
        root = Node(val)
        return

    if val >= root.value:
        # value to be inserted lies in right subtree
        insert(root.right, val)
    else:
        # value to be inserted is in the right subtree
        insert(root.left, val)


# root: the root node of the BST
def inorder(root):
    inorder(root.left)
    print(root.value)
    inorder(root.left)

