#!/usr/bin/env python
# -*- coding: utf-8 -*-


import view as v


from user_input import *


count = [] # coherently filling to be aware of the game state


def game(game):
    if game != 'f':
        choices = list(game)
        turn = 'X'

        for i in range(10):
            for item in choices:
                if  v.field[item] == item:
                    v.field[item] = turn
                    count.append(item) # filling with every move

                # after five moves we check if there is a winner 
                if len(count) >= 5:
                    if v.field['7'] == v.field['8'] == v.field['9'] != ' ': # the top
                        v.field['7'] = 'w'
                        v.field['8'] = 'o'
                        v.field['9'] = 'n'
                        print(" *** " +turn + " won. ***")                
                        return ('0')
                    elif v.field['4'] == v.field['5'] == v.field['6'] != ' ': # the middle
                        v.field['4'] = 'w'
                        v.field['5'] = 'o'
                        v.field['6'] = 'n'
                        print(" *** " +turn + " won. ***")
                        return ('0') 
                    elif v.field['1'] == v.field['2'] == v.field['3'] != ' ': # the bottom
                        v.field['1'] = 'w'
                        v.field['2'] = 'o'
                        v.field['3'] = 'n'
                        print(" *** " +turn + " won. ***")
                        return ('0') 
                    elif v.field['1'] == v.field['4'] == v.field['7'] != ' ': # down the left side
                        v.field['1'] = 'n'
                        v.field['4'] = 'o'
                        v.field['7'] = 'w'
                        print(" *** " +turn + " won. ***")
                        return ('0') 
                    elif v.field['2'] == v.field['5'] == v.field['8'] != ' ': # down the middle
                        v.field['2'] = 'n'
                        v.field['5'] = 'o'
                        v.field['8'] = 'w'                                    
                        print(" *** " +turn + " won. ***")
                        return ('0') 
                    elif v.field['3'] == v.field['6'] == v.field['9'] != ' ': # down the right side
                        v.field['3'] = 'n'
                        v.field['6'] = 'o'
                        v.field['9'] = 'w'
                        print(" *** " +turn + " won. ***")
                        return ('0') 
                    elif v.field['7'] == v.field['5'] == v.field['3'] != ' ': # diagonal
                        v.field['7'] = 'w'
                        v.field['5'] = 'o'
                        v.field['3'] = 'n'
                    
                                  
                        print(" **** " +turn + " won. ****")
                        return ('0') 
                    elif v.field['1'] == v.field['5'] == v.field['9'] != ' ': # diagonal
                        v.field['1'] = 'w'
                        v.field['5'] = 'o'
                        v.field['9'] = 'n'
                        print(" *** " +turn + " won. ***")
                        return ('0')

                
            
                
                # If we have no winner, we'll declare a 'tie'.
                if len(count) == 8:
                    del count[:] # refresh the list for new game
                    print("Looks like we have a tie here...")
                    return ('1')

                # Switcher from X to zero and back
                if turn =='X':
                    turn = 'O'
                else:
                    turn = 'X'

    else:
        return game # flag in case of place occupied


if __name__ == '__main__':
    print('***Im just collateral module. Start the game with "main" module***')

    
        
            
        
    

        


            
                

          
        
