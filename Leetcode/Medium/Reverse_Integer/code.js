/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    str = "";
    newStr = "";
    str += x;
    for (i = str.length - 1; i >= 0; i--) {
        if(str[i] !== '-'){
            newStr += str[i];
        }
    }
    if(x < 0){newStr = "-" + newStr;}
    if(Number(newStr) > 2147483647 || Number(newStr) < -2147483648){return 0;}
    return Number(newStr);
};