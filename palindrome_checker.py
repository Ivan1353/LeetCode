

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        if len(x) == 1:
            return True
        if x[:int(len(x)/2)] == list(reversed(x[-int(len(x)/2):])):
            return True
        else:
            return False

