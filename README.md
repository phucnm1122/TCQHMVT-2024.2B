TCQHMVT-2024.2B

Source code: https://github.com/xcourtesy/ToChucQuyHoachMangVienThong20182.git

Phiên bản Python sử dụng: 3.10
IDE: Pycharm 2025.1

Đề 1. Cho mạng gồm 100 nút. Các nút được đặt một cách ngẫu nhiên trên mặt phẳng kích
thước 1000x1000. Giá của mỗi liên kết được tính bẳng round (0.4x khoảng cách đề các). 
1. Xuất file lưu thông tin về mạng theo kiểu danh sách cạnh.
W=2, R=0,3. dung lượng liên kết C=16.Lưu lượng giữa nút i và i+46 là 1, và lưu lượng
giữa i và i+96 là 6, lưu lượng giữa nút 2 và 23 là 22, lưu lượng giữa 60 và 99 là 28 và lưu lượng
giữa 20 và 68 là 38. Lưu lượng giữa nút 45 và 29 là 10.
1. Sử dụng giải thuật MENTOR để tìm nút backbone và các nút truy nhập tương ứng với nút
Backbone. ( ghi kết quả ra file)
Tính lưu lượng giữa các nút, trọng số của các nút và lưu lượng thực tế đi qua các nút backbone
(ghi ra file)
2.Sử dụng giải thuật Mentor để tính topology mạng Backbone biết umin =85%. α =0.2 Đưa
ra kết quả ra file số đường sử dụng trên từng liên kết và độ sử dụng trên liên kết đó.
3. Nếu tăng thêm lưu lượng giữa nút 3 và 20 là 3, lưu lượng giữa nút 13 và 67 là 4, lưu lượng
giữa 15 và 30 là 3 và lưu lượng giữa 40 và 58 là 5 thì mạng backbone vừa tạo ra ở mục 2 thay đổi
tại những liên kết nào. Ghi ra file kết quả số đường sử dụng trên từng liên kết và độ sử dụng trên
liên kết đó. ( Giả sử các nút backbones là không thay đổi).
4. Nếu tăng thêm lưu lượng giữa các nút lên 10% , 20% ,50% thì mạng backbone và giá của
mạng backbone vừa tạo ra ở mục 2 thay đổi như thế nào. Ghi ra file kết quả số đường sử dụng trên
từng liên kết và độ sử dụng trên liên kết đó. Đưa ra đánh giá và nhận xét.

Để chạy chương trình, mở file Main.py và Run

Các tham số có thể điều chỉnh tùy theo bài toán:

File Main.py
<pre>
  MAX = 1000 # MAX là thông số độ dài cạnh của mặt phẳng hình vuông kích thước MAX*MAX, nơi các nút được đặt lên.
  NumNode = 100 # Số lượng nút trong mạng
  RadiusRatio = 0.3 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
  C = 16 # Dung lượng 1 liên kết
  w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
  alpha = 0.2
  umin = 0.85
</pre>

File InitialTopo.py: Điều chỉnh lưu lượng giữa 2 nút 

<pre>
    for i in range(NumNode):

        if i + 46 < NumNode:
            set_traffic0(i, i + 46, 1)
        if i + 96 < NumNode:
            set_traffic0(i, i + 96, 6)

    set_traffic(2, 23, 22)
    set_traffic(60, 99, 28)
    set_traffic(20, 68, 38)
    set_traffic(45, 29, 10)
</pre>
