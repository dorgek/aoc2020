from ship import ship

def part_one() : 
    a_file     = open( "src/day12/puzzleInput.txt" )
    directions = a_file.read().splitlines()
    ship_val   = ship( [0, 0] )
    a_file.close()

    for direction in directions : 
        ship_val.update_position( direction )

    print( "Part One: ", ship_val.manhattan_distance() )

def part_two() :
    

def main() :
    part_one()


if __name__ == '__main__' :
    main()