import queue
n=int(input('Enter number of vertices: '))

m=int(input('Enter number of edges: '))
visited=[ False for i in range(n)]
def bfs(s):
    visited[s]=True
    q=queue.Queue(50)
    q.put(s)
    print(s, end=" ")
    while(not q.empty()):
        p=q.get()
        if visited[p] is False:
        	print(p, end=' ')
        visited[p]=True
        # print(p,end=' ')
        for i in range(len(adj[p])):
            if(not visited[adj[p][i]]):
                q.put(adj[p][i])
print('Enter graph edges: ')
adj=[ None for i in range(n)]
for i in range(n):
    adj[i]=[]
for i in range(m):
    a=input()
    l=a.split(' ')
    x=int(l[0])
    y=int(l[1])
    adj[x].append(y)
    adj[y].append(x)
count=0
for i in range(n):
    if(not visited[i]):
        bfs(i)
        count=count+1
        print(' ')
print('Number of components:',count)
