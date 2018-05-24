n=int(input())
a = []
b = []
for i in range(0,n):
  i=int(input())
  a.append(i)
print(a)
for j in range(0,n):
  j=int(input())
  b.append(j)
print(b)
c = []
for bx in b:
    if bx in a:
        c.append(bx)
if c:
    print ("yes")
else:
    print ("no")
