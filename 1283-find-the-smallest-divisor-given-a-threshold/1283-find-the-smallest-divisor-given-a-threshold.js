/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
    let l = 1
    let r = Math.max(...nums)
    
    while (l<=r){
        let mid = Math.floor((l+r)/2);
        let sum1 = 0
        for (let n of nums){
            sum1 += Math.ceil(n/mid);
        }
        if (sum1 > threshold){
            l =  mid + 1
        }else{
            r = mid -1
        }
        
    }
    return l
};