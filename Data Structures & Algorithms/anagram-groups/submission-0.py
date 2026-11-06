class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            #check if the sorted word exists in map
            if sorted_word in anagram_dict:
                #put the value appended
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        return list(anagram_dict.values())

        