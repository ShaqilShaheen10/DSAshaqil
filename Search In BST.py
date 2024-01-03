Search In BST
Given a BST and an integer k. Find if the integer k is present in given BST or not. You have to return true, if node with data k is present, return false otherwise.
Note: Assume that BST contains all unique elements.

Input Format
First Line array size
Second line array elements
Third line target value

Constraints
Time:- 1 Sec

Output Format
The first and only line of output contains a boolean value. Print true, if node with data k is present, print false otherwise.

Sample Input 0
6
8 5 10 2 6 7
2

Sample Output 0
true

Sample Input 1
6
8 5 10 2 6 7
12

Sample Output 1
false

Python Code:

import java.util.Scanner;
class TreeNode {
    int key;
    TreeNode left, right;
    public TreeNode(int item) {
        key = item;
        left = right = null;
    }
}
class BST {
    private TreeNode root;
    public void insert(int key) {
        root = insertRec(root, key);
    }
    private TreeNode insertRec(TreeNode root, int key) {
        if (root == null) {
            return new TreeNode(key);
        }
        if (key < root.key) {
            root.left = insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }
        return root;
    }
    public boolean search(int key) {
        return searchRec(root, key);
    }
    private boolean searchRec(TreeNode root, int key) {
        if (root == null) {
            return false;
        }
        if (key == root.key) {
            return true;
        } else if (key < root.key) {
            return searchRec(root.left, key);
        } else {
            return searchRec(root.right, key);
        }
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        BST bst = new BST();
        for (int i = 0; i < size; i++) {
            bst.insert(scanner.nextInt());
        }
        int target = scanner.nextInt();
        boolean result = bst.search(target);
        System.out.println(result);
    }
}
