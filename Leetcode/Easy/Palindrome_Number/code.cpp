class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int sum = 0;
        vector<int> X;
        while (x != 0) {
            int y = x % 10;
            X.push_back(y);
            x /= 10;
        }
        vector<int> Y;
        for (int i =  X.size() - 1; i >= 0; i--) {
            Y.push_back(X[i]);
        }
        for (int i = 0; i < X.size(); i++) {
            if (X[i] != Y[i]) sum++;
        }
        if (sum > 0) { return false; }
        else { return true; }
    }
};