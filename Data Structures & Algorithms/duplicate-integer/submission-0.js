class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hashmap = {};
        for(let i = 0; i < nums.length; i++){
            if(hashmap[nums[i]] != undefined){
                return true;
            }
            else {
                hashmap[nums[i]] = true;
            }
        }
        return false;
    }
}
