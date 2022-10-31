n,p = map(int, input().split())
nlist = map(int, input().split())
nlist = list(nlist)

sumarray = [[-1 for i in range(n)] for j in range(n)]
ans = -1
length = n-1
for i in range(n):
    sumarray[i][1] = nlist[i]

for i in range(1,n):
    for j in range(i):
        if nlist[j] < nlist[i]:
            for k in range(1,length):
                if sumarray[j][k] != -1:
                    sumarray[i][k+1] = max(sumarray[i][k+1],sumarray[j][k] + nlist[i])
for i in range(n):
    if ans < sumarray[i][length]:
        ans = sumarray[i][length]
        
print(ans)


#for i in range(1,n):
#    for j in range(i):
#        print(sumarray[i][j])
