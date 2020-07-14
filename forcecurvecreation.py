# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:49:09 2020

@author: cwiens
"""

from ImportForce_TXT import ImportForce_TXT
import matplotlib.pyplot as plt
from FindContactIntervals import FindContactIntervals

file_c = 'D:/Collections/191118 Bball/Force Files/Trial 022.txt'
file_m = 'D:/Collections/191118 Bball/Force Files/Trial 064.txt'
file_l = 'D:/Collections/191118 Bball/Force Files/Trial 104.txt'

data_c, samp, bw = ImportForce_TXT(file_c)
fy_c = data_c['Attila49 9286BA_Fy'] + data_c['Ryan52 9286BA_Fy']
fz_c = data_c['Attila49 9286BA_Fz'] + data_c['Ryan52 9286BA_Fz']
ci_c = FindContactIntervals(fz_c, thresh=20)
sync_f_c = fz_c.iloc[ci_c['Start'][0]:ci_c['End'][0]].idxmax()
release_f_c = sync_f_c + (1037-474)*(1200/120)
t_c = data_c['Time'] - data_c['Time'][release_f_c]

data_m, samp, bw = ImportForce_TXT(file_m)
fy_m = data_m['Attila49 9286BA_Fy'] + data_m['Ryan52 9286BA_Fy']
fz_m = data_m['Attila49 9286BA_Fz'] + data_m['Ryan52 9286BA_Fz']
ci_m = FindContactIntervals(fz_m, thresh=20)
sync_f_m = fz_m.iloc[ci_m['Start'][0]:ci_m['End'][0]].idxmax()
release_f_m = sync_f_m + (867-475)*(1200/120)
t_m = data_m['Time'] - data_m['Time'][release_f_m]

data_l, samp, bw = ImportForce_TXT(file_l)
fy_l = data_l['Attila49 9286BA_Fy'] + data_l['Ryan52 9286BA_Fy']
fz_l = data_l['Attila49 9286BA_Fz'] + data_l['Ryan52 9286BA_Fz']
ci_l = FindContactIntervals(fz_l, thresh=20)
sync_f_l = fz_l.iloc[ci_l['Start'][0]:ci_l['End'][0]].idxmax()
release_f_l = sync_f_l + (635-229)*(1200/120)
t_l = data_l['Time'] - data_l['Time'][release_f_l]



plt.subplot(3,1,1)
plt.title('Close', size=14, color='red')
plt.plot(t_c, fy_c, label='Horizontal Force')
plt.plot(t_c, fz_c, label='Vertical Force')
plt.hlines(0, t_c[0], t_c.iloc[-1])
plt.vlines(0, -100, 2000, linestyles='dashed', label='release')
plt.xlim(-1.5,1)
plt.ylabel('Force (N)', size=14)
plt.legend()

plt.subplot(3,1,2)
plt.title('Medium', size=14, color='green')
plt.plot(t_m, fy_m, label='Horizontal Force')
plt.plot(t_m, fz_m, label='Vertical Force')
plt.hlines(0, t_m[0], t_m.iloc[-1])
plt.vlines(0, -100, 2000, linestyles='dashed', label='release')
plt.xlim(-1.5,1)
plt.ylabel('Force (N)', size=14)

plt.subplot(3,1,3)
plt.title('Long', size=14, color='blue')
plt.plot(t_l, fy_l, label='Horizontal Force')
plt.plot(t_l, fz_l, label='Vertical Force')
plt.hlines(0, t_l[0], t_l.iloc[-1])
plt.vlines(0, -100, 2000, linestyles='dashed', label='release')
plt.xlim(-1.5,1)
plt.ylabel('Force (N)', size=14)
plt.xlabel('Time (s)', size=14)