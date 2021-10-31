from unittest import TestCase

from LCA import *

class Test(TestCase):
    def test_bst(self):
        # when root is not defined in BST
        tree=BST()
        self.assertEqual((tree.root),None)


    def test_lca(self):
    # most basic case tree with two children
    #    2
    #   / \
    #  1   3
        tree=BST()
        tree.build(2)
        tree.build(1)
        tree.build(3)
        self.assertEqual(lca(tree.root, 1, 3).info, 2)

    def test_EmptyLCA(self):
        #finding LCA when root doesn't exist
        tree=BST()
        self.assertEqual(lca(tree.root, 1, 3),None)

    def test_OnlyRootLCA(self):
        # when only root exist
        tree=BST()
        tree.build(1)
        self.assertEqual(lca(tree.root, 1, 1).info, 1)

    def test_BalancedLCA(self):
        #     45
        #   /    \
        #  10     80
        # /  \   /
        # 7   12 50
        # non balanced tree
        tree = BST()
        tree.build(45)
        tree.build(10)
        tree.build(7)
        tree.build(12)
        tree.build(80)
        tree.build(50)
        self.assertEqual(lca(tree.root, 7, 80).info, 45)

        #     45
        #   /    \
        #  10     80
        # /  \   /  \
        # 7   12 50 90
        #  balanced tree
        tree.build(90)
        self.assertEqual(lca(tree.root, 7, 90).info, 45)

        #Testing when the root is not the LCA, its on the right
        self.assertEqual(lca(tree.root, 50, 90).info, 80)

        #Testing when the root is not the LCA, its on the left
        self.assertEqual(lca(tree.root, 7, 12).info, 10)

        #Testing for the LCA, when one of the node is in left subtree and other on right subtree
        self.assertEqual(lca(tree.root, 7, 80).info, 45)

    def test_RightAlignedTree(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        tree=BST()
        tree.build(1)
        tree.build(2)
        tree.build(3)
        tree.build(4)
        self.assertEqual(lca(tree.root, 3, 4).info, 3)
    
    def test_DAG(self):
        root = DAGNode(1)
        node1 = DAGNode(2)
        node2 = DAGNode(3)
        node3 = DAGNode(4)
        node4 = DAGNode(5)
        node5 = DAGNode(6)
        root.suc = [node1, node2, node3, node4, node5]
        node1.suc = [node5]
        node1.pre = [root]
        node2.suc = [node3, node4]
        node2.pre = [root]
        node3.suc = [node4]
        node3.pre = [node1, node2, root]
        node4.pre = [node2, node3, root]
        node5.pre = [node4]


        self.assertEqual(dag_lca(root,root,node2).info,1)

    #testing an empty graph
    def test_DAG_empty(self):
        self.assertEqual(dag_lca(None,None,None),None)

    #testing types
    def test_DAG_type(self):
        root = DAGNode(1)
        node = DAGNode(2)

        self.assertEqual(dag_lca(root,"I",node),None)

    def test_DAG_type2(self):
        root = DAGNode(1)
        self.assertEqual(dag_lca("8",root,99),None)

    def test_DAG_same(self):
        root = DAGNode(1)
        node1 = DAGNode(2)
        node2 = DAGNode(3)
        node3 = DAGNode(4)
        node4 = DAGNode(5)
        node5 = DAGNode(6)
        root.suc = [node1, node2, node3, node4, node5]
        node1.suc = [node5]
        node1.pre = [root]
        node2.suc = [node3, node4]
        node2.pre = [root]


        self.assertEqual(dag_lca(root, node2, node2), 3)

    def test_new_DAG(self):
        root = DAGNode(0)
        node1 = DAGNode(1)
        node2 = DAGNode(2)
        node3 = DAGNode(3)
        node4 = DAGNode(4)
        node5 = DAGNode(5)
        root.suc = [node1,node5]
        node1.pre=[root]
        node1.suc=[node2]
        node2.pre = [node1]
        node2.suc=[node4,node3]
        node3.pre=[node1,node2]
        node3.suc=[root]
        node4.pre=[node1,node2]
        node5.pre=[root]

        self.assertEqual(dag_lca(root, node4, node3), 2)
        self.assertEqual(dag_lca(root, node5, node3), root)
        self.assertEqual(dag_lca(root, node2, node3), 1)
        self.assertEqual(dag_lca(root, node1, node2), 1)
















