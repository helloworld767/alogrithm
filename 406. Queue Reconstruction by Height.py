import heapq
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
dic = {tuple(i): i[1] for i in people}
res = []
q = []
for i in people:
    if i[1] == 0:
        heapq.heappush(q, i)
while q:
    person = heapq.heappop(q)
    res.append(person)
    del dic[tuple(person)]
    for k in dic:
        if k[0] <= person[0]:
            dic[k] -= 1
            if dic[k] == 0:
                heapq.heappush(q, list(k))
print(res)
print(dic)
b = 1
a = 2
b += a < 0
print(b)