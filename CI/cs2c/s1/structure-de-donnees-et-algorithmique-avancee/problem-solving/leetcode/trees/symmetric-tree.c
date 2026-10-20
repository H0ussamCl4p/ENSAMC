// By CHOUBIK Houssam - Time complexity O(n)

bool isSymmetric(struct TreeNode* root) {
    if(root==NULL) return true;
    bool check(struct TreeNode* t1, struct TreeNode* t2) {
        if (t1 == NULL && t2 == NULL) return true;
        if (t1 == NULL || t2 == NULL) return false;
        if (t1->val != t2->val) return false;
        return check(t1->left, t2->right) && check(t1->right, t2->left);
    }
    return check(root->left, root->right);
}
