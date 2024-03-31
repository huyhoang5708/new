def UCLN(a,b):
    if b==0:
        return a
    return UCLN(b,a%b)

def BCNN(a,b):
    return int((a*b)/UCLN(a,b))

a= int(input())
b=int(input())





print(UCLN(a,b))
print(BCNN(a,b))