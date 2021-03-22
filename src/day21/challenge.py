import numpy as np 
import re 

def callculate_allergens( food_allergens ) :
    allergy_list    = {}
    products_list   = []
    solved_products = []

    for food_allergen in food_allergens : 
        allergens = re.findall( "(?<=contains)[\\sa-zA-Z,]+", food_allergen )[0].replace( " ", "")
        products  = re.findall( "[a-zA-Z\\s]+(?=\()", food_allergen )[0].split()

        products_list.extend( products )

        # check if any of these products already have a value assigned to it and then
        # if so remove from list of available products 
        products = [i for i in products if i not in solved_products]

        for allergy in allergens.split( "," ) :
            
            if allergy not in allergy_list :
                allergy_list[allergy] = products

            else :
                # compare current products against whats available and remove
                # those that don't appear 
                current_allergens = allergy_list[allergy]
                
                if len( current_allergens ) != 1 :
                    temp = list( set( current_allergens ) & set( products ) )
                    allergy_list[allergy] = temp

                    # check if one value is available then this is the value of the allergy
                    # update the dictionary to list possible values 
                    if len( temp ) == 1 : 
                        value = temp[0]
                        
                        remove_allergen( allergy_list, allergy, value, solved_products )
                        solved_products.append( value )


    # find all items that is not an allergen
    allergy_values = []

    for k in sorted( allergy_list ) :
        allergy_values.append( allergy_list[k][0] )

    no_allergens = np.setdiff1d( products_list, allergy_values )

    count = 0

    for no_allergen in no_allergens :
        count += products_list.count( no_allergen )

    print( "Part One: ", count )
    print( "Part Two: ", ",".join( allergy_values ) )



def remove_allergen( allergy_list, allergy, product, solved_products ) : 
    remove_allergens = {}

    for k in allergy_list :
        if k != allergy and product in allergy_list[k] :
            temp = allergy_list[k]
            temp.remove( product )

            # determine if new value also needs to be removed 
            if len( allergy_list[k] ) == 1 :
                remove_allergens[k] = allergy_list[k][0]
                solved_products.append( allergy_list[k][0] )

    # remove used allergens 
    for k in remove_allergens :
        remove_allergen( allergy_list, k, allergy_list[k][0], solved_products )


def main() : 
    a_file      = open( "src/day21/puzzleInput.txt" )
    data_input  = a_file.read().splitlines()
    a_file.close()

    callculate_allergens( data_input )


if __name__ == '__main__' :
    main()