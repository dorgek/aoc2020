import numpy as np
from itertools import product


class ConwaysGame3D : 

    def __init__( self, initial_state ) :
        """
            initialise the map for the conways game of life to 3D. note that the size
            of the space is infinite
        """
        self._map = np.array( initial_state, copy=True )
        self._map = np.pad( initial_state, 1, 'constant' )
        self._map = np.reshape( self._map, np.insert( self._map.shape, 0, 1 ) )

        temp = self._map.shape
        
        
        self._map = np.insert( self._map, 0, np.zeros( temp ), axis=0 )
        self._map = np.append( self._map, np.zeros( temp ), axis=0 )

        self._map = np.pad( self._map, 1, 'constant' )

        self._size = self._map.shape
        

    
    def update( self ) :
        updates = []
        pad = False 

        for z in range( 1, self._size[0] - 1 ) :
            # z axis 

            for x in range( 1, self._size[1] - 1 ) :
                # x axis 

                for y in range( 1, self._size[2] - 1 ) :
                    # y axis 
                    next_state = self._next_state( z, x, y )
                    updates.append( [next_state, z, x, y])

                    if next_state == 1 and ( ( z == 1 or z == self._size[0] - 2 ) or ( x == 1 or x == self._size[1] - 2 ) or ( y == 1 or y == self._size[2] - 2 ) ) :
                        pad = True 

        # update the map 
        for update in updates :
            self._map[update[1], update[2], update[3]] = update[0]
        
        if pad :
            self._map = np.pad( self._map, 1, 'constant' )
            self._size = self._map.shape
            
            


    def print_map( self ) :
        print( self._map )

    def count_active( self ) :
        return np.count_nonzero( self._map == 1 )


    def _next_state( self, z, x, y ) : 
        """
            check the neighbours of the current position to determine if 
            the next state should be active or inactive
        """
        neighbours = []

        for z_i in range( z-1, z+2 ) :
            for x_i in range( x-1, x+2 ) :
                for y_i in range( y-1, y+2 ) :
                    if z_i != z or x_i != x or y_i != y :
                        neighbours.append( [z_i, x_i, y_i] )

        active = 0
        
        for neighbour_z, neighbour_x, neighbour_y in neighbours : 
            active += self._map[neighbour_z,neighbour_x,neighbour_y]

        # print( active )

        if ( self._map[z,x,y] == 1 and ( active == 2 or active == 3 ) ) or ( self._map[z,x,y] == 0 and active == 3 ) :
            # print( 'test')
            return 1
        else  :
            return 0

                

