class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let lettersHashmap = {};
        if (s.length != t.length){
            return false;
        }
        else{
            for(let letter = 0; letter < s.length; letter++){
                if(lettersHashmap[s[letter]] === undefined){
                    lettersHashmap[s[letter]] = 1;
                }
                else{
                    lettersHashmap[s[letter]]++
                }
            }
        }

        for(let letter = 0; letter < t.length; letter++){
            if(lettersHashmap[t[letter]] != undefined){
                lettersHashmap[t[letter]]--;
                if(lettersHashmap[t[letter]] < 0){
                    return false;
                }
            }
            else{
                return false;
            }
        }
    return true;
    }
}
