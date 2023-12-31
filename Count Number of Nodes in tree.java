Count Number of Nodes in tree
You are given the root node of a binary tree.Count the number of nodes present.

Input Format
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or 
right node data exist for root, it will not be a part of the node data.

Constraints
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Output Format
The only line of output prints the number of nodes in Binary Tree

Sample Input 0
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 0
7

Sample Input 1
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1

Sample Output 1
6

Python Code:
    
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
class TreeNode {
    int value;
    TreeNode left, right;
    public TreeNode(int value) {
        this.value = value;
        this.left = this.right = null;
    }
}
public class BinaryTree {
    public static int countNodes(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
    public static TreeNode buildTree(int[] nodes) {
        if (nodes == null || nodes.length == 0)
            return null;
        TreeNode root = new TreeNode(nodes[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int i = 1;
        while (!queue.isEmpty() && i < nodes.length) {
            TreeNode current = queue.poll();
            if (nodes[i] != -1) {
                current.left = new TreeNode(nodes[i]);
                queue.add(current.left);
            }
            i++;
            if (i < nodes.length && nodes[i] != -1) {
                current.right = new TreeNode(nodes[i]);
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int[] nodes = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            nodes[i] = Integer.parseInt(input[i]);
        }
        TreeNode root = buildTree(nodes);
        int result = countNodes(root);
        System.out.println(result);
    }
}
