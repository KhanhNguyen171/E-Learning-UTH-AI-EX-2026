from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode(df, cols):
    """
    One-Hot Encoding cho các cột có ít nhãn.

    Parameters
    ----------
    df : DataFrame
        DataFrame đầu vào.

    cols : list
        Danh sách cột cần One-Hot Encoding.

    Returns
    -------
    DataFrame
        DataFrame sau khi encoding.
    """

    encoder = OneHotEncoder(
        drop='first',
        sparse_output=False,
        handle_unknown='ignore',
        dtype=int
    )

    encoded_array = encoder.fit_transform(df[cols])

    encoded_col_names = (
        encoder.get_feature_names_out(cols)
    )

    df_encoded = pd.DataFrame(
        encoded_array,
        columns=encoded_col_names,
        index=df.index
    )

    df = pd.concat(
        [df.drop(columns=cols), df_encoded],
        axis=1
    )

    print(
        f"Kích thước DataFrame sau One-Hot: {df.shape}"
    )

    return df