n=int(input("Enter number of nodes:"))
cost=0
def main():
 global a,visit
 a=[[0 for i in range(n)]
 for j in range(n)]
 visit=[0 for i in range(n)]
 for i in range(n):
    for j in range(n):
      temp=int(input())
    a[i][j]=temp
 for i in range(n):
   for j in range(n):
    print(a[i][j],end="\t")
   print("\n")
 print("Path is")
 mincost(0)
def mincost(c):
  global cost
  visit[c]=1
  print(c+1,end="-->")
  x=least(c)
  if x==999:
    x=0
    print(x+1)
    cost=cost+a[c][x]
  return
  mincost(x)
def least(u):
 global cost
 mini=v=999
 for i in range(n):
  if a[u][i]!=0 and visit[i]==0:
   if a[u][i]+a[i][u]<mini:
    mini=a[i][u]+a[u][i]
    kmin=a[u][i]
    v=i
  if mini!=999:
   cost=cost+kmin
   return v
main()
print("Minimum Cost is : ",cost)
