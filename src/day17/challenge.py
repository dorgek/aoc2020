from ConwaysGame3D import ConwaysGame3D
import numpy as np


def part_one( initial_state ) :
    game = ConwaysGame3D( initial_state )

    for i in range( 0, 6 ) :
        print( i )
        game.update()

    print( "Part One: ", game.count_active() )



def main() :
    a_file      = open( "src/day17/puzzleInput.txt" )
    data_input  = a_file.read() # "\n".join( [ s for s in a_file.read().splitlines() if s]).splitlines()
    a_file.close()

    temp = data_input.replace( '.', "0 " )
    temp = temp.replace( '#', "1 " )
    temp = temp.replace( '\n', ';' )

    initial_state = np.matrix(temp)

    part_one( initial_state )
    



if __name__ == '__main__' :
    main()