class Solution:
    def reverse(self, x: int) -> int:
        x= str(x)
        if x[0] == "-":
            x = x[1:]
            return -int("".join(list(reversed(x))))
        else:
            return int("".join(list(reversed(x))))

