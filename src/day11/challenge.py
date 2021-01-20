import copy 

def split( word ) :
    return [char for char in word]

def can_sit( x, y, input ) :
    # if outside the bounds treat as floor
    if ( x < 0 or y < 0 ) or ( y >= len( input ) or x >= len( input[y] ) ):
        return True 

    if input[y][x] == 'L' or input[y][x] == '.' :
        return True 
    else :
        return False

def is_floor( x, y, input ) :
    # if outside the bounds treat as floor
    if ( x < 0 or y < 0 ) or ( y >= len( input ) or x >= len( input[y] ) ):
        return True 

    if input[y][x] == '.' :
        return True 
    else :
        return False

def sit( x, y, input ) :
    update = []
    
    if input[y][x] == 'L' :
        # determine if adjacent seats available 
        avail_seats = 0
        if can_sit( x-1, y-1, input ) :
            avail_seats += 1
        if can_sit( x, y-1, input ) :
            avail_seats += 1
        if can_sit( x+1, y-1, input ) :
            avail_seats += 1
        if can_sit( x-1, y, input ) :
            avail_seats += 1
        if can_sit( x+1, y, input ) :
            avail_seats += 1
        if can_sit( x-1, y+1, input ) :
            avail_seats += 1
        if can_sit( x, y+1, input ) :
            avail_seats += 1
        if can_sit( x+1, y+1, input ) :
            avail_seats += 1

        if avail_seats == 8 :
            update = [x, y]

    return update 

def can_vacate( x, y, input ) : 
    # if outside the bounds treat as floor
    if ( x < 0 or y < 0 ) or ( y >= len( input ) or x >= len( input[y] ) ):
        return False 

    if input[y][x] == '#' :
        return True 
    else :
        return False 

def remove_person( x, y, input ) :
    update = [] 

    if input[y][x] == '#' :
        occupied_seats = 0
        if can_vacate( x-1, y-1, input ) :
            occupied_seats += 1
        if can_vacate( x, y-1, input ) :
            occupied_seats += 1
        if can_vacate( x+1, y-1, input ) :
            occupied_seats += 1
        if can_vacate( x-1, y, input ) :
            occupied_seats += 1
        if can_vacate( x+1, y, input ) :
            occupied_seats += 1
        if can_vacate( x-1, y+1, input ) :
            occupied_seats += 1
        if can_vacate( x, y+1, input ) :
            occupied_seats += 1
        if can_vacate( x+1, y+1, input ) :
            occupied_seats += 1

        if occupied_seats >= 4 :
            update = [x, y]

    return update 

def parse( input ) :
    update = []

    for y in range( len( input ) ) :
        for x in range( len( input[0] ) ) :
            temp = sit( x, y, input )
            if len( temp ) > 0 :
                update.append( temp )
    
    # update list 
    for [x, y] in update :
        input[y][x] = '#'

    update = []

    for y in range( len( input ) ) :
        for x in range( len( input[0] ) ) :
            temp = remove_person( x, y, input )
            if len( temp ) > 0 :
                update.append( temp )

    for [x, y] in update :
        input[y][x] = 'L'

    return input

def count_occupied( input ) : 
    val = 0

    for y in range( len( input ) ) :
        for x in range( len( input[0] ) ) :
            if input[y][x] == '#' :
                val += 1
    
    return val

def part_one( input ) :

    prev_iter = []

    input = parse( input )

    while prev_iter != input :
        prev_iter = copy.deepcopy( input )
        input = parse( input )
    
    print( "Part one solution: ", count_occupied( input ) )


def sit_part_two( x, y, input ) :
    update       = [] 
    num_occupied = 0

    if input[y][x] == 'L' :
        
                # vertical upwards
        for y_line in range( y - 1, -1, -1 ) : 
            if not can_sit( x, y_line, input ) :
                num_occupied += 1
                break 
            if not is_floor( x, y_line, input ) :
                break

        # vertical downwards 
        for y_line in range( y + 1, len( input ) ) :
            if not can_sit( x, y_line, input ) :
                num_occupied += 1
                break 
            if not is_floor( x, y_line, input ) :
                break

        # horizontal left 
        for x_line in range( x - 1, -1, -1 ) :
            if not can_sit( x_line, y, input ) :
                num_occupied += 1 
                break 
            if not is_floor( x_line, y, input ) :
                break

        # horizontal right 
        for x_line in range( x + 1 , len( input[y] ) ) :
            if not can_sit( x_line, y, input ) :
                num_occupied += 1 
                break 
            if not is_floor( x_line, y, input ) :
                break

        # top left 
        for y_line, x_line in zip( range( y - 1, -1, -1 ), range( x - 1, -1, -1 ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # top right 
        for y_line, x_line in zip( range( y - 1, -1, -1 ), range( x + 1, len( input[y] ) ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # bottom left 
        for y_line, x_line in zip( range( y + 1, len( input ) ), range( x - 1, -1, -1 ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # bottom right 
        for y_line, x_line in zip( range( y + 1, len( input ) ), range( x + 1, len( input[y] ) ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        if num_occupied == 0 :
            update = [x, y]
            
        
    return update 

def remove_part_two( x, y, input ) :
    num_occupied = 0
    update = []

    if input[y][x] == '#' :
        
        # vertical upwards
        for y_line in range( y - 1, -1, -1 ) : 
            if not can_sit( x, y_line, input ) :
                num_occupied += 1
                break 
            if not is_floor( x, y_line, input ) :
                break

        # vertical downwards 
        for y_line in range( y + 1, len( input ) ) :
            if not can_sit( x, y_line, input ) :
                num_occupied += 1
                break 
            if not is_floor( x, y_line, input ) :
                break

        # horizontal left 
        for x_line in range( x - 1, -1, -1 ) :
            if not can_sit( x_line, y, input ) :
                num_occupied += 1 
                break 
            if not is_floor( x_line, y, input ) :
                break

        # horizontal right 
        for x_line in range( x + 1 , len( input[y] ) ) :
            if not can_sit( x_line, y, input ) :
                num_occupied += 1 
                break 
            if not is_floor( x_line, y, input ) :
                break

        # top left 
        for y_line, x_line in zip( range( y - 1, -1, -1 ), range( x - 1, -1, -1 ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # top right 
        for y_line, x_line in zip( range( y - 1, -1, -1 ), range( x + 1, len( input[y] ) ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # bottom left 
        for y_line, x_line in zip( range( y + 1, len( input ) ), range( x - 1, -1, -1 ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        # bottom right 
        for y_line, x_line in zip( range( y + 1, len( input ) ), range( x + 1, len( input[y] ) ) ) :
            if not can_sit( x_line, y_line, input ) :
                num_occupied += 1 
                break
            if not is_floor( x_line, y_line, input ) :
                break

        if num_occupied > 4 :
            update = [x, y]

    return update 
    

def parse_part_two( input ) :
    update = []

    for y in range( len( input ) ) :
        for x in range( len( input[0] ) ) :
            temp = sit_part_two( x, y, input )
            if len( temp ) > 0 :
                update.append( temp )
    
    # update list 
    for [x, y] in update :
        input[y][x] = '#'

    update = []

    for y in range( len( input ) ) :
        for x in range( len( input[0] ) ) :
            temp = remove_part_two( x, y, input )
            if len( temp ) > 0 :
                update.append( temp )

    for [x, y] in update :
        input[y][x] = 'L'

    return input


def part_two( input ) :

    prev_iter = [] 
    input = parse_part_two( input )

    while prev_iter != input :
        prev_iter = copy.deepcopy( input )
        input = parse_part_two( input )

    print( "Part two solution: ", count_occupied( input ) )


def main() :
    a_file   = open( "src/day11/puzzleInput.txt" )
    input    = a_file.read().splitlines()
    input    = [split( val ) for val in input]
    inputTwo = copy.deepcopy( input )
    a_file.close()

    part_one( input )
    part_two( inputTwo )


if __name__ == '__main__' :
    main()