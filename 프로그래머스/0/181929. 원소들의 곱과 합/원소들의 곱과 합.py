def solution(num_list):
    answer = 0
    sum = 0
    prod = 1
    for num in num_list:
        sum = sum + num
        prod = prod * num
    if prod < sum ** 2:
        return 1
    else:
        return 0
    return answer