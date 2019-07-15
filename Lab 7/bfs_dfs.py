#import collections
graph={'A':['B','C','D'],'B':['E','F'],'C':['G','H'],'D':['I','J'],'E':['K','L'],'F':['M'],'G':['N'],'H':['O'],'I':['P','Q'],'J':['R'],'K':['S'],'L':['T'],'M':[],'N':[],'O':[],'P':['U'],'Q':[],'R':[],'S':[],'T':[]}


def BFS(graph,start,end):
    
    frontier=[]
    frontier.append(start)
    visited=[]
    while(frontier):
        i=frontier[0]
        if (i==end):
            visited.append(i)
            break
        elif i not in visited:
            frontier.extend(graph[i])
            visited.append(i)
        else:
            frontier.pop(0)
    print(visited)


def DFS(graph,start,goal):
    path=[]
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
          path=path+[v]
          if v==goal:
              return path
        q=graph[v]+q
    return path


BFS(graph,'A','N')
print(DFS(graph,'A','N'))