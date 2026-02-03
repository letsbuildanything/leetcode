# two sum problem

# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        list_len = len(nums)

        for i in range(list_len-1):
            for j in range(i+1, list_len):
                if(( nums[i]+nums[j]) == target):
                    result.append(i)
                    result.append(j)
                    return result
        