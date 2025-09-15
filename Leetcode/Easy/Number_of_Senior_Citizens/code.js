/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let strNum = ""
    let count = 0;
    for(let i = 0; i < details.length; i++){
        strNum = "" + details[i][details[i].length-4] + details[i][details[i].length-3];
        if(Number(strNum) > 60) count++;
        strNum = "";
    }
    return count;
};