import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
# np.random.seed(19680801)

# create random data
# data1 = np.random.random([6, 50])
# data1 = [[1, 2, 3,  4, 5],[8,9,10,11,12,13]]
# plt.eventplot(data1)

# set different colors for each set of positions
# colors1 = ['C{}'.format(i) for i in range(6)]

# set different line properties for each set of positions
# note that some overlap
# lineoffsets1 = np.array([-15, -3, 1, 1.5, 6, 10])
# linelengths1 = [5, 2, 1, 1, 3, 1.5]
#
# fig, axs = plt.subplots(1, 1)

# create a horizontal plot
# axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
#                     linelengths=linelengths1)

# create a vertical plot
# axs[1, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
#                     linelengths=linelengths1, orientation='vertical')

# create another set of random data.
# the gamma distribution is only used fo aesthetic purposes
# data2 = np.random.gamma(4, size=[60, 50])

# use individual values for the parameters this time
# these values will be used for all data sets (except lineoffsets2, which
# sets the increment between each data set in this usage)
# colors2 = 'black'
# lineoffsets2 = 1
# linelengths2 = 1

# create a horizontal plot
# axs[0, 1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
#                     linelengths=linelengths2)


# create a vertical plot
# axs[1, 1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
#                     linelengths=linelengths2, orientation='vertical')

# plt.show()

# ['7', '7', '7', '7', '7', '2', '7', '17', '71238', '734',
#  '387', '7', '7', '7', '7', '7', '7', '321', '378', '78',
#  '78', '8', '87', '73281', '83', '42', '2', '2', '2', '2',
#  '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
#
fig, ax = plt.subplots()

ax.set_ylim(0, 11)
ax.set_xlim(0, 2879)

ax.broken_barh([(1, 100)], (6.5, 1), facecolors='tab:blue')
ax.broken_barh([(10, 100)], (9.5, 1), facecolors='tab:red')
#
# ax.set_xlabel('The PIR sensor signals')
# ax.set_xticks([0, 1440, 2879])
# ax.set_xticklabels(['00:00', '12:00', '23:59'])
# ax.set_yticks([1, 2])
# ax.set_yticklabels(['Room 1', 'Room 2'])
# ax.grid(True)
# ax.annotate('race interrupted', (61, 25),
#             xytext=(0.8, 0.9), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             fontsize=16,
#             horizontalalignment='right', verticalalignment='top')

ax.set_xlabel('The PIR sensor signals')
ax.set_xticks([0, 720, 1440, 2160, 2879])
ax.set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticklabels(
    ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5', 'Room 6', 'Room 7', 'Room 8', 'Room 9', 'Room 10'])

plt.show()

#
# t = np.arange(0.0, 2.0, 0.01)
# s1 = np.sin(2*np.pi*t)
# s2 = np.sin(4*np.pi*t)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t, s1)
# plt.subplot(212)
# plt.plot(t, 2*s1)
#
# plt.figure(2)
# plt.plot(t, s2)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t, s2, 's')
# ax = plt.gca()
# ax.set_xticklabels([])
#
# plt.show()
