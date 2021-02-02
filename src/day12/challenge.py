from ship import Ship
from shipTwo import ShipTwo

def part_one() : 
    a_file     = open( "src/day12/puzzleInput.txt" )
    directions = a_file.read().splitlines()
    ship_val   = Ship( [0, 0] )
    a_file.close()

    for direction in directions : 
        ship_val.update_position( direction )

    print( "Part One: ", ship_val.manhattan_distance() )


def part_two() : 
    a_file     = open( "src/day12/puzzleInput.txt" )
    directions = a_file.read().splitlines()
    ship_val   = ShipTwo( [0, 0], [ 10, -1 ] )
    a_file.close()

    for direction in directions : 
        ship_val.update_position( direction )

    print( "Part Two: ", ship_val.manhattan_distance() )
    

def main() :
    part_one()
    part_two()


if __name__ == '__main__' :
    main()