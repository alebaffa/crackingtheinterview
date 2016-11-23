# HackerRank challenge: Even Tree
# https://www.hackerrank.com/challenges/even-tree

# First sample input 
# Expected output: 2
'''
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
'''

# Second sample input
# Expected output: 4
'''
20 19
2 1
3 1
4 3
5 2
6 5
7 1
8 1
9 2
10 7
11 10
12 3
13 7
14 8
15 12
16 6
17 6
18 10
19 1
20 8
'''

def read_line():
    a, b = str(raw_input()).split(' ')
    a, b = int(a), int(b)
    return a, b
    
def load(m):
    graph = {}
    for i in range(m):
        a, b = read_line()
        if a == 1:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = list([b])
        else:
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = list([a])
    return graph
        
def compute_sub_tree_length(node):
    tot = 1
    if node in graph:
        for i in graph.get(node):
            tot += compute_sub_tree_length(i)
    return tot
    
def prune(node):
    tot = 0
    if node in graph:
        subtrees = graph.get(node)
        for st in subtrees:
            sub_tree_length = compute_sub_tree_length(st)
            if sub_tree_length%2 == 0:
                tot += 1 + prune(st)
            else:
                tot += prune(st)
    return tot

n, m = read_line()
graph = load(m)
# print graph
if n%2 == 1:
    print 0
print prune(1)

