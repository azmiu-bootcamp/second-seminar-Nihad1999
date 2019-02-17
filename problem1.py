
Student: Nihad abdulla
  1- ci mesele
  
  n = int(input())

cem = 0

while n>0:
    cem += n%10
    n -= n%10
    n //= 10

print(cem)

