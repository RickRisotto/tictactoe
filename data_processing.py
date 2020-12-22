#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


winner_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_battlefield_state(control_data):
    '''I ll take the user input and remove str corresponding to it
       from winner_state'''

    while not None:
        for cd in control_data:
            for w in winner_state:
                    if cd == w:
                        winner_state.remove(w)
                        return w
                
                
def check_state(control_data):
    '''I ll take mashine input and remove str corresponding to it
       from winner_state'''

    while not None:
        for cd in control_data:
            for w in winner_state:
                    if cd == w:
                        winner_state.remove(w)
                        return w


def machine_step(ws):
    '''I am randomly choosing item from winner_state'''

    result = (random.choice(ws))
    return result


def machine_write(winner_state):
    '''I ll take machine choice, pass it into check_state func, return it'''

    machine = machine_step(winner_state)
    machine_res = check_state(machine)
    return machine_res


def check(lst):
    ''' if 8 items was deleted from winner_state, i update the list'''

    if len(lst) == 1:
        del winner_state[:]
        update =['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for item in update:
            winner_state.append(item)


def compare(l):
    ''' If l not in winner_state, place already chosen'''
    result = True if l in winner_state else False
    return result


def result_checker(item):
    ''' I ll get user input, and return machine choice, user choice'''

    if item:
        comp = compare(item)
        while comp == True:
            result = check_battlefield_state(item)
            if result:
                res = machine_write(winner_state)
                check(winner_state)
                return result, res
        else:
            f = 'f' # flag if place chosen
            return f


if __name__ == '__main__':
    print('***Im just collateral module. Start the game with "main" module***')

     
   
   
    




        
    

        
    
            
                
        
        
    
            
            

