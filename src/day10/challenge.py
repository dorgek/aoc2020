from functools import reduce
import itertools
import operator
import math
from numpy import loadtxt

def merge( arr, l, m, r ) :
    n1 = m - l + 1
    n2 = r - m 

    # temp arrays
    L = [0] * ( n1 )
    R = [0] * ( n2 )

    # copy data to temp arrays 
    for i in range( 0, n1 ) : 
        L[i] = arr[l + i]
    
    for j in range( 0, n2 ) :
        R[j] = arr[m + 1 + j] 

    # merge the temp arrays back in
    i = 0
    j = 0
    k = l 

    while i < n1 and j < n2 :
        if L[i] <= R[j] :
            arr[k] = L[i] 
            i += 1
        else :
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1


def merge_sort( arr, l, r ) :
    if l < r :
        # find the middle point of the array
        m = ( l + ( r - 1 ) ) // 2

        # call merge sort on the first part
        merge_sort( arr, l, m )

        # call merge sort for second half
        merge_sort( arr, m + 1, r )

        # merge the two arrays
        merge( arr, l, m, r )


def can_remove( prev_val, following_val ) :
    if ( following_val - prev_val <= 3 ) :
        return True 
    else :
        return False

# determine all variations of the list available. Note that it is of jumps of either 1, 2, 3 less than. 
# can remove those that allow for a jump of 3 or less than on either side
def variations( arr, dub ) :
    # find values that can be removed
    rem = []

    for i in range( 1, len( arr ) - 1 ) :
        if ( can_remove( arr[i-1], arr[i+1] ) ) :
            rem.append( arr[i] )
    ret = 1

    arr_copy = arr.copy()

    if len( rem ) > 0 :
        for x in rem :
            arr_copy.remove( x )
            

            if  arr_copy not in dub :
                ret += variations( arr_copy, dub )
                dub.append( arr_copy )

            arr_copy = arr.copy()

    return ret


def create_blocks( arr ) : 
    ret  = [] 
    temp = []
    
    temp.append( arr[0] )

    for i in range( 1, len( arr ) ) :
        if ( arr[i] - arr[i-1] < 3 ) :
            temp.append( arr[i] )
        else :
            if ( len( temp ) > 2 ) :
                ret.append( temp )
            temp = []
            temp.append( arr[i] )

    return ret 


def part_two( arr ) :
    blocks = create_blocks( arr )
    ret    = []

    for block in blocks : 
        temp = variations( block, [] )
        ret.append( temp )

    

    return reduce( ( lambda x, y : x * y ), ret )
        

def main():
    # part 1
    joltageAdapters = loadtxt( "src/day10/joltageAdapters.txt" ).tolist()
    

    # append the starting adaptor
    joltageAdapters.append( 0 )
    inBuiltJoltageAdapter = max( joltageAdapters ) + 3          # get inbuilt joltage adapter

    merge_sort( joltageAdapters, 0, len( joltageAdapters ) - 1 )

    # append inBuiltJoltageAdapter
    joltageAdapters.append( inBuiltJoltageAdapter );

    diff = list(itertools.starmap( operator.sub, zip( joltageAdapters[1:], joltageAdapters ))) # TODO: work out what is happening here
    print( 'Part One: ', diff.count( 1 ) * diff.count( 3 ) )
    print( 'Part Two: ', part_two( joltageAdapters ) )

    

if __name__ == '__main__' :
    main()
