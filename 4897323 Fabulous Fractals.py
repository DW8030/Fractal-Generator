# -*- coding: utf-8 -*-
"""
@author: Derk Wiersma s4897323

This program can also be found my GitHub page:
    https://github.com/DW8030/Fractal-Generator
"""

import turtle

#speed up cursor
turtle.speed(0)
#relocate cursor at start
turtle.penup()
turtle.goto(0, -380)
#this value might need to change based on the screen resolution
turtle.pendown()
#turtle.penup() #this is recommended when running fractal2

      
def fractal(lvl, function, lst):
    """
    Generates a list with information about how the fractal should look like
    by using a starting list and a function that is called repeatedly

    Parameters
    ----------
    lvl : int
        the zoom level, how many times the function has to be repeated.
    function : function
        the name of the function to be used.
    lst : list
        contains the initial data.

    Returns
    -------
    lst : list
        contains the final data.

    """
    for i in range(lvl):
        #iterates the fuction for each zoom level
        lst = function(lst)
        #updates the list according to the function
    return lst
             
       
def show_fractal(lvl, function, lst, left_length, right_length,
                 left_angle, right_angle):
    """
    Draws the fractal using turtle

    Parameters
    ----------
    lvl : int
        'zoom level' of the fractal.
    function : function
        the fuction that generates the data.
    lst : list
        DESCRIPTION.
    left_length : int
        the length of the parts drawn by turtle after turning left.
    right_length : int
        the length of the parts drawn by turtle after turning right.    
    left_angle : int
        the angle by which the cursor has to turn left.
    right_angle : int
        the angle by which the cursor has to turn right.
    Returns
    -------
    The fractal is drawn by turtle

    """
    lst2 = ['+'] + fractal(lvl, function, lst)
    for item in lst2:
        if item == '+':
            turtle.left(left_angle)
            turtle.forward(left_length)
        if item == '-':
            turtle.right(right_angle)
            turtle.forward(right_length)

def function(lst):
    """
    Takes in list and generates a new one based on the values in it.
    This function is called in the loop of fractal(lvl, function, lst).

    Parameters
    ----------
    lst : list
        contains information about how the fractal should look like.

    Returns
    -------
    new_list : list
        contains information about how the fractal should look like.

    """
    new_list = []
    #creates new list
    for item in lst: 
        #looks at every item in the list and extends the new list
        #according to the rules below
        if item == '+':
            new_list.append('+')
        if item == '-':
            new_list.append('-')
        if item == 'a':
            new_list.extend(['b', '-', 'a', '-', 'b'])
        if item == 'b':
            new_list.extend(['a', '+', 'b', '+', 'a'])
    return new_list
      
def fractal2(length, lvl, n, go_back, extra_angle, angle_multiplier):
    """
    Generates a fractal according to parameters length, lvl, n, and draws
    it with help of turtle

    Parameters
    ----------
    length : int
        the length of the lines between points on the points in the drawing
        (set it high enough so the graph doesn't look too cramped).
    lvl : int
        the 'level' of the fractal, this is how many times it will repeat 
        itself.
    n : int
        the number of columns of the polygon.
    extra_angle: boolean
        wether the cursor should turn an additional time
    go_back : boolean
        whether the cursor should move back
    angle_multiplier : float or int
        additional multiplier for angle  

    Returns
    -------
    Draws fractal

    """
    angle = 360 / n * angle_multiplier
    #if lvl > 1: dot()
    #prints a dot on the places where it starts a new zoom level
    if lvl == 0:
        turtle.dot() 
    #draw a dot when it has reached deepest zoom level
    else:
       for i in range(n):
          #repeats the process below n times, so the cursor rototates 
          #and all corners are drawn
          turtle.forward(length)
          #moves cursor forward by length
          if extra_angle == True:
              turtle.left(angle)
          #turns around by angle    
          fractal2(length/2, lvl -1, n, go_back, extra_angle, angle_multiplier)  
          #calls itself to go a level deeper in the fractal
          if go_back == True:
             turtle.backward(length)
          #moves cursor back to center of sub-polygon to draw the other corners
          turtle.left(angle)
          #turns around by angle
       

#calls function with example values for parameters   
if __name__ == '__main__': 
#makes sure function is run as script instead of being imported from elsewhere
    show_fractal(8, function, ['a'], 2, 2, 60, 60) 
   # fractal2(100, 5, 3, True, True, 1) #another Sierpinski Triangle
    #calls function with some example values