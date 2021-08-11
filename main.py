n = 10
N = [[]]
print('0' + '=' + str(N[0]))
for i in range(1, n+1):
    N.append(N[i-1] + [N[i-1]])
    print(str(i) + '=' + str(N[i]))
