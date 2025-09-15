/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){return false;}
    else{
        let strNum = x.toString();
        let revNum = "";
        for(i = strNum.length-1; i >= 0; i--){
            revNum += strNum[i];
        }
        if(strNum === revNum){
            return true;
        }
        else{
            return false;
        }
    }
};