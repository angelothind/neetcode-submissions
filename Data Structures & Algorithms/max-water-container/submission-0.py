class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatestVol = 0
        startPtr = 0
        endPtr = len(heights) - 1
        while startPtr < endPtr :
            width = endPtr - startPtr
            startHeight =  heights[startPtr]
            endHeight = heights[endPtr]
            if startHeight < endHeight :
                area = startHeight * width
                if area > greatestVol:
                    greatestVol = area
                startPtr += 1
            else:
                area = endHeight * width
                if area > greatestVol:
                    greatestVol = area
                endPtr -= 1
                
        return greatestVol     