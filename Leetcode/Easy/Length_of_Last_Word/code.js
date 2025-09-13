/**
 * @param {string} s
 * @return {number}
 */
function removeExtraSpaces(str) {
    return str.replace(/\s+/g, ' ').trim();
}


var lengthOfLastWord = function(s) {
    s = removeExtraSpaces(s);
    let i = s.length-1;
    let count = 0;
    while(i >= 0 && s[i] != " "){
        count++;
        i--;
    }
    return count;
};