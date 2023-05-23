A,B,C=map(float,input().split())
n=(B**2)-4*A*C
if A==0 and n<0:
  print("Impossivel calcular")
else:
  x1=(-B+(n**(1/2)))/(2*A)
  x2=(-B-(n**(1/2)))/(2*A)
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')