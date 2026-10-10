# Quản lý sinh viên đơn giản (Student Management)

def hien_thi_menu():
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Xem danh sách sinh viên")
    print("2. Thêm sinh viên")
    print("3. Xóa sinh viên")
    print("4. Thoát")


def xem_danh_sach(danh_sach):
    print("\n--- DANH SÁCH SINH VIÊN ---")
    if not danh_sach:
        print("Danh sách hiện đang trống.")
        return

    print(f"{'Mã SV':<10} | {'Họ và tên'}")
    print("-" * 32)
    for sv in danh_sach:
        print(f"{sv['ma']:<10} | {sv['ten']}")


def tim_sinh_vien_theo_ma(danh_sach, ma_sv):
    for sv in danh_sach:
        if sv["ma"].strip().upper() == ma_sv.strip().upper():
            return sv
    return None


def them_sinh_vien(danh_sach):
    print("\n--- THÊM SINH VIÊN ---")
    ma_sv = input("Nhập mã sinh viên: ").strip()
    if not ma_sv:
        print("Lỗi: Mã sinh viên không được để trống!")
        return

    if tim_sinh_vien_theo_ma(danh_sach, ma_sv):
        print(f"Lỗi: Mã sinh viên '{ma_sv}' đã tồn tại trong hệ thống!")
        return

    ten_sv = input("Nhập tên sinh viên: ").strip()
    if not ten_sv:
        print("Lỗi: Tên sinh viên không được để trống!")
        return

    danh_sach.append({"ma": ma_sv, "ten": ten_sv})
    print(f"Thêm thành công: {ten_sv} ({ma_sv})")


def xoa_sinh_vien(danh_sach):
    print("\n--- XÓA SINH VIÊN ---")
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip()
    sv = tim_sinh_vien_theo_ma(danh_sach, ma_sv)

    if sv:
        danh_sach.remove(sv)
        print(f"Đã xóa thành công sinh viên có mã '{ma_sv}'.")
    else:
        print(f"Lỗi: Không tìm thấy sinh viên có mã '{ma_sv}'!")


def main():
    # Danh sách khởi tạo có sẵn 2 sinh viên mẫu
    danh_sach_sinh_vien = [
        {"ma": "SV01", "ten": "Nguyễn Văn A"},
        {"ma": "SV02", "ten": "Trần Thị B"}
    ]

    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng (1-4): ").strip()

        if lua_chon == "1":
            xem_danh_sach(danh_sach_sinh_vien)
        elif lua_chon == "2":
            them_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == "3":
            xoa_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == "4":
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 4.")


if __name__ == "__main__":
    main()
