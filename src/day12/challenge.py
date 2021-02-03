from ship import Ship
from shipTwo import ShipTwo

def part_one( directions ) : 
    ship_val   = Ship( [0, 0] )

    for direction in directions : 
        ship_val.update_position( direction )

    print( "Part One: ", ship_val.manhattan_distance() )


def part_two( directions ) : 
    ship_val   = ShipTwo( [0, 0], [ 10, -1 ] )

    for direction in directions : 
        ship_val.update_position( direction )

    print( "Part Two: ", ship_val.manhattan_distance() )
    

def main() :
    a_file     = open( "src/day12/puzzleInput.txt" )
    directions = a_file.read().splitlines()
    a_file.close()

    part_one( directions )
    part_two( directions )


if __name__ == '__main__' :
    main()