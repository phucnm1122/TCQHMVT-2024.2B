# Thư viện
import random
import math
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
num_inf = math.inf
num_ninf = -math.inf


# Các cài đặt mặc định


# Lớp mô hình hóa các nút
# Thuộc Tính:
#   Tọa độ x,y
#   Khoảng cách tới nút trung tâm đang tạm xét (tính theo Đề các)
#   Tên nút đánh từ 1 đến nút MAX
class Node:
    name = 0
    x = 0
    y = 0

    # MENTOR
    traffic = 0
    weight = 0
    awardPoint = 0
    distanceToCenter = 0

    # Esau William
    weight_ew = 0
    weight_of_group = 0
    group_node_to_center = 0
    thoa_hiep = num_ninf
    cost_to_center = num_inf
    next_connect = 0
    group_size = 1


    def __init__(self):
        self.ListConnect = []

    def create_name(self, name):
        self.name = name
        self.group_node_to_center = name

    def create_position(self, MAX):
        self.x = random.randint(0, MAX)
        self.y = random.randint(0, MAX)

    def set_position(self, x, y):
        self.x = round(x,2)
        self.y = round(y,2)

    def set_distance(self, other):
        self.distanceToCenter = round(math.sqrt((self.get_position_x() - other.get_position_x()) ** 2 + (
                self.get_position_y() - other.get_position_y()) ** 2),4)

    def set_traffic(self, t):
        self.traffic = t

    def set_award(self, t):
        self.awardPoint = t

    def set_ew_pre(self, name, x, y, w):
        self.name = name
        self.group_node_to_center = name
        self.x = x
        self.y = y
        self.weight = w

    def set_weight(self, w):
        self.weight = w

    def set_weight_ew(self, w):
        self.weight_ew = w
        self.weight_of_group = w

    def set_connect(self,i):
        #print("Go set neighbor:",i,"in Node:",self.get_name())
        self.ListConnect.append(i)


    def check_connect(self,i):
        if i in self.ListConnect:
            return True
        return False

    def remove_connect(self,i):
        self.ListConnect.remove(i)

    def get_list_connect(self):
        return self.ListConnect

    def reset_list_connect(self):
        self.ListConnect.clear()

    def get_weight_ew(self):
        return self.weight_ew

    def set_thoahiep(self, t):
        self.thoa_hiep = t

    def set_next_connect(self, index):
        self.next_connect = index


    def set_cost_to_center(self, c):
        self.cost_to_center = c

    def set_weight_of_group(self, w):
        self.weight_of_group = w

    def set_group_node_to_center(self,index):
        self.group_node_to_center = index

    def get_group_node_to_center(self):
        return self.group_node_to_center

    def set_group_size(self,s):
        self.group_size = s

    def get_group_size(self):
        return self.group_size

    def get_weight_of_group(self):
        return self.weight_of_group

    def get_cost_to_center(self):
        return self.cost_to_center


    def get_next_connect(self):
        return self.next_connect

    def get_thoahiep(self):
        return self.thoa_hiep

    def get_weight(self):
        return self.weight

    def get_award(self):
        return self.awardPoint

    def get_traffic(self):
        return self.traffic

    def get_distance(self):
        return self.distanceToCenter

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def get_name(self):
        return self.name

    def compare_position(self, other):  # Return 1 if same 0 if not same
        return (self.get_position_x() == other.get_position_x()) and (self.get_position_y() == other.get_position_y())

    def copyNode(self, other):
        self.x = other.get_position_x()
        self.y = other.get_position_y()
        self.name = other.get_name()
        self.traffic = other.get_traffic()


    def printInitial(self):
        print('Node: {:<3} | Position: x = {:<4} y = {:<4} | Traffic: {:<2}'.format(self.get_name(),
                                                                                                       self.get_position_x(),
                                                                                                       self.get_position_y(),
                                                                                                       self.get_traffic(),
                                                                                                       self.get_weight_ew()))

    def printMentor(self):
        print('Node: {:<3} | Position: x = {:<4} y = {:<4} | Traffic: {:<2}'.format(
            self.get_name(),
            self.get_position_x(),
            self.get_position_y(),
            self.get_traffic()))

    def printCenterPress(self):
        print('Node trung tâm trọng lực: Position: x = {:<6} y = {:<6}'.format(round(self.x,2),round(self.y,2)))

    def printEW(self):
        print(
            'Node: {:<3} | Position: x = {:<4} y = {:<4} | Thỏa hiệp: {:<9} | Liên kết mới khi thỏa hiệp tới node: {:<3} | Trọng số nhánh: {:<2} | Node về tâm {:<3} | Khoảng cách về tâm {:<4}'.format(
                self.get_name(),
                self.get_position_x(),
                self.get_position_y(),
                round(self.get_thoahiep(), 4),
                self.get_next_connect(),
                self.get_weight_of_group(),
                self.get_group_node_to_center(),
                self.get_cost_to_center()))
        print("List Connect:", self.ListConnect)

    def print(self):
        print(self.get_name(),end=' ')


'''




'''


# Tạo một số hàm

# Hàm sắp xếp danh sách dựa trên tọa độ x của node


def sortListPosition(m):
    return m.get_position_x()


def printList(_list):
    for i in _list:
        i.print()
    print()

def printInitialList(_list):
    for i in _list:
        i.printInitial()

def printMentorList(_list):
    for i in _list:
        i.printMentor()

def printEWList(_list):
    for i in range(1,len(_list)):
        _list[i].printEW()


def printList2D(_list):
    for i in _list:
        for j in i:
            print(j.get_name(), end=' ')
        print()


def find_index_node(m,ListPosition):
    for i in range(0, len(ListPosition)):
        if ListPosition[i].get_name() == m:
            return i
    return 0

def matplotList(_list, MAX):
    xpos = []
    ypos = []
    npos = []
    for i in _list:
        xpos.append(i.get_position_x())
        ypos.append(i.get_position_y())
        npos.append(i.get_name())

    for i in range(0, len(_list)):
        plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
                 )
    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])
    plt.show()


def matplotconnectpoints(x, y, n1, n2,ListPosition):
    p1 = n1
    p2 = n2
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')


def matplotListToCenter(_list, MAX):
    xpos = []
    ypos = []
    npos = []
    for i in _list:
        xpos.append(i.get_position_x())
        ypos.append(i.get_position_y())
        npos.append(i.get_name())

    #for i in range(1, len(_list)):
    #    matplotconnectpoints(xpos, ypos, i, 0)

    plt.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
             markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
             markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])


# def matplot_esau_william(_list, MAX):
#     xpos = []
#     ypos = []
#     npos = []
#     for i in _list:
#         xpos.append(i.get_position_x())
#         ypos.append(i.get_position_y())
#         npos.append(i.get_name())
#
#     plt.text(xpos[0], ypos[0], str(_list[0].get_name()), color='white', size=10, rotation=0.,
#              ha="center", va="center",
#              bbox=dict(facecolor=(1., 0., 0.), edgecolor='black', boxstyle='round')
#              )
#     for i in range(1,len(_list)):
#         plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
#                  ha="center", va="center",
#                  bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
#                  )
#
#     for i in range(1, len(_list)):
#
#         for j in _list[i].get_list_connect():
#             matplotconnectpoints(xpos, ypos, i, find_index_node(j, _list), _list)
#
#
#     plt.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
#              markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))
#
#     plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
#              markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))


def matplot_mentor(_list_mentor,MAX):
    for _list in _list_mentor:
        xpos = []
        ypos = []
        npos = []
        for i in _list:
            xpos.append(i.get_position_x())
            ypos.append(i.get_position_y())
            npos.append(i.get_name())

        plt.text(xpos[0], ypos[0], str(_list[0].get_name()), color='white', size=10, rotation=0.,
                 ha="center", va="center",
                 bbox=dict(facecolor=(1., 0., 0.), edgecolor='black', boxstyle='round')
                 )
        for i in range(1, len(_list)):
            plt.text(xpos[i], ypos[i], str(_list[i].get_name()), color='black', size=10, rotation=0.,
                     ha="center", va="center",
                     bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
                     )

        plt.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

        plt.plot(xpos[0], ypos[0], 'ro', markersize=10, markerfacecolor='r',
                 markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))
    plt_margin = MAX * 0.05
    plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])

def matplot_mentor_circle(_list_mentor, MAX, RM):
    from matplotlib.patches import Circle
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    for _list in _list_mentor:
        xpos = []
        ypos = []
        npos = []

        for i in _list:
            xpos.append(i.get_position_x())
            ypos.append(i.get_position_y())
            npos.append(i.get_name())

        # Plot mentor node (first node in the list)
        mentor_x = xpos[0]
        mentor_y = ypos[0]

        ax.text(
            mentor_x, mentor_y, str(_list[0].get_name()),
            color='white', size=10, rotation=0.,
            ha="center", va="center",
            bbox=dict(facecolor=(1., 0., 0.), edgecolor='black', boxstyle='round')
        )

        # Draw a circle around the mentor node
        mentor_circle = Circle((mentor_x, mentor_y), radius=RM,
                               fill=False, linestyle='--', color='blue', linewidth=1.5)
        ax.add_patch(mentor_circle)

        # Plot other nodes in the group
        for i in range(1, len(_list)):
            ax.text(
                xpos[i], ypos[i], str(_list[i].get_name()),
                color='black', size=10, rotation=0.,
                ha="center", va="center",
                bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round')
            )

            # Draw connection line from node to mentor
            ax.plot([mentor_x, xpos[i]], [mentor_y, ypos[i]],
                    linestyle='-', color='gray', linewidth=1)

        # Plot all node positions (red outline, white center)
        ax.plot(xpos, ypos, 'ro', markersize=5, markerfacecolor='w',
                markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

        # Emphasize the mentor node
        ax.plot(mentor_x, mentor_y, 'ro', markersize=10, markerfacecolor='r',
                markeredgewidth=1.5, markeredgecolor=(0, 0, 0, 1))

    # Set plot limits
    plt_margin = MAX * 0.05
    ax.set_xlim([-plt_margin, MAX + plt_margin])
    ax.set_ylim([-plt_margin, MAX + plt_margin])
    ax.set_aspect('equal')
    plt.title("Mentor Nodes with Coverage Radius & Connections")
    plt.show()


# def matplot_total(_list,MAX):
#     for i in _list:
#         matplot_esau_william(i, MAX)
#     plt_margin = MAX * 0.05
#     plt.axis([-plt_margin, MAX + plt_margin, -plt_margin, MAX + plt_margin])



def visualize_backbone_with_access_and_radius(ListMentor, Parent, MAX, RM):
    from matplotlib.patches import Circle
    from matplotlib.widgets import CheckButtons
    fig, ax = plt.subplots(figsize=(8, 6))
    ListNode = [mentor[0] for mentor in ListMentor]
    circles = []  # keep track of coverage circles

    # --- draw backbone edges ---
    for i in range(len(ListNode)):
        if Parent[i] != -1:
            child = ListNode[i]
            parent = ListNode[Parent[i]]
            ax.plot(
                [child.get_position_x(), parent.get_position_x()],
                [child.get_position_y(), parent.get_position_y()],
                'k--'
            )

    # --- draw backbone nodes (+ circles, hidden by default) ---
    for i, node in enumerate(ListNode):
        x, y = node.get_position_x(), node.get_position_y()
        if Parent[i] == -1:  # root
            ax.text(x, y, str(node.get_name()), color="white", size=10,
                     ha="center", va="center",
                     bbox=dict(facecolor=(1., 0., 0.), edgecolor='black', boxstyle='round'))
            ax.plot(x, y, 'ro', markersize=10, markerfacecolor='r',
                     markeredgewidth=1.5, markeredgecolor='black')
        else:
            ax.text(x, y, str(node.get_name()), color="black", size=10,
                     ha="center", va="center",
                     bbox=dict(facecolor=(1., 0.8, 0.8), edgecolor='none', boxstyle='round'))
            ax.plot(x, y, 'ro', markersize=5, markerfacecolor='w',
                     markeredgewidth=1.5, markeredgecolor='black')

        # prepare coverage circle (hidden initially)
        coverage_circle = Circle((x, y), radius=RM,
                                 fill=False, linestyle='--', color='blue', linewidth=1.2)
        coverage_circle.set_visible(False)  # start hidden
        ax.add_patch(coverage_circle)
        circles.append(coverage_circle)

    # --- draw access nodes (always visible) ---
    for mentor in ListMentor:
        backbone = mentor[0]
        for access_node in mentor[1:]:
            x, y = access_node.get_position_x(), access_node.get_position_y()
            ax.plot(
                [x, backbone.get_position_x()],
                [y, backbone.get_position_y()],
                'g:'
            )
            ax.text(x, y, str(access_node.get_name()), color="blue", size=8,
                     ha="center", va="center",
                     bbox=dict(facecolor=(0.8, 0.9, 1.0), edgecolor='none', boxstyle='round'))
            ax.plot(x, y, 'bo', markersize=4, markerfacecolor='cyan',
                     markeredgewidth=1.0, markeredgecolor='blue')

    # --- setup plot ---
    plt_margin = MAX * 0.05
    ax.set_xlim(-plt_margin, MAX + plt_margin)
    ax.set_ylim(-plt_margin, MAX + plt_margin)
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Kết nối sau Prim-Djikstra")

    # --- interactive checkbox for radius toggle ---
    rax = plt.axes([0.8, 0.7, 0.15, 0.15])  # position of checkbox
    check = CheckButtons(rax, ["Show Radius"], [False])

    def toggle(label):
        for c in circles:
            c.set_visible(not c.get_visible())
        plt.draw()

    check.on_clicked(toggle)
    plt.show()






