class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 贪心
        # time： O(n), space: O(1)
        if not bills:
            return True
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True