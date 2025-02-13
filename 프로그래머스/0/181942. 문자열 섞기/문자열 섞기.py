def solution(str1, str2):
    answer = ''
    for idx in range(len(str1)):
        answer += str1[idx]
        answer += str2[idx]
    return answer