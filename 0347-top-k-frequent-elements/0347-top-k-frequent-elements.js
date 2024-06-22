/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let mp ={}
    let freq = []
    let res = []
    for (let n of nums){
        if (n in mp){
            mp[n]+=1
        }else{
            mp[n] = 1
        }
    }

    const entries = Object.entries(mp);
    entries.sort((a,b) => b[1] - a[1]);
    for (let i =0; i<k; i++){
        res.push(entries[i][0])
    }
    return res
};