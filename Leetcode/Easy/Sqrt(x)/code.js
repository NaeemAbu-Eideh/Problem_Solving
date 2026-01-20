/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if(x < 2)return x;

    ans = 0;
    left = 0;
    right = Math.floor(x / 2);
    while(left <= right){
        mid = Math.floor((left + right) / 2);
        if((x / mid) >= mid){
            ans = mid;
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return ans;
};