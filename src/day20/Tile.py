import numpy as np


class Tile : 

    def __init__( self, tile, tile_num, tile_size ) :
        self._tile        = np.reshape( np.fromstring( tile, sep=' ', dtype=int ), tile_size )
        self._tile_num    = tile_num 
        self._grid_loc    = []

    
    def match_tile( self, tile ) :
        """
            Compare against the tile to determine if they match against each other

            Returns a number indicating the edge of the square that the 
            match occurred at: 
                0 = left
                1 = top 
                2 = right
                3 = bottom

            Returns -1 if no match is found
        """

        # compare rotation of tiles 
        edge_num = self._compare_rotation( tile, tile.get_tile() )
        if  edge_num != -1 : 
            return edge_num

        # flip tile and check if tile then matches
        
        # flip horizontally 
        flip_horiz = np.flip( tile.get_tile(), axis=1 )
        edge_num = self._compare_rotation( tile, flip_horiz )
        if  edge_num != -1 : 
            return edge_num

        # flip vertically
        flip_vert = np.flip( tile.get_tile(), axis=0 )
        edge_num = self._compare_rotation( tile, flip_vert )
        if  edge_num != -1 : 
            return edge_num
        

        # no match is found 
        return -1 

    def _compare_rotation( self, tile, tile_object ) : 
        """
            compare all edges against the required edges of the tile
            to determine if any of the tiles match

            Returns a number indicating the edge of the square that the 
            match occurred at: 
                0 = left
                1 = top 
                2 = right
                3 = bottom

            Returns -1 if no match is found
        """
        match_tile_copy = np.copy( tile_object )

        for i in range( 0, 4 ) : 
            edge_compare = self._get_tile( self._tile, i )
            
            for j in range( 0, 4 ) :
                match_tile_copy = np.rot90( match_tile_copy )
                match_edge_copy = self._get_tile( match_tile_copy, ( ( i + 2 ) % 4 ) )

                # compare the top edge to see if they match 
                if np.array_equal( edge_compare, match_edge_copy ) : 
                    # match is found set the new rotation of both objects
                    tile.set_tile( match_tile_copy )
                    
                    return i

        return -1
                

    def get_tile( self ) :
        return self._tile

    def set_tile( self, tile ) :
        self._tile = tile

    def set_grid_location( self, x, y ) :
        self._grid_loc.append( x )
        self._grid_loc.append( y )

    def get_grid_location( self ) :
        return self._grid_loc

    def get_tile_num( self ) :
        return self._tile_num

    def get_tile_no_boarder( self ) : 
        return self._tile[1:-1,1:-1]

    def _get_tile( self, tile, i ) :
        edge_compare = []

        if i == 0 : 
            # check left edge 
            edge_compare = tile[:,0]
        elif i == 1 :
            # check top edge 
            edge_compare = tile[0,:]
        elif i == 2 :
            # check right edge 
            edge_compare = tile[:,-1]
        elif i == 3 :
            # check bottom edge 
            edge_compare = tile[-1,:]

        return edge_compare