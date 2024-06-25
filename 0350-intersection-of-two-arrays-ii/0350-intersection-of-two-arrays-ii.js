/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1,  nums2){
    nums1 = nums1.sort((a,b) => a -b)
    nums2 = nums2.sort((a,b) => a- b)
    let i= 0
    let j = 0
    let res = []
    while (i<nums1.length && j < nums2.length){
        if (nums1[i] < nums2[j]) i++
        else if (nums1[i] > nums2[j]) j++
        else {
            res.push(nums1[i])
            i++
            j++
        }
    }
    return res
}
var intersect1 = function(nums1, nums2) {
    let res = []
    for (let n of nums1){
        if (n in nums2){
            res.push(n)
            nums2= nums2.filter(function(item){
                                return item !== n
                                })
        }
    }
    return res
};