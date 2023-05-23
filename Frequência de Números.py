num=int(input())
vez={}
for x in range(num):
    x = int(input())
    if x not in vez:
        vez[x] = 1
    else:
        vez[x] += 1
for x in sorted(vez.keys()):
    print(f"{x} aparece {vez[x]} vez(es)")