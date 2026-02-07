# Leetcode 202. Happy Number
class Solution:

    def squeres(self, n: int) -> int:
        result = 0
        pending = n
        while pending > 0:
            result += (pending % 10)**2
            pending = pending // 10
        return result

    def isHappy(self, n: int) -> bool:
        visited = set()
        number = n
        while True:
            if number == 1:
                return True
            elif number in visited:
                return False
            else:
                visited.add(number)
            number = self.squeres(number)


if __name__ == "__main__":
    s = Solution()
    assert s.isHappy(19) == True
    assert s.isHappy(2) == False