p = 29
ints = [14, 6, 11]
flag = 100000 # max
for n in ints:
    for a in range(1,29):
        if pow(a,2,p) == n:
            flag = min(flag,a)
print(flag)
# Answer: 8