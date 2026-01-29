import sys
input = sys.stdin.readline

def main():
    N, T = map(int, input().split())

    # 1 ≤ T ≤ 1000
    timeline = a = [0] * 1200

    # 1. 입력 받으면서 깃발 꽂기 (차분 배열)
    for _ in range(N):
        # 각 사람이 가능한 시간대의 개수
        k = int(input())
        for _ in range(k):
            s, e = map(int, input().split())
            # 전부 채우는 대신
            timeline[s] += 1
            timeline[e] -= 1
    
    # 2. 꽂은 깃발을 바탕으로 실제 인원수 채우기
    for i in range(len(timeline)):
        timeline[i] += timeline[i - 1]

    # 3. T시간만큼 슬라이딩 윈도우로 최대 구간 찾기
    max_sum = 0
    curr_sum = 0
    start_time = 0

    # (1) 0부터 T시간까지의 합 구하기
    for i in range(T):
        curr_sum += timeline[i]
    max_sum = curr_sum

    # (2) 한 칸씩 밀면서 확인
    for i in range(1200 - T):
        # 윈도우 이동: 맨 앞 칸(i) 빼고, 다음 칸(i + T) 더하기
        curr_sum = curr_sum - timeline[i] + timeline[i + T]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start_time = i + 1
    
    print(start_time, start_time + T)


if __name__ == "__main__":
    main()