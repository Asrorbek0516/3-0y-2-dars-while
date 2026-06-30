balandlik = 100

tormozlash = int(input("son kiriting: "))

tezlik = 0

while balandlik>0:
    tezlik +=10
    tezlik-=tormozlash
    balandlik -= tezlik

if tezlik<5:
    print("muvaffaqiyatli qo'ndi")
else:
    print("kema halokatga uchradi")
print(tezlik)