from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 255 ]
stack = []
temp = new_matrix()
ident(temp)
stack.append(temp)

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', stack, screen, color )
