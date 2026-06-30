H = int(input("Quduq chuqurligi H= "))
U = int(input("Baqa kunduzi chiqadigan masofa U= "))
D = int(input("Baqa kechasi sirg'anadigan masofa D= "))

kun = 0
masofa = 0

while masofa < H:
    masofa += U
    kun += 1
    if masofa >= H:
        break
    
    masofa -= D

print(f"Baqa {kun} kunda quduqdan chiqadi.")
