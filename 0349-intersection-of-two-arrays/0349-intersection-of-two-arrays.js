/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let res = []
    let seen = new Set(nums1)
    for( let n of nums2){
        if(seen.has(n)){
            res.push(n)
            seen.delete(n)
        }
    }
    
    return res
};