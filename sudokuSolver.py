# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:57:21 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

import numpy as np
import sys
import sudokuLib as sdk


#Always parsing the user input
#---------------------#

if len(sys.argv) != 3:
    print('Invalid input. Usage: python sudoku_solver.py CSV_INPUT_PATH CSV_OUTPUT_PATH')
    sdk.pause()
    sys.exit(1)

csv_input_path = sys.argv[1]
csv_output_path = sys.argv[2] 


try:
    matrix = np.loadtxt(csv_input_path, delimiter=',').astype('int');
except IOError as e:
    print('There was an IO error trying to read in path: ' + csv_input_path + \
    '\nThe system returns: ' + e.strerror)
    sdk.pause()
    sys.exit(1)

if matrix.shape != (9,9) or\
    matrix.min() < 0 or \
    matrix.max() > 9:
        
    print('Sorry, this sudoku solver only works with the standard sudoku version' \
    + ' of a 9x9 grid with values between 1 and 9, using 0 as a blank box')
    sdk.pause()
    sys.exit(1)

#---------------------#


print('\nThis is the given sudoku:\n\n')
sdk.sudokuPrinter(matrix)

print('Please, wait while solving\n...\n')



try:
    sdk.sudokuSolver(matrix)
except:
    e = sys.exc_info()[0]
    print("The solver has unexpectedly crashed. \nBecause it uses recursive functions, \
    the most probable reason is that the sudoku level was too hard and this process \
    was run out of memory. We suggest to try with an easier sudoku or run this software \
    in a machine with more RAM.\n\n The system returns the following message:\n" \
    + e)
    sdk.pause()
    sys.exit(1)     
    
    
    
print('Solving process already done')
sdk.pause()

print('This is the solved sudoku:\n\n')
sdk.sudokuPrinter(matrix)
sdk.pause()

print('Saving in ' + csv_output_path + ' ...\n')



try:
    np.savetxt(csv_output_path, matrix, fmt='%d', delimiter=',')
except IOError as e:
    print('There was an IO error trying to write in path: ' + csv_output_path + \
    '\nThe system returns: ' + e.strerror)
    sdk.pause()
    sys.exit(1)
    
    
print('Complete')