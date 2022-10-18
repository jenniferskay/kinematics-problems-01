'''
kayHomogeneousTransformations.py

Jennifer S. Kay, kay@rowan.edu
Version 2022-02-01

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 

**** IMPORTANT NOTE - THIS CODE MAY *NOT* BE SHARED ON COMMERCIAL WEBSITES THAT CHARGE USERS FOR CONTENT ****

So, for example, it would be a breach of this license to post this code on chegg.com 
Please see: http://creativecommons.org/licenses/by-nc-sa/4.0/  for the nitty gritty details 

'''

import numpy as np
import math
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)}) 


#----------------------- makeTransform --------------------------------
# Create a 4x4 homogeneous transform (represented as a 4x4 numpy matrix) 
# 
# Input arguments: 4 tuples of length 3
# Use these arguments as column vectors and filling in the 0,0,0,1 for the 
# last row
#
def makeTransform(xDirection, yDirection, zDirection, originLocation):
    assert isinstance(originLocation, tuple), "Arguments to makeTransform must be tuples"
    assert isinstance(xDirection, tuple), "Arguments to makeTransform must be tuples"
    assert isinstance(yDirection, tuple), "Arguments to makeTransform must be tuples"
    assert isinstance(zDirection, tuple), "Arguments to makeTransform must be tuples"
    assert len(xDirection) == 3, "Args to makeTransform must be tuples of len==3"
    assert len(yDirection) == 3, "Args to makeTransform must be tuples of len==3"
    assert len(zDirection) == 3, "Args to makeTransform must be tuples of len==3"
    assert len(originLocation) == 3, "Args to makeTransform must be tuples of len==3"
     
    x = np.append(np.array(xDirection), 0)
    y = np.append(np.array(yDirection), 0)  
    z = np.append(np.array(zDirection), 0)
    origin = np.append(np.array(originLocation), 1)
       
    t= np.column_stack((x,y,z,origin))
    return t

#----------------------- identityTransform --------------------------------
# A quick way to make a 4x4 identity matrix
#
def identityTransform():
    return np.identity(4)
    
# -------------------- makePoint ------------------------------------------
# Take the x, y, z values (as ints or floats) and return a vertical 4x1 vector
# (with 1 as the bottom value, of course)
#
def makePoint(a,b,c):
    assert isinstance(a, (int,float)), "Arguments to Translate must be ints or floats"
    assert isinstance(b, (int,float)), "Arguments to Translate must be ints or floats"
    assert isinstance(c, (int,float)), "Arguments to Translate must be ints or floats"
    x = np.array((a,b,c,1))
    colVector = x[:,np.newaxis]
    return colVector

# --------------------- doTrans ---------------------------------------
# Unfortunately, the convention is that the homogeneous transformation 
# operators that we use are identified by an uppercase first letter, but 
# python convention is that I should start methods with a lowercase first
# letter, and thus we have an awkward name ...
#
# This method takes as input three ints or floats u, v, and w which represent
# the x,y,z values and returns the corresponding 4x4 homogenious transformation matrix.
def doTrans(u,v,w):
    assert isinstance(u, (int,float)), "Arguments to Translate must be ints or floats"
    assert isinstance(v, (int,float)), "Arguments to Translate must be ints or floats"
    assert isinstance(w, (int,float)), "Arguments to Translate must be ints or floats"
    t = np.identity(4)
    t[0,3]=u
    t[1,3]=v
    t[2,3]=w
    return t
    
# A pile of rotation matrices, for your convenience offered in radians and degrees 
# All of them, of course, return a 4x4 rotation matrix
def radiansRotX(rad):
    assert isinstance(rad, (int,float)), "Argument to degreesRotX must be int or float"
    x = (1,0,0)
    y = (0, math.cos(rad), math.sin(rad))
    z = (0, -1*math.sin(rad), math.cos(rad))
    t = (0,0,0)
    return makeTransform(x,y,z,t)
     

def degreesRotX(deg):
    assert isinstance(deg, (int,float)), "Argument to degreesRotX must be int or float"
    rad = math.radians(deg)
    return radiansRotX(rad)


def radiansRotY(rad):
    assert isinstance(rad, (int,float)), "Argument to degreesRotX must be int or float"
    x = (math.cos(rad), 0, -1*math.sin(rad))
    y = (0,1,0)
    z = (math.sin(rad), 0, math.cos(rad))
    t = (0,0,0)
    return makeTransform(x,y,z,t)
       

def degreesRotY(deg):
    assert isinstance(deg, (int,float)), "Argument to degreesRotX must be int or float"
    rad = math.radians(deg)
    return radiansRotY(rad)
    


def radiansRotZ(rad):
#    assert isinstance(rad, (int,float)), "Argument to degreesRotX must be int or float"
    x = (math.cos(rad), math.sin(rad),0)
    y = (-1*math.sin(rad), math.cos(rad), 0)
    z = (0,0,1)
    t = (0,0,0)
    return makeTransform(x,y,z,t)
       

def degreesRotZ(deg):
    assert isinstance(deg, (int,float)), "Argument to degreesRotX must be int or float"
    rad = math.radians(deg)
    return radiansRotZ(rad)
    



