/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode InsertIntoBST(TreeNode root, int val) {
        TreeNode newNode = new TreeNode(val);
        if(root == null){
            root = newNode;
            return root;
        }
        if(val > root.val){
            if(root.right == null){
                root.right = newNode;
                return root;
            }
            InsertIntoBST(root.right, val);
        }
        else{
            if(root.left == null){
                root.left = newNode;
                return root;
            }
            InsertIntoBST(root.left, val);
        }
        return root;
    }
}