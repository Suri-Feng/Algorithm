def Karatsuba(x, y):
    if len(x) == 1 or len(y) == 1:
        return str(int(x)*int(y))
    cut1 = len(x)//2 + len(x)%2
    cut2 = len(y)//2 + len(y)%2
    a = x[:cut1]
    b = x[cut1:]
    c = y[:cut2]
    d = y[cut2:]
    ac = int(Karatsuba(a, c))
    bd = int(Karatsuba(b, d))
    ad_bc = int(Karatsuba(str(int(a) + int(b)), str(int(c)+ int(d)))) - ac - bd
    ans = (10**(len(x)//2*2))*ac + (10**(len(x)//2))*ad_bc + bd
    return str(ans) 


x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'
print(int(x)*int(y))
#x = '23'
#y = '100'
print(Karatsuba(x,y))