from graph import Graph

def main():
    g= Graph()
    print(g)
    # n = int(input("Number of edges: "))
    # for i in range(n+1):
    #     g.insert(input())
    g.insert("0 1")
    g.insert("0 2")
    g.insert("1 2")
    g.insert("1 3")
    g.insert("1 4")
    g.insert("2 3")
    print(g)
    g.adjacency_matrix()
    print
    print
    print("DFSing...")
    u = g.findNode(2)
    g.dfs(u)

    for i in g.nodes:
        print(i.string)

if __name__== '__main__':
    main()