data = input()
data = data.split()
x = int(data[0])
y = int(data[1])

fib = [0,1,1]
for i in range(x+1):
    fib.append(fib[-1] + fib[-2])
while x > 2:
    if y > fib[x-2]:
        y -= fib[x-2]
        x -= 1
    else:
        x -= 2
if x == 1:
    print("N")
if x == 2:
    print("A")
