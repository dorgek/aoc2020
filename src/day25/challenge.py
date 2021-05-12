import math


def decode( public_door_key, subject_number ) :

    init_value = 1
    i_door = 0

    while public_door_key != init_value :
        init_value = ( subject_number * init_value ) %  20201227

        i_door += 1

    return i_door


def main() :

    door_public_key = 4206373
    card_public_key = 15113849

    door_loop = decode( door_public_key, 7 )

    encryption_key = pow( card_public_key, door_loop, 20201227 )

    print( "Encryption key: ", encryption_key )




if __name__ == '__main__' :
    main()