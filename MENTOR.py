# Thư viện
import random
import math
import matplotlib.pyplot as plt
import Node
import csv
num_inf = math.inf
num_ninf = -math.inf

# Các cài đặt mặc định

def MenTor(ListPosition,MAX,C,w,RadiusRatio,Limit,DeBug):
    ListMentor = []
    '''

    Bước 2: Tìm Nút Backbone và phân cây truy nhập dựa trên thuật toán MENTOR

    '''
    print("{:*<100}".format(''))
    print("Bước 2: Tìm Nút Backbone và phân cây truy nhập dựa trên thuật toán MENTOR")
    print("{:*<100}".format(''))

    ListBackboneType1 = []

    for i in ListPosition:
        if i.get_traffic() / C > w:
            # i.print()
            ListBackboneType1.append(i)
            ListPosition.remove(i)

    if DeBug:
        print("2.1. List Backbone do lưu lượng chuẩn hóa lớn hơn ngưỡng")
        Node.printMentorList(ListBackboneType1)


    # Tìm MaxCost
    if DeBug:
        print("Tìm MaxCost và R*MaxCost")
    MaxCost = 0
    for i in range(len(ListPosition)):
        for j in range(i + 1, len(ListPosition)):
            dc = math.sqrt((ListPosition[i].get_position_x() - ListPosition[j].get_position_x()) ** 2 + (
                    ListPosition[i].get_position_y() - ListPosition[j].get_position_y()) ** 2)
            if dc > MaxCost:
                # print(ListPosition[i].get_name(), ListPosition[j].get_name(), dc)
                MaxCost = dc

    RM = RadiusRatio * MaxCost
    if DeBug:
        print('MaxCost = {:<8} & R*MaxCost = {:<8}'.format(round(MaxCost,3), round(RM,3)))

    # Dựng hàm cập nhật các nút đầu cuối cho các nút backbone

    DEBUG_UpdateTerminalNode = 0

    def updateTerminalNode(_ListPosition, _ListMentor, _centerNode):

        if DEBUG_UpdateTerminalNode:
            print("Enter Update Terminal Node Function! ")
            print("Node backbone", _centerNode.get_name())

        # Kiểm tra khoảng cách các node so với node backbone
        ListBackbone = []
        ListBackbone.append(_centerNode)

        def check_non_exist(index,listbackbone,listmentor):
            if DEBUG_UpdateTerminalNode:
                for i in listbackbone:
                    print(i.get_name(),end =' ')
                print()
                for i in listmentor:
                    for j in i:
                        print(j.get_name(), end=' ')
                print()
            for i in listbackbone:
                if i.get_name() == index:
                    if DEBUG_UpdateTerminalNode:
                        print("in list backbone. no check any more")
                    return False
            for i in listmentor:
                for j in i:
                    if j.get_name() == index:
                        if DEBUG_UpdateTerminalNode:
                            print("in list mentor. no check any more")
                        return False
            return True

        #Node.printList(_ListPosition)
        for i in _ListPosition:
            i.set_distance(_centerNode)
            if DEBUG_UpdateTerminalNode:
                print("Check Distance Node", i.get_name(), " : ", i.get_distance())
            if check_non_exist(i.get_name(),ListBackbone,_ListMentor):
                if i.get_distance() <= RM:
                    if DEBUG_UpdateTerminalNode:
                        print("Node", i.get_name(), "is terminal node of Node center", _centerNode.get_name())
                    ListBackbone.append(i)

        # Xử lý giới hạn số nút đầu cuối của nút backbone

        def sort_by_distance_to_backbone(m):
            return  m.get_distance()

        ListBackbone.sort(key=sort_by_distance_to_backbone)

        if Limit > 0:
            if DEBUG_UpdateTerminalNode:
                for i in ListBackbone:
                    print(i.get_name(),end =' ')
                print()
            if len(ListBackbone)-1 > Limit:
                ListBackbone = ListBackbone[0:Limit+1]
            if DEBUG_UpdateTerminalNode:
                for i in ListBackbone:
                    print(i.get_name(),end =' ')
                print()



        _ListMentor.append(ListBackbone)

        for i in ListBackbone:
            for j in _ListPosition:
                if i.get_name() == j.get_name():
                    _ListPosition.remove(j)

        if DEBUG_UpdateTerminalNode:
            print("Exit Update Terminal Node Function! ")


    for i in ListBackboneType1:
        updateTerminalNode(ListPosition, ListMentor, i)

    del ListBackboneType1
    if DeBug:
        print("-----------Danh sách các nút Backbone và cây truy nhập đi kèm sau khi tìm Backbone dựa trên ngưỡng lưu lượng -----------")

        Node.printList2D(ListMentor)

        print("-----------Dach sách các nút còn lại chưa được phân cây truy nhập-----------")

        Node.printMentorList(ListPosition)


    '''

    Bước 3: Đối với các nút còn lại, tiến hành tìm nút backbone dựa trên giá trị thưởng, sau đó cập nhật các nút đầu cuối

    '''
    if DeBug:
        print()
        print(
        "2.2. Đối với các nút còn lại, tiến hành tìm nút Backbone dựa trên giá trị thưởng, sau đó cập nhật cây truy nhập tương ứng với nút Backbone mới")
        print()
    center = Node.Node()
    iloop = 1
    while len(ListPosition) > 0:
        if DeBug:
            print("Vòng lặp tìm giá trị thưởng lần", iloop)
        iloop = iloop + 1
        # Tìm trung tâm trọng lực
        sumx = 0
        sumy = 0
        sumw = 0
        xtt = 0
        ytt = 0
        maxw = 1
        maxdc = 1
        maxaward = 0
        indexBB = 0

        for i in ListPosition:
            sumx = sumx + (i.get_position_x()) * i.get_traffic()
            sumy = sumy + (i.get_position_y()) * i.get_traffic()
            sumw = sumw + i.get_traffic()
            if i.get_traffic() > maxw:
                maxw = i.get_traffic()
        xtt = sumx / sumw
        ytt = sumy / sumw

        center.set_position(xtt, ytt)

        if DeBug:
            center.printCenterPress()

        for i in ListPosition:
            i.set_distance(center)
            if i.get_distance() > maxdc:
                maxdc = i.get_distance()
        if DeBug:
            print("MaxDistance = {:<6} & Max Weight: {:<3}".format(round(maxdc,2), maxw))
        for i in ListPosition:
            i.set_award((0.5 * (maxdc - i.get_distance() / maxdc)) + (0.5 * i.get_traffic() / maxw))
            if i.get_award() > maxaward:
                maxaward = i.get_award()

        for i in ListPosition:
            if i.get_award() >= maxaward:
                e = Node.Node()
                e.copyNode(i)
                if DeBug:
                    print("Nút Thưởng được chọn làm backbone: {:<3}".format(e.get_name()))
                ListPosition.remove(i)
                if DeBug:
                    print("--- Danh sách các nút còn lại sau khi bỏ nút backbone ---")
                    Node.printMentorList(ListPosition)
                if DeBug:
                    print("---------------------")
                if DeBug:
                    print("Cập nhật cây truy nhập cho nút backbone mới")
                updateTerminalNode(ListPosition, ListMentor, e)
                if DeBug:
                    print("---------------------")
                    print("--- Danh sách các nút còn lại sau khi cập nhật cây truy nhập cho nút backbone mới ---")
                    Node.printMentorList(ListPosition)
                    print("---------------------")
                break
    '''
    
    Tính toán cost của từng liên kết
    
    '''

    for ListPosition in ListMentor:
        NumNode = len(ListPosition)

        if DeBug:
            print("Số nút đầu cuối: {:<3}\n".format(NumNode-1))
            for i in ListPosition:
                print(i.get_name(), end=' ')
            print()
        if DeBug:
            print("Xây dựng ma trận giá thành liên kết giữa các nút:\n")
        link_cost = [[num_inf] * NumNode for i in range(NumNode)]

        def print_linkcostmatrix(_link_cost):
            for i in range(len(_link_cost)):
                for j in range(len(_link_cost[i])):
                    print("{:<8}".format(_link_cost[i][j]), end='\t')
                print()

        def set_linkcost(_link, i, j, c):
            _link[i][j] = c
            _link[j][i] = c

        # Xây dựng hàm cập nhật giá theo distance (cost = distance)

        def calc_distance_2Dpoint(a, b):
            return round(math.sqrt(
                (a.get_position_x() - b.get_position_x()) ** 2 + (a.get_position_y() - b.get_position_y()) ** 2), 4)

        def link_cost_by_distance(_list, _link_cost):
            for i in range(len(_list)):
                for j in range(i + 1, (len(_list))):
                    set_linkcost(_link_cost, i, j, round(0.4*calc_distance_2Dpoint(_list[i], _list[j]),4))

        link_cost_by_distance(ListPosition, link_cost)

        # print_linkcostmatrix(link_cost)

        # Cập nhật giá về nút trung tâm ban đầu
        for i in range(1, len(ListPosition)):
            ListPosition[i].set_cost_to_center(link_cost[0][i])

    # Tạo access_dict từ ListMentor
    access_dict = {}
    for group in ListMentor:
        backbone = group[0]
        access_nodes = group[1:]
        access_dict[backbone.get_name()] = [node.get_name() for node in access_nodes]

    # Tạo access_dict từ ListMentor
    access_dict = {}
    for group in ListMentor:
        backbone = group[0]
        access_nodes = group[1:]
        access_dict[backbone.get_name()] = [node.get_name() for node in access_nodes]

    # Tạo list backbones từ ListMentor
    backbones = [group[0].get_name() for group in ListMentor]

    '''

    Kết thúc thuật toán, hiển thị kết quả

    '''

    if DeBug:
        print("-------Kết quả thuật toán Mentor-------")

        for i in ListMentor:
            for j in i:
                print(j.get_name(), end=' ')
            print()

    print("------Xuất file lưu thông tin về mạng kiểu danh sách cạnh------")
    with open("mentor_output.txt", "w") as f:
        for i in ListMentor:
            backbone = i[0]
            if len(i) > 1:
                for j in range(1, len(i)):
                    line = f"({backbone.get_name()}, {i[j].get_name()}, {i[j].get_cost_to_center()})"
                    f.write(line)
            f.write("\n")  # new line after each mentor group

    # Xuất file CSV chứa trọng số (traffic) của từng nút
    with open("mentor_weights.csv", mode="w", newline="", encoding="utf-8") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(["Node", "Traffic", "Backbone"])
        for group in ListMentor:
            backbone = group[0]
            for node in group:
                writer.writerow([node.get_name(), node.get_traffic(), backbone.get_name()])

    Node.matplot_mentor_circle(ListMentor,MAX,RM)
    Node.plt.show()
    return ListMentor, RM, access_dict, backbones