from math import sqrt

def solution(brown, yellow):
    answer = []

    a = 1
    b = -1 * (2 + 0.5 * brown)
    c = yellow + brown

    width = int(((-1 * b) + sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    height = (brown + yellow) // width

    answer.append(width)
    answer.append(height)

    return answer