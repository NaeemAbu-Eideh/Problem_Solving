class Solution {
public:
    int getNum(char chr) {
        switch (chr)
        {

        case 'I': return 1;
        case 'i': return 1;
        case 'v': return 5;
        case 'V': return 5;
        case 'x': return 10;
        case 'X': return 10;
        case 'l': return 50;
        case 'L': return 50;
        case 'c': return 100;
        case 'C': return 100;
        case 'd': return 500;
        case 'D': return 500;
        case 'm': return 1000;
        case 'M': return 1000;
        default: return 0;

        }
    }
    int romanToInt(string s) {
        int sum = 0;
        for (int i = 0; i < s.length();) {
            if (i < s.length() - 1 && getNum(s[i]) >= getNum(s[i+1])) {
                sum += getNum(s[i]);
                i++;
            }
            else if (i != s.length() - 1 && getNum(s[i]) < getNum(s[i+1])) {
                sum += (getNum(s[i + 1]) - getNum(s[i]));
                i+=2;
            }
            else {
                sum += getNum(s[i]);
                i++;
            }
        }
        return sum;
    }
};