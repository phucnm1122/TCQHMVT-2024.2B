import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import CheckButtons
import math

import matplotlib.pyplot as plt
def calc_backbone_traffic(TrafficMatrix, backbones, access_dict):
    """
    TrafficMatrix: ma trận lưu lượng NxN
    backbones: list index backbone nodes (dạng 1-based, lấy từ get_name())
    access_dict: dict {backbone_index (1-based): [list access node index (1-based)]}
    """
    n_backbone = len(backbones)
    T_b = [[0] * n_backbone for _ in range(n_backbone)]

    for i1, b1 in enumerate(backbones):
        for i2, b2 in enumerate(backbones):
            if i1 == i2:
                continue

            trafic = 0

            # 1. access của b1 -> b2
            for a1 in access_dict.get(b1, []):
                trafic += TrafficMatrix[a1 - 1][b2 - 1]

                # 2. access b1 -> access b2
                for a2 in access_dict.get(b2, []):
                    trafic += TrafficMatrix[a1 - 1][a2 - 1]

            # 3. b1 -> access của b2
            for a2 in access_dict.get(b2, []):
                trafic += TrafficMatrix[b1 - 1][a2 - 1]

            # 4. b1 -> b2
            trafic += TrafficMatrix[b1 - 1][b2 - 1]

            T_b[i1][i2] = trafic

    # Ghi ra file CSV
    with open("BackboneTraffic.csv", "w", newline="") as f:
        writer = csv.writer(f)

        # header
        header = [""] + [f"Node{b}" for b in backbones]
        writer.writerow(header)

        # từng hàng
        for i, b1 in enumerate(backbones):
            row = [f"Node{b1}"] + T_b[i]
            writer.writerow(row)
    return T_b



def optimize_and_visualize_backbone(TrafficFile, ListMentor, MAX, RM, C, umin, center_node,
                                    OutputFile="OptimizedBackbone.csv",
                                    NFile="N_matrix.csv", UFile="U_matrix.csv"):
    from matplotlib.patches import Circle
    from matplotlib.widgets import CheckButtons
    import pandas as pd
    import matplotlib.pyplot as plt
    import math

    """
    Tối ưu backbone theo thuật toán (n, u, umin),
    Xuất file CSV: backbone traffic, ma trận n, ma trận u,
    và vẽ kết quả.
    """

    # --- Bước 1: Đọc traffic matrix ---
    df = pd.read_csv(TrafficFile, index_col=0)
    nodes = df.index.tolist()
    new_df = pd.DataFrame(0, index=nodes, columns=nodes)

    # --- Khởi tạo ma trận n và u ---
    n_matrix = pd.DataFrame(0, index=nodes, columns=nodes, dtype=float)
    u_matrix = pd.DataFrame(0.0, index=nodes, columns=nodes, dtype=float)

    # --- Bước 2: Thuật toán tối ưu ---
    for i, N1 in enumerate(nodes):
        for j, N2 in enumerate(nodes):
            if i == j:
                continue

            traffic = df.loc[N1, N2]
            if traffic == 0:
                continue

            # số kênh cần thiết
            n = math.ceil(traffic / C)
            if n == 0:
                continue

            # tính độ sử dụng
            u = traffic / (n * C)

            # lưu vào ma trận n và u
            n_matrix.loc[N1, N2] = n
            u_matrix.loc[N1, N2] = u

            if u > umin:
                # giữ liên kết trực tiếp
                new_df.loc[N1, N2] += traffic
            else:
                # chuyển lưu lượng qua hub H
                for H in nodes:
                    if H not in [N1, N2]:
                        new_df.loc[N1, H] += traffic
                        new_df.loc[H, N2] += traffic
                        break  # chỉ chọn 1 hub đầu tiên

    # --- Bước 3: Xuất ra file CSV ---
    new_df.to_csv(OutputFile, index=True)   # backbone traffic
    n_matrix.to_csv(NFile, index=True)      # ma trận n
    u_matrix.to_csv(UFile, index=True)      # ma trận u

    # --- Bước 4: Vẽ backbone tối ưu ---
    ListNode = [mentor[0] for mentor in ListMentor]
    node_map = {node.get_name(): node for node in ListNode}

    fig, ax = plt.subplots(figsize=(8, 6))
    circles = []

    for N1 in new_df.index:
        for N2 in new_df.columns:
            if N1 == N2:
                continue
            traffic = new_df.loc[N1, N2]
            if traffic > 0:
                n1, n2 = node_map[int(N1.replace("Node", ""))], node_map[int(N2.replace("Node", ""))]
                x1, y1 = n1.get_position_x(), n1.get_position_y()
                x2, y2 = n2.get_position_x(), n2.get_position_y()
                ax.plot([x1, x2], [y1, y2], 'r-', linewidth=1.5)
                ax.text((x1+x2)/2, (y1+y2)/2, str(traffic),
                        color="blue", fontsize=8, ha="center", va="center")

    # backbone nodes
    root_node = center_node

    for node in ListNode:
        x, y = node.get_position_x(), node.get_position_y()
        node_name = str(node.get_name())

        if node == root_node:
            ax.text(x, y, node_name, color="white", size=10,
                     ha="center", va="center",
                     bbox=dict(facecolor="red", edgecolor='black', boxstyle='round'))
            ax.plot(x, y, 'ro', markersize=10, markerfacecolor='red',
                     markeredgewidth=1.5, markeredgecolor='black')
        else:
            ax.text(x, y, node_name, color="black", size=10,
                     ha="center", va="center",
                     bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='black', boxstyle='round'))
            ax.plot(x, y, 'ro', markersize=6, markerfacecolor='w',
                     markeredgewidth=1.5, markeredgecolor='black')

        coverage_circle = Circle((x, y), radius=RM,
                                 fill=False, linestyle='--', color='blue', linewidth=1.2)
        coverage_circle.set_visible(False)
        ax.add_patch(coverage_circle)
        circles.append(coverage_circle)

    for mentor in ListMentor:
        backbone = mentor[0]
        for access_node in mentor[1:]:
            x, y = access_node.get_position_x(), access_node.get_position_y()
            ax.plot([x, backbone.get_position_x()],
                    [y, backbone.get_position_y()], 'g:')
            ax.text(x, y, str(access_node.get_name()), color="blue", size=8,
                     ha="center", va="center",
                     bbox=dict(facecolor=(0.8, 0.9, 1.0), edgecolor='none', boxstyle='round'))
            ax.plot(x, y, 'bo', markersize=4, markerfacecolor='cyan',
                     markeredgewidth=1.0, markeredgecolor='blue')

    plt_margin = MAX * 0.05
    ax.set_xlim(-plt_margin, MAX + plt_margin)
    ax.set_ylim(-plt_margin, MAX + plt_margin)
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Backbone sau tối ưu")

    rax = plt.axes([0.8, 0.7, 0.15, 0.15])
    check = CheckButtons(rax, ["Show Radius"], [False])

    def toggle(label):
        for c in circles:
            c.set_visible(not c.get_visible())
        plt.draw()

    check.on_clicked(toggle)
    plt.show()

    return n_matrix, u_matrix
