class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> result(nums.size());
        int localCount;
        for(int i = 0; i<nums.size(); i++) {
            localCount = 0;
            for(int j = 0; j<nums.size(); j++) {
                if(i == j)
                    continue;
                if(nums[i] > nums[j])
                    ++localCount;
                result[i] = localCount;   
            }
        }
        return result;
    }
};