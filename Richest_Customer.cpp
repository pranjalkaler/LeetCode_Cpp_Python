class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max = 0;
        int rowMax = 0;
        for(int i = 0; i<accounts.size(); i++) {
            rowMax = 0;
            for(int j = 0; j<accounts[0].size(); j++) {
                rowMax += accounts[i][j];
            }
            if (rowMax > max)
                max = rowMax;
        }
        return max;
    }
};