
class LinkageContainer:

    linkage_list: list

    def __init__(self):
        self.linkage_list = []

    def add_linkage_element(self,
                            first_cluster_num,
                            second_cluster_num,
                            distance,
                            num_of_clustering):
        self.linkage_list.append([float(first_cluster_num),
                                  float(second_cluster_num),
                                  float(distance),
                                  float(num_of_clustering)])

