import math
from itertools import permutations

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    digits = []
    for number in numbers:
        digits.append(number)
    perms = permutations(digits)

    results = set()
    for perm in perms:
        result = 0
        for idx in range(len(perm)):
            results.add(int(perm[idx]))
            result += int(perm[idx]) * 10 ** idx
        results.add(result)
    
    for result in results:
        if is_prime(result):
            answer += 1

    return answer

