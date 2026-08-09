from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = sum(nums[0:k])/k
        for i in range(0,len(nums)-k+1):
            j = i+k
            current_avg = 0
            for n in range(i,j):
                current_avg += nums[n]
            max_avg = max(max_avg, (current_avg/k))
        return max_avg

obj = Solution()
print(obj.findMaxAverage(nums =[1,12,-5,-6,50,3], k = 4))