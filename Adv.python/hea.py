import heapq

L=[]

heapq.heappush(L,10)

heapq.heappush(L,1)
print(L)

heapq.heappop(L)
print(L)


L1=[70,80,10,20,50,40,30,60]

heapq.heapify(L1)

print(L1)

heapq.heappop(L1)
print(L1)

print(heapq.nlargest(1,L1))




