class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def words_count(word):
            k = dict()
            for cha in word:
                if cha not in k:
                    k[cha] = 0
                k[cha] += 1
            return k

        s1 = words_count(s)
        t1 = words_count(t)

        if len(s) != len(t):
            return False

        for key in s1:
            if key in t1 and s1[key] == t1[key]:
                pass
            else:
                return False
        return True
            

        
        