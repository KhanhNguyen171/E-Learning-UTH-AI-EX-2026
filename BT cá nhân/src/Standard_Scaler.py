import pandas as pd
from sklearn.preprocessing import StandardScaler

def standard_scale(df, columns, return_scaler=False, verbose=True):
    """
    Chuẩn hóa các cột dữ liệu số bằng StandardScaler (Z-score scaling).

    Tham số
    ----------
    df : pandas.DataFrame
        Bảng dữ liệu đầu vào.

    columns : list
        Danh sách các cột dữ liệu số cần chuẩn hóa.

    return_scaler : bool, mặc định=False
        Nếu True, hàm sẽ trả về thêm bộ scaler đã được fit.

    verbose : bool, mặc định=True
        Nếu True, in thông tin chi tiết của quá trình chuẩn hóa.

    Trả về
    -------
    pandas.DataFrame
        Bảng dữ liệu sau khi đã được chuẩn hóa.
    """

    data = df.copy()

    scaler = StandardScaler()

    data[columns] = scaler.fit_transform(data[columns])

    if verbose:
        print("=" * 50)
        print("StandardScaler Summary")
        print("=" * 50)

        for col in columns:
            print(f"{col:20s}"
                  f" Mean = {data[col].mean():8.4f}"
                  f" | Std = {data[col].std():8.4f}")

        print("=" * 50)

    if return_scaler:
        return data, scaler

    return data