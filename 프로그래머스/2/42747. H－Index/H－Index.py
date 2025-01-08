def solution(citations):
    answer = len(citations)

    # Rank the publications in descending order by the number of times they have been cited
    citations.sort(reverse=True)

    # Initialize a variable to keep track of the number of publications
    # h번 이상 인용된 논문의 수를 count로 세어줌
    count = len(citations)
    
    # Loop through to find the entry where the rank is greater than the number of citations
    for h in range(len(citations)):
        if citations[h] <= h:
            answer = h
            break
        count -= 1
    return answer