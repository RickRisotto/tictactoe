#!/usr/bin/env python
# -*- coding: utf-8 -*-


field = {'7': '7' , '8': '8' , '9': '9' ,
            '4': '4' , '5': '5' , '6': '6',
            '1': '1' , '2': '2' , '3': '3' }
            


def printField(*args):
    ''' I ll print the gamefield according to field dict'''
    
    print(field['7'] + '|' + field['8'] + '|' + field['9'])
    print('-+-+-')
    print(field['4'] + '|' + field['5'] + '|' + field['6'])
    print('-+-+-')
    print(field['1'] + '|' + field['2'] + '|' + field['3'])


if __name__ == '__main__':
    print('***Im just collateral module. Start the game with "main" module***')





