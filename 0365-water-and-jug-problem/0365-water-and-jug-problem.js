/**
 * @param {number} x
 * @param {number} y
 * @param {number} target
 * @return {boolean}
 */
var canMeasureWater = function(x, y, target) {
    let seen = new Set()
    function dfs(total){
        if (total === target) return true
        if (seen.has(total) || x + y <total || total < 0) return false
        seen.add(total)
        return dfs(total + x) || dfs(total + y) || dfs(total - x) || dfs(total - y)
    }
    return dfs(0)
    
};