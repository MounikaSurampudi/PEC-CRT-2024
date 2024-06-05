class Solution:
    def __init__(self):
        self.memo = {}
    
    def wordBreak(self, s, wordDict, idx=0):
        if idx in self.memo:
            return self.memo[idx]
        
        if idx==len(s):
            return True
        
        for word in wordDict:
            if s.startswith(word,idx):
                if self.wordBreak(s,wordDict, idx+len(word)):
                    return True
        
        self.memo[idx]=False
        return False
