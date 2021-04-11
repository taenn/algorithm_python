# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)

first = data[0]
second = data[1]

quot = int(m / (k + 1))
remain = m % (k + 1)

sum = (first * k + second) * quot + first * remain

print(sum)