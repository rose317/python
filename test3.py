def get_odd():
    return [k for k in range(10) if k%2 ==1]

j=0
for i in get_odd():
    j += 1
    if j == 3:
        print(i)