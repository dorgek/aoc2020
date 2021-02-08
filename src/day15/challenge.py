def part_one( data_input, i ) :
    """
        i - the iteration of the number spoken
    """
    current_iter = len( data_input )


    # loop until the required number is reached - treat 0 as a value
    for j in range( current_iter, i ) : # i
        prev_val = data_input[j-1] # get prev num

        if prev_val in data_input[:j-1] :
            # find the latest index of this value
            data_input.append( ( data_input[::-1][1:] ).index( prev_val ) + 1 ) 
        else :
            data_input.append( 0 )

    print( "Part One: ", data_input[-1] )

def main() :
    a_file      = open( "src/day15/testInput.txt" )
    data_input  = [ int( a ) for a in a_file.read().split( "," ) ]
    a_file.close()

    part_one( data_input, 2020 )
    



if __name__ == '__main__' :
    main()