import random
import math
import matplotlib.pyplot as plt
import Node


def PrimDjikstra(ListMentor, alpha):
    ListTree = []
    ListU = []

    for i in range(len(ListMentor)):
        ListU.append(ListMentor[i][0])

    def calc_distance_2Dpoint(a, b):
        return round(math.sqrt(
            (a.get_position_x() - b.get_position_x()) ** 2 +
            (a.get_position_y() - b.get_position_y()) ** 2
        ), 4)

    # --- tìm backbone trung tâm ---
    backbone_distance = [[calc_distance_2Dpoint(ListU[i], ListU[j]) for i in range(len(ListU))]
                         for j in range(len(ListU))]

    moment = [0 for i in range(len(ListU))]
    for i in range(len(ListU)):
        for j in range(len(ListU)):
            moment[i] += backbone_distance[i][j] * ListU[j].get_traffic()

    min_moment = min(moment)
    min_index = moment.index(min_moment)

    print(f"Central Backbone Node is: {ListU[min_index].get_name()}\n")
    ListTree.append(ListU[min_index])
    ListU.pop(min_index)

    # --- thuật toán Prim-Djikstra ---
    cost = [math.inf for _ in range(len(ListU))]
    P = [-1 for _ in range(len(ListMentor))]  # parent của mỗi node (theo index trong ListMentor)

    # gốc có parent = -1
    root_node = ListTree[0]
    root_index = [mentor[0] for mentor in ListMentor].index(root_node)
    P[root_index] = -1

    # setup initial cost từ root
    for i, node in enumerate(ListU):
        cost[i] = calc_distance_2Dpoint(root_node, node)
        idx = [mentor[0] for mentor in ListMentor].index(node)
        P[idx] = root_index

    while ListU:
        # chọn node có cost nhỏ nhất
        min_cost = min(cost)
        min_index = cost.index(min_cost)
        new_node = ListU[min_index]

        # thêm vào cây
        ListTree.append(new_node)

        # xóa khỏi U và cost
        ListU.pop(min_index)
        cost.pop(min_index)

        # cập nhật cost
        for i, node in enumerate(ListU):
            new_cost = alpha * min_cost + calc_distance_2Dpoint(new_node, node)
            if new_cost < cost[i]:
                cost[i] = new_cost
                idx = [mentor[0] for mentor in ListMentor].index(node)
                P[idx] = [mentor[0] for mentor in ListMentor].index(new_node)

    return [mentor[0] for mentor in ListMentor], P,ListTree
