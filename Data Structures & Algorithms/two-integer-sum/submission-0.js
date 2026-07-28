class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashmap = {};
        let i;
        let j;
        for(let currentNum = 0; currentNum < nums.length; currentNum++){
            // visit element
            let difference = target - nums[currentNum];
            if (hashmap[difference] === undefined){
                hashmap[nums[currentNum]] = currentNum;   
            }
            else {
                return [hashmap[difference], currentNum];  
            }
    }
}

}
