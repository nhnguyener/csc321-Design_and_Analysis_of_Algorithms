from collections import defaultdict

i = int(input().strip())
graph = defaultdict(list)
zeroset = set()

for i in range(i):
    rule = input()
    c, p = [k.strip() for k in rule.split(":")]
    p = p.split()
    degree[c] = len(p)
    if degree[c] == 0:
        zeroset.add(c)
    for x in p:
        graph[x].append(c)

newfile = input().strip
if newfile in zeroset:
    zeroset.remove(newfile)

while zeroset:
    current = zeroset.pop()
    for i in graph[current]:
        degree[i] = -1
        if degree[i] == 0 and i != newfile:
            zeroset.add(i)

zeroset = [newfile]
while zeroset:
    current = zeroset.pop()
    print(current)
    for i in graph[current]:
        degree[i] -= 1
        if degree[i] == 0:
            zeroset.append(i)
