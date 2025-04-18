import math


def solution(n):
    answer = 6 * n // math.gcd(n, 6) // 6
    return answer