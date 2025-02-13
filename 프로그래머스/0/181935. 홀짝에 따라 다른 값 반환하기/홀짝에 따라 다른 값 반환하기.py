def solution(n):
    result = 0
    if n % 2 == 1:
        for i in range(1, n + 1):
            if i % 2 == 1:
                result += i
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                result += i ** 2
    return result