# --- NHẬN DỮ LIỆU TỪ NGƯỜI DUNG ---
ten = input("Nhập tên nhân viên:")
so_ngay_lam = input("Nhập số ngày làm:")
luong_ngay = input("Nhập lương ngày (VNĐ):")
ngay_nghi = input("Nhập số ngày nghỉ phép:")

# --- CHUYỂN ĐỔI KIỂU DỮ LIỆU ---
so_ngay_lam = int(so_ngay_lam)
luong_ngay = int(luong_ngay)
ngay_nghi = int(ngay_nghi)

# --- TÍNH TOÁN ---
tong_luong = (so_ngay_lam-ngay_nghi) * luong_ngay
luong_sau_thue = tong_luong * 0.9

# --- IN KẾT QUẢ ĐẸP VỚI F-STRING ---
print(f"--- BẢNG LƯƠNG ---")
print(f"Nhân viên       : {ten}")
print(f"Số ngày làm     : {so_ngay_lam}")
print(f"Số ngày nghỉ    : {ngay_nghi}")
print(f"Lương ngày      : {luong_ngay:,} VNĐ")
print(f"Tổng lương      : {tong_luong:,} VNĐ")
print(f"Lương sau thuế  : {luong_sau_thue:,.0f} VNĐ")
