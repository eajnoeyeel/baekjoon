from math import sqrt

def solution(brown, yellow):
    a = 1
    b = -(2 + 0.5 * brown)
    c = yellow + brown

    width = ((-1 * b) + sqrt(abs(b ** 2 - 4 * a * c))) // 2 * a
    height = (brown + yellow) // width
    
    return [width, height]