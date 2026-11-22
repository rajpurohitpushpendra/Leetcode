class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";

        string hex = "";
        string digits = "0123456789abcdef";
        unsigned int n = num;

        while (n != 0) {
            hex = digits[n & 15] + hex;
            n >>= 4;
        }

        return hex;
    }
};