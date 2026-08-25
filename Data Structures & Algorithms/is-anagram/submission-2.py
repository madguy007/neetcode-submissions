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

        s_length = len(s)
        t_length = len(t)

        if s_length >= t_length:
            m = s1
            n = t1
        else:
            m = t1
            n = s1

        for key in m:
            if key in n and s1[key] == t1[key]:
                pass
            else:
                return False
        return True
            

        
        