/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    let freq = Math.floor(arr.length/4)
    for(let i =0; i<arr.length - freq ; i++){
        if(arr[i] == arr[i+freq]){
            return arr[i]
        }
    }
    
};