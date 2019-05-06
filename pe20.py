mult = 1
for i in range(1, 101):
    mult *= i
print(sum(list(map(int, list(str(mult))))))

