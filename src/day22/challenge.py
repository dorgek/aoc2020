from more_itertools import split_after
import copy
from enum import Enum

class Players( Enum ) :
    PLAYER_ONE = 1
    PLAYER_TWO = 1 


def prepare_data( data_input ) :
    players    = list( split_after( data_input, lambda x: x == '' ) )
    player_one = [int( numeric_string ) for numeric_string in players[0][1:-1]]
    player_two = [int( numeric_string ) for numeric_string in players[1][1:]]

    return player_one, player_two

def game( player_one, player_two ) : 
    player_one_played = player_one.pop(0)
    player_two_played = player_two.pop(0)

    if player_one_played < player_two_played :
        player_two.append( player_two_played )
        player_two.append( player_one_played )
    else :
        player_one.append( player_one_played )
        player_one.append( player_two_played )

def game_two( player_one, player_two, player_one_prev_rounds, player_two_prev_rounds ) : 
    # check if the cards are the same as the previous round if yes, player 1 wins
    for i in range( len( player_one_prev_rounds ) ) :
        if player_one == player_one_prev_rounds[i] and player_two == player_two_prev_rounds[i] :
            player_two.clear()
            return player_one, player_two

    # keep track of played hands this game 
    player_one_prev_rounds.append( copy.deepcopy( player_one ) )
    player_two_prev_rounds.append( copy.deepcopy( player_two ) )

    player_one_played = player_one.pop(0)
    player_two_played = player_two.pop(0)
    player_one_res    = []
    player_two_res    = []
    sub_game          = False

    if player_one_played <= len( player_one ) and player_two_played <= len( player_two ) :
        # playing subgame 
        sub_game = True 
        player_one_sub = copy.deepcopy( player_one[:player_one_played] )
        player_two_sub = copy.deepcopy( player_two[:player_two_played] )

        player_one_prev_rounds_sub = []
        player_two_prev_rounds_sub = []

        while len( player_two_sub ) > 0 and len( player_one_sub ) > 0 :
            player_one_res, player_two_res = game_two( player_one_sub, player_two_sub, player_one_prev_rounds_sub, player_two_prev_rounds_sub )

    
    if ( player_one_played < player_two_played and not sub_game ) or ( sub_game and len( player_one_res ) < len( player_two_res ) ) :
        player_two.append( player_two_played )
        player_two.append( player_one_played )
    else :
        player_one.append( player_one_played )
        player_one.append( player_two_played )

    return player_one, player_two
    


def part_one( player_one, player_two ) :
    while len( player_two ) > 0 and len( player_one ) > 0 :
        game( player_one, player_two )

    if len( player_two ) > 0 :
        winning_player = player_two
    else :
        winning_player = player_one

    index_multiply = list( range( 1, len( winning_player ) + 1 ) )
    score = sum( [a*b for a, b in zip( reversed( winning_player ), index_multiply )] )

    print( "Part one: ", score )

def part_two( player_one, player_two ) :
    player_one_prev_rounds = []
    player_two_prev_rounds = []

    while len( player_two ) > 0 and len( player_one ) > 0 :
        game_two( player_one, player_two, player_one_prev_rounds, player_two_prev_rounds )

    if len( player_two ) > 0 :
        winning_player = player_two
    else :
        winning_player = player_one

    index_multiply = list( range( 1, len( winning_player ) + 1 ) )
    score = sum( [a*b for a, b in zip( reversed( winning_player ), index_multiply )] )

    print( "Part two: ", score )


def main() :
    a_file     = open( "src/day22/puzzleInput.txt" )
    data_input = a_file.read().splitlines()
    a_file.close()

    player_one, player_two = prepare_data( data_input )
    part_one( copy.deepcopy( player_one ), copy.deepcopy( player_two ) )
    part_two( player_one, player_two )


if __name__ == '__main__' :
    main()