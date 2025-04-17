import statistics


def solution(array):
    answer = statistics.multimode(array)
    if len(answer) == 1:
        return int(answer[0])
    return -1