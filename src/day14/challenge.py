import re 

def part_one( input ) :
    mem  = [0] * 65465
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

    
    print( "Part One: ", sum( mem ) )


def apply_mask( bin, mask ) :
    for i, bit in enumerate( mask ) :
        if bit == '1'  :
            bin[i] = '1'
        elif bit == '0' :
            bin[i] = '0'



def main() :
    a_file      = open( "src/day14/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    a_file.close()

    part_one( data_input )
    



if __name__ == '__main__' :
    main()