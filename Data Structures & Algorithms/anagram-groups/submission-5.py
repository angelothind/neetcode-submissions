class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createKey(word: str):
            list_key = [0] * 26
            converted_word = list(word.encode('ascii'))
            for letter in converted_word:
                index = letter - 97
                list_key[index] = list_key[index] + 1
            
            string_key = "".join((str(count) + " ") for count in list_key)
            return string_key
        
        anagram_group = {}
        for word in strs:
            key = createKey(word)
            if anagram_group.get(key) == None:
                anagram_group[key] = [word]
            else:
                anagram_group[key].append(word)

        anagram_groups = [group for grouping, group in anagram_group.items()]
        return anagram_groups
        

                

        