import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0 
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        temp1 = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        mix = (temp1 + temp2*2)
        heapq.heappush(scoville, mix)
        cnt += 1
    return cnt