class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoDec_stack = []
        monoDec_stack.append([temperatures[0], 0])
        results = [0]
        topPtr = 0
        for currentIndex in range(1, len(temperatures)):
            #Checking the top of the stack
            topStack = monoDec_stack[topPtr]
            currentPair = [temperatures[currentIndex], currentIndex]
            results.append(0)
            if topStack[0] < currentPair[0]:
                #Handle if Larger than
                while topStack[0] < currentPair[0]:
                    indexDiff = currentPair[1] - topStack[1]
                    results[topStack[1]] = indexDiff
                    monoDec_stack.pop(-1)
                    topPtr -= 1
                    if topPtr < 0:
                        break
                    topStack = monoDec_stack[topPtr]
                monoDec_stack.append(currentPair)
                topPtr += 1
            else:
                monoDec_stack.append(currentPair)
                topPtr += 1
        return results


        