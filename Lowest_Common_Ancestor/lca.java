//import java.util.Scanner;

class lca {
    class Node {
        Node left;
        Node right;
        int data;

        Node(int data) {
            this.data = data;
            left = null;
            right = null;
        }
    }

    Node root;

    // intialise root
    lca() {
        root = null;
    }

    void insert(int data) {
        root = insert_RecursiveNode(root, data);
    }

    Node insert_RecursiveNode(Node root, int data) {
        // tree empty
        if (root == null) {
            root = new Node(data);
            return root;
            // traverse tree
        } else {
            Node temp;
            if (data <= root.data) {
                temp = insert_RecursiveNode(root.left, data);
                root.left = temp;
            } else {
                temp = insert_RecursiveNode(root.right, data);
                root.right = temp;
            }
            return root;
        }
    }

    public static Node lcaSol(Node root, int search1, int search2) {
        if (root == null) {
            return null;
        } else if (root.data == search1 || root.data == search2) {
            return root;
        }
        // lca is on left subtree
        else if (root.data > search1 && root.data > search2) {
            return lcaSol(root.left, search1, search2);
        }
        // lca is on right
        else if (root.data < search1 && root.data < search2) {
            return lcaSol(root.right, search1, search2);
        }
        return root;
    }

    // as per the constrains no value shall be repeated in the tree and nodes need
    // to be unique.
    // public static void main(String[] args) {
    // was done using user input where tree wasn't intialised.
    // Scanner input = new Scanner(System.in);
    // System.out.print("Please enter number of nodes first, then followed by
    // values.");
    // int numNodes = input.nextInt();
    // Node root = null;
    // while (numNodes-- > 0) {
    // int value = input.nextInt();
    // root = insert(root, value);
    // // System.out.print(root.data);
    // }
    // System.out.print("Enter the two value for which you want to find LCA:");
    // int search1 = input.nextInt();
    // int search2 = input.nextInt();
    // input.close();
    // Node lca = lca(root, search1, search2);
    // System.out.print(lca.data);

    // intialise tree
    // lca bst = new lca();
    // System.out.print("Got intialised");
    // bst.insert(45);
    // bst.insert(10);
    // bst.insert(7);
    // bst.insert(12);
    // bst.insert(90);
    // bst.insert(50);
    // Node resultNode = lcaSol(bst.root, 7, 90);
    // System.out.print(resultNode.data);
    // }
}
