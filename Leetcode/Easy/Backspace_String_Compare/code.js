/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let result1 = "", result2 = "";
    for(let char of s){
        if(char != "#") result1 += char;
        else result1 = result1.slice(0, -1);
    }

    for(let char of t){
        if(char != "#") result2 += char;
        else result2 = result2.slice(0, -1);
    }

    if(result1 === result2) return true;
    else return false;
};