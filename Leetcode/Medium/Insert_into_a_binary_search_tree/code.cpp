/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* newNode = new TreeNode(val);
        if(root == NULL){
            root = newNode;
            return root;
        }
        if(val > root->val){
            if(root->right == NULL){
                root->right = newNode;
                return root;
            }
            insertIntoBST(root->right, val);
        }
        else{
            if(root->left == NULL){
                root->left = newNode;
                return root;
            }
            insertIntoBST(root->left, val);
        }
        return root;
    }
};