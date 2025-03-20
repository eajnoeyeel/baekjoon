def solution(code):
    answer = []
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                answer.append(code[idx])
            if code[idx] == "1":
                mode = 1
        else:
            if code[idx] != "1" and idx % 2 == 1:
                answer.append(code[idx])
            if code[idx] == "1":
                mode = 0
    if not answer:
        return "EMPTY"
    return ''.join(answer)