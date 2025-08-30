import Node
import InitialTopo
import MENTOR

import PrimDjikstra
import directConnectBackbone
MAX = 1000 # MAX là thông số độ dài cạnh của mặt phẳng hình vuông kích thước MAX*MAX, nơi các nút được đặt lên.
NumNode = 100 # Số lượng nút trong mạng
RadiusRatio = 0.3 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
C = 16 # Dung lượng 1 liên kết
w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
alpha = 0.2
umin = 0.85

# ListPosition, TrafficMatrix = InitialTopo.Global_Init_Topo(MAX,NumNode,True)
ListPosition,TrafficMatrix = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,True)
# False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị

ListMentor,RM, access_dict, backbones = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,0,True)
T_b = directConnectBackbone.calc_backbone_traffic(TrafficMatrix,backbones,access_dict)

# 5: Là số giới hạn nút đầu cuối của thuật toán MENTOR.
# Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt của một mạng truy nhập tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
# False/ True: Bật tắt giám sát thuật toán

# ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,5,False)
# False/ True: Bật tắt giám sát thuật toán
# 5: Giới hạn số nút trên cây truy nhập. Nếu đặt bằng 0 thì không giới hạn.

ListNode, Parent, ListTree = PrimDjikstra.PrimDjikstra(ListMentor, alpha)
Node.visualize_backbone_with_access_and_radius(ListMentor, Parent, MAX, RM)

directConnectBackbone.optimize_and_visualize_backbone(
    TrafficFile="BackboneTraffic.csv",
    ListMentor=ListMentor,
    MAX=MAX,
    RM=RM,
    C=C,
    umin=umin,
    center_node=ListTree[0],
    OutputFile="OptimizedBackbone.csv"
)

# Node.printList2D(ListFinish)
# Node.matplot_total(ListFinish,MAX)
# Node.plt.show()
