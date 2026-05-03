# for --- dùng khi biết trước số lần lặp
# while --- dùng khi chưa biết số lần lặp, chỉ biết điều kiện dừng
# ============================================
# BÀI 4 - VÒNG LẶP
# ============================================

# --- PHẦN 1: for loop cơ bản ---
print("=== BẢNG CƯU CHƯƠNG 7 ===")
for i in range(1, 11):
    print(f"7 x {i:2} = {7 * i}")
print() # in dòng trông cho đẹp

# --- PHẦN 2: Tính tổng doanh thu ---
print("=== NHẬP DOANH THU 5 NGÀY ===")
tong_doanh_thu = 0

for ngay in range(1, 6):
    doanh_thu = int(input(f"Doanh thu ngày {ngay}: "))
    tong_doanh_thu += doanh_thu

trung_binh = tong_doanh_thu / 5
print(f"\n Tổng doanh thu   :   {tong_doanh_thu:,} VNĐ")
print(f"Trung bình/ngày     :   {trung_binh:,.0f} VNĐ")

print()

# --- PHẦN 3: while loop ---
print("=== ĐẶT MẬT KHẨU ===")
mat_khau_dung = "python123"
so_lan_thu = 0

while so_lan_thu < 3:
    nhap_vao = input("Nhập mật khẩu: ")
    so_lan_thu += 1

    if nhap_vao == mat_khau_dung:
        print("✅ Đăng nhập thành công!")
        break # thoát vòng lặp ngay lập tức
    else:
        con_lai = 3 - so_lan_thu
        if con_lai > 0:
            print(f"❌ Sai mật khẩu! Còn {con_lai} lần thử.")
if so_lan_thu == 3 and nhap_vao != mat_khau_dung:
    print("🔒 Tài khoản bị khóa!")

# --- VIẾT VÒNG LẶP TÍNH TỔNG TẤT CẢ SỐ CHẴN TỪ 1 ĐẾN 100. KẾT QUẢ ĐÚNG LÀ 25500
## Dùng vòng lặp for với bước nhảy là 2
tong = 0
for i in range(2, 101, 2):
    tong += i
print(f"Tổng các số chẵn từ 1 đến 100 là: {tong}")
