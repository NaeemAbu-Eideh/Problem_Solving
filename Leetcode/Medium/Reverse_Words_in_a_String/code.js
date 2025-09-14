/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {

    var arr = s.split(" ");
 
    s = "";

    for(i = arr.length-1; i >= 0; i--){
        s+= arr[i] += " ";
    }

    s = s.replace(/\s+/g, " ");

    return s.trim();
};