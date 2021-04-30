class Solution {
public:
    string defangIPaddr(string address) {
        string da = "";
        for (int i = 0; i<address.size(); i++) {
            char x = address[i];
            if (x == '.') {
                da.push_back('[');
                da.push_back('.');
                da.push_back(']');
            }
            else {
                da.push_back(x);
            }
        }
        return da;
    }
};