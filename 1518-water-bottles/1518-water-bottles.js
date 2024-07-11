/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let max_bottle = numBottles;
    while(numBottles >= numExchange){
        max_bottle += Math.floor(numBottles/numExchange);
        numBottles = Math.floor(numBottles/numExchange) + numBottles%numExchange;
    }
    return max_bottle
    
};