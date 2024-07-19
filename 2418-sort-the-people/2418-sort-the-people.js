/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let a1 = []
    for (let i = 0; i<names.length; i++){
        a1.push([heights[i], names[i]])
    }
    a1.sort((a,b) => b[0] -a[0])
    b = []
    for( i = 0; i<a1.length; i++){
        b.push(a1[i][1])
    }
    return b
    
    
};