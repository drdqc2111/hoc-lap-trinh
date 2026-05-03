# TẠO LIST - DANH SÁCH CÓ THỨ TỰ
    # san_pham = ["cà phê", "bánh mì", "sữa"]

    # # Truy cập theo vị trí (bắt đầu từ 0)
    # print(san_pham[0])   # → cà phê
    # print(san_pham[1])   # → bánh mì
    # print(san_pham[-1])  # → sữa (đếm từ cuối)

    # # Thêm/xóa
    # san_pham.append("nước")      # thêm vào cuối
    # san_pham.remove("bánh mì")   # xóa theo giá trị

    # # Độ dài
    # print(len(san_pham))  # → 3

# TẠO DICTIONARY - TỪ ĐIỂN KEY-VALUE
    # nhan_vien = {
    #     "ten": "Cường",
    #     "tuoi": 25,
    #     "luong": 9_900_000,
    #     "phong_ban": "Kỹ thuật"
    # }

    # # Truy cập theo key
    # print(nhan_vien["ten"])       # → Cường
    # print(nhan_vien["luong"])     # → 9900000

    # # Thêm/sửa
    # nhan_vien["email"] = "cuong@company.com"  # thêm key mới
    # nhan_vien["luong"] = 11_000_000           # sửa giá trị

    # # Kiểm tra key có tồn tại không
    # if "email" in nhan_vien:
    #     print("Có email!")
# KẾT HỢP: LIST OF DICTIONARIES
    # danh_sach = [
    #     {"ten": "Cường", "luong": 9_900_000},
    #     {"ten": "An",    "luong": 10_260_000},
    #     {"ten": "Bình",  "luong": 13_440_000},
    # ]

    # for nv in danh_sach:
    #     print(f"{nv['ten']}: {nv['luong']:,} VNĐ")

# ============================================
# BÀI 6 — LIST & DICTIONARY
# ============================================

# --- PHẦN 1: List cơ bản ---
diem_thi = [8.5, 7.0, 9.0, 6.5, 8.0]

tong = sum(diem_thi)
trung_binh = tong / len(diem_thi)
cao_nhat = max(diem_thi)
thap_nhat = min(diem_thi)

print("=== KẾT QUẢ THI ===")
print(f"Số bài thi  : {len(diem_thi)}")
print(f"Điểm TB     : {trung_binh:.1f}")
print(f"Cao nhất    : {cao_nhat}")
print(f"Thấp nhất   : {thap_nhat}")

print()

# --- PHẦN 2: Dictionary ---
san_pham = {"ten": "Cà phê sữa", 
            "gia": 45_000, 
            "so_luong": 100, 
            "con_hang": True}
print("=== THÔNG TIN SẢN PHẨM ===")
for key, value in san_pham.items():
    print(f"{key:12}: {value}")

print()

# --- PHẦN 3: List of Dictionaries ---
kho_hang = [
    {"ten": "Cà phê sữa",   "gia": 45_000, "so_luong": 100},
    {"ten": "Trà đào",      "gia": 40_000, "so_luong": 50},
    {"ten": "Sinh tố bơ",   "gia": 55_000, "so_luong": 30},
]
kho_hang.append({"ten": "Trà đá", "gia": 20_000, "so_luong": 20})
print("=== KHO HÀNG ===")
tong_gia_tri = 0
for sp in kho_hang:
    gia_tri = sp["gia"] * sp["so_luong"]
    tong_gia_tri += gia_tri
    print(f"{sp['ten']:15}: {gia_tri:>12,} VNĐ")

print(f"{'Tổng kho':15}: {tong_gia_tri:>12,} VNĐ")

