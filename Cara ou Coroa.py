while True:
    n=int(input())
    if n==0:
        break
    m =j=0
    for i in input().split():
        if i =='0':
            m+=1
        else:
            j+=1
    print(f"Mary won {m} times and John won {j} times")