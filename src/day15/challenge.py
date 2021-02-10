def list_construct( data_input, i ) :
    """
        i - the iteration of the number spoken
    """
    current_iter = len( data_input )
    index_of_values = {}
    current_val = 0
    prev_val = data_input[-1]
    prev_index = len( data_input ) - 1

    # set up the initial map 
    for j, val in enumerate( data_input[:-1] ) :
        index_of_values[val] = j

    # loop until the required number is reached - treat 0 as a value
    for j in range( current_iter, i ) : # i
        
        # check if previous val was in dictionary
        if prev_val in index_of_values :
            # determine new value
            current_val = j - index_of_values[prev_val] - 1
        else  :
            current_val = 0

        index_of_values[prev_val] = prev_index
        prev_val = current_val
        prev_index = j

    return current_val

def main() :
    a_file      = open( "src/day15/puzzleInput.txt" )
    data_input  = [ int( a ) for a in a_file.read().split( "," ) ]
    data_input_two = data_input.copy()
    a_file.close()

    print( "Part One: ", list_construct( data_input, 2020 ) )
    print( "Part Two: ", list_construct( data_input_two, 30000000 ) )
    



if __name__ == '__main__' :
    main()