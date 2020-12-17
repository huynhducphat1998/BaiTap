def convert_number(n,b):
	if(n < 0 or b< 2  or b>16):
		return ""
	sb = ""
	m = 0
	remainde = n
	while (remainde >0):
		if( b > 10):
			m = remainde %b 
			if ( m >=10):
				sb = sb +str(chr(55 +m))
			else:
				sb =sb + str(m)
		else:
			sb = sb + str(remainde % b )
		remainde = int(remainde / b)
	return "".join(reversed(sb))
n = int (input("nhap so nguyen duong n = "))
print("he co so so 2 ",n ," la" ,convert_number(n,2))
print("he co so so 16 ",n ," la" ,convert_number(n,16))