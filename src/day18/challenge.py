from operators import Operators 
from queue import Queue

def _infix_to_posfix_part_one( input ) : 
    output = Queue()
    operator_stack = []
    bracket_count = 0
    grouped_operators = ''

    for c in input : 
        if represents_int(c) and bracket_count == 0:
            output.put(int(c))
        elif bracket_count > 0 or Operators(c) == Operators.OPEN_BRACKET :
            # push all values grouped together and recursively solve
            grouped_operators += c 

            is_number = represents_int(c)

            if not is_number and Operators(c) == Operators.OPEN_BRACKET :
                bracket_count += 1 
            elif not is_number and Operators(c) == Operators.CLOSE_BRACKET :
                bracket_count -= 1 

                # if last close bracket solve and treat as operator
                if bracket_count == 0 :
                    output.put(evaluate_equation_part_one(grouped_operators[1:-1]))
                    grouped_operators = ''
        
        elif len( operator_stack ) > 0 :
            # equal precedence
            output.put(operator_stack.pop())
            operator_stack.append(Operators(c))

        else :
            operator_stack.append(Operators(c))

    for val in operator_stack[::-1] :
        output.put(val)

    return output

def _infix_to_posfix_part_two( input ) : 
    output = Queue()
    operator_stack = []
    bracket_count = 0
    grouped_operators = ''

    for c in input : 
        if represents_int(c) and bracket_count == 0:
            output.put(int(c))
        elif bracket_count > 0 or Operators(c) == Operators.OPEN_BRACKET :
            # push all values grouped together and recursively solve
            grouped_operators += c 

            is_number = represents_int(c)

            if not is_number and Operators(c) == Operators.OPEN_BRACKET :
                bracket_count += 1 
            elif not is_number and Operators(c) == Operators.CLOSE_BRACKET :
                bracket_count -= 1 

                # if last close bracket solve and treat as operator
                if bracket_count == 0 :
                    output.put(evaluate_equation_part_two(grouped_operators[1:-1]))
                    grouped_operators = ''
        
        elif len( operator_stack ) > 0 :
            # peek at last operator to determine precedence level 
            last_operator = operator_stack[-1]
            current_operator = Operators(c)

            # addition is evaluated before multiplication
            _check_operator( output, operator_stack, current_operator, last_operator )

        else :
            operator_stack.append(Operators(c))

    for val in operator_stack[::-1] :
        output.put(val)

    return output


def _check_operator( output, operator_stack, current_operator, last_operator ) :
    # equal precedence
    if len( operator_stack ) == 0 :
        operator_stack.append(current_operator)
    elif ( current_operator == Operators.PLUS and last_operator == Operators.PLUS ) or ( current_operator == Operators.MULTIPLY and last_operator == Operators.MULTIPLY ) :
        output.put( operator_stack.pop() )
        operator_stack.append( current_operator )
    elif ( current_operator == Operators.PLUS ) : # higher precedence 
        operator_stack.append( current_operator )
    elif ( current_operator == Operators.MULTIPLY ) : # lower precedence 
        output.put( operator_stack.pop() )

        if len( operator_stack ) > 0 :
            new_last_operator = operator_stack[-1]
            _check_operator( output, operator_stack, current_operator, new_last_operator )
        else :
            operator_stack.append( current_operator )

def _evaluate( posfix ) : 
    stack = []

    for q in posfix.queue : 
        if represents_int(q) :
            stack.append(q) 
        else :
            a = stack.pop()
            b = stack.pop() 
            c = 0

            if q == Operators.PLUS :
                c = a + b 
            elif q == Operators.MINUS : 
                c = a - b 
            elif q == Operators.MULTIPLY :
                c = a * b 
            elif q == Operators.DIVIDE :
                c = a / b 

            stack.append(c)

    return stack[0]

def evaluate_equation_part_one( eqn ) : 
    return _evaluate( _infix_to_posfix_part_one( eqn ) )


def evaluate_equation_part_two( eqn ) : 
    return _evaluate( _infix_to_posfix_part_two( eqn ) )

def part_one( data_input ) :
    eval_exp = []

    for equation in data_input :
        eval_exp.append( evaluate_equation_part_one( equation ) )

    print( "Part One: ", sum( eval_exp ) )


def part_two( data_input ) :
    eval_exp = []

    for equation in data_input :
        eval_exp.append( evaluate_equation_part_two( equation ) )

    print( "Part two: ", sum( eval_exp ) )

def represents_int(s) :
    try:
        int(s)
        return True 
    except ( ValueError, TypeError ) :
        return False


def main() :
    a_file      = open( "src/day18/puzzleInput.txt" )
    data_input  = [c.replace( " ", "" ) for c in a_file.read().splitlines()]
    a_file.close()

    part_one( data_input )
    part_two( data_input )
    



if __name__ == '__main__' :
    main()