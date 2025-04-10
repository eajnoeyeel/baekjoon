import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer3 = int(numer1 * denom2 + numer2 * denom1)
    denom3 = int(denom1 * denom2)
    
    answer.append(numer3 / math.gcd(numer3, denom3))
    answer.append(denom3 / math.gcd(numer3, denom3))
    return answer