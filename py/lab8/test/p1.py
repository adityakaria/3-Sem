n=int(input('enter number of vertices: '))
adjm=[ None for i in range(n+1)]
for i in range(n+1):
	adjm[i]=[ 0 for j in range(n+1)]

adjl=[ None for i in range(n+1)]
for i in range(n+1):
	adjl[i]=[]

m = int(input('enter number of edges: '))
k=0

print("Enter the Edges")
while(k<m):
	t=input()
	a=t.split()
	x=int(a[0])
	y=int(a[1])
	adjm[x][y]=1
	adjm[y][x]=1
	adjl[x].append(y)
	adjl[y].append(x)
	k=k+1
	

print("adjacency matrix is")
for i in range(0,n):
	for j in range(0,n):
		print(adjm[i][j],end=' ')
	print('')


print('adjacency list is ')
for i in range(0,n):
	print('vertex',i)
	for j in range(len(adjl[i])):
		print(adjl[i][j],end=' ')
	print(' ')





