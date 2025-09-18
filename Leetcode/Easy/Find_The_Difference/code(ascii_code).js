/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let sumS = 0, sumT = 0;
    let i = 0;
    for(; i < s.length; i++){
        sumS += s.charCodeAt(i);
        sumT += t.charCodeAt(i);
    }
    sumT += t.charCodeAt(s.length);
    return String.fromCharCode(sumT - sumS);
};