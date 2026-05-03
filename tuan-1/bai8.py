# ============================================
# BÀI 8 — OOP: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG
# ============================================

class NhanVien:
    """Bản thiết kế cho một nhân viên."""
    
    # --- KHỞI TẠO ---
    def __init__(self, ten, luong_ngay, so_ngay_lam = 22, thue=0.1):
        self.ten = ten
        self.luong_ngay = luong_ngay
        self.so_ngay_lam = so_ngay_lam
        self.ngay_nghi = 0
        self.thue = thue
    
    # --- HÀNH ĐỘNG ---
    def nghi_phep(self, so_ngay):
        """Đăng ký nghỉ phép."""
        if so_ngay > self.so_ngay_lam:
            print(f"❌ {self.ten} không thể nghỉ {so_ngay} ngày!")
        else:
            self.ngay_nghi = so_ngay
            print(f"✅ {self.ten} đã đăng ký nghỉ {so_ngay} ngày.")
    
    def tinh_luong(self):
        """Tính lương sau thuế."""
        ngay_thuc_te = self.so_ngay_lam - self.ngay_nghi
        tong = ngay_thuc_te * self.luong_ngay
        return tong * (1 - self.thue)
    
    def tinh_thuong(self):
        """Tính thưởng chuyên cần."""
        if self.ngay_nghi == 0:
            return 500_000
        elif 1 <= self.ngay_nghi <= 2:
            return 200_000
        return 0
    
    def xep_loai(self):
        """Xếp loại nhân viên."""
        tong = self.tinh_luong() + self.tinh_thuong()
        if tong >= 15_000_000:
            return "⭐ Xuất sắc"
        elif tong >= 10_000_000:
            return "✅ Tốt"
        elif tong >= 5_000_000:
            return "🆗 Trung bình"
        return "⚠️ Cần cải thiện"
    
    def in_bang_luong(self):
        """In bảng lương đẹp."""
        luong = self.tinh_luong()
        thuong = self.tinh_thuong()
        tong = luong + thuong
        print(f"{'='*30}")
        print(f"    Nhân viên   : {self.ten}")
        print(f"    Lương       : {luong:>12,.0f} VNĐ")
        print(f"    Thưởng      : {thuong:>12,} VNĐ")
        print(f"    Tổng        : {tong:>12,.0f} VNĐ")
        print(f"    Xếp loại    : {self.xep_loai()}")
        print(f"{'='*30}")

# ============================================
# SỬ DỤNG
# ============================================

# Tạo nhân viên
cuong = NhanVien("Cường", 500_000)
an    = NhanVien("An",    600_000)
binh  = NhanVien("Bình",  800_000, thue=0.2)

# Đăng ksy nghỉ phép
cuong.nghi_phep(3)
binh.nghi_phep(1)

print()

# In bảng lương
cuong.in_bang_luong()
an.in_bang_luong()
binh.in_bang_luong()

# THÊM PHÒNG BAN

class PhongBan:
    def __init__(self,ten_phong):
        self.ten_phong = ten_phong
        self.nhan_vien = []

    def them_nhan_vien(self,nv):
        self.nhan_vien.append(nv)
        # thêm vn vào self.nhan_vien
        # gợi ý: dùng append()
    def tong_quy_luong(self):
        tong = 0
        for nv in self.nhan_vien:
            tong += nv.tinh_luong()
        return tong
        # cộng lương tất cả nhân viên lại
        # gợi ý: vòng lặp for + tinh_luong()

# Tạo phòng ban
phong_kt = PhongBan("Kỹ thuật")

# Thêm nhân viên vào phòng
phong_kt.them_nhan_vien(cuong)
phong_kt.them_nhan_vien(an)
phong_kt.them_nhan_vien(binh)

# In tổng quỹ lương
print(f"Phòng {phong_kt.ten_phong}: {phong_kt.tong_quy_luong():,.0f} VNĐ")