class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore

        listaindice = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    listaindice.append(i)
                    listaindice.append(j)

                    return listaindice
            
