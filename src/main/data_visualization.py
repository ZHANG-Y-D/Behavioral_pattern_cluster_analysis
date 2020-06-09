import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram


def presentation_dendrogram(day_deck,
                            linkage,
                            the_corresponding_level_of_max_cluster):
    print("Executing dendrogram presentation...")
    if day_deck is not None:
        label = day_deck.data_name_labels
    else:
        label = None
    plt.figure()
    color_list = dendrogram(linkage, labels=label, color_threshold=the_corresponding_level_of_max_cluster)
    plt.title("Hierarchical Clustering")
    plt.axhline(y=the_corresponding_level_of_max_cluster,
                label='Level of critical distance DT = '+str(the_corresponding_level_of_max_cluster),
                color='tomato',
                linestyle=':')
    plt.legend()
    return color_list['color_list']


def set_parameter_for_axis(ax, year):
    ax.set_title(str(year))

    # For days
    ax.set_xlim(0, 32)
    day_label = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    ax.set_xticks(day_label)
    ax.set_xticklabels([str(ele) for ele in day_label])

    # For months
    ax.set_ylim(0, 13)
    ax.set_yticks(list(range(1, 13)))
    ax.set_yticklabels(['January', 'February', 'March', 'April',
                        'May', 'June', 'July', 'August', 'September',
                        'October', 'November', 'December'])


def presentation_calendar(common_pattern_list, color_list):
    print("Executing calendar presentation...")
    year_list = []

    # Build the color list
    color_list = sorted(set(color_list), key=color_list.index)
    if 'b' in color_list:
        color_list.remove('b')

    # Find out how many years there are
    for ele in common_pattern_list:
        for date in ele.clustered_date:
            if date.year not in year_list:
                year_list.append(date.year)
    ax = plt.figure().subplots(len(year_list))

    # Set coefficient for each year
    if len(year_list) == 1:
        set_parameter_for_axis(ax, year_list[0])
    else:
        for year in year_list:
            set_parameter_for_axis(ax[year_list.index(year)], year)

    # Color for date on the corresponding year
    for ele in common_pattern_list:
        # Determinate color for this day
        if len(ele.clustered_date) == 1:
            color = 'b'
            color_list.insert(common_pattern_list.index(ele), color)
        else:
            color = color_list[common_pattern_list.index(ele)]
        for date in ele.clustered_date:
            if len(year_list) > 1:
                ax[year_list.index(date.year)].broken_barh([(date.day - 0.4, 0.8)],
                                                           (date.month - 0.4, 0.8), facecolors=color)
            else:
                ax.broken_barh([(date.day - 0.4, 0.8)], (date.month - 0.4, 0.8), facecolors=color)


def presentation_common_pattern(common_pattern_list, appliances_sampling_interval):
    print("Executing common pattern presentation...")
    for ele in common_pattern_list:

        plot = plt.figure()

        if len(ele.clustered_date) == 1:
            plot.suptitle('Abnormal days: ' + ele.clustered_date[0].strftime("%Y-%m-%d"))
            print("Presenting abnormal days: " + ele.clustered_date[0].strftime("%Y-%m-%d"))
        else:
            ele.clustered_date.sort()
            common_pattern_date = ""
            for date in ele.clustered_date:
                common_pattern_date = common_pattern_date + date.strftime("%Y-%m-%d")
                common_pattern_date = common_pattern_date + "  "
            plot.suptitle('Common Pattern: ' + common_pattern_date)
            print("Presenting common pattern: " + common_pattern_date)

        ax = plot.subplots(2, 2)

        if ele.get_pir_list() is not None:
            presentation_pir_list(ax[0, 0], ele.get_pir_list())
        if ele.get_lumen_list() is not None:
            presentation_lumen_list(ax[0, 1], ele.get_lumen_list())
        if ele.get_temp_list() is not None:
            presentation_temp_list(ax[1, 0], ele.get_temp_list())
        if ele.get_power_list() is not None:
            presentation_power_list(ax[1, 1], ele.get_power_list(), appliances_sampling_interval)
    print("Hint:Maximize the window to get the best visual effect.")


def presentation_lumen_list(ax, lumen_list):
    ax.set_title('The lumen sensor signals')
    ax.set_ylim(0, 11)
    ax.set_xlim(0, 288)
    ax.set_xticks([0, 72, 144, 216, 287])
    ax.set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_yticklabels(['Room  1', 'Room  2', 'Room  3', 'Room  4', 'Room  5',
                        'Room  6', 'Room  7', 'Room  8', 'Room  9', 'Room 10'])
    for room_num, ele in enumerate(lumen_list):
        for time_index, sub_ele in enumerate(ele):
            if sub_ele == 0:  # Buio
                color = '#0E091B'
            elif sub_ele == 1:  # Scarsa
                color = '#312877'
            elif sub_ele == 2:  # Discreta
                color = '#5044C1'
            elif sub_ele == 3:  # Buona
                color = '#6666CC'
            elif sub_ele == 4:  # Molto buona
                color = '#8190D5'
            elif sub_ele == 5:  # Ottima
                color = '#ABB8E3'
            else:
                color = 'white'
            ax.broken_barh([(time_index, 1)], (room_num + 0.6, 0.8), facecolors=color)


def presentation_temp_list(ax, temp_list):
    ax.set_title('The temp sensor signals')
    ax.set_ylim(0, 11)
    ax.set_xlim(0, 72)
    ax.set_xticks([0, 18, 36, 54, 71])
    ax.set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_yticklabels(['Room  1', 'Room  2', 'Room  3', 'Room  4', 'Room  5',
                        'Room  6', 'Room  7', 'Room  8', 'Room  9', 'Room 10'])
    for room_num, ele in enumerate(temp_list):
        for time_index, sub_ele in enumerate(ele):
            if sub_ele == 'X' or sub_ele is None:
                color = 'white'
            else:
                # g = 1-sub_ele/26
                # g = math.log(sub_ele*10, 260)
                g = 1 - (sub_ele ** 2) / 700
                if g > 1:
                    g = 1.0
                elif g < 0:
                    g = 0.0
                color = (1.0, g, 0.0)
            ax.broken_barh([(time_index, 1)], (room_num + 0.6, 0.8), facecolors=color)


def presentation_power_list(ax, power_list, appliances_sampling_interval):
    """
            There are 9 domestic appliances
            1.Microonde: No.24, sampling interval is 30s
            2.Televisione: No.26, sampling interval is 120s
            3.HC2 Power: No.28, sampling interval is 300s
            4.Frigorifero: No.32, sampling interval is 1200s
                            Power_level: 0w, 2w, 50w
            5.Forno: No.34, sampling interval is 120s
            6.Lavatrici: No.36, sampling interval is 120s
            7.Serra A: No.45, sampling interval is 120s,
                        Directly record the original value
            8.Lavastoviglie: No.148, sampling interval is 120s
            9.PC: No.150, sampling interval is 120s, threshold: 5w

        Method of sampling:
            For all appliances except refrigerators,Serra A,
            We use True and False to indicate on/off,
            Above the threshold is on and vice versa.
            Attention: PC has no threshold in sql, but we use 5w
            For refrigerators, we use power_level [0,2,50] -> 0,1,2
            For Serra A, we use the original value of sql
    """
    ax.set_title('The power sensor signals')
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 2880)
    ax.set_xticks([0, 720, 1440, 2160, 2879])
    ax.set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ax.set_yticklabels(['Microonde', 'Televisione', 'HC2 Power', 'Frigorifero', 'Forno',
                        'Lavatrici', 'Serra A', 'Lavastoviglie', 'PC'])

    for power_num, ele in enumerate(power_list):
        for time_index, sub_ele in enumerate(ele):
            if power_num + 1 in [1, 2, 3, 5, 6, 8, 9]:  # sampling interval is 120s
                if sub_ele is True:
                    color = 'tomato'
                elif sub_ele is False:
                    color = 'gray'
                else:
                    color = 'white'
            elif power_num + 1 == 7:  # for Serra A, sampling interval is 120s
                if sub_ele is None or sub_ele == 'X':
                    color = 'white'
                elif sub_ele == 0:
                    color = 'mistyrose'
                elif sub_ele == 1:
                    color = 'salmon'
                elif sub_ele == 2:
                    color = 'red'
                elif 2 < sub_ele <= 4:
                    color = 'darkred'
                else:
                    color = 'black'
            elif power_num + 1 == 4:  # for Frigorifero, sampling interval is 1200s
                if sub_ele is None or sub_ele == 'X':
                    color = 'white'
                elif sub_ele == 0:
                    color = 'mistyrose'
                elif 0 < sub_ele <= 2:
                    color = 'salmon'
                elif 2 < sub_ele <= 50:
                    color = 'red'
                elif 50 < sub_ele:
                    color = 'darkred'
                else:
                    color = 'white'
            else:
                color = 'white'

            time_index = time_index * (appliances_sampling_interval[power_num] / 30)
            ax.broken_barh([(time_index, appliances_sampling_interval[power_num] / 30)], (power_num + 0.6, 0.8),
                           facecolors=color)


def presentation_pir_list(ax, pir_list):
    ax.set_title('The PIR sensor signals')
    ax.set_ylim(0, 12)
    ax.set_xlim(0, 2880)
    ax.set_xticks([0, 720, 1440, 2160, 2879])
    ax.set_xticklabels(['00:00', '6:00', '12:00', '18:00', '23:59'])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    ax.set_yticklabels(['Room  1', 'Room  2', 'Room  3', 'Room  4', 'Room  5',
                        'Room  6', 'Room  7', 'Room  8', 'Room  9', 'Room 10',
                        'Outside'])

    for i, ele in enumerate(pir_list):
        if ele is None:
            continue
        for sub_ele in ele:
            if sub_ele == 'a':
                num_room = 10
            elif sub_ele == 'f':
                num_room = 11
            elif sub_ele == 'X':
                break
            else:
                num_room = int(sub_ele)
            ax.broken_barh([(i, 1)], (num_room - 0.5, 1), facecolors='tab:blue')


def show_all_figure():
    plt.show()
