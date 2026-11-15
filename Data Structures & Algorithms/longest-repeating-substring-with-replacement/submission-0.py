class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        longest = 0
        left  = 0

        #walk through the string

        for right in range(len(s)):

            #put the first char in map with count
            count[s[right]] = count.get(s[right],0) + 1

            # check if box is valid
            #formula : size of box - most pop character count = imposters

            while(right - left + 1 ) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            #box is valid , update the record if this is the biggest

            longest  = max(right - left + 1,longest)

        return longest


            

        