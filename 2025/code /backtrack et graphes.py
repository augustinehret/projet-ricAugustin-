def dfs(G,s):
    l = G[s].copy
    a_visiter = l
    visiter = [s]
    while a_visiter != []:
        suivant = a_visiter.pop()
        if not suivant in visiter :
            visiter.append(suivant)
            a_visiter = a_visiter + G[suivant]
    return visiter 


def Dijkstra(G,s):
    n = len(G)
    visiter = []
    t = [-1 for i in range(n)]
    for i in range(n):
        if G[s][i] != 0 :
            t[i] = G[s][i]
            visiter.append(i)
    a_visiter =        





def to_dico(G):
    dico = {}
    for i in range(len(G)-1):
        l = []
        for j in range(len(G[i])):
            if G[i][j]:
                l.append[j]
        dico[i] = l
    return dico 


def to_matrix(d):
    m = [[0 for k in range(len(d))] for i in range(len(d))]
    for j in range(len(d)):
        for k in range(len(d[j])):
            m[j][d[j][k]] = 1
    return m


def successor(G,s):
    res = []
    d = to_dico(G)
    for i in range(len(d)):
        if s in d[i]:
            res.append(i)
    return res 


def input_degree(G,s):
    return len(successor(G,s))


def output_degree(G,s):
    d = to_dico(G)
    return len(d[s])


def DFS(G,s):
    d = to_dico(G)
    visiter = []
    l = d[s].copy
    a_visiter = l
    while a_visiter != []:
        x = a_visiter.pop() 
        if not x in visiter :
            visiter.append(x)
            a_visiter.append(d[x])
    


def BFS(G,s):
    d = to_dico(G)
    visiter = []
    l = d[s].copy
    a_visiter = l
    while a_visiter != []:
        x = a_visiter.pop(0) 
        if not x in visiter :
            visiter.append(x)
            for k in d[x] : 
                a_visiter.append(k) 
    
   
   

def position(l):
    for i in range(l):
        if l[i]==1: 
            return i 
        

def check(l):
    flag = True 






def interdit(m):
    n = len(m)
    res= [[1 for i in range(n)] for j in range(n)]
    l_1 = [0]*n
    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                res[i]=l_1
                for k in range(n):
                    res[k][j] = 0
                    if (i+k < n) and (j+k < n):
                        res[i+k][j+k] = 0
                    if (i-k < 0) and (j-k < 0):
                         res[i+k][j+k] = 0
    return res 



def check(m,p):
   (x,y) = p 
   interdits = interdit(m) 
   interdits[x][y] == 1


def backtrack(n):
    m_base = [[0]*n]*n
    res = []
    def aux(acc,m): 
        if acc == (n-1) : 
            res.append(m)
        else : 
            for i in range(n):
                if check(m,(i,acc)):
                    m_suivant = m.copy
                    m_suivant[i][acc] = 1
                    aux(acc+1,m_suivant)
    aux(0,m_base)  
    return res   


def nombres_solutions(n):
    return len((backtrack(n)))

























