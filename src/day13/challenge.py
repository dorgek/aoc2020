def part_one() :
    a_file      = open( "src/day13/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    time_depart = int( data_input[0] )
    time_start  = int( data_input[0] )
    bus_ids     = [val for val in data_input[1].split( "," )]
    a_file.close()

    solution   = False 
    bus_id_val = 0

    while not solution :

        for i, bus_id in enumerate( bus_ids ) :
            if not bus_id == 'x' :
                bus_id_val = int( bus_id )
                solution = check_solution( int( bus_id ), time_start )
            
            if solution :
                break 

        if solution : 
            break

        time_start += 1 

    val = ( time_start - time_depart ) * bus_id_val

    print( "Part One: ", val )

def check_solution( bus_id, time ) : 
    if ( ( time % bus_id ) == 0 ) : 
        return True 
    else : 
        return False 


def main() :
    part_one()


if __name__ == '__main__' :
    main()