def solution(nums):
    answer = len(nums) / 2
    
    # Hash table to store the frequency of each number
    freq = [0] * 200000
    for num in nums:
        freq[num - 1] += 1
    
    count = 0
    for elem in freq:
        if (elem != 0):
            count += 1
            
    if (count < len(nums) / 2):
        answer = count
        
    return answer