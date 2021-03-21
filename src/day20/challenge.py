from Tile import Tile 
import numpy as np
import re 
import math


def process_data( tiles ) : 

    tile_objects = []
    
    for tile in tiles : 
        tile_lines = tile.splitlines()
        tile_val = int( re.findall( "\\d+", tile_lines[0] )[0] )

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

    i = 0
    while i < len( placed ) :
        tile = placed[i] # cannot move these tiles as they have been placed already
        j = 0
        i += 1

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


def part_one( grid ) :
    print( "Part one: ", grid[0,0].get_tile_num() * grid[0,-1].get_tile_num() * grid[-1,-1].get_tile_num() * grid[-1,0].get_tile_num() )



def part_two( grid ) : 
    no_boarders_grid_size = grid[0,0].get_tile_no_boarder().shape
    tiles = np.zeros( ( np.array( no_boarders_grid_size ) ) * len( grid ), dtype=int )
    offset = no_boarders_grid_size[0] + 1

    x1 = 0
    x2 = offset - 1
    y1 = 0
    y2 = offset - 1
    
    for i, grid_row in enumerate( grid ) : 

        x1 = 0
        x2 = offset - 1

        for j, tile in enumerate( grid_row ) :
            tiles[x1:x2,y1:y2] = tile.get_tile_no_boarder()

            x1 = x2 
            x2 += offset - 1

        y1 = y2 
        y2 += offset - 1
    
    # search for sea monsters
    sea_monster_mask = np.array( [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False],
                             [True, False, False, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, True],
                             [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, False]], dtype=bool )

    ocean = np.copy( tiles )

    sea_monsters_found = 0

    for j in range( 2 ) :

        for i in range( 4 ) : 
            ocean = np.rot90( ocean ) # rotate until all iterations are completed or sea monsters are found 

            sea_monsters_found = 0

            x1 = 0
            x2 = len( sea_monster_mask[0] )
            y1 = 0
            y2 = len( sea_monster_mask )

            while y2 <= len( ocean ) and x2 <= len( ocean ) :
                search_area = ocean[y1:y2,x1:x2]

                search_area = np.ma.array(search_area, mask=~sea_monster_mask)

                # check if search area is a sea monster 
                zeros_present = np.any( search_area == 0 )

                if not zeros_present :
                    sea_monsters_found += 1

                    # mark that a sea dragon is here 
                    [y, x] = np.where( search_area == 1 )
                    ocean[y+y1,x+x1] = 2

                x1 += 1 
                x2 += 1 
                
                if x2 == len( ocean ) + 1:
                    y1 += 1 
                    y2 += 1

                    x1 = 0
                    x2 = len( sea_monster_mask[0] )

            if sea_monsters_found > 0 :
                break

        if sea_monsters_found > 0 :
            break

        ocean = np.flip( tiles, axis=j )

    # count calm sea's
    calm_seas = len( np.where( ocean == 1 )[0] )
    print( "Part Two: ", calm_seas )




def main() :
    a_file      = open( "src/day20/puzzleInput.txt" )
    data_input  = a_file.read().split( "\n\n" )
    a_file.close()

    grid = sort_grid( data_input )

    part_one( grid )
    part_two( grid )


if __name__ == '__main__' :
    main()