maxi=9999999
n=int(input("Enter the number of nodes:"))
selected=[False for i in range(n)]
def main(n,cost):
 n_edge=0
 selected[0]=True
 while n_edge<n-1:
   minimum=maxi
   x=y=0
 for i in range(n):
   if selected[i]:
    for j in range(n):
     if not selected[j] and cost[i][j]:
      if minimum>cost[i][j]:
       minimum=cost[i][j]
    x=i
    y=j
 print(x,'-->',y,':',cost[x][y])
 selected[y]=True
 n_edge+=1
cost=[[int(x) for x in input().split()]
 for j in range(n)]
for i in range(n):
 for j in range(n):
  if cost[i][j]==0:
   cost[i][j]=maxi
print("The shortest path using Prim's Algorithm is :\n")
main(n,cost)
