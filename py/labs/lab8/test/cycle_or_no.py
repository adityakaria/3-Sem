import queue
n=int(input('enter number of vertices'))

m=int(input('enter number of edges'))
visited=[ False for i in range(n)]
def bfs(s,flag):
    visited[s]=True
    q=queue.Queue(50)
    q.put(s)
    while(not q.empty()):
        p=q.get()
        visited[p]=True

        for i in range(len(adj[p])):
            if(not visited[adj[p][i]]):
                q.put(adj[p][i])
            else:
                flag=1
                break
        if(flag==1):
            break
    return flag

print('enter graph')
adj=[ None for i in range(n)]
for i in range(n):
    adj[i]=[]
for i in range(m):
    a=input()
    l=a.split(' ')
    x=int(l[0])
    y=int(l[1])
    adj[x].append(y)
    

for i in range(n):
    if(not visited[i]):
        flag=bfs(i,0)
        if(flag==1):
            break
if(flag==1):
    print('graph has cycle')
else:
    print('graph is with no cycle')
        
