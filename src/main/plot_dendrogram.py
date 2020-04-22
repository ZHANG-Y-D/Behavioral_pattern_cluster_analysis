# import plotly.figure_factory as ff
#
# import numpy as np
#
# X = [[1571, 1450, 1606, 1853, 2100], [1428, 1682, 1782, 2121], [1660, 1830, 2152], [2094, 2149], [1853]]
# # X = np.random.rand(15, 10) # 15 samples, with 10 dimensions each
# fig = ff.create_dendrogram(X, color_threshold=1.5)
# fig.update_layout(width=800, height=500)
# fig.show()
#
# X = np.random.rand(15, 10) # 15 samples, with 10 dimensions each
# fig = ff.create_dendrogram(X, color_threshold=1.5)
# fig.update_layout(width=800, height=500)
# fig.show()

# import numpy as np
# from scipy.cluster import hierarchy
# import matplotlib.pyplot as plt

# ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268.,
#                    400., 754., 564., 138., 219., 869., 669.])
#
# ytdist = np.array([1571, 1450, 1606, 1853, 2100, 1428, 1682, 1782, 2121, 1660, 1830, 2152, 2094, 2149, 1853])
# ytdist = np.array([5690, 8050, 7620, 6906, 8738, 8804, 7384, 5781, 5406, 5782, 6811, 7189, 6397, 3155, 4321, 5620, 6076, 8253, 3963, 5088, 5660, 7919, 5460, 5816, 8366, 4360, 7266, 5764])
# ytdist = np.array([[5690, 8050, 7620, 6906, 8738, 8804, 7384], [5781, 5406, 5782, 6811, 7189, 6397], [3155, 4321, 5620, 6076, 8253], [3963, 5088, 5660, 7919], [5460, 5816, 8366], [4360, 7266], [5764]])
# Z = hierarchy.linkage(ytdist, 'single')
# plt.figure()
# dn = hierarchy.dendrogram(Z)
#
#
# hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
# fig, axes = plt.subplots(1, 2, figsize=(8, 3))
# dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='y',
#                            orientation='top')
# dn2 = hierarchy.dendrogram(Z, ax=axes[1],
#                            above_threshold_color='#bcbddc',
#                            orientation='right')
# hierarchy.set_link_color_palette(None)  # reset to default after use
# plt.show()

#
# import numpy as np
# from scipy.cluster.hierarchy import dendrogram, linkage
# from scipy.spatial.distance import squareform
# import matplotlib.pyplot as plt
# mat = np.array([[0,4,25,24,9,7], [4,0,21,20,5,3], [25,21,0,1,16,18], [24,20,1,0,15,17], [9,5,16,15,0,2], [7,3,18,17,2,0] ])
# dists = squareform(mat)
# linkage_matrix = linkage(dists, "complete")
# dendrogram(linkage_matrix, labels=["A","B","C","D","E","F"])
# plt.title("Complete Link")
# plt.show()
