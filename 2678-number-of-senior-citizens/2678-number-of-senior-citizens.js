/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let count = 0
    for (let age of details ){
        if (age.substring(11,13) > 60){
            count +=1
        }
    }
    return count
};