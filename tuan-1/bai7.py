# ============================================
# BÀI 7 — ĐỌC/GHI FILE & XỬ LÝ LỖI
# ============================================
import csv

# --- PHẦN 1: ĐỌC FILE CSV ---
def doc_file_csv(ten_file):
    """Đọc file CSV, trả về list of dictionaries."""
    danh_sach = []
    try:
        with open(ten_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for dong in reader:
                danh_sach.append(dong)
        print(f"✅ Đọc thành công {len(danh_sach)} nhân viên!")
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {ten_file}")
    return danh_sach

# --- PHẦN 2: TÍNH LƯƠNG ---
def tinh_luong(nv, thue = 0.1):
    """Nhận dict nhân viên, trả về lương sau thuế."""
    so_ngay = int(nv["so_ngay_lam"]) - int(nv["ngay_nghi"])
    luong_ngay = int(nv["luong_ngay"])
    return so_ngay * luong_ngay * (1 - thue)

# --- PHẦN 3: GHI KẾT QUẢ RA FILE ---
def ghi_ket_qua(danh_sach, ten_file):
    """Ghi kết quả lương ra file CSV mới."""
    with open(ten_file, "w", encoding="utf-8", newline ="") as f:
        fieldnames = ["ten", "luong_sau_thue"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for nv in danh_sach:
            luong = tinh_luong(nv)
            writer.writerow({
                "ten": nv["ten"],
                "luong_sau_thue": f"{luong:,.0f}"})
    print(f"✅ Đã ghi kết quả ra file: {ten_file}")

# --- CHẠY CHƯƠNG TRÌNH ---
print("=== HỆ THỐNG TÍNH LƯƠNG ===\n")

# Đọc file
danh_sach_nv = doc_file_csv("nhan_vien.csv")

if danh_sach_nv:
    # In ra màn hình
    print("\n=== BẢNG LƯƠNG ===")
    tong = 0
    for nv in danh_sach_nv:
        luong = tinh_luong(nv)
        tong += luong
        print(f"{nv['ten']:10}: {luong:>12,.0f} VNĐ")
    print(f"{'TỔNG':10}: {tong:>12,.0f} VNĐ")

    # Ghi ra file
    print()
    ghi_ket_qua(danh_sach_nv, "ket_qua_luong.csv")

# Test xử lý lỗi
print("\n--- Test lỗi ---")
doc_file_csv("file_khong_ton_tai.csv")