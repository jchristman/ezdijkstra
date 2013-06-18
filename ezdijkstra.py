'''
ezdijkstra.py
Author: suntzu_II

Notes: Adapted from code found online. One major change to algorithm is that it did not
correctly find paths in which the graph had a cycle. That error was discoverd and fixed
by the_doctor (much thanks). The useful part of this script is simplifying the process
of using the script. There is a 2D list converter and a 3D list converter.
'''

import sys
from priodict import priority_dict

'''
Pass in a 2D board and an adjacency_matrix and this will convert the board. The adj mat
must be a list of tuples which represent relative positions from each spot that will connect.
The method will take the adj mat and apply it to every spot on the board, resulting in a
directed, weighted graph. Character weights must be a dictionary that assigns weights to
characters that are in the board. Any edge of the graph that leads TO the associated character
will be assigned the weight. The diagonal_weight variable is used to show that there the
path from one node diagonally to another is sqrt(2) distance. If the weight doesn't matter,
you can change this variable.

Example:
    board = [['x','x',' ','x','x']
             ['x',' ',' ','x','x']
             ['x',' ','x',' ','x']
             ['x',' ','x','x',' ']
             ['x',' ',' ',' ','x']]
    adjacency_matrix = [(-1,-1),
                        (-1, 0),
                        (-1, 1),
                        ( 0,-1),
                        ( 0, 1),
                        ( 1,-1),
                        ( 1, 0),
                        ( 1, 1)]
    character_weights = {'x':-1,' ':1} # -1 means not possible in this case
    G = convertBoard(board, adjacency_matrix, character_weights)
'''
def convert2DBoard(board,adjacency_matrix,character_weights,diagonal_weight=1.41,delimeter='_'):
    G = {}
    for row in xrange(len(board)): 
        for col in xrange(len(board[row])):
            current_spot = str(row) + delimeter + str(col)
            G[current_spot] = {}
            for adj in adjacency_matrix:
                try:
                    if row + adj[0] < 0 or col + adj[1] < 0:
                        raise IndexError()
                    char = board[row + adj[0]][col + adj[1]]
                    weight = -1
                    try:
                        weight = character_weights[char]
                    except KeyError as e:
                        print "'" + char +"' not found in the character_weights. Treating it as impassable."
                    if not adj[0] == 0 and not adj[1] == 0:
                        weight *= diagonal_weight
                    adjacent_spot = str(row + adj[0]) + delimeter + str(col + adj[1])
                    if weight >= 0:
                        G[current_spot][adjacent_spot] = weight
                except IndexError as e:
                    pass # Ignore index errors because we just don't care
    return G

def convert3DBoard(board,adjacency_matrix,character_weights,coplaner_diagonal_weight=1.41,noncoplaner_diagonal_weight=1.73,delimeter='_'):
    G = {}
    for plane in xrange(len(board)):
        for row in xrange(len(board[plane])): 
            for col in xrange(len(board[plane][row])):
                current_spot = str(plane) + delimeter + str(row) + delimeter + str(col)
                G[current_spot] = {}
                for adj in adjacency_matrix:
                    try:
                        if plane + adj[0] < 0 or row + adj[1] < 0 or col + adj[2] < 0:
                            raise IndexError()
                        char = board[plane + adj[0]][row + adj[1]][col + adj[2]]
                        weight = -1
                        try:
                            weight = character_weights[char]
                        except KeyError as e:
                            print "'" + char +"' not found in the character_weights. Treating it as impassable."
                        if adj.count(0) == 0:
                            weight *= noncoplaner_diagonal_weight
                        elif adj.count(0) == 1:
                            weight *= coplaner_diagonal_weight
                        adjacent_spot = str(plane + adj[0]) + delimeter + str(row + adj[1]) + delimeter + str(col + adj[2])
                        if weight >= 0:
                            G[current_spot][adjacent_spot] = weight
                    except IndexError as e:
                        pass # Ignore index errors because we just don't care
    return G

def dijkstra(G, start, end=None):
    D = {}	          # dictionary of final distances
    P = {}	          # dictionary of predecessors
    Q = priority_dict()   # est.dist. of non-final vert.
    
    # initialize Q and P
    for vertex in G:
        Q[vertex] = float("inf")
        P[vertex] = None
    
    Q[start] = 0
    
    for v in Q: # iterate and pop the smallest item in Q
        D[v] = Q[v]
        if v == end: break # we have reached the end

        for w in G[v]: # for all of v's adjacent vertices
            vwLength = D[v] + G[v][w]
            if (w not in D) and (w not in Q or vwLength < Q[w]):
                Q[w] = vwLength
                P[w] = v

    return D, P

def findshortestPath(G, start, end):
    """Find a single shortest path from the given start vertex to the given end vertex.
    The input has the same conventions as dijkstra().
    The output is a list of the vertices in order along
    the shortest path.

    Input: G - the input graph in the adjacency list representation via a dictionary
    start - the starting vertex
    end - the ending vertex

    Note: This method is not needed in the current exercise, however, it would be nice to know the shortest path from one vertex to another sometimes"""

    _, P = dijkstra(G, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start: break
        end = P[end] # find the next predecessor
    path.reverse() # reverse the list since we are appending from the back
    return path
