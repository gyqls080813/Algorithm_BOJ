import heapq
N = int(input())
heap_list = []
for _ in range(N):
    input_number = int(input())
    if input_number == 0:
        if heap_list:
            print(heapq.heappop(heap_list)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap_list, [abs(input_number), input_number])
    