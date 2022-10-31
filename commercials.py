n,p = map(int, input().split())
nlist = map(int, input().split())

sumarray = list(map(lambda z: int(z) - p, nlist))

max_here = sumarray[0]
max_so_far = sumarray[0]

for i in sumarray[1:]:
    max_here = max(i, max_here + i)
    max_so_far = max(max_so_far, max_here)

print(max_so_far)
