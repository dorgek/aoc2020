import re 
from FieldRange import FieldRange

def part_one( input_data ) :
    your_ticket = False
    other_tickets = False  
    valid_ranges = []
    error_rate = 0
    
    for line in input_data :
        if not your_ticket and not other_tickets :
            valid_ranges.append( get_valid_rows( line ) )
        elif ( your_ticket or other_tickets ) and ':' not in line : 

            for val in line.split( ',' ) :
                valid = check_valid_range( valid_ranges, int( val ) )

                if not valid :
                    error_rate += int( val )
                    break

        if "your ticket" in line : 
            your_ticket = True 
        if "nearby tickets" in line :
            your_ticket = False 
            other_tickets = True


    print( "Part one: ", error_rate )
                


def check_valid_range( valid_ranges, val ) :
    for valid_range in valid_ranges :
        if valid_range.is_in_range( val ) : 
            return True 

    return False 




def get_valid_rows( line ) :
    ret = FieldRange()

    matches = re.findall( "[0-9-]+", line )
    
    ret.set_range_values( matches )

    return ret


    

        



def main() :
    a_file      = open( "src/day16/puzzleInput.txt" )
    data_input  = "\n".join( [ s for s in a_file.read().splitlines() if s]).splitlines()
    a_file.close()

    part_one( data_input )
    



if __name__ == '__main__' :
    main()