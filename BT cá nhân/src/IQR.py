import pandas as pd

def remove_outliers_iqr(df, columns, factor=1.5, verbose=True):
    """Hàm tính toán và loại bỏ điểm dị biệt (Outliers) bằng phương pháp IQR.

    Công thức:
    - IQR = Q3 - Q1
    - Lower Limit = Q1 - 1.5 * IQR
    - Upper Limit = Q3 + 1.5 * IQR
    
    Tham số:
    - df (DataFrame): Bảng dữ liệu gốc cần xử lý.
    - columns (list): Danh sách các cột dạng số cần lọc outliers.
    - factor (float): Hệ số nhân với IQR (mặc định là 1.5).
    - verbose (bool): Cho phép in báo cáo chi tiết ra màn hình hay không.
    """

    data = df.copy()

    original_rows = len(data)

    for col in columns:

        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - factor * IQR
        upper = Q3 + factor * IQR

        before = len(data)

        data = data[
            (data[col] >= lower) &
            (data[col] <= upper)
        ]

        after = len(data)

        if verbose:
            print(f"    BÁO CÁO OUTLIERS CHO CỘT: {col}")
            print(f"  Q1 (25th percentile)          : {Q1:.2f}")
            print(f"  Q3 (75th percentile)          : {Q3:.2f}")
            print(f"  IQR (Interquartile Range)     : {IQR:.2f}")
            print(f"  Giới hạn dưới (Lower Limit)   : {lower:.2f}")
            print(f"  Giới hạn trên (Upper Limit)   : {upper:.2f}")
            print(f"  Số dòng Đã xóa                : {before-after}")
            print("-" * 40)

    if verbose:
        print(f"Tổng số dòng ban đầu : {original_rows}")
        print(f"Số dòng còn lại      : {len(data)}")
        print(f"Tổng số dòng đã xóa  : {original_rows - len(data)}")

    return data