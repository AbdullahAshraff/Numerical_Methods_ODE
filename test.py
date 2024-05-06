from math import sin,cos


x = 0
y = 1
ydash = lambda x,y : (sin(x)**3)*y
h = 0.1

k = ydash(x,y)

print("{x}\t{y}\t{k1}\t{xn1}\t{yn11}\t{k2}\t{ynplus1}")

for i in [0.0,0.1,0.2,0.3,0.4]:
  x = i
  xn1 = i+0.1

  k1 = round(ydash(x,y),5)
  yn11 = round(y+k1*h,5)
  k2 = round(ydash(xn1,yn11),5)
  ynplus1 = round(y + (h/2)*(k1+k2),5)

  print(f"{x}\t{y}\t{k1}\t{xn1:.2f}\t{yn11}\t{k2}\t{ynplus1}")
  y = ynplus1
