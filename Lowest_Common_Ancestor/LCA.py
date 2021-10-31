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

class DAGNode:
    def __init__(self, info):
        self.info = info
        self.suc = []
        self.pre = []


def dag_lca(root, search1, search2):
    if type(root) != DAGNode or type(search1) != DAGNode or type(search2) != DAGNode:
        return None
    if root is None:
        return None
    if root == search1 or root == search2:
        return root
    if search1 == search2:
        return search1.info

    result = []
    for i in range(len(search1.pre)):
        for j in range(len(search2.pre)):
            if (search1.pre[i].info == search2.pre[j].info):
                result.append(search1.pre[i].info)

    if (result == []):
        if (search1.info > search2.info):
            result.append(dag_lca(root, search1.pre[0], search2))
        else:
            result.append(dag_lca(root, search1, search2.pre[0]))

    return max(result)


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

