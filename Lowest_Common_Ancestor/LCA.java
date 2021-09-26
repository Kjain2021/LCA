import java.util.Scanner;

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

class lca {

    public static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node temp;
            if (data <= root.data) {
                temp = insert(root.left, data);
                root.left = temp;
            } else {
                temp = insert(root.right, data);
                root.right = temp;
            }
            return root;
        }
    }

    public static Node lca(Node root, int search1, int search2) {
        if (root == null) {
            return null;
        } else if (root.data == search1 || root.data == search2) {
            return root;
        }
        // lca is on left subtree
        else if (root.data > search1 && root.data > search2) {
            return lca(root.left, search1, search2);
        }
        // lca is on right
        else if (root.data < search1 && root.data < search2) {
            return lca(root.right, search1, search2);
        }
        return root;
    }

    // as per the constrains no value shall be repeated in the tree and nodes need
    // to be unique.
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter number of nodes first, then followed by values.");
        int numNodes = input.nextInt();
        Node root = null;
        while (numNodes-- > 0) {
            int value = input.nextInt();
            root = insert(root, value);
            // System.out.print(root.data);
        }
        System.out.print("Enter the two value for which you want to find LCA:");
        int search1 = input.nextInt();
        int search2 = input.nextInt();
        input.close();
        Node lca = lca(root, search1, search2);
        System.out.print(lca.data);
    }
}