def minSteps(n: int) -> int:
    res = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            res += factor
            n //= factor
        factor += 1
    return res
