/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    let total = 10
    let curr = 9
    let start = 9
    if (n === 0) return 1
    while(n > 1 && curr > 0){
        curr *= start
        total += curr
        start -=1
        n --
    }
    return total
    
};