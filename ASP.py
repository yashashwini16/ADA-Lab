n=int(input("Enter the number of nodes:"))
graph=[[0 for i in range(n)] for j in range(n)]
print("Enter the adjacency matrix in boolean values:")
for i in range(n):
 for j in range(n):
  temp=int(input())
  graph[i][j]=temp
print("The adjacency matrix in boolean values:") 
for i in range(n):
 for j in range(n):
 
  print(graph[i][j],end="\t")
  print("\n")
for k in range(n):
 for i in range(n):
  for j in range(n):
   if graph[i][k]==1 and graph[k][j]==1:
     graph[i][j]=1
print("*******WARSHALL'S TRANSITIVE CLOSURE********")
for i in range(n):
 for j in range(n):
 
  print(graph[i][j],end="\t")
  print("\n")
