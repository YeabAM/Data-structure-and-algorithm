import heapq
def minimumAverage(customers):    
    # Write your code here
    n = len(customers)
    customers.sort(reverse=True)
    for i in range(len(customers)):
        customers[i][0], customers[i][1] = customers[i][1], customers[i][0]
        
    heap = [customers.pop()]
    current_time  = 0 #heapq.heappop(heap)[0]
    waiting_time = 0
    
    while heap:
        
        curr_order= heapq.heappop(heap)
        if current_time >= curr_order[1]:
            current_time += curr_order[0]
        else:
            current_time = curr_order[0] + curr_order[1]
        waiting_time += current_time - curr_order[1]
        
        # print("curr_order = ",curr_order,"wait = " ,waiting_time, "current = ",current_time, heap)
        
        while customers and customers[-1][1] <= current_time:
            heapq.heappush(heap, customers.pop())
        
        if not heap  and customers:
            heapq.heappush(heap, customers.pop())
            
    print(waiting_time//n)
    return waiting_time//n


def main():
    n = int(input())
    customers = []
    for _ in range(n):
        start,end = map(int,input().split())
        customers.append([start,end])
    minimumAverage(customers)

main()