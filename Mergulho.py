while True:
    try:
        n,r= map(int,input().split())
    except EOFError:
        break
    mergulhadores = set(range(1, n+1))
    retornados = set(map(int, input().strip().split()))
    nao= mergulhadores-retornados
    if nao:
        print(*sorted(nao))
        
    else:
        print('*')
        break