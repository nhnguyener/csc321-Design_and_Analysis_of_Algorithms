from itertools import combinations
n,m = map(int, input().split())
bans = list()
count = 1
for x in range(m):
    a,b = map(int, input().split())
    pair = list()
    pair.append(a)
    pair.append(b)
    bans.append(pair)

ingredients = list()
for x in range(n):
    ingredients.append(x+1)

for x in range(n):
    combo = combinations(ingredients, x+1)
    for y in list(combo):
        print('combo ', y)
        count += 1
        set1 = set(y)
        for z in bans:
            set2 = set(z)
            if set2.issubset(set1):
                print('ban ', z)
                print('minus')
                count -= 1
                break
print(count)
    
    
