/* https://leetcode.com/problems/decode-xored-array/
faster than 95.41%, 20 ms
*/
class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        encoded.insert(encoded.begin(), first);
        for(auto it = encoded.begin() + 1; it < encoded.end(); it++) *it ^= *(it - 1);
        return encoded;
    }
};
