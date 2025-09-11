/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let i = 0;
    let j = (s.length)-1
    for(; i < s.length && j >= 0 && (i != j && i != j+1); j--,i++){
        let swap = s[i] ;
        s[i] = s[j];
        s[j] = swap;
    }
    return s;
};