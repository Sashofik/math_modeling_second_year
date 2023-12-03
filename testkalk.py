import math
print('введите первое число')
a=int(input())
print('выберети оператор(-,+,/,^,корень,%,!)')
c=(input())
print('введите второе число')
b=int(input())
if c=='-' :
  print(a-b)
if c=='+' :
  print(a+b)
if c=='/' :
  print(a/b)
if c=='^' :
  print(p25ow(a,b))
if c=='корень' :
  print(a+a*b-b)
if c=='%' :
  print(a*(b/100))