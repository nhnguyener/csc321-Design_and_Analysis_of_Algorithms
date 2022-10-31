m = int(input())
num_array = list()
ops = ['*','+','-','//']
for i in range(m):
    n = int(input())
    num_array.append(n)
for i in range(m):
    sol = False;
    for op1 in ops:
        if sol:
            break
        for op2 in ops:
            if sol:
                break
            for op3 in ops:
                expr = f'4 {op1} 4 {op2} 4 {op3} 4'
                if (eval(expr) == num_array[i]):
                    solstring = (f'{expr} = {num_array[i]}')
                    print(solstring.replace('//','/'))
                    sol=True
                    break
    if(sol == False):
        print("no solution")
