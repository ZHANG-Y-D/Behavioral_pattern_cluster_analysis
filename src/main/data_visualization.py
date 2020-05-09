from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt


def presentation_dendrogram(day_deck, linkage):
    dendrogram(linkage, labels=day_deck.data_name_labels)
    plt.title("Hierarchical Clustering")
    plt.show()

