class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        longest_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_sum = 1
                current_num = num

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_sum += 1
                
                longest_seq  = max(longest_seq,current_sum)
        return longest_seq
        