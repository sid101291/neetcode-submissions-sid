class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        three_sum_list = []

        for i in range(0, len(nums) -  2):
            #skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # for each anchor check for 3 sum using left and right pointers 
            left = i + 1
            right = len(nums) - 1

            while left < right :

                total  = nums[i] + nums[left] + nums[right]

                if total  == 0:
                    three_sum_list.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    #skip left duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total > 0:
                    right -= 1

                else:
                    left += 1
        return three_sum_list
            

                


