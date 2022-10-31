n = int(input())
weights = []
possible = [False for i in range(2001)]
possible[0] = True

for i in range(n):
    weights.append(int(input()))

for i in range(n):
    currWeight = weights[i]
    cap = 2001 - currWeight

    for j in range(cap, 0, -1):
        if possible[j]:
            possible[j + currWeight] = true

for i in range(len(possible)):
    if possible[1000 + i]:
        print(1000 + i)
        break;
    elif possible[1000-i]:
        print(1000 - i)
        break;

