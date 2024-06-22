/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let vowels = "aeiouAEIOU"
    s = s.split("")
    let l = 0;
    let r = s.length -1;
    while (l < r){
        if(!vowels.includes(s[l])) l++
        else if (!vowels.includes(s[r])) r--;
        if (vowels.includes(s[l]) && vowels.includes(s[r])){
            [s[l] , s[r]] = [s[r], s[l]]
            l ++;
            r--;
        }
    }
    return s.join('')
    
};