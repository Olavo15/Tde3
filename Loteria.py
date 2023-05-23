m=list(map(int,input().split()))
c=list(map(int,input().split()))
acertos=0
for num in m:
    if num in c:
        acertos+=1
if acertos>=6:
    print("sena")
elif acertos==5:
    print("quina")
elif acertos==4:
    print("quadra")
elif acertos==3:
    print("terno")
else:
    print("azar")