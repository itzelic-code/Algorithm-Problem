import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        cmd, val = op.split()
        val = int(val)
        
        if cmd == 'I':
            heapq.heappush(heap, val)
        elif heap:
            if val == 1:
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)
    
    return [max(heap), heap[0]] if heap else [0, 0]