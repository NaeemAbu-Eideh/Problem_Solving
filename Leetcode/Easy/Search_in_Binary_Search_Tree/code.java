/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null){
            return null;
        }
        if(root.val == val){
            System.out.println("node found");
            System.out.println("inside find " + root);
            return root;
        }
        if(val > root.val){
            System.out.println("go Right");
            return searchBST(root.right, val);
        }
        else{
            System.out.println("go Left");
             return searchBST(root.left, val);
        }
    }
}