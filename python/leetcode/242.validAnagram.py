class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        contagem = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in contagem:
                contagem[i] += 1
            else:
                contagem[i] = 1

        for i in t:
            if i in contagem:
                contagem[i] -= 1
                if contagem[i] < 0:
                    return False
            else:
                return False

        return True