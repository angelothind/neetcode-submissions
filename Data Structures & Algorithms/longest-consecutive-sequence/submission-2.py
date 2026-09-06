class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Sort List to allow to identify beginnings and endings of sequences
        nums.sort()
        longestSequence = 0
        currentSequence = 0
        for i in range(len(nums)):
            if(i == 0):
                previousNumber = nums[i]
                longestSequence = 1
                currentSequence += 1
            else:
                currentNumber = nums[i]
                if(currentNumber == (previousNumber + 1)):
                    currentSequence += 1
                    if(currentSequence > longestSequence):
                        longestSequence = currentSequence
                    previousNumber = currentNumber
                elif(currentNumber == previousNumber):
                    previousNumber = currentNumber
                else:
                    currentSequence = 1
                    previousNumber = currentNumber
        return longestSequence
                    

                

            


        