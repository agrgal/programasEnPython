#!/usr/bin/env python
"""
An animated image demonstrating circular motion
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#generate a figure onto which our animation will be plotted
fig = plt.figure()
#add a subplot to this figure
#"111" means generate a 1x1 grid of plots, and this subplot goes in the 1st available grid space
#the returned variable is a representation of the axes of the subplot (hence ax)
ax = fig.add_subplot(111, xlim=(-1, 1), ylim=(-1, 1))
#prepare the line variable by assigning it to an empty line on these axes
#'o-' means plot points as circles (o) and connect them with solid lines (-)
line, = ax.plot([], [], 'o-')

#first we define an initialisation function for our line
def init():
    #set the data to [], [] for the x, y coordinates, respectively
    line.set_data([], [])
    return line

#now we define a function which will animate the line forward one step
def animate(i):
    #first generate an angle in radians
    angle = i/10. * np.pi
    #now set the coordinates of the points along the line to [0,0] and [cos(angle), sin(angle)]
    thisx = [0, np.cos(angle)]
    thisy = [0, np.sin(angle)]
    #set the x, y coordinates to these new values
    line.set_data(thisx, thisy)
    return line

#generate the animation using animation.FuncAnimation
#inputs are: fig, the figure we'll plot to; animate, the animation function to use;
#np.arange(1,100); the series of inputs used to generate each animation frame;
#interval, the time between frames in miliseconds;
#init_func, the name of the initialisation function for our animated object
ani = animation.FuncAnimation(fig, animate, np.arange(1, 100), interval=25, init_func=init)

#show the animation
plt.show()
