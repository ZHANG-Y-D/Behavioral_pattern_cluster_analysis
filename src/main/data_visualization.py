from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt


def presentation_dendrogram(day_deck, linkage):
    plt.figure(1)
    dendrogram(linkage, labels=day_deck.data_name_labels)
    plt.title("Hierarchical Clustering")


def presentation_common_pattern(common_pattern_list):
    for i, ele in enumerate(common_pattern_list):
        plot = plt.figure(i + 2)
        plot.suptitle('Common Pattern ' + str(i + 1))
        if ele.get_pir_list() is not None:
            presentation_pir_list(plot, ele.get_pir_list())


def presentation_pir_list(fig, pir_list):
    # print(pir_list)
    ax = fig.subplots(2, 2)

    ax[0, 0].set_title('The PIR sensor signals')
    ax[0, 0].set_ylim(0, 12)
    ax[0, 0].set_xlim(0, 2880)

    for i, ele in enumerate(pir_list):
        for sub_ele in ele:
            if sub_ele == 'a':
                num_room = 10
            elif sub_ele == 'f':
                num_room = 11
            elif sub_ele == 'X':
                break
            else:
                num_room = int(sub_ele)
            ax[0, 0].broken_barh([(i, 1)], (num_room - 0.5, 1), facecolors='tab:blue')

    ax[0, 0].set_xticks([0, 720, 1440, 2160, 2879])
    ax[0, 0].set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
    ax[0, 0].set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    ax[0, 0].set_yticklabels(['Room  1', 'Room  2', 'Room  3', 'Room  4', 'Room  5',
                              'Room  6', 'Room  7', 'Room  8', 'Room  9', 'Room 10',
                              'Outside'])


def show_all_figure():
    plt.show()
