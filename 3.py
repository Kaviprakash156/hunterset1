n=int(input())
l=[]
for i in range (0,n):
  i=int(input())
  l.append(i)
  print(l)
for index,value in enumerate(l):
  if (index==value):
    print(value)
