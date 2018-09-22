def karatsuba(x,y):
	if(len(str(x)) or len(str(y))) == 1:
		return x*y
	else:
		maxLen = max(len(str(x)),len(str(y)))
		mid = maxLen//2
		a = x//(10**(mid))
		b = x%(10**(mid))
		c = y//(10**(mid))
		d = y%(10**(mid))
	return((10**(2*mid)*karatsuba(a,c)) + karatsuba(b,d) + (10**(mid)) * (karatsuba(a,d) + karatsuba(b,c)))

m = int(input("Enter the Number m "))
n = int(input("Enter the Number n "))
print(karatsuba(m,n))

