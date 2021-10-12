class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BST:
    def __init__(self):
        self.root = None

    def build(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            temp = self.root
            while True:
                if val < temp.info:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = Node(val)
                        break
                elif val > temp.info:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = Node(val)
                        break
                else:
                    break

def lca(root, search1, search2):
    if root is None:
        return root
    if ((search1 < root.info) and (search2 < root.info)):
        root = lca(root.left,search1,search2)
    elif ((search1 > root.info) and (search2 > root.info)):
        root = lca(root.right,search1,search2)
    elif ((search1 < root.info) and (search2 > root.info)):
        return root
    return root

#for building tree
#tree = BST()
#tree.build(2)
#tree.build(1)
#tree.build(3)

#intial build using user input
# print("Enter the number of nodes")
# size= int(input())

# takes node values
#print("Enter Values")
#for i in range(size):
    #values = int(input())
    #tree.build(values)


#print("First node for lca:")
#search1 = int(input())
#print("Second node for lca:")
#search2 = int(input())
#result = lca(tree.root, search1, search2)
#print(result.info)

