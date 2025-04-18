import math


def solution(n):
    # lcm = a * b * gcd
    answer = (6 * n // math.gcd(n, 6)) // 6
    return answer