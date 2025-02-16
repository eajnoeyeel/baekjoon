def solution(number, k):
    stack = []
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 남은 k만큼 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)