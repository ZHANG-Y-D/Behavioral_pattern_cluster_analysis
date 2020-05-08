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
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt

# mat = np.array([[0,4,25,24,9,7], [4,0,21,20,5,3], [25,21,0,1,16,18], [24,20,1,0,15,17], [9,5,16,15,0,2], [7,3,18,17,2,0] ])
# mat = np.array([[0, 3, 10, 8], [3, 0, 9, 7], [10, 9, 0, 2], [8, 7, 2, 0]])

# mat = np.array([[0, 3, 10], [3, 0, 9], [10, 9, 0]])
# dists = squareform(mat)
# linkage_matrix = linkage(dists, "single")

# linkage_matrix = [[2., 3., 2., 2.], [0., 1., 3., 2.], [4., 5., 7., 4.]]
# linkage_matrix = [[2., 3., 2., 2.], [0., 1., 3., 2.], [4., 5., 10., 4.]]
# linkage_matrix = [[2., 3., 2., 2.], [0., 1., 3., 2.], [4., 5., 8.5, 4.]]
# linkage_matrix = [[2., 3., 2., 2.], [0., 1., 3., 2.], [4., 5., 8.38152731, 4.]]
# linkage_matrix = [[0., 1., 3., 2.], [2., 3., 9., 3.]]
linkage_matrix = [[7., 9., 3, 2.],
                  [4., 6., 4, 2.],
                  [5., 12., 5, 3.],
                  [2., 13., 6, 4.],
                  [3., 14., 7, 5.],
                  [1., 15., 8, 6.],
                  [10., 11., 9, 3.],
                  [8., 17., 10, 4.],
                  [0., 16., 11, 7.],
                  [18., 19., 12, 11.]]
# linkage_matrix = [[0., 1., 4., 2.], [2., 3., 5., 2.], [4., 5., 6., 2.]
# linkage_matrix = [[0., 1., 2, 2], [2, 3, 3, 2], [4, 5, 4, 2], [6, 7, 5, 2], [8, 9, 6, 2], [13, 14, 7, 4],
#                   [10, 12, 8, 3], [11, 17, 9, 5], [15, 18, 10, 7], [16, 19, 11, 11]]
print(linkage_matrix)
# dendrogram(linkage_matrix, labels=["A", "B", "C", "D"])
# dendrogram(linkage_matrix, labels=["A", "B", "C"])
dendrogram(linkage_matrix)

# plt.title("Single Link")
plt.show()

# import plotly.figure_factory as ff
#
# import numpy as np

# X = np.random.rand(15, 10) # 15 samples, with 10 dimensions each
# print(X)
# X = [[0, 3, 10, 8], [3, 0, 9, 7], [10, 9, 0, 2], [8, 7, 2, 0]]
# X = [[1,0,1,1,0,1,1,1,0,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,0,0,0,0,1],[1,1,1,1,1,0,0,0,0,1,1,1,1,0],[1,1,1,1,1,0,0,1,0,0,1,1,1,0]]
# X = np.array(X)
# names = ['A', 'B', 'C', 'D']
# fig = ff.create_dendrogram(X, color_threshold=1.5, labels=names)
# fig.update_layout(width=800, height=500)
# fig.show()

# from plotly.figure_factory import create_dendrogram
#
# import numpy as np
# import pandas as pd
#
# Index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# df = pd.DataFrame(abs(np.random.randn(10, 10)), index=Index)
# fig = create_dendrogram(df, labels=Index)
# fig.show()
#
# import pandas as pd
# import seaborn as sns
# sns.set()
#
# # Load the brain networks example dataset
# df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
#
# # Select a subset of the networks
# used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
# used_columns = (df.columns.get_level_values("network")
#                           .astype(int)
#                           .isin(used_networks))
# df = df.loc[:, used_columns]
#
# # Create a categorical palette to identify the networks
# network_pal = sns.husl_palette(8, s=.45)
# network_lut = dict(zip(map(str, used_networks), network_pal))
#
# # Convert the palette to vectors that will be drawn on the side of the matrix
# networks = df.columns.get_level_values("network")
# network_colors = pd.Series(networks, index=df.columns).map(network_lut)
#
# # Draw the full plot
# sns.clustermap(df.corr(), center=0, cmap="vlag",
#                row_colors=network_colors, col_colors=network_colors,
#                linewidths=.75, figsize=(13, 13))


# import igraph
#
# dendrogram = igraph.clustering.Dendrogram()


# import matplotlib.pyplot as plt
#
# # plt.style.use('ggplot')
# print(plt.style.available)
