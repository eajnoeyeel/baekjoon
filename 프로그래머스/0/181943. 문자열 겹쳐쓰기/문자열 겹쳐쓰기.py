def solution(my_string, overwrite_string, s):
    answer = ''
    
    for idx in range(len(my_string)):
        if s <= idx and idx <= (len(overwrite_string) + s - 1):
            answer += overwrite_string[idx - s]
        else:
            answer += my_string[idx]
            
    return answer