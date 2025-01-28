import math
from itertools import *

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
    combs = []
    for number in numbers:
        digits.append(int(number))
    
    for i in range(len(digits)):
        combs.extend(combinations(digits, i + 1))

    perms = set()
    for comb in combs:
        perms.update(permutations(comb))

    results = set()
    for perm in perms:
        result = 0
        for idx in range(len(perm)):
            results.add(perm[idx])
            result += perm[idx] * 10 ** idx
        results.add(result)
    print(results)
    
    for result in results:
        if is_prime(result):
            answer += 1

    return answer
