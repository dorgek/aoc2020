import re 


class FieldRange :

    def __init__( self ) : 
        self._range_values = []

    def set_range_values( self, ranges ) :
        for range in ranges : 
            temp = []

            for num in re.findall( '[0-9]+', range ) :
                temp.append( int( num ) )

            self._range_values.append( temp )

    
    def is_in_range( self, val ) : 
        for range_value in self._range_values :
            if val < range_value[0] :
                # check to see if can exit early from loop
                return False 
            elif val >= range_value[0] and val <= range_value[1] :
                return True

        return False 