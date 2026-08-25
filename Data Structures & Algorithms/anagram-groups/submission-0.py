class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in word_dict:
                word_dict[s_word] = []
            word_dict[s_word].append(word)
        return list(word_dict.values())