class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ele_freq = {}

        for num in nums:
            count = ele_freq.get(num,0) + 1
            ele_freq[num] = count
        
        sorted_elements = sorted(ele_freq,key=ele_freq.get,reverse=True)

        return sorted_elements[:k]


        