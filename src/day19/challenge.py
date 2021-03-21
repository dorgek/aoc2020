from Rules import Rules 
from more_itertools import split_after
import re 
import sys
import threading, resource

def part_one( data_input ) :
    vals = list( split_after( data_input, lambda x: x == '' ) )
    rule_str = vals[0][0:-1]
    sequences = vals[1]

    print('hello')

    total_passed = 0

    rule = Rules()    
    
    for rule_input in rule_str :
        rule_idx = re.findall( "(\\d+)(?=:)", rule_input )[0]
        rule_val = re.findall( "(?<=:\\s)[\\d\\sa-zA-Z|\\\"]+", rule_input )[0].replace( "\"", "" )
        
        rule.process_rule( int( rule_idx ), rule_val )


    for sequence in sequences : 
        # print(total_passed)
        if rule.validate_sequence( sequence ) :
            total_passed += 1
    
    print( "Part One: ", total_passed )


def main() :
    a_file      = open( "src/day19/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    a_file.close()



    part_one( data_input )

    
    



if __name__ == '__main__' :
    # threading.stack_size(8500000000)
    # resource.setrlimit(resource.RLIMIT_STACK, (2**45,-1))
    # sys.setrecursionlimit(2 ** 30)

    # thread = threading.Thread(target=main)
    # thread.start()
    main()