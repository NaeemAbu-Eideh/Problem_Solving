// User function Template for javascript

/**
 * @param {string}s
 * @returns {string}
 */

class Solution {
    modify(s) {
        var newStr = "";
        for(let i = 0; i < s.length; i++){
            if(s[i]!= ' '){
                newStr += s[i];
            }
        }
        return newStr;
    }
}
