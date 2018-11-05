from graph import Graph

def main():
    g= Graph()
    print(g)
    n = int(input("Number of edges: "))
    for i in range(n):
        g.insert(input())
    # g.insert("0 1")
    # g.insert("0 5")
    # g.insert("1 2")
    # g.insert("1 3")
    # g.insert("2 3")
    # g.insert("3 5")
    # g.insert("3 4")
    # g.insert("3 6")
    # g.insert("4 7")
    print(g)
    g.adjacency_matrix()
    print()
    print()
    p = int(input("Enter source vertex: ")) #3
    print("DFSing...")
    u = g.findNode(p)
    g.dfs(u)
    print()
    for i in g.nodes:
        print(i.string)

if __name__== '__main__':
    main()