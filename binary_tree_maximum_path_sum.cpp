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
    int getSum(TreeNode* node, int& result) {
        if (node == nullptr)
            return 0;
        // std :: cout << node->val << " " << result << std :: endl;
        int leftSum = getSum(node->left, result);
        int rightSum = getSum(node->right, result);
        int temp = node->val + std :: max(0, std :: max(leftSum, rightSum));
        int temp2 = std :: max(temp, leftSum + rightSum + node->val);
        result = std :: max(result, temp2);
        return temp;
    }
    int maxPathSum(TreeNode* root) {
        int result = INT_MIN;
        getSum(root, result);
        return result;
    }
};
