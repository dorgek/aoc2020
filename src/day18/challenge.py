from operators import Operators 
from queue import Queue

def _infix_to_posfix( input ) : 
    output = Queue()
    operator_stack = []

    for c in input : 
        if represents_int(c) :
            output.put(int(c))
        elif len( operator_stack ) > 0 :
            # TODO: take into account braces
            # potentially make the algorithm recursive to handle braces and
            # solve this part recursively

            # equal precedence
            output.put(operator_stack.pop())
            operator_stack.append(Operators(c))

        else :
            operator_stack.append(Operators(c))

    for val in operator_stack :
        output.put(val)

    return output

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

def evaluate_equation( eqn ) : 
    
    return _evaluate( _infix_to_posfix( eqn ) )

def part_one() :
    temp = '1+(2*3)+(4*(5+6))'

    print( "Part One: ", evaluate_equation( temp ) )

        

def represents_int(s) :
    try:
        int(s)
        return True 
    except ( ValueError, TypeError ) :
        return False


def main() :
    part_one()
    



if __name__ == '__main__' :
    main()