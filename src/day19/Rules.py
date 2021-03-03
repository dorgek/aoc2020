from more_itertools import split_after

class Rules() :

    def __init__( self ) : 
        self._rule_dictionary = {}
        self.glb_idx = 0

    def process_rule( self, idx, vals ) :
        list_vals = list( split_after( vals, lambda x: x == '|') )

        for list_val in list_vals : 
            while " " in list_val :
                list_val.remove( " " )
            while "|" in list_val :
                list_val.remove( "|" )

        self._rule_dictionary[idx] = list_vals

    def validate_sequence( self, sequence ) : 
        print('help')
        checked = self._validate_rule_seq( self._rule_dictionary[0][0], sequence, 0 )
        

        if checked > 0 and len( sequence ) == checked :
            return True 
        else :
            return False 

        


    
    def _validate_rule_seq( self, rule_seq, sequence, seq_idx ) : 
        # self.glb_idx += 1
        # print( self.glb_idx )
        
        for next_rule_idx in rule_seq :
            next_val = self._rule_dictionary[int(next_rule_idx)]

            if next_val[0][0].isalpha() :
                # print(sequence[seq_idx + idx], ' ', seq_idx + idx, ' ', next_val[0][0] )
                if sequence[seq_idx] != next_val[0][0] :
                    return -1 
                else : 
                    seq_idx += 1
            else : 
                # another rule set to evaluate (unknown number of variations)
                matchesFound = False 

                for next_rule_seqs in next_val :
                    # print( next_rule_seqs )
                    res = self._validate_rule_seq( next_rule_seqs, sequence, seq_idx )
                    if res != -1 :
                        matchesFound = True 
                        seq_idx = res 
                        # print( next_rule_idx, ' ', next_rule_seqs )
                        break 
                    else :
                        continue

                if matchesFound == False :
                    return -1 
                
        return seq_idx  

        
            
