class Solution {
public:
    bool isValid(string s) {
        int check = 0;
        stack<char> S;
        for(int i=0;i< s.length();i++){
            if (s[i] != '}' && s[i] != ']' && s[i] != ')') { S.push(s[i]); }
            else {
                if (S.empty()) check = 1;
                else {
                    if (s[i] == ')') {
                        while (!S.empty() && S.top() != '(' && S.top() != '{' && S.top() != '[') {
                            S.pop();
                        }
                        if (S.empty()) check = 1;
                        if (S.top() != '(') check = 1;
                        else {
                            S.pop();
                        }
                    }
                    else if (s[i] == '}') {
                        while (!S.empty() && S.top() != '(' && S.top() != '{' && S.top() != '[') {
                            S.pop();
                        }
                        if (S.empty()) check = 1;
                        if (S.top() != '{') check = 1;
                        else {
                            S.pop();
                        }
                    }
                    else {
                        while (!S.empty() && S.top() != '(' && S.top() != '{' && S.top() != '[') {
                            S.pop();
                        }
                        if (S.empty()) check = 1;
                        if (S.top() != '[') check = 1;
                        else {
                            S.pop();
                        }
                    }
                
                }
            }
        }
        if (!S.empty()) return false;
        if (check == 0) return true;
        else return false;
    }
};