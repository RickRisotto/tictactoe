#!/usr/bin/env python
# -*- coding: utf-8 -*-


import data_processing as dp
import game as g
import view as v



def dialog_master():
    ''' I'm responsible for conversation with user'''
    try:
        inpt = input()
        user_input = str(inpt)
    except NameError as ne:
        print('Something went wrong... Think twice before typing: {}'.format(ne))
        return user_input
    else:
        return user_input


  
def choice_checker(inpt):
    ''' I am checking if user's choice is suitable for the gamefield.'''  

    allowed_ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #consider as int
    result = True if inpt in allowed_ints else False
    return result



def dialog():
    ''' I have a conversation with user and pass his/her inputs to
    "data_processing" module, get the result, pass it into the "game" module
    get result from now it and decide if we proceed or the game is over. I check
    if wrong input or the exception occurs also'''


    try:
        user_input = str(dialog_master().upper())
    except AttributeError as er:
        print('Dont feed me with spaces!'.format(er))
    except SyntaxError as sr:
        print('Dont feed me with spaces!'.format(sr))
    except NameError as ne:
        print('Something went wrong... Think twice before typing: {}'.format(ne))
    else:    
        while True:
            if user_input == ('Y'):
                print('ok...')
                print('Enter number corresponding to your choice... type exit to escape while playing')
                v.printField()
                try:
                    inpt = str(dialog_master())
                    choice_ch_result = choice_checker(inpt)
                    if choice_ch_result == True:
                        pass
                    else:
                        print('Type from 1 to 9 inclusively. {} is wrong input'.format(inpt))
                        break
                except SyntaxError as sr:
                    print('Hey fella! Try not to pass this mess into me anymore: {}'.format(sr))
                except NameError as ne:
                    print('Something went wrong... Think twice before typing: {}'.format(ne))
                else:
                    data_writed = dp.result_checker(inpt)
                    res = g.game(data_writed)
                    if res == '0':
                        print(v.printField())
                        print("\nGame Over.\n")
                        break
                    elif res == '1':
                        print(v.printField())
                        print("\nGame Over.\n")
                        print("\nDo you want to play again? (y/n)\n")
                        answ = (dialog_master().upper())
                        if answ == ('Y') or answ == ('y'):
                            for key in v.field.keys():
                                new_game = {key : key}
                                v.field.update(new_game)
                                continue
                        elif answ == ('N') or answ == ('n'):
                            return answ
                    elif res == 'f': #flag if place on the gamefield occupied
                        print('This place has already chosen. Choose another')
                        break
            elif user_input == 'n':
                print('As you wish.')
                break
            elif user_input == 'exit':
                print('As you wish.')
                break
            else:
                print('There is something i cant get properly. Watch your hands!')
                break


if __name__ == '__main__':
    print('***Im just collateral module. Start the game with "main" module***')
          
            
       
    
    
    
