def frequency_encode(df, cols):
    """
    Frequency Encoding cho các cột có nhiều nhãn.
    """

    df = df.copy()

    for col in cols:

        freq_map = (
            df[col]
            .value_counts()
            .to_dict()
        )

        df[f"{col}_FE"] = (
            df[col]
            .map(freq_map)
        )

        print(
            f"{col} -> thêm cột {col}_FE"
        )

    return df