while True:
    try:
        n,m = input().split()
        soma = sum(int(d) for d in m)
        div = (soma % 3 == 0)
        print("{} {}".format(soma, "sim" if div else "nao"))
    except EOFError:
        break