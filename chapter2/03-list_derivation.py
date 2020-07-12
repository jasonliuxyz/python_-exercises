ls = list()
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                ls.append((x,y))
print(ls)
