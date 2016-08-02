class Solution(object):
    def reverseWords(self, s):
        return ' '.join([w for w in s.split(' ') if w][::-1])
