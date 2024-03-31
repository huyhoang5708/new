def tong_cac_chu_so(data):
    s = 0
    while data>0:
        s=s+ data%10 
        data = int(data/10)
    return s

a = int(input())
print(tong_cac_chu_so(a))
