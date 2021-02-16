import numpy as np



class ConwaysGame3D : 

    def __init__( self, initial_state ) :
        """
            initialise the map for the conways game of life to 3D. note that the size
            of the space is infinite
        """
        self._map = np.array( initial_state, copy=True )
        self._map = np.pad( initial_state, (50, 50), 'constant' )
        self._map = np.reshape( self._map, ( 1, 108, 108 ) )

        temp = self._map.shape

        # zeros = np.zeros( self._map.shape )
        # zerosTwo = np.zeros( self._map.shape )
        # zerosthree = np.zeros( self._map.shape )
        # temp  = np.zeros( self._map.shape )
        
        for i in range( 0, 25 ) :
            self._map = np.insert( self._map, 0, np.zeros( temp ), axis=0 )
            self._map = np.append( self._map, np.zeros( temp ), axis=0 )

        self._size = self._map.shape
        

    
    def update( self ) :
        updates = []

        for z in range( 1, self._size[0] - 1 ) :
            # z axis 

            for x in range( 1, self._size[1] - 1 ) :
                # x axis 

                for y in range( 1, self._size[2] - 1 ) :
                    # y axis 
                    updates.append( [self._next_state(z, x, y), z, x, y])

        
        # update the map 
        for update in updates :
            self._map[update[1], update[2], update[3]] = update[0]
            
            


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
        neighbours.append([z-1, x, y])
        neighbours.append([z-1, x-1, y])
        neighbours.append([z-1, x, y-1])
        neighbours.append([z-1, x-1, y-1])
        neighbours.append([z-1, x+1, y])
        neighbours.append([z-1, x, y+1])
        neighbours.append([z-1, x+1, y+1])
        neighbours.append([z-1, x+1, y-1])
        neighbours.append([z-1, x-1, y+1])
        neighbours.append([z, x-1, y])
        neighbours.append([z, x, y-1])
        neighbours.append([z, x-1, y-1])
        neighbours.append([z, x+1, y])
        neighbours.append([z, x, y+1])
        neighbours.append([z, x+1, y+1])
        neighbours.append([z, x+1, y-1])
        neighbours.append([z, x-1, y+1])
        neighbours.append([z+1, x, y])
        neighbours.append([z+1, x-1, y])
        neighbours.append([z+1, x, y-1])
        neighbours.append([z+1, x-1, y-1])
        neighbours.append([z+1, x+1, y])
        neighbours.append([z+1, x, y+1])
        neighbours.append([z+1, x+1, y+1])
        neighbours.append([z+1, x+1, y-1])
        neighbours.append([z+1, x-1, y+1])

        active = 0
        
        for neighbour_z, neighbour_x, neighbour_y in neighbours : 
            active += self._map[neighbour_z,neighbour_x,neighbour_y]

        # print( active )

        if ( self._map[z,x,y] == 1 and ( active == 2 or active == 3 ) ) or ( self._map[z,x,y] == 0 and active == 3 ) :
            # print( 'test')
            return 1
        else  :
            return 0

                

