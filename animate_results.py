#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
load and aniamte code

Created on Tue Dec 11 23:00:45 2018
@author: Richard Boyne rmb115@ic.ac.uk
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation


class animate():
    def __init__(self, x, y, z, times):
        """
        array is 2d with time on axis=0 and function values for x
        points on axis=1
        """
        # setup data
        self.x = x
        self.y = y
        self.z = z
        self.times = times
        self.N = len(times)
        assert self.N == x.shape[0] == y.shape[0] == z.shape[0], \
            'all inputs need same number of time entries'
        assert x.shape[1] == y.shape[1] == z.shape[1], \
            'all inputs need same number of points enteries'

        # setup options
        self.save = ''
        self.interval = 20
        r_x = self.x.max() - self.x.min()
        r_y = self.y.max() - self.y.min()
        self.xlims = np.array([self.x.min() - r_x/10, self.x.max() + r_x/10])
        self.ylims = np.array([self.y.min() - r_y/10, self.y.max() + r_y/10])

    def blank(self):
        self.scat = self.ax.scatter([], [])
        self.text.set_text('')
        return self.scat, self.text

    def update(self, i):
        self.scat = self.ax.scatter(self.x[i], self.y[i], c=self.z[i])
        self.text.set_text('t={0:.2f}'.format(self.times[i]))
        return self.scat, self.text

    def animate(self):
        # initialise figure
        self.fig, self.ax = plt.subplots()
        self.scat = self.ax.scatter([], [])
        self.text = self.ax.text(0.75, 0.95, '', transform=self.ax.transAxes)

        # set axis limits
        self.ax.set_xlim(self.xlims)
        self.ax.set_ylim(self.ylims)

        # animate
        self.ani = FuncAnimation(self.fig,
                                 self.update,
                                 frames=range(len(self.times)),
                                 interval=self.interval,
                                 blit=True,
                                 init_func=self.blank)
        if self.save != "":
            self.ani.save(self.save)


def load_and_set(file_name, color_key='V_x'):
    # load data
    data = pd.read_csv(file_name, skiprows=2, index_col=False)
    data = data.set_index('Time')

    # format data
    times = np.unique(data.index)
    x, y, z = [], [], []
    for t in times:
        x.append(np.array(data.loc[t]['R_x']))
        y.append(np.array(data.loc[t]['R_y']))
        z.append(np.array(data.loc[t][color_key]))
    x, y, z = np.array(x), np.array(y), np.array(z)

    # run animation
    ani = animate(x, y, z, times)
    return ani

#ani = load_and_set('raw_data/2018-12-12-10hr-54m.csv', 'Density')
ani = load_and_set(domain.file.name, 'Density')
ani.animate()