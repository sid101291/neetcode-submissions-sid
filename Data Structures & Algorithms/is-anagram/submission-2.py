class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_map_s = {}
        count_map_t = {}

        self.count_occurences(s,count_map_s)
        self.count_occurences(t,count_map_t)

        if count_map_s == count_map_t:
            return True
        else:
            return False

    def count_occurences(self,ana_string,count_map):
        
        for char in ana_string:
            if char in count_map:
                current_count = count_map[char]
                current_count = current_count + 1
                count_map[char] = current_count
            else:
                count_map[char] = 1
    

        