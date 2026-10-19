void inorder(struct TreeNode* root, int* res, int* returnSize) {
    if (root == NULL) return;

    inorder(root->left, res, returnSize);   // visit left
    res[*returnSize] = root->val;          // visit root
    (*returnSize)++;                        // move index
    inorder(root->right, res, returnSize); // visit right
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* res = (int*)malloc(1000 * sizeof(int)); // allocate memory
    *returnSize = 0;
    inorder(root, res, returnSize);
    return res;
}
