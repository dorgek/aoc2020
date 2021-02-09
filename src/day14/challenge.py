from itertools import product
import re 

def part_one( input ) :
    mem  = {}
    mask = []

    for line in input :
        if "mask =" in line :
            # get the current mask
            mask = [i for i in re.sub( "[^0-9X]+", "", line )]
        else :
            # new instruction is found
            loc = int( re.sub( "[\[\]]", "", re.search( "(\[\d+\])", line ).group(0) ) )
            val = "{0:036b}".format( int( re.sub( "[=\s]", "", re.search( "(=\s\d+)", line ).group(0) ) ) )
            val = [i for i in val]

            apply_mask( val, mask )

            # convert back into integer
            mem[loc] = int( "".join( val ), 2 )

    
    print( "Part One: ", sum( mem.values() ) )


def apply_mask( bin, mask ) :
    for i, bit in enumerate( mask ) :
        if bit == '1'  :
            bin[i] = '1'
        elif bit == '0' :
            bin[i] = '0'



def part_two( input ) :
    mem  = {}
    mask = []

    for line in input :
        if "mask =" in line :
            # get the current mask
            mask = [i for i in re.sub( "[^0-9X]+", "", line )]
        else :
            loc      = "{0:036b}".format( int( re.sub( "[\[\]]", "", re.search( "(\[\d+\])", line ).group(0) ) ) )
            loc      = [i for i in loc]
            new_locs = []
            val      = int( re.sub( "[=\s]", "", re.search( "(=\s\d+)", line ).group(0) ) )

            new_masks = permutate_masks( mask )

            for new_mask in new_masks : 
                new_loc = loc.copy()
                apply_mask_two( new_loc, new_mask )
                new_locs.append( new_loc )

            # write all values to memeory 
            for new_loc in new_locs :
                mem[int("".join(new_loc), 2)] = val 

    print( "Part Two: ",  sum( mem.values() ) )


def permutate_masks( mask ) : 
    ret = []

    floating_values = mask.count( 'X' )
    all_possible_sequences = [x for x in product([2, 1], repeat=floating_values)] # TODO: work out alternative way to do this function
    
    # apply all possible values 
    for val in all_possible_sequences :
        new_mask = mask.copy()
        for q in val :
            new_mask[new_mask.index( 'X' )] = str( q )

        ret.append( new_mask )

    return ret 


def apply_mask_two( bin, mask ) :
    for i, bit in enumerate( mask ) :
        if bit == '1'  :
            bin[i] = '1'
        if bit == '2' :
            bin[i] = '0'


def main() :
    a_file      = open( "src/day14/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    a_file.close()

    part_one( data_input )
    part_two( data_input )
    



if __name__ == '__main__' :
    main()