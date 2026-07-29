class Solution(object):
    def lengthOfLastWord(self, s):
        txt = s.split()
        return len(txt[-1])