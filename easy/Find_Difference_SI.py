class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t 

    
    def find_difference(self):
        if len(self.s) == len(self.t) :
            return False
        
        if len(self.s)+1 == len(self.t):
            return self.t[-1]



s = Solution('abcd','abcde')
print(s.find_difference())