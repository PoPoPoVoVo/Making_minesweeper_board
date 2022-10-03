import numpy as np
def start():
    X,Y,N = input("게임을 수행할 크기 X*Y를 입력하세요: X(space)Y // 설치할 지뢰 개수를 설정하세요:" ).split()
    X = int(X)
    Y = int(Y)
    N = int(N)
    if N > X*Y :
        print("ERROR! 지뢰 개수가 게임을 수행할 공간보다 큽니다!")
        L,N,M = start()
        L = int(L)
        N = int(N)
        M = int(M)
        return L,N,M
    return X,Y,N
    
def make_grid(X,Y):
    Grid = np.array( [[0 for i in range(Y)] for j in range(X) ] )
    return Grid


def insert_mine(Grid):
    global X,Y
    G = Grid
    mine_X = np.random.randint(X)
    mine_Y = np.random.randint(Y)
    if G[mine_X][mine_Y] != 100:
        G[mine_X][mine_Y] = 100
    else:
        G = insert_mine(Grid)
    return G


def count_around_mine(Grid):
    global X,Y
    G = Grid
    for i in range(X):
        for j in range(Y):
            c = 0
            if G[i][j] != 100:
                for p in [-1,0,1]:
                    for q in [-1,0,1]:
                        if i+p >=0 and j+q>=0 and i+p<=X-1 and j+q<=Y-1:
                            if G[i+p][j+q] == 100:
                                c += 1
                G[i][j] = c
    return G

def N_insert_mine(Grid, N):
    G_N = Grid
    N = N
    for i in range(N):
        G_N = insert_mine(Grid)
    G_N = count_around_mine(G_N)
    return G_N
    
    
    
    
    
/////////////////////////////////    
X,Y,N = start()
print(X,Y,N)
Grid = make_grid(X,Y)
Grid = N_insert_mine(Grid,N)
