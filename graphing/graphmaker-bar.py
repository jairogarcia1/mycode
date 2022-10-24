#!/usr/bin/env python3
""" Alta3 Research | Jgarcia | matplotlib"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
plt.savefig("/home/student/mycode/graphing/plot.png")
    # save a copy to "~/static" (the "files" view)
plt.savefig("/home/student/static/plot.png")
