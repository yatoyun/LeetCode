#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = set()
        
        for i in range(ord("a"),ord("z")+1):
            alphabet_set.add(chr(i))
        
        return set(list(sentence)) == alphabet_set
# @lc code=end

