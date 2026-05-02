"""# Giải phẫu một hàm
def tinh_tong(a,b) # def = define (định nghĩa)
    ket_qua = a + b
    return ket_qua
## Gọi hàm
x = tinh_tong(3, 5) # x = 8
y = tinh_tong(10, 20) # y = 30"""


# ============================================
# BÀI 5 — HÀM (FUNCTION)
# ============================================

def tinh_thuong(ngay_nghi):
    """Trả về tiền thưởng dựa trên số ngày nghỉ."""
    if ngay_nghi == 0:
        return 500_000
    elif 1 <= ngay_nghi <= 2:
        return 200_000
    return 0  # không cần else nếu đã return ở trên


def tinh_luong(so_ngay_lam, ngay_nghi, luong_ngay, thue=0.1):
    """Trả về tổng thu nhập sau thuế và thưởng."""
    ngay_thuc_te = so_ngay_lam - ngay_nghi
    luong_sau_thue = ngay_thuc_te * luong_ngay * (1 - thue)
    thuong = tinh_thuong(ngay_nghi)
    return luong_sau_thue, thuong  # trả về 2 giá trị cùng lúc


def xep_loai(tong_thu_nhap):
    """Xếp loại dựa trên tổng thu nhập."""
    if tong_thu_nhap >= 15_000_000:
        return "⭐ Xuất sắc"
    elif tong_thu_nhap >= 10_000_000:
        return "✅ Tốt"
    elif tong_thu_nhap >= 5_000_000:
        return "🆗 Trung bình"
    return "⚠️ Cần cải thiện"


def in_bang_luong(ten, luong_sau_thue, thuong):
    """In bảng lương đẹp cho một nhân viên."""
    tong = luong_sau_thue + thuong
    loai = xep_loai(tong)
    print(f"{'='*15}")
    print(f"  Nhân viên  : {ten}")
    print(f"  Lương      : {luong_sau_thue:>12,.0f} VNĐ")
    print(f"  Thưởng     : {thuong:>12,} VNĐ")
    print(f"  Tổng       : {tong:>12,.0f} VNĐ")
    print(f"  Xếp loại   : {loai}")
    print(f"{'='*15}")


# ============================================
# SỬ DỤNG
# ============================================
nhan_vien = [
    ("Cường", 22, 0, 500_000, 0.1),
    ("An",    22, 3, 600_000, 0.1),
    ("Bình",  22, 1, 800_000, 0.2),
]

for ten, so_ngay, ngay_nghi, luong_ngay, thue in nhan_vien:
    luong, thuong = tinh_luong(so_ngay, ngay_nghi, luong_ngay, thue)
in_bang_luong(ten, luong, thuong)