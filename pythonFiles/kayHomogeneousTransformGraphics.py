'''
kayHomogeneousTransformGraphics.py

Jennifer S. Kay, kay@rowan.edu
Version 2022-02-01

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 

**** IMPORTANT NOTE - THIS CODE MAY *NOT* BE SHARED ON COMMERCIAL WEBSITES THAT CHARGE USERS FOR CONTENT ****

So, for example, it would be a breach of this license to post this code on chegg.com 
Please see: http://creativecommons.org/licenses/by-nc-sa/4.0/  for the nitty gritty details 

'''

import matplotlib.pyplot as plt
import numpy as np
import kayHomogeneousTransformations as ht
import kayColorPalette as cp


np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})   # set all np prints to just 3 decimal places


# ------------------------------------ createNewBlank3DFigure -----------------------------------------------
#
# the Lim values are the range for each of the dimensions of the background. 
#
def createNewBlank3DFigure(title="", xLabel="X", yLabel="Y", zLabel="Z", xLim=(0,1), yLim=(0,1), zLim =(0, 1)):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    
    #Figure Title
    ax.set_title(title)

    # Labels for Figure Axes
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)

    # Need to set how big a space to display
    ax.set_xlim(xLim[0],xLim[1])
    ax.set_ylim(yLim[0],yLim[1])
    ax.set_zlim(zLim[0],zLim[1])
    
    return (fig, ax)  
    
 
# ------------------------------- draw3DFrame -------------------------------------
#
# ax: You need to have already created the blank figure on which to draw the frame
#     and ax is the axis value that function returned  
#
# operatorAsFrame: A 4x4 Homogeneous Transform Matrix (probably created by makeTransform or some
#     rotations and translations of a transform
#
# labelOffset: Where along each of the arrows to put the label (between 0 and 1)
#
# originLabel: A label to put next to the origin
#
# labelExtra: We'll be labelling x, y, and z, but maybe with an extra string concatenated to
#     it for specifying the name of the coords or something
#
# colorChoice: Can be a string like "red" or "blue" or one of the cp colors imported or
#     an RGV value in hex like #ff00ff
#
# axisLength: How long each arrow should be
#
# plotOrigin: Do you want to plot a blob at the origin?
#
# blobSize: How big a blob to plot at the origin (assuming you print anything)
#
def draw3DFrame(ax, operatorAsFrame, labelOffset=0.5, originLabel="", labelExtra="", 
                colorChoice=cp.one, axisLength = 1, plotOrigin = True, blobSize=60):
    # We need to extract the columns of the matrix. Since it's easier to extract rows, I'm just going to 
    # transpose the matrix first and then extract the rows. 
    
    transFrame = np.transpose(operatorAsFrame)
    
    #Slice off the first 3 elements of the last row (so we're dropping the 1 at the end)
    origin = transFrame[3,:3]
        
    x,y,z = origin
    
    
    labels = ["X"+labelExtra, "Y"+labelExtra, "Z"+labelExtra]
    
    # plot and label the origin
    if plotOrigin: 
        ax.scatter(x,y,z,  color=colorChoice, s=blobSize)
        ax.text(x,y,z,originLabel, color=colorChoice)
    
    # Now we're going to loop through the i, j, and k direction vectors to draw the axes
    for i in range(3):
        # Grab row i from locations 0-2 inclusive
        axis = transFrame[i, :3]
        u,v,w = axis
        ax.quiver(x,y,z,u,v,w, length = axisLength, normalize = True, color=colorChoice)
        
        
        # Figure out where to put the label
        # Start by computing where the end of the quiver is
        quiverEnd = origin + axisLength*axis
        labelLocation = origin + (axisLength*axis)*labelOffset
        uLabelLoc, vLabelLoc, wLabelLoc = labelLocation

        ax.text(uLabelLoc, vLabelLoc, wLabelLoc, labels[i], color=colorChoice)
        
        

# ----------------------- drawDottedLine -------------------------------------
def drawDottedLine(ax, startPoint, endPoint, numDots = 20, colorChoice = cp.four, label="", labelXOffset=0.2, labelYOffset=0.2, labelZOffset=0.2,  blobSize=10):
    start_x = startPoint.flat[0]
    start_y = startPoint.flat[1]
    start_z = startPoint.flat[2]
    end_x = endPoint.flat[0]
    end_y = endPoint.flat[1]
    end_z = endPoint.flat[2]
    i = np.linspace(start_x, end_x, num=numDots)
    j = np.linspace(start_y, end_y, num=numDots)
    k = np.linspace(start_z, end_z, num=numDots)


    ax.scatter(i,j,k,  color=colorChoice, s=blobSize)

    if (label != ""):
        labelXLocation = i[numDots//2]+labelXOffset
        labelYLocation = j[numDots//2]+labelYOffset
        labelZLocation = k[numDots//2]+labelZOffset

        ax.text(labelXLocation, labelYLocation, labelZLocation, label, color=colorChoice)






# ------------------------------- plot3DPoint -------------------------------------
#
# ax: You need to have already created the blank figure on which to draw the frame
#     and ax is the axis value that function returned  
#
# point: A 4x1 verticle np vector (probably created using makePoint)
#
# labelOffset: Something to add to the x,y,z value of where the label will be printed
#
# blobSize: How big a dot to plot
#
# xyzLabel: should you print the x,y,z location of the point
#
# labelExtra: anything else to add to the label 
#
# colorChoice: Can be a string like "red" or "blue" or one of the cp colors imported or
#     an RGV value in hex like #ff00ff
#
#
def plot3DPoint(ax, point, labelOffset=0, blobSize=60, xyzLabel=True, labelExtra="", colorChoice=cp.two):
    
    # Extract x, y, and z parts
    x = point.flat[0]
    y = point.flat[1]
    z = point.flat[2]
    
    ax.scatter(x,y,z,  color=colorChoice, s=blobSize)
    
   
    if xyzLabel:
        label ="  ("+str(x)+" ,"+str(y)+", "+str(z)+")" + labelExtra
    else:
        label = labelExtra
     
    labelXLocation = x+labelOffset    
    labelYLocation = y+labelOffset
    labelZLocation = z+labelOffset 
    
    ax.text(labelXLocation, labelYLocation, labelZLocation, label, color=colorChoice)
    
    
