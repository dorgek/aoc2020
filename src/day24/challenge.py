from collections import abc
import copy
import numpy as np

def prepare_input( data_input ) :
    temp_size     = 60
    center_offset = int( temp_size / 2 )
    grid          = np.zeros( ( temp_size, temp_size ), dtype=int )

    # step through data input from reference tile 
    for l in data_input :
        char_iter = iter( l )
        
        # axial coordinates
        q = 0
        r = 0

        for c in char_iter :
            if c == 'n' or c == 's':
                c += next( char_iter )

            if c == 'nw' :
                r -= 1
            elif c == 'se' :
                r += 1
            elif c == 'ne' :
                q += 1
                r -= 1 
            elif c == 'sw' :
                q -= 1
                r += 1
            elif c == 'w' :
                q -= 1
            elif c == 'e' :
                q += 1

        
        # toggle tile 
        grid[center_offset + q, center_offset + r] = 0 if grid[center_offset + q, center_offset + r] == 1 else 1

    return grid

def count_neighbours( grid, x, y ) :
    possible_neighbours = [[0, -1],
                        [1, -1],
                        [1, 0],
                        [0, 1],
                        [-1, 1],
                        [-1, 0]]

    count = 0

    for x_offset, y_offset in possible_neighbours :
        if grid[x + x_offset, y + y_offset] == 1 :
            count += 1 

    return count 

def count_tiles( grid ) :
    return np.sum( grid )


def generation( grid ) :
    temp_grid = copy.deepcopy( grid )
    size = len( temp_grid ) - 2

    increase_grid = False

    for x in range( 1, size ) :
        for y in range( 1, size ) :
            # for z in range( 1, size ) :
            neighbour_count = count_neighbours( grid, x, y) 

            if grid[x, y] == 1  and ( neighbour_count == 0 or neighbour_count > 2 ) : # black
                temp_grid[x, y] = 0 # change to white
            elif grid[x, y] == 0 and ( neighbour_count == 2 ) :
                temp_grid[x, y] = 1 # flip to black

                # if edge tile is black mark flag to increase size of grid 
                if x - 2 <= 0 or x + 2 >= size or y - 2 <= 0 or y + 2 >= size : 
                    increase_grid = True 

    # increase grid size 
    if increase_grid :
        temp_grid = np.pad( temp_grid, 2, 'constant' )

    return temp_grid


            

def main() :
    a_file     = open( "src/day24/puzzleInput.txt" )
    data_input = a_file.read().splitlines()
    a_file.close()

    # part one
    grid = prepare_input( data_input )

    print( "Part One: ", count_tiles( grid ) )

    # part two 
    for _ in range( 100 ) :
        grid = generation( grid )

    print( 'Part Two: ', count_tiles( grid ) )


if __name__ == '__main__' :
    main()