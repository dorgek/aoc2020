class Node : 
    def __init__( self, data ) :
        self._data = data 
        self._next = None
        self._prev = None

class DoublyLinkedList :
    def __init__( self ) :
        self._head = None 
        self._tail = None 
        self._dictionary_access = {}
        self._min_val = 1000
        self._max_val = -1 

    def push_back( self, data ) : 
        new_node = Node( data ) 
        new_node._prev = self._tail

        self._min_val = data if data < self._min_val else self._min_val
        self._max_val = data if data > self._max_val else self._max_val

        self._dictionary_access[data] = new_node

        if self._tail == None :
            self._head = new_node
            self._tail = new_node
        
        else :
            self._tail._next = new_node
            self._tail       = new_node

    def get_dictionary_access( self ) :
        return self._dictionary_access

def create_data_structure( cups ) :

    linked_list = DoublyLinkedList()

    # generate doubly linked list
    for cup in cups :
        linked_list.push_back( cup )

    return linked_list

def print_part_one( linked_list ) :
    current_node = linked_list._head 
    res = ""

    while current_node != None :
        res += str( current_node._data )
        current_node = current_node._next

    print( "Part One: ", res[1:] )

def move( linked_list, dictionary, n ) : 
    position_found = False 

    # get the current cup 
    # print(n)
    current_cup = dictionary[n]

    # get the next three cups to update 
    first_cup  = _get_next_cup( current_cup, linked_list )
    second_cup = _get_next_cup( first_cup, linked_list )
    third_cup  = _get_next_cup( second_cup, linked_list )

    picked_up_cups = [first_cup._data, second_cup._data, third_cup._data]

    current_search = n - 1

    # find new position
    while not position_found : 
        if current_search in dictionary and current_search not in picked_up_cups :
            position_found = True
            tail_node = False  

            destination_node = dictionary[current_search]

            if current_cup._next == None :
                tail_node = True 

            # update positions 
            current_cup._next = third_cup._next
            first_cup._prev = destination_node
            third_cup._next = destination_node._next 
            destination_node._next = first_cup
            destination_node._prev = first_cup._prev if destination_node._prev != None else None

            if tail_node :
                destination_node._next = None 

        else :
            current_search -= 1 

            if current_search < linked_list._min_val :
                current_search = linked_list._max_val

    next_node = dictionary[n]._next._data if dictionary[n]._next != None else linked_list._head._data

    return next_node

def _get_next_cup( node, linked_list ) :
    if node._next == None :
        return linked_list._head 
    else :
        return node._next 

def main() :
    cup_list = "167248359";
    cups     = list( map( int, cup_list )  )

    linked_list = create_data_structure( cups )

    current_cup = cups[0]

    # Part One
    for _ in range( 100 ) : 
        current_cup = move( linked_list, linked_list.get_dictionary_access(), current_cup )

    lookup = linked_list.get_dictionary_access()[1]

    print_part_one( linked_list )

    # Part Two
    cups = list( map( int, cup_list )  )
    cups.extend( list( range( max( cups ) + 1, 1000001 ) ) )

    linked_list = create_data_structure( cups )

    current_cup = cups[0]

    for _ in range( 10000000 ) : 
        current_cup = move( linked_list, linked_list.get_dictionary_access(), current_cup )

    lookup = linked_list.get_dictionary_access()[1]

    print( "Part two: ", lookup._next._data * lookup._next._next._data )




if __name__ == '__main__' :
    main()