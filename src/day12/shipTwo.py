from direction import Direction
import re 

class ShipTwo : 


    def __init__( self, start_position, way_point_position ) :
        # treat the current position as 0, 0 on a grid
        self._current_position   = start_position
        self._direction_faceing  = Direction.E
        self._way_point_position = way_point_position # relative to ship

    def update_position( self, instruction ) :
        """
            Update the position of the ship / waypoint based on the instruction passed through
        """
        dir  = Direction( re.sub( "[^a-zA-Z]+", "", instruction ) )
        dist = re.sub( "[a-zA-Z]+", "", instruction )

        # if left or right then rotate waypoint w.r.t the ship
        if dir == Direction.L : 
            self._turn_left( int( dist ) )
        elif dir == Direction.R : 
            self._turn_right( int( dist ) )

        if dir == Direction.F : 
            self._move_ship( int( dist ) )
        else : 
            self._move_waypoint( dir, int( dist ) )

    
    def manhattan_distance( self ) :
        return abs( self._current_position[0] ) + abs( self._current_position[1] )


    def _update_waypoint( self, dir, dist ) :
        """
            Update the waypoint position relative to the ship
        """
        if dir == Direction.N :
            self._way_point_position[1] -= dist
        elif dir == Direction.S : 
            self._way_point_position[1] += dist 
        elif dir == Direction.E : 
            self._way_point_position[0] += dist 
        elif dir == Direction.W :
            self._way_point_position[0] -= dist 

    def _turn_left( self, deg ) : 
        """
            Update the waypoint to rotate counter-clockwise 
        """
        x = self._way_point_position[0]
        y = self._way_point_position[1]

        if deg == 90 :
            self._way_point_position[0] = y
            self._way_point_position[1] = -1 * x
        elif deg == 180 : 
            self._way_point_position[0] = -1 * x
            self._way_point_position[1] = -1 * y
        elif deg == 270 :
            self._way_point_position[0] = -1 * y 
            self._way_point_position[1] = x

    def _turn_right( self, deg ) :
        """
            Update the waypoint to rotate clockwise 
        """
        x = self._way_point_position[0]
        y = self._way_point_position[1]

        if deg == 90 :
            self._way_point_position[0] = -1 * y 
            self._way_point_position[1] = x
        elif deg == 180 : 
            self._way_point_position[0] = -1 * x
            self._way_point_position[1] = -1 * y
        elif deg == 270 :
            self._way_point_position[0] = y
            self._way_point_position[1] = -1 * x
    
    def _turn_right_ninty( self ) : 
        self._way_point_position[1] = -1 * self._way_point_position[1]

    
    def _move_waypoint( self, dir, dist ) : 
        if dir == Direction.N :
            self._way_point_position[1] -= dist
        elif dir == Direction.S : 
            self._way_point_position[1] += dist 
        elif dir == Direction.E : 
            self._way_point_position[0] += dist 
        elif dir == Direction.W :
            self._way_point_position[0] -= dist 


    def _move_ship( self, dist ) :
        """
            The ship will only move forward if F is passed through, and it moves towards
            the way point by x times
        """
        self._current_position[0] += dist * self._way_point_position[0]
        self._current_position[1] += dist * self._way_point_position[1]
        