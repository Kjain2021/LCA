import static org.junit.Assert.*;

import org.junit.Test;

public class lcaTest {

    @Test
    public void testEmptyTree() {
        lca bst1 = new lca();
        // Empty tree, so the LCA doesn't exist and LCA doesn't exist as root is null
        assertEquals("The LCA is null as root is null(empty tree)", null, lca.lcaSol(bst1.root, 4, 5));
    }

    @Test
    public void testLCA() {

        //     45
        //  /     \
        // 10    80
        // /\    /
        //7 12 50
        // Testing when the root is the LCA, incomplete tree, and
        lca bst = new lca();
        bst.insert(45);
        bst.insert(10);
        bst.insert(7);
        bst.insert(12);
        bst.insert(80);
        bst.insert(50);
        assertEquals("The lowest common ancestor of 7 and 80 is:", 45, (lca.lcaSol(bst.root, 7, 80).data));

        // Testing when the tree is complete, LCA is root
        //  45
        //  / \
        // 10 80
        // /\ / \
        //7 12 50 90
        bst.insert(90);
        assertEquals("The lowest common ancestor of 7 and 90 is:", 45, (lca.lcaSol(bst.root, 7, 90).data));

        // Testing when the root is not the LCA, its on the right
        assertEquals("The lowest common ancestor of 50 and 90 is:", 80, (lca.lcaSol(bst.root, 50, 90).data));

        // Testing when the root is not the LCA, its on the left
        assertEquals("The lowest common ancestor of 7 and 12 is:", 10, (lca.lcaSol(bst.root, 7, 12).data));

        // Testing for the LCA, when one of the node is in left subtree and other on
        // right subtree
        assertEquals("The lowest common ancestor of 7 and 80 is:", 45, (lca.lcaSol(bst.root, 7, 80).data));

    }

    @Test
    public void TestOneChild() {
        // Testing when have one child
        // 1
        //  \
        //   2
        //    \
        //     3
        //      \
        //       4
        lca bst2 = new lca();
        bst2.insert(1);
        bst2.insert(2);
        bst2.insert(3);
        bst2.insert(4);
        assertEquals("The lowest common ancestor of 3 and 4 is:", 3, (lca.lcaSol(bst2.root, 3, 4).data));

        //  2
        // / \
        // 1  3
        //    \
        //     4

        lca bst3 = new lca();
        bst3.insert(2);
        bst3.insert(1);
        bst3.insert(3);
        bst3.insert(4);
        assertEquals("The lowest common ancestor of 1 and 3 is:", 2, (lca.lcaSol(bst3.root, 1, 3).data));

    }

}
