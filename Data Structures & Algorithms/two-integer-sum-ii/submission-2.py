class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = -1
        currentSum = numbers[leftPointer] + numbers[rightPointer]
        while(currentSum != target):
            if currentSum > target:
                rightPointer -= 1
            else:
                leftPointer += 1
            currentSum = numbers[leftPointer] + numbers[rightPointer]
            
        return [(leftPointer + 1), (len(numbers) + rightPointer + 1)]
        