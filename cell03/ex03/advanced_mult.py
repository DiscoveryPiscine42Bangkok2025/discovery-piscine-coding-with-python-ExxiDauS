import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i < 11:
        j = 0
        num = []
        while j < 11:
            num.append(str(i * j))
            j += 1
        print(f"Table de {i}: {' '.join(num)}")
        i += 1