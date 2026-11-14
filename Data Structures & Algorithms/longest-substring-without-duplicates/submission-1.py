class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        current_window = 0
        max_window = 0

        char_set = set()

        for i in range(0, len(s)):
            if s[i] not in char_set:
                char_set.add(s[i])
                current_window += 1

            else:
                while s[i] in char_set:
                    char_set.remove(s[left])
                    current_window -= 1
                    left += 1
                
                char_set.add(s[i])
                current_window += 1
            
            max_window = max(current_window,max_window)
        
        return max_window


    
        