n = int(input(('nhap so : ')))
def giaithua(n):
	
	if n ==0:
		return 1
	return n * giaithua(n-1)
print (giaithua(n))