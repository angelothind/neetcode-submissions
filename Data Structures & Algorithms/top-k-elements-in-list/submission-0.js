class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let numbFreqHash = new Map();
        for (let i = 0; i < nums.length; i++) {  // fix 1: .length not .size
            let currentNumber = nums[i];
            if (numbFreqHash.has(currentNumber)) {
                let currentFrequency = numbFreqHash.get(currentNumber);
                numbFreqHash.set(currentNumber, currentFrequency + 1);  // fix 2: .set(), not assigning to .get()
            }
            else {
                numbFreqHash.set(currentNumber, 1);
            }
        }

        let leaderBoard = new Map();
        let uniqueNumbers = Array.from(numbFreqHash.keys());  // fix 3: convert iterator to array

        for (let j = 0; j < k; j++) {
            leaderBoard.set(j, [uniqueNumbers[j], numbFreqHash.get(uniqueNumbers[j])]);
        }

for (let value = k; value < uniqueNumbers.length; value++) {
    let candidateFreq = numbFreqHash.get(uniqueNumbers[value]);

    // Step 1: find the current weakest leader on the board, period.
    let lowestReplaceIndex = 0;
    let lowestReplaceFreq = leaderBoard.get(0)[1];
    for (let currentLeader = 1; currentLeader < k; currentLeader++) {
        if (leaderBoard.get(currentLeader)[1] < lowestReplaceFreq) {
            lowestReplaceFreq = leaderBoard.get(currentLeader)[1];
            lowestReplaceIndex = currentLeader;
        }
    }

    // Step 2: only replace if the candidate actually beats the weakest leader.
    if (candidateFreq > lowestReplaceFreq) {
        leaderBoard.set(lowestReplaceIndex, [uniqueNumbers[value], candidateFreq]);
    }
}

        let answerArray = [];
        for (let j = 0; j < k; j++) {
            answerArray.push(leaderBoard.get(j)[0]);
        }

        return answerArray;  // fix 6: return the result
    }
}