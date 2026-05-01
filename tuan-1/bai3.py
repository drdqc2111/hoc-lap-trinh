# --- TÍNH LƯƠNG CÓ KIỂM TRA HỢP LỆ ---

ten = input("Nhập tên nhân viên: ")
so_ngay_lam = int(input("Nhập số ngày làm: "))
ngay_nghi = int(input("Nhập số ngày nghỉ phép: "))
luong_ngay = int(input("Nhập lương ngày (VNĐ): "))

# --- KIỂM TRA HỢP LỆ ---
if ngay_nghi > so_ngay_lam:
    print("❌ Lỗi: Số ngày nghỉ không thể lớn hơn số ngày làm!")
elif ngay_nghi < 0:
    print("❌ Lỗi: Số ngày nghỉ không thể âm!")
else:
    ngay_thuc_te = so_ngay_lam - ngay_nghi

    # Thưởng chuyên cần — NẰM TRONG ELSE
    if ngay_nghi == 0:
        thuong = 500000
        print("🌟 Chuyên cần! Được thưởng 500,000 VNĐ")
    else:
        thuong = 0

    # Tính lương — NẰM TRONG ELSE
    tong_luong = ngay_thuc_te * luong_ngay
    luong_sau_thue = tong_luong * 0.9
    tong_thu_nhap = luong_sau_thue + thuong

    # In kết quả — NẰM TRONG ELSE
    print(f"\n--- BẢNG LƯƠNG: {ten} ---")
    print(f"Ngày làm thực tế : {ngay_thuc_te} ngày")
    print(f"Lương sau thuế   : {luong_sau_thue:,.0f} VNĐ")
    print(f"Thưởng chuyên cần: {thuong:,} VNĐ")
    print(f"Tổng thu nhập    : {tong_thu_nhap:,.0f} VNĐ")