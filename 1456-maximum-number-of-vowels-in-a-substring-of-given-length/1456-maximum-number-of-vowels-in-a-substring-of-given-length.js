/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let count = 0
    let vowel = new Set()
    vowel.add('a')
    vowel.add('e')
    vowel.add('i')
    vowel.add('o')
    vowel.add('u')
    
    for (let i = 0; i<k; i++){
        if (vowel.has(s[i])) count +=1
        
    }
    
    let max_count = count
    for (let i= 0; i<s.length - k; i++){
        if(vowel.has(s[i]) ){
            count -=1 
            }
        if (vowel.has(s[i+k]) ){
            count +=1
            }
        console.log(count)
        max_count = Math.max(max_count , count)
    }
    return max_count
    
};