n = int(input('so phan tu: '))
lst = []
for i in range(n):
	lst.append(int(input()))
answer = 0
for v in lst:
	answer += v
print(answer)