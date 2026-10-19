/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i,j;
    int *arr=(int*)malloc(2*sizeof(int));

    if(arr==NULL || nums==NULL || numsSize<2){
        *returnSize=0;
        return NULL;
    }

    for(i=0;i<numsSize;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                *returnSize=2;
                arr[0]=i;
                arr[1]=j;
                return arr;
            }
        }
    }

    *returnSize=0;
    free(arr);
    return NULL;
}
