class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedList = sorted(nums)
        outputArray = []

        for i in range(len(sortedList) - 2):
            # Skip duplicates for the fixed number
            if i > 0 and sortedList[i] == sortedList[i - 1]:
                continue
                
            startPointer = i + 1
            endPointer = len(sortedList) - 1

            while startPointer < endPointer:
                total = sortedList[i] + sortedList[startPointer] + sortedList[endPointer]

                if total > 0:
                    endPointer -= 1
                elif total < 0:
                    startPointer += 1
                else:
                    outputArray.append([sortedList[i], sortedList[startPointer], sortedList[endPointer]])
                    
                    startPointer += 1
                    endPointer -= 1
                    
                    # Skip duplicate start/end elements
                    while startPointer < endPointer and sortedList[startPointer] == sortedList[startPointer - 1]:
                        startPointer += 1
                    while startPointer < endPointer and sortedList[endPointer] == sortedList[endPointer + 1]:
                        endPointer -= 1
        
        return outputArray