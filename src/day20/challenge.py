from Tile import Tile 
import numpy as np
import re 
import math


def process_data( tiles ) : 

    tile_objects = []
    
    for tile in tiles : 
        tile_lines = tile.splitlines()
        tile_val = int( re.findall( "\d+", tile_lines[0] )[0] )

        tile_pattern = "\n".join(tile_lines[1:])
        tile_pattern = tile_pattern.replace( '#', '1 ' )
        tile_pattern = tile_pattern.replace( '.', '0 ' )

        size = len( tile_lines[1] )
        
        tile_objects.append( Tile( tile_pattern, tile_val, ( size, size ) ) )

    return tile_objects 


def sort_grid( data ) : 
    tiles = process_data( data )
    grid  = np.zeros( ( 3, 3 ), dtype=Tile )

    place  = tiles[1:]
    placed = [tiles[0]]

    grid[1,1] = tiles[0]
    tiles[0].set_grid_location( 0, 0 ) # center of grid currently is 0, 0

    # for i, tile in enumerate( tiles ) :
    i = 0
    while i < len( placed ) :
        tile = placed[i] # cannot move these tiles as they have been placed already
        j = 0
        i += 1

        # for j, tile_match in enumerate( tiles[i+1:] ) : 
        while j < len( place ) :
            tile_match = place[j]
            j += 1

            edge = tile.match_tile( tile_match )
            x = 0
            y = 0

            offset = math.floor(grid.shape[0]/2)

            if edge == 0 : # insert to the left side 

                placed_loc = tile.get_grid_location()
                new_loc = [placed_loc[0] - 1, placed_loc[1]]

                tile_match.set_grid_location( new_loc[0], new_loc[1] )

                # enter into grid 
                offset = math.floor(grid.shape[0]/2)
                x = new_loc[0] + offset
                y = new_loc[1] + offset

            elif edge == 1 : # insert above 

                placed_loc = tile.get_grid_location()
                new_loc = [placed_loc[0], placed_loc[1]-1]

                tile_match.set_grid_location( new_loc[0], new_loc[1] )

                # enter into grid 
                x = new_loc[0] + offset
                y = new_loc[1] + offset

            elif edge == 2 : # insert to the right 

                placed_loc = tile.get_grid_location()
                new_loc = [placed_loc[0]+1, placed_loc[1]]

                tile_match.set_grid_location( new_loc[0], new_loc[1] )

                # enter into grid 
                x = new_loc[0] + offset
                y = new_loc[1] + offset

            elif edge == 3 : # insert bellow 

                placed_loc = tile.get_grid_location()
                new_loc = [placed_loc[0], placed_loc[1]+1]

                tile_match.set_grid_location( new_loc[0], new_loc[1] )

                # enter into grid 
                x = new_loc[0] + offset
                y = new_loc[1] + offset
                

            if edge != -1 :
                j -= 1
                placed.append( tile_match )
                place.pop(j)

                grid[x, y] = tile_match

                # check if need to pad out grid 
                if x == 0 or y == 0 or x == len( grid ) - 1 or y == len( grid ) - 1 :
                    grid = np.pad( grid, 1, 'constant' )
                    

    index = np.where( grid != 0 )

    x = index[0][0]
    y = index[1][0]
    offset = int(math.sqrt(len(data)))

    return grid[x:x+offset, y:y+offset]


def part_one( data ) :
    grid = sort_grid( data )

    print( "Part one: ", grid[0,0].get_tile_num() * grid[0,-1].get_tile_num() * grid[-1,-1].get_tile_num() * grid[-1,0].get_tile_num() )







def main() :
    a_file      = open( "src/day20/puzzleInput.txt" )
    data_input  = a_file.read().split( "\n\n" )
    a_file.close()

    part_one( data_input )


if __name__ == '__main__' :
    main()