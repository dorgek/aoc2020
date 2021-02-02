from direction import Direction
import re 

class Ship : 


    def __init__( self, start_position ) :
        # treat the current position as 0, 0 on a grid
        self._current_position  = start_position
        self._direction_faceing = Direction.E

    def update_position( self, instruction ) :
        dir  = Direction( re.sub( "[^a-zA-Z]+", "", instruction ) )
        dist = re.sub( "[a-zA-Z]+", "", instruction )

        if dir == Direction.L : # ship is turning left
            self._turn_left( int( dist ) )
        elif dir == Direction.R : 
            self._turn_right( int( dist ) )

        # move ship 
        if dir == Direction.F : 
            self._move_ship( self._direction_faceing, int( dist ) )
        else :
            self._move_ship( dir, int( dist ) )

    
    def manhattan_distance( self ) :
        return abs( self._current_position[0] ) + abs( self._current_position[1] )



    def _turn_left( self, deg ) : 
        for x in range( 0, int( deg / 90 ) ) :
            self._turn_left_ninty()

    def _turn_left_ninty( self ) :
        if self._direction_faceing == Direction.N :
            self._direction_faceing = Direction.W 
        elif self._direction_faceing == Direction.W : 
            self._direction_faceing = Direction.S 
        elif self._direction_faceing == Direction.S : 
            self._direction_faceing = Direction.E 
        elif self._direction_faceing == Direction.E :
            self._direction_faceing = Direction.N 

    def _turn_right( self, deg ) :
        for x in range( 0, int( deg / 90 ) ) :
            self._turn_right_ninty()
    
    def _turn_right_ninty( self ) : 
        if self._direction_faceing == Direction.N :
            self._direction_faceing = Direction.E 
        elif self._direction_faceing == Direction.E : 
            self._direction_faceing = Direction.S 
        elif self._direction_faceing == Direction.S :
            self._direction_faceing = Direction.W 
        elif self._direction_faceing == Direction.W :
            self._direction_faceing = Direction.N


    def _move_ship( self, dir, dist ) :
        if dir == Direction.N :
            self._current_position[1] -= dist
        elif dir == Direction.S : 
            self._current_position[1] += dist 
        elif dir == Direction.E : 
            self._current_position[0] += dist 
        elif dir == Direction.W :
            self._current_position[0] -= dist 