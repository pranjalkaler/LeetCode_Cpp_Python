class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int j = n;
        vector<int> result(n*2);
        for(int i = 0; i<2*n; i+=2)
        {
            result[i] = nums[i/2];
            result[i+1] = nums[j++];
        }        
        return result;
    }
};