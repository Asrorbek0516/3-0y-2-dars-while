balans = int(input("jami summa: "))
olinadigan_sum = int(input("Olinadigan summa: "))
count = 0

if balans/2<olinadigan_sum:
    while balans > olinadigan_sum:
        balans-=olinadigan_sum
        balans*=2
        count+=1
    print(f"{count} martada tugaydi\nqoldiq {balans}")
    
else:
    print("cheksiz")