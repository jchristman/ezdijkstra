import ezdijkstra

board = [['x','x',' ','x','x'],
         ['x',' ',' ','x','x'],
         ['x',' ','x',' ','x'],
         ['x',' ','x','x',' '],
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
G = ezdijkstra.convert2DBoard(board, adjacency_matrix, character_weights)
print ezdijkstra.findshortestPath(G, '0_2','4_3')

board = [[['x','x',' ','x','x'],
          ['x',' ',' ','x','x'],
          ['x','x','x',' ','x'],
          ['x',' ','x','x','x'],
          ['x',' ',' ',' ','x']],

         [['x','x','x','x','x'],
          ['x','x','x','x','x'],
          ['x',' ','x','x','x'],
          ['x','x','x','x',' '],
          ['x','x','x','x','x']]]
adjacency_matrix = [(-1,-1,-1),(-1,-1, 0),(-1,-1, 1),
                    (-1, 0,-1),(-1, 0, 0),(-1, 0, 1),
                    (-1, 1,-1),(-1, 1, 0),(-1, 1, 1),
                    ( 0,-1,-1),( 0,-1, 0),( 0,-1, 1),
                    ( 0, 0,-1),           ( 0, 0, 1),
                    ( 0, 1,-1),( 0, 1, 0),( 0, 1, 1),
                    ( 1,-1,-1),( 1,-1, 0),( 1,-1, 1),
                    ( 1, 0,-1),( 1, 0, 0),( 1, 0, 1),
                    ( 1, 1,-1),( 1, 1, 0),( 1, 1, 1)]
character_weights = {'x':-1,' ':1} # -1 means not possible in this case
G = ezdijkstra.convert3DBoard(board, adjacency_matrix, character_weights)
print ezdijkstra.findshortestPath(G, '0_0_2', '0_4_3')
