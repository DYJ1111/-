def nthUglyNumber(self, n: int) -> int:
    if n <= 0:
        return 0

    memo = [1] * n
    p1, p2, p3 = 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = memo[p1] * 2, memo[p2] * 3, memo[p3] * 5
        memo[i] = min(n2, n3, n5)

        while n2 == memo[i]:
            p1 += 1
        while n3 == memo[i]:
            p2 += 1
        while n5 == memo[i]:
            p3 += 1

    return memo[-1]