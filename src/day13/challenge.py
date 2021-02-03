import numpy as np

def part_one( bus_ids, time_start, time_depart ) :

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

def part_two( bus_ids ) :
    remainder_theorom( bus_ids )

def remainder_theorom( bus_ids ) :
    bi    = []
    ni    = []
    prodi = []
    idx   = 0

    for i, bus_id in enumerate( bus_ids ) :
        if i == 0 :
            bi.append( 0 )
            ni.append( int( bus_id ) )
        elif bus_id != 'x' and i != 0 :
            bi.append( int( bus_id ) - idx )
            ni.append( int( bus_id ) )

        idx += 1

    N = 1

    for idx, n in enumerate( ni ) :
        Ni = int( np.prod( ni[:idx] ) * np.prod( ni[idx+1:] ) )
        N  *= n
        xi = pow( Ni, -1, ni[idx] ) # inverse of Ni, x*y = 1 mod(p) -- y = pow(x, -1, p)
        
        prodi.append( bi[idx] * Ni * xi )

    print( "Part two: ", sum( prodi ) % N )


def check_solution( bus_id, time ) : 
    if ( ( time % bus_id ) == 0 ) : 
        return True 
    else : 
        return False 


def main() :
    a_file      = open( "src/day13/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    time_depart = int( data_input[0] )
    time_start  = int( data_input[0] )
    bus_ids     = [val for val in data_input[1].split( "," )]
    a_file.close()

    part_one( bus_ids, time_start, time_depart )
    part_two( bus_ids )


if __name__ == '__main__' :
    main()